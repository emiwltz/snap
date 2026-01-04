"""Unified OpenRouter API client."""

from dataclasses import dataclass
from typing import Any

import httpx


@dataclass
class CompletionResponse:
    """Response from OpenRouter completion API."""

    content: str
    """Generated text content."""

    model: str
    """Model that generated the response."""

    finish_reason: str
    """Reason for completion (stop, length, etc.)."""

    usage: dict[str, int]
    """Token usage statistics."""

    latency_ms: float
    """Response latency in milliseconds."""

    raw_response: dict[str, Any] | None = None
    """Full API response for debugging."""


class OpenRouterClient:
    """Unified client for all models via OpenRouter.

    Handles authentication, rate limiting, retries, and caching
    for all LLM API calls.
    """

    BASE_URL = "https://openrouter.ai/api/v1"

    def __init__(
        self,
        api_key: str,
        cache_enabled: bool = True,
        rate_limit_rpm: int = 60,
    ) -> None:
        """Initialize OpenRouter client.

        Args:
            api_key: OpenRouter API key.
            cache_enabled: Whether to cache responses.
            rate_limit_rpm: Requests per minute limit.
        """
        self.api_key = api_key
        self.cache_enabled = cache_enabled
        self.rate_limit_rpm = rate_limit_rpm
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "OpenRouterClient":
        """Async context manager entry."""
        raise NotImplementedError

    async def __aexit__(self, *args: Any) -> None:
        """Async context manager exit."""
        raise NotImplementedError

    async def complete(
        self,
        model: str,
        messages: list[dict[str, str]],
        temperature: float = 0.0,
        max_tokens: int = 150,
    ) -> CompletionResponse:
        """Make a completion request.

        Args:
            model: OpenRouter model ID (e.g., "anthropic/claude-3-opus").
            messages: List of message dicts with "role" and "content".
            temperature: Sampling temperature.
            max_tokens: Maximum tokens to generate.

        Returns:
            CompletionResponse with generated text.

        Raises:
            APIError: On API communication failure.
            RateLimitError: When rate limit is exceeded.
        """
        raise NotImplementedError

    async def health_check(self) -> bool:
        """Check if API is reachable.

        Returns:
            True if API responds successfully.
        """
        raise NotImplementedError

    def get_cache_key(
        self, model: str, messages: list[dict[str, str]], temperature: float
    ) -> str:
        """Generate cache key for a request.

        Args:
            model: Model ID.
            messages: Request messages.
            temperature: Temperature setting.

        Returns:
            Unique cache key string.
        """
        raise NotImplementedError
