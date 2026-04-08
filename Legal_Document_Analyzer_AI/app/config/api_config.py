"""
API Configuration for Legal AI Integration

This module contains configuration settings for the Legal AI API integration.
"""

import os
from typing import Optional

# Legal AI API Configuration
LEGAL_AI_API_URL = os.getenv("LEGAL_AI_API_URL")
LEGAL_AI_API_VERSION = os.getenv("LEGAL_AI_API_VERSION", "v1")
LEGAL_AI_APP_ID = os.getenv("LEGAL_AI_APP_ID")
LEGAL_AI_API_KEY = os.getenv("LEGAL_AI_API_KEY")

# API Timeout Settings
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))  # seconds

# Retry Settings
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "1"))  # seconds


def get_legal_ai_headers() -> dict:
    """
    Get headers for Legal AI API requests

    Returns:
        dict: Headers dictionary
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LEGAL_AI_API_KEY}",
        "X-API-Version": LEGAL_AI_API_VERSION,
        "User-Agent": "LegalDocumentAnalyzer/1.0",
    }


def validate_api_config() -> bool:
    """
    Validate that required API configuration is present

    Returns:
        bool: True if configuration is valid, False otherwise
    """
    if not LEGAL_AI_API_URL:
        return False
    if not LEGAL_AI_APP_ID:
        return False
    if not LEGAL_AI_API_KEY:
        return False
    return True


def get_analysis_endpoint() -> str:
    """
    Get the full endpoint URL for document analysis

    Returns:
        str: Complete API endpoint URL
    """
    return f"{LEGAL_AI_API_URL}/document-analysis"


# API Client Configuration
API_CONFIG = {
    "base_url": LEGAL_AI_API_URL or "https://api.legal-ai.com/",
    "api_key": LEGAL_AI_API_KEY,
    "timeout": API_TIMEOUT,
    "version": LEGAL_AI_API_VERSION,
    "app_id": LEGAL_AI_APP_ID,
    "max_retries": MAX_RETRIES,
    "retry_delay": RETRY_DELAY
}
