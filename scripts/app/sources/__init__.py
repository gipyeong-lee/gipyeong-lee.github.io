"""Topic discovery source adapters."""
from .base import SourceAdapter
from .hackernews import HackerNewsSource
from .arxiv import ArxivSource
from .corporate_blogs import (
    OpenAIBlogSource,
    AnthropicBlogSource,
    DeepMindBlogSource,
    MetaAIBlogSource,
    XAIBlogSource,
    MistralBlogSource,
    ALL_CORPORATE_SOURCES,
)

ALL_SOURCES: list[type[SourceAdapter]] = [
    HackerNewsSource,
    ArxivSource,
    *ALL_CORPORATE_SOURCES,
]

__all__ = [
    "SourceAdapter",
    "HackerNewsSource",
    "ArxivSource",
    "OpenAIBlogSource",
    "AnthropicBlogSource",
    "DeepMindBlogSource",
    "MetaAIBlogSource",
    "XAIBlogSource",
    "MistralBlogSource",
    "ALL_SOURCES",
]
