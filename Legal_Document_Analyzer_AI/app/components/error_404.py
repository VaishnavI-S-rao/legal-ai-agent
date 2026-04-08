"""
404 Error Page Component for Legal Document Analyzer

This component creates a custom 404 error page for invalid routes.
"""

import streamlit as st
from utils.logger import get_logger
from utils.css_styles import get_common_styles, get_component_specific_styles
from components.header import create_header

def create_404_page():
    """
    Creates a custom 404 error page component.
    
    Returns:
        None: Renders the 404 page directly to the Streamlit app
    """
    # Get logger for 404 page
    logger = get_logger(__name__)
    logger.warning("🚫 404 Error - Invalid page accessed")
    
    # Load common CSS styles and component-specific styles
    st.markdown(get_common_styles(), unsafe_allow_html=True)
    st.markdown(get_component_specific_styles('header'), unsafe_allow_html=True)
    
    # Create header
    create_header(show_tagline=True)
    
    # 404 Error Content
    st.markdown("""
    <div class="error-404-container">
        <div class="error-404-content">
            <div class="error-404-icon">🚫</div>
            <h1 class="error-404-title">404 - Page Not Found</h1>
            <p class="error-404-message">
                The page you're looking for doesn't exist or has been moved.
            </p>
            <div class="error-404-suggestions">
                <h3>Available Pages:</h3>
                <ul>
                    <li><a href="/">🏠 Home</a> - Landing page</li>
                    <li><a href="/?page=analyzer">📄 Document Analyzer</a> - AI-powered document analysis</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 Go to Home", key="404_home", use_container_width=True):
            st.session_state.current_page = "landing"
            st.rerun()
        
        if st.button("📄 Document Analyzer", key="404_analyzer", use_container_width=True):
            st.session_state.current_page = "analyzer"
            st.rerun()
    
    logger.info("✅ 404 error page rendered")

def create_error_page(error_type="404", error_message="Page not found"):
    """
    Creates a generic error page component.
    
    Args:
        error_type (str): Type of error (404, 500, etc.)
        error_message (str): Error message to display
    """
    # Get logger for error page
    logger = get_logger(__name__)
    logger.error(f"🚫 {error_type} Error - {error_message}")
    
    # Load common CSS styles and component-specific styles
    st.markdown(get_common_styles(), unsafe_allow_html=True)
    st.markdown(get_component_specific_styles('header'), unsafe_allow_html=True)
    
    # Create header
    create_header(show_tagline=True)
    
    # Error Content
    st.markdown(f"""
    <div class="error-container">
        <div class="error-content">
            <div class="error-icon">⚠️</div>
            <h1 class="error-title">{error_type} - Error</h1>
            <p class="error-message">{error_message}</p>
            <div class="error-suggestions">
                <h3>What you can do:</h3>
                <ul>
                    <li>Try refreshing the page</li>
                    <li>Go back to the <a href="/">Home page</a></li>
                    <li>Contact support if the problem persists</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 Go to Home", key=f"{error_type}_home", use_container_width=True):
            st.session_state.current_page = "landing"
            st.rerun()
        
        if st.button("🔄 Refresh Page", key=f"{error_type}_refresh", use_container_width=True):
            st.rerun()
    
    logger.info(f"✅ {error_type} error page rendered")
