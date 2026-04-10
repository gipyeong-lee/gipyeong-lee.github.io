"""Fact-checked blog post agents."""

from .researcher import ResearcherAgent
from .writer import WriterAgent
from .fact_checker import FactCheckerAgent
from .editor import EditorAgent
from .translator import TranslatorAgent
from .image_generator import ImageGeneratorAgent
from .script_writer import ScriptWriterAgent
from .tts_voice import TTSVoiceAgent
from .segment_illustrator import SegmentIllustratorAgent
from .video_animator import VideoAnimatorAgent
from .video_composer import VideoComposerAgent
from .thumbnail_maker import ThumbnailMakerAgent
from .youtube_metadata import YouTubeMetadataAgent
from .youtube_uploader import YouTubeUploaderAgent
from .deploy_fixer import DeployFixerAgent

__all__ = [
    "ResearcherAgent",
    "WriterAgent",
    "FactCheckerAgent",
    "EditorAgent",
    "TranslatorAgent",
    "ImageGeneratorAgent",
    # Phase E — video pipeline
    "ScriptWriterAgent",
    "TTSVoiceAgent",
    "SegmentIllustratorAgent",
    "VideoAnimatorAgent",
    "VideoComposerAgent",
    "ThumbnailMakerAgent",
    "YouTubeMetadataAgent",
    "YouTubeUploaderAgent",
    # Deploy self-healing
    "DeployFixerAgent",
]
