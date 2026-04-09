"""AI-relevance keyword list + scorer.

Kept deliberately simple — a curated keyword list + a weighted hit count
is dramatically more reliable than a small ML model and needs no runtime
dependencies beyond stdlib `re`.
"""
from __future__ import annotations

import re

# Ordered by approximate signal strength — stronger terms first so ties
# in hit count prefer the more specific term during logging.
AI_KEYWORDS: list[str] = [
    # Labs / products
    "openai", "gpt", "chatgpt", "gpt-4", "gpt-5", "o1", "o3",
    "anthropic", "claude", "claude 3", "claude 4", "claude sonnet", "claude opus",
    "google deepmind", "deepmind", "gemini", "gemma",
    "meta ai", "llama", "llama 3", "llama 4",
    "xai", "grok",
    "mistral", "mixtral",
    "cohere", "command r",
    "stability ai", "stable diffusion",
    "perplexity",
    "hugging face", "huggingface",
    # Core concepts
    "llm", "large language model", "foundation model",
    "transformer", "attention", "self-attention",
    "diffusion", "diffusion model",
    "rag", "retrieval augmented", "retrieval-augmented generation",
    "fine-tuning", "fine tune", "lora", "peft", "qlora",
    "embedding", "vector database", "vector search",
    "prompt engineering", "chain of thought", "cot",
    "in-context learning",
    "agent", "agentic", "autonomous agent", "multi-agent",
    "reasoning model", "tool use", "tool calling", "function calling",
    "mixture of experts", "moe",
    "inference", "quantization", "distillation",
    "reinforcement learning", "rlhf", "dpo", "rlaif",
    "alignment", "ai safety", "red team",
    "mlops", "llmops",
    "code generation", "coding assistant", "copilot",
    "arxiv",
    # Broader but still AI-relevant
    "machine learning", "deep learning", "neural network",
    "computer vision", "nlp", "natural language",
    "generative ai", "genai",
    "multimodal", "vision language", "vlm",
    "text-to-image", "text to image", "text-to-video", "text to video",
    "speech recognition", "text-to-speech",
    "robotics", "embodied ai",
    "foundation model", "frontier model",
    "benchmark", "eval", "evaluation",
    "dataset", "synthetic data",
    "open source model", "open-source model",
    "model card",
    "safety evaluation",
    "hallucination",
    "context window", "long context",
    "training run", "pretraining",
    "scaling law",
    "ai regulation", "ai policy", "ai act",
]

# Precompile regexes — word boundaries so "rag" doesn't match "dragon"
# and multi-word phrases match as whole substrings (case-insensitive).
_PATTERNS: list[tuple[str, re.Pattern[str]]] = []
for kw in AI_KEYWORDS:
    if " " in kw or "-" in kw:
        pat = re.compile(re.escape(kw), re.IGNORECASE)
    else:
        pat = re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE)
    _PATTERNS.append((kw, pat))


def compute_keyword_hits(text: str) -> tuple[list[str], float]:
    """Return (matched keywords, relevance bonus in [0, 1]).

    Bonus = min(1.0, 0.25 * unique_hits). 4+ hits saturates to 1.0.
    """
    if not text:
        return [], 0.0
    hits: list[str] = []
    seen: set[str] = set()
    for kw, pat in _PATTERNS:
        if pat.search(text) and kw not in seen:
            seen.add(kw)
            hits.append(kw)
    bonus = min(1.0, 0.25 * len(hits))
    return hits, bonus


def is_ai_relevant(text: str, min_hits: int = 1) -> bool:
    hits, _ = compute_keyword_hits(text)
    return len(hits) >= min_hits
