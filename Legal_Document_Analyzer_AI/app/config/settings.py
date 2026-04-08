"""
Configuration Settings for Legal Document Analyzer

This module contains configuration settings and constants for the application.
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent.parent

# Application settings
APP_NAME = "Legal Document Analyzer"
APP_VERSION = "1.0.0"
APP_TAG_LINE = "AI-Powered Legal Intelligence for Smart Document Review"

# Streamlit configuration
STREAMLIT_CONFIG = {
    "page_title": APP_NAME,
    "page_icon": "app/assets/superwise_icon.svg",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
}

# File upload settings
FILE_UPLOAD_CONFIG = {
    "max_file_size": int(os.getenv("MAX_FILE_SIZE_MB", "10")) * 1024 * 1024,  # Convert MB to bytes
    "allowed_extensions": ['.pdf', '.doc', '.docx'],
    "max_files": 1,
}

# API settings
API_CONFIG = {
    "timeout": int(os.getenv("API_TIMEOUT", "30")),
    "retry_attempts": int(os.getenv("API_RETRY_ATTEMPTS", "3")),
}

# Superwise API settings
SUPERWISE_API_CONFIG = {
    "base_url": os.getenv("SUPERWISE_API_URL", ""),
    "api_version": os.getenv("SUPERWISE_API_VERSION", "v1"),
    "app_id": os.getenv("SUPERWISE_APP_ID", ""),
    "ask_endpoint": f"{os.getenv('SUPERWISE_API_URL', '')}/{os.getenv('SUPERWISE_API_VERSION', 'v1')}/app-worker/{os.getenv('SUPERWISE_APP_ID', '')}/{os.getenv('SUPERWISE_API_VERSION', 'v1')}/ask"
}

# Feature flags
FEATURES = {
    "document_analysis": True,
    "ai_recommendations": True,
    "risk_assessment": True,
    "clause_extraction": True,
    "obligation_identification": True,
    "missing_terms_detection": True,
}

# UI settings
UI_CONFIG = {
    "theme": "light",
    "primary_color": "#3b82f6",
    "secondary_color": "#10b981",
    "accent_color": "#f59e0b",
    "ai_color": "#8b5cf6",
    "risk_color": "#dc2626",
    "max_width": 1200,
}

# Analysis settings
ANALYSIS_CONFIG = {
    "max_documents": 10,
    "refresh_interval": 300,  # seconds
    "confidence_threshold": 0.7,
}
