"""SQLAlchemy ORM models.

Schema mirrors the plan in docs/plan: topics, runs, logs, settings,
post_history, source_state.
"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import (
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime


class Base(DeclarativeBase):
    pass


# -- topics --------------------------------------------------------------


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    source: Mapped[str] = mapped_column(String, nullable=False)
    source_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    canonical_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    raw_payload: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    score: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    keyword_hits: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False, default="queued")
    discovered_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    selected_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    used_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    fail_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    priority_boost: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

    __table_args__ = (
        UniqueConstraint("source", "source_id", name="uq_topics_source_sourceid"),
        Index("idx_topics_status_score", "status", "score"),
        Index("idx_topics_canonical", "canonical_url"),
    )


# -- runs ----------------------------------------------------------------


class Run(Base):
    __tablename__ = "runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("topics.id"), nullable=True
    )
    trigger: Mapped[str] = mapped_column(String, nullable=False)
    stage: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False)
    started_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    revision_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    final_slug: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    fact_check_verdict: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    git_commit_sha: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    topic = relationship("Topic", lazy="joined")
    logs = relationship(
        "LogEntry", back_populates="run", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_runs_status", "status"),
        Index("idx_runs_started_at", "started_at"),
    )


# -- logs ----------------------------------------------------------------


class LogEntry(Base):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("runs.id"), nullable=True
    )
    ts: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    level: Mapped[str] = mapped_column(String, nullable=False)
    stage: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    agent: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    meta: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    run = relationship("Run", back_populates="logs")

    __table_args__ = (Index("idx_logs_run_id_ts", "run_id", "ts"),)


# -- settings ------------------------------------------------------------


class Setting(Base):
    __tablename__ = "settings"

    key: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(Text, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )


# -- post_history --------------------------------------------------------


class PostHistory(Base):
    __tablename__ = "post_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    title: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    topic: Mapped[str] = mapped_column(String, nullable=False)
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    run_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("runs.id"), nullable=True
    )
    git_commit_sha: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    languages: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    __table_args__ = (Index("idx_post_history_published_at", "published_at"),)


# -- diagnoses -----------------------------------------------------------


class Diagnosis(Base):
    """Automated root-cause analysis for a failed pipeline run."""

    __tablename__ = "diagnoses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("runs.id"), nullable=False, unique=True
    )
    category: Mapped[str] = mapped_column(String, nullable=False)
    root_cause: Mapped[str] = mapped_column(Text, nullable=False)
    evidence: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # JSON snippet
    suggested_fix: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    auto_applied: Mapped[bool] = mapped_column(Integer, nullable=False, default=0)
    applied_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )

    run = relationship("Run", lazy="joined")

    __table_args__ = (
        Index("idx_diagnoses_category", "category"),
        Index("idx_diagnoses_created_at", "created_at"),
    )


# -- source_state --------------------------------------------------------


class SourceState(Base):
    __tablename__ = "source_state"

    source: Mapped[str] = mapped_column(String, primary_key=True)
    last_poll_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_success_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    last_error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    consecutive_errors: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    next_poll_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


# -- videos --------------------------------------------------------------


class Video(Base):
    """Generated YouTube news video for a published post (1:1 by slug)."""

    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    post_slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    script: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    duration_seconds: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    mp4_path: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    thumbnail_path: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    audio_path: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    youtube_video_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    youtube_privacy: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    youtube_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    uploaded_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False, default="queued")
    last_error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    fail_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True, onupdate=func.current_timestamp()
    )

    __table_args__ = (
        Index("idx_videos_status", "status"),
        Index("idx_videos_created_at", "created_at"),
    )


class DeployIncident(Base):
    """Recorded GitHub Pages deploy failure + (auto-)applied fix.

    One row per failing GitHub Actions run (unique on `gh_run_id`).
    Populated by `scripts/app/deploy_watcher.py` which polls `gh run list`
    on a schedule. When the classifier matches a known pattern and an
    auto-fix handler succeeds, the fixer commits the repair and records
    the `fix_commit_sha` here so the next deploy run is traceable.
    """

    __tablename__ = "deploy_incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    gh_run_id: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    workflow_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    branch: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    commit_sha: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    category: Mapped[str] = mapped_column(String, nullable=False, default="unknown")
    root_cause: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    evidence: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    suggested_fix: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    auto_applied: Mapped[bool] = mapped_column(Integer, nullable=False, default=0)
    applied_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    fix_commit_sha: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    fix_error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    recovered: Mapped[bool] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )

    __table_args__ = (
        Index("idx_deploy_incidents_category", "category"),
        Index("idx_deploy_incidents_created_at", "created_at"),
    )


class VideoRun(Base):
    """One execution attempt of the video pipeline for a Video row."""

    __tablename__ = "video_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    video_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("videos.id"), nullable=True
    )
    trigger: Mapped[str] = mapped_column(String, nullable=False)  # auto | manual | retry
    stage: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False)  # running | success | failed
    started_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.current_timestamp()
    )
    ended_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    duration_seconds: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    video = relationship("Video", lazy="joined")

    __table_args__ = (
        Index("idx_video_runs_video_id", "video_id"),
        Index("idx_video_runs_status", "status"),
    )
