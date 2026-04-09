"""Source adapter abstract base.

Each adapter implements `name` and `poll()`. Adapters are plain async
callables — they do NOT persist anything themselves; the caller feeds
results into the scorer + queue_service.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from ..schemas import RawTopic


class SourceAdapter(ABC):
    name: str

    @abstractmethod
    async def poll(self) -> list[RawTopic]:
        """Fetch the current batch of candidate topics from this source."""


USER_AGENT = (
    "aiblog-daemon/0.1 (+https://gipyeong-lee.github.io) python-httpx"
)
