"""Async rate limiter for API calls."""

import asyncio
from collections import deque
from typing import Any


class RateLimiter:
    """Token bucket rate limiter for async operations.

    Ensures API calls don't exceed the specified rate limit.
    """

    def __init__(self, requests_per_minute: int = 60) -> None:
        """Initialize rate limiter.

        Args:
            requests_per_minute: Maximum requests allowed per minute.
        """
        self.rpm = requests_per_minute
        self.interval = 60.0 / requests_per_minute
        self._timestamps: deque[float] = deque()
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        """Acquire permission to make a request.

        Blocks until rate limit allows another request.
        """
        raise NotImplementedError

    async def wait_if_needed(self) -> float:
        """Wait if necessary and return wait time.

        Returns:
            Time waited in seconds.
        """
        raise NotImplementedError

    @property
    def current_rate(self) -> float:
        """Return current request rate (requests per minute)."""
        raise NotImplementedError

    def reset(self) -> None:
        """Reset the rate limiter state."""
        self._timestamps.clear()


class AdaptiveRateLimiter(RateLimiter):
    """Rate limiter that adapts to API responses.

    Automatically adjusts rate based on rate limit headers
    and error responses.
    """

    def __init__(self, initial_rpm: int = 60) -> None:
        """Initialize adaptive rate limiter.

        Args:
            initial_rpm: Starting requests per minute.
        """
        super().__init__(initial_rpm)
        self._backoff_factor = 1.0

    def update_from_response(self, headers: dict[str, Any]) -> None:
        """Update rate limit from response headers.

        Args:
            headers: Response headers with rate limit info.
        """
        raise NotImplementedError

    def backoff(self, factor: float = 2.0) -> None:
        """Apply backoff after rate limit error.

        Args:
            factor: Backoff multiplier.
        """
        raise NotImplementedError

    def recover(self) -> None:
        """Gradually recover from backoff."""
        raise NotImplementedError
