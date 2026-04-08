"""
Header component for Legal Document Analyzer

This module creates the application header with branding and navigation.
"""

import streamlit as st
import base64
from config.settings import APP_NAME, APP_TAG_LINE
from utils.css_styles import get_component_specific_styles

def create_header(show_tagline=True):
    """
    Create the application header with logo and title.
    
    Args:
        show_tagline (bool): Whether to show the tagline
    """
    # Load header CSS styles
    st.markdown(get_component_specific_styles('header'), unsafe_allow_html=True)
    
    # Read and encode logo as base64
    with open("app/assets/superwise_logo.svg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    # Header with brand gradient
    tagline_html = f'<span class="header-tagline">{APP_TAG_LINE}</span>' if show_tagline else ''
    
    st.markdown(f"""
    <div class="header-container">
        <div class="header-content">
            <div class="header-left">
                <img src="data:image/svg+xml;base64,{encoded}" alt="SUPERWISE Logo" height="40px" width="auto">
                <div>
                    <h1 class="header-title">{APP_NAME}</h1>
                    {tagline_html}
                </div>
            </div>
            <div class="header-nav">
                <a href="/" class="nav-button" target="_self">Home</a>
                <a href="/?page=analyzer" class="nav-button" target="_self">Document Analyzer</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation handled by anchor tags above


def create_simple_header():
    """
    Create a simple header without tagline for minimal pages.
    """
    return create_header(show_tagline=False)
