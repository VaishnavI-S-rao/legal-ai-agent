"""
Landing Page Component for Legal Document Analyzer

This component creates the landing page shown when user is not logged in.
"""

import streamlit as st
import base64

# Import global logging
from utils.logger import get_logger
from utils.css_styles import get_common_styles, get_component_specific_styles, get_global_styles
from components.header import create_header

def create_landing_page():
    """
    Creates the landing page component with header and analyzer redirect.
    
    Returns:
        None: Renders the landing page directly to the Streamlit app
    """
    # Get logger for landing page
    logger = get_logger(__name__)
    logger.info("🚀 Creating Legal Document Analyzer landing page component")
    
    # Load global, common CSS styles and component-specific styles
    st.markdown(get_global_styles(), unsafe_allow_html=True)
    st.markdown(get_common_styles(), unsafe_allow_html=True)
    st.markdown(get_component_specific_styles('header'), unsafe_allow_html=True)
    st.markdown(get_component_specific_styles('landing_page'), unsafe_allow_html=True)
    
    # Create header using the reusable component
    create_header(show_tagline=True)
    
    # Hero Banner with Legal Theme
    st.markdown("""
    <div class="image-banner legal-banner">
        <div class="banner-content">
            <div class="banner-text">
                <h1 class="banner-title">AI-Powered Legal Document Analysis</h1>
                <p class="banner-subtitle">
                    Transform your legal document review process with intelligent AI analysis. 
                    Extract key clauses, identify risks, and highlight missing terms in seconds.
                </p>
                <div class="banner-features">
                    <div class="banner-feature">
                        <span class="feature-icon">⚡</span>
                        <span>Instant Analysis</span>
                    </div>
                    <div class="banner-feature">
                        <span class="feature-icon">🛡️</span>
                        <span>Accurate Results</span>
                    </div>
                    <div class="banner-feature">
                        <span class="feature-icon">🎯</span>
                        <span>Risk Detection</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features Section with Attractive Card Design
    st.markdown("---")
    st.markdown("## ✨ Key Features")
    
    # Create feature cards in a single row layout
    feature_col1, feature_col2, feature_col3, feature_col4, feature_col5, feature_col6 = st.columns(6)
    
    with feature_col1:
        # Lightning Fast Feature Card
        st.markdown("""
        <div class="feature-card feature-card-lightning">
            <div class="feature-card-icon">⚡</div>
            <h3 class="feature-card-title">Lightning Fast</h3>
            <p class="feature-card-description">Analyze documents in under 30 seconds with our advanced AI processing engine</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col2:
        # Secure & Private Feature Card
        st.markdown("""
        <div class="feature-card feature-card-secure">
            <div class="feature-card-icon">🛡️</div>
            <h3 class="feature-card-title">Secure & Private</h3>
            <p class="feature-card-description">Your documents are processed securely with enterprise-grade encryption and privacy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col3:
        # Accurate Results Feature Card
        st.markdown("""
        <div class="feature-card feature-card-accurate">
            <div class="feature-card-icon">🎯</div>
            <h3 class="feature-card-title">Accurate Results</h3>
            <p class="feature-card-description">AI-powered analysis with 95% accuracy rate and comprehensive legal insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col4:
        # PDF Support Feature Card
        st.markdown("""
        <div class="feature-card feature-card-pdf">
            <div class="feature-card-icon">📄</div>
            <h3 class="feature-card-title">PDF Support</h3>
            <p class="feature-card-description">Full PDF document support with OCR text recognition and multi-page processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col5:
        # Word Support Feature Card
        st.markdown("""
        <div class="feature-card feature-card-word">
            <div class="feature-card-icon">📝</div>
            <h3 class="feature-card-title">Word Documents</h3>
            <p class="feature-card-description">Support for .doc and .docx files with full text extraction and formatting</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col6:
        # File Size Feature Card
        st.markdown("""
        <div class="feature-card feature-card-files">
            <div class="feature-card-icon">📏</div>
            <h3 class="feature-card-title">Large Files</h3>
            <p class="feature-card-description">Process files up to 10MB with secure temporary storage and fast processing</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Legal Services Section - Using Streamlit Columns (Solution 2)
    st.markdown("---")
    st.markdown("""
    <div class="legal-services-header">
        <h2 class="legal-services-title">
            <span>🏛️</span>
            Legal Services
        </h2>
        <p class="legal-services-subtitle">
            Comprehensive legal document analysis services tailored for modern legal professionals.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Create service cards using Streamlit columns instead of CSS Grid
    service_col1, service_col2, service_col3 = st.columns(3)

    with service_col1:
        st.markdown("""
        <div class="legal-service-card legal-service-contract">
            <span class="legal-service-icon">📄</span>
            <span class="legal-service-category">CONTRACT ANALYSIS</span>
            <h3 class="legal-service-title">Contract Review</h3>
            <p class="legal-service-description">
                Analyze contracts for key terms, obligations, and potential risks with AI-powered insights.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with service_col2:
        st.markdown("""
        <div class="legal-service-card legal-service-compliance">
            <span class="legal-service-icon">📋</span>
            <span class="legal-service-category">COMPLIANCE</span>
            <h3 class="legal-service-title">Compliance Check</h3>
            <p class="legal-service-description">
                Ensure documents meet regulatory requirements and industry standards.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with service_col3:
        st.markdown("""
        <div class="legal-service-card legal-service-risk">
            <span class="legal-service-icon">⚠️</span>
            <span class="legal-service-category">RISK ASSESSMENT</span>
            <h3 class="legal-service-title">Risk Analysis</h3>
            <p class="legal-service-description">
                Identify potential legal risks and liabilities with comprehensive analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Legal Team and Trust Section - Improved Alignment with Header Background
    st.markdown("""
    <div class="bottom-section">
        <div class="legal-team-section">
            <div class="legal-team-title">LEGAL PROFESSIONALS</div>
            <div class="legal-team-content">
                <div class="legal-team-item">Lawyers</div>
                <div class="legal-team-item">Compliance Officers</div>
                <div class="legal-team-item">Business Teams</div>
            </div>
        </div>
        <div class="trust-section">
            <div class="trust-title">Trusted Legal Technology</div>
            <div class="trust-features">
                <div class="trust-item">Secure Processing</div>
                <div class="trust-item">AI-Powered Analysis</div>
                <div class="trust-item">Confidential Review</div>
                <div class="trust-item">Professional Grade</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    logger.info("✅ Legal Document Analyzer landing page rendering completed")
