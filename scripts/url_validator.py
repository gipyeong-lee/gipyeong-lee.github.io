"""URL validation utility with HEAD/GET fallback and parallel execution."""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple

# Domains that block HEAD requests
HEAD_BLOCKED_DOMAINS = {"medium.com", "towardsdatascience.com", "levelup.gitconnected.com"}

LIVE_STATUS_CODES = {200, 301, 302, 303, 307, 308}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

TIMEOUT = 10


def _is_head_blocked(url: str) -> bool:
    """Check if the URL's domain is known to block HEAD requests."""
    for domain in HEAD_BLOCKED_DOMAINS:
        if domain in url:
            return True
    return False


def check_url(url: str) -> Tuple[str, bool, int]:
    """Check if a URL is live. Returns (url, is_live, status_code)."""
    try:
        if not _is_head_blocked(url):
            # Try HEAD first (faster)
            try:
                resp = requests.head(url, headers=HEADERS, timeout=TIMEOUT,
                                     allow_redirects=True)
                if resp.status_code in LIVE_STATUS_CODES:
                    return (url, True, resp.status_code)
                if resp.status_code == 405:
                    pass  # Fall through to GET
                else:
                    return (url, False, resp.status_code)
            except requests.RequestException:
                pass  # Fall through to GET

        # GET fallback with stream to avoid downloading full body
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT,
                            allow_redirects=True, stream=True)
        is_live = resp.status_code in LIVE_STATUS_CODES
        return (url, is_live, resp.status_code)

    except requests.ConnectionError:
        return (url, False, 0)
    except requests.Timeout:
        return (url, False, 0)
    except requests.RequestException:
        return (url, False, 0)


def validate_urls(urls: List[str], max_workers: int = 5) -> List[Tuple[str, bool, int]]:
    """Validate multiple URLs in parallel.

    Returns list of (url, is_live, status_code) tuples.
    """
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_url, url): url for url in urls}
        for future in as_completed(futures):
            results.append(future.result())
    return results
