"""
Main Legal Document Analyzer Application

This is the main entry point for the Legal Document Analyzer Streamlit application.
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import components
from components.header import create_header
from components.landing_page import create_landing_page
from components.document_analyzer import create_document_analyzer
from components.error_404 import create_404_page, create_error_page

# Import utilities
from utils.logger import get_logger
from utils.document_processor import DocumentProcessor
from utils.analysis_utils import (
    calculate_analysis_stats, 
    update_analysis_stats, 
    get_analysis_stats, 
    get_analysis_count
)
from utils.css_styles import get_global_styles

# Page navigation helper functions
def set_page(page_name: str):
    """Set the current page in session state"""
    if st.session_state.current_page != page_name:
        st.session_state.current_page = page_name
        logger = get_logger(__name__)
        logger.info(f"🔄 Page set to: {page_name}")
        st.rerun()


def get_current_page() -> str:
    """Get the current page from session state"""
    return st.session_state.get("current_page", "landing")


def navigate_to_page(page_name: str):
    """Navigate to a specific page"""
    set_page(page_name)

def handle_url_routing():
    """
    Handle URL parameters and routing logic.
    
    Returns:
        str: The page to display
    """
    # Get query parameters
    query_params = st.query_params
    
    # Handle page parameter
    if 'page' in query_params:
        page = query_params['page']
        
        # Validate page parameter
        valid_pages = ['landing', 'analyzer']
        if page in valid_pages:
            # Update session state with the page from URL
            st.session_state.current_page = page
            # Clear the query parameter to avoid confusion
            st.query_params.clear()
            return page
        else:
            # Invalid page parameter - show 404
            st.query_params.clear()
            return '404'
    
    # If no page parameter, check session state for current page
    current_page = st.session_state.get('current_page', 'landing')
    
    # If we're in analyzer mode but no page param, stay on analyzer
    if current_page == 'analyzer':
        return 'analyzer'
    
    # Default to landing page
    return 'landing'


# Page configuration
st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="app/assets/superwise_icon.svg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load global CSS styles
st.markdown(get_global_styles(), unsafe_allow_html=True)


def main():
    """
    Main application function that orchestrates all components.
    """

    # Get logger for main application
    logger = get_logger(__name__)
    logger.info("🎯 Legal Document Analyzer main application started")

    # Initialize page state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "landing"
        logger.info("🔧 Initialized session state: current_page = landing")

    # Initialize analysis history
    if "analysis_history" not in st.session_state:
        st.session_state.analysis_history = []
        logger.info("🔧 Initialized analysis history")
    
    # Initialize analysis statistics
    if "analysis_stats" not in st.session_state:
        st.session_state.analysis_stats = {
            "total_analyses": 0,
            "high_risk_count": 0,
            "medium_risk_count": 0,
            "low_risk_count": 0,
            "last_analysis_time": None
        }
        logger.info("🔧 Initialized analysis statistics")

    # Handle URL routing
    current_page = handle_url_routing()
    
    # Update session state if needed
    if st.session_state.current_page != current_page:
        st.session_state.current_page = current_page
        logger.info(f"🔄 URL routing changed page to: {current_page}")

    # Route to appropriate page
    if current_page == "landing":
        create_landing_page()
        return
    elif current_page == "analyzer":
        # User is on main application - show header
        create_header(show_tagline=True)
        show_analyzer()
        return
    elif current_page == "404":
        create_404_page()
        return
    else:
        # Fallback to 404 for any other cases
        create_404_page()
        return


def show_analyzer():
    """
    Displays the main document analyzer page.
    """
    # Create document analyzer interface
    create_document_analyzer()


if __name__ == "__main__":
    main()
