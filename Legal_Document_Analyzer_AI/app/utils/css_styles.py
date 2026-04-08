"""
CSS Styles for Legal Document Analyzer

This module contains all the CSS styles used across components
to maintain consistency and provide attractive UI.
"""

def get_common_styles():
    """Returns the common CSS styles used across all components."""
    return """
    <style>
    /* ===== COMMON CARD STYLES ===== */
    .common-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    .common-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    /* ===== BUTTON STYLES ===== */
    .btn-primary {
        background-color: #3b82f6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }
    
    .btn-primary:hover {
        background-color: #2563eb;
    }
    
    /* ===== FORM STYLES ===== */
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        width: 100%;
    }
    
    .form-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    </style>
    """

def get_global_styles():
    """Returns global CSS styles for the entire application."""
    return """
    <style>
    /* ===== GLOBAL STYLES ===== */
    .main .block-container {
        padding-top: 0rem;
        padding-bottom: 2rem;
    }
    
    /* Remove any top margin from the first element */
    .main .block-container > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Ensure header starts from top */
    .stApp > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Remove main content area spacing */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }
    
    /* Ensure proper text colors */
    .stMarkdown, .stMarkdown * {
        color: #31333f !important;
    }
    
    .stHeader, .stHeader * {
        color: #31333f !important;
    }
    
    .stSubheader, .stSubheader * {
        color: #31333f !important;
    }
    
    /* Main content text colors */
    .main div, .main div * {
        color: #31333f !important;
    }
    
    /* Legal Analysis styling */
    .legal-analysis {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .risk-alert {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* 404 Error Page Styles */
    .error-404-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 60vh;
        padding: 2rem;
    }
    
    .error-404-content {
        text-align: center;
        max-width: 600px;
    }
    
    .error-404-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .error-404-title {
        color: #e74c3c;
        margin-bottom: 1rem;
    }
    
    .error-404-message {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #666;
    }
    
    .error-404-suggestions {
        text-align: left;
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
    
    .error-404-suggestions h3 {
        color: #333;
        margin-bottom: 1rem;
    }
    
    .error-404-suggestions ul {
        list-style-type: none;
        padding: 0;
    }
    
    .error-404-suggestions li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .error-404-suggestions a {
        color: #667eea;
        text-decoration: none;
    }
    
    .error-404-suggestions a:hover {
        text-decoration: underline;
    }
    
    /* Navigation button styles for anchor tags */
    .nav-button {
        display: inline-block;
        padding: 10px 20px;
        margin: 0 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none !important;
        border-radius: 25px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 500;
        text-align: center;
    }
    
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        text-decoration: none !important;
        color: white;
    }
    
    .nav-button:active {
        transform: translateY(0);
    }
    
    .nav-button:visited {
        color: white;
        text-decoration: none !important;
    }
    
    .nav-button:focus {
        text-decoration: none !important;
        outline: none;
    }
    
    .nav-button:link {
        text-decoration: none !important;
    }
    
    /* Feature Cards Styles */
    .feature-card {
        background: white;
        color: #1e293b;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin-bottom: 1rem;
        border: 3px solid var(--card-border-color);
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        height: 400px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .feature-card-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .feature-card-title {
        margin: 0 0 0.5rem 0 !important;
        color: #1e293b !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
    }
    
    .feature-card-description {
        margin: 0 !important;
        color: #64748b !important;
        font-size: 0.9rem !important;
        line-height: 1.4 !important;
    }
    
    /* Specific feature card border colors - Matte Palette */
    .feature-card-lightning {
        --card-border-color: #6b7280;
    }
    
    .feature-card-secure {
        --card-border-color: #059669;
    }
    
    .feature-card-accurate {
        --card-border-color: #d97706;
    }
    
    .feature-card-pdf {
        --card-border-color: #dc2626;
    }
    
    .feature-card-word {
        --card-border-color: #2563eb;
    }
    
    .feature-card-files {
        --card-border-color: #7c3aed;
    }
    
    /* Legal Services Section - Professional Design */
    .legal-services-container {
        max-width: 1200px !important;
        margin: 0 auto !important;
        padding: 3rem 2rem !important;
        text-align: center !important;
    }
    
    .legal-services-header {
        margin-bottom: 3rem;
    }
    
    .legal-services-title {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #1a202c !important;
        margin-bottom: 1rem !important;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
    }
    
    .legal-services-subtitle {
        font-size: 1.125rem !important;
        color: #4a5568 !important;
        line-height: 1.6 !important;
        max-width: 700px !important;
        margin: 0 auto !important;
    }
    
    .legal-services-grid {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 2rem !important;
        margin-top: 2rem !important;
    }
    
    .legal-service-card {
        background: white;
        border-radius: 1rem;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 3px solid var(--service-border-color);
        transition: all 0.3s ease;
        cursor: pointer;
        height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .legal-service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .legal-service-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
        display: block;
        filter: var(--icon-filter);
    }
    
    .legal-service-category {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--service-border-color);
        margin-bottom: 0.75rem;
        display: block;
    }
    
    .legal-service-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1a202c;
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .legal-service-description {
        font-size: 1rem !important;
        color: #4a5568 !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }
    
    /* Specific legal service card colors */
    .legal-service-contract {
        --service-border-color: #4285F4;
        --icon-filter: hue-rotate(200deg) saturate(1.5);
    }
    
    .legal-service-compliance {
        --service-border-color: #34A853;
        --icon-filter: hue-rotate(120deg) saturate(1.5);
    }
    
    .legal-service-risk {
        --service-border-color: #FBBC05;
        --icon-filter: hue-rotate(45deg) saturate(1.5);
    }
    
    @media (max-width: 768px) {
        .legal-services-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .legal-services-title {
            font-size: 2rem;
        }
        
        .legal-service-card {
            height: 250px;
            padding: 2rem;
        }
    }
    </style>
    """

def get_component_specific_styles(component_name):
    """
    Returns component-specific CSS styles.
    
    Args:
        component_name (str): Name of the component
        
    Returns:
        str: Component-specific CSS styles
    """
    styles = {
        'header': """
        <style>
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            border-radius: 0;
            margin: 0;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: white;
        }
        
        .header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }
        
        .header-left {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .logo-icon {
            font-size: 2rem;
        }
        
        .header-title {
            font-size: 1.75rem !important;
            font-weight: 700 !important;
            margin: 0 !important;
            color: white !important;
        }
        
        .header-container .header-tagline {
            font-size: 1.2rem !important;
            margin: 0;
            opacity: 0.9;
            color: #FACC15 !important;
        }
        
        .header-nav {
            display: flex;
            gap: 1rem;
        }
        
        .nav-button {
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: white !important;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .nav-button:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-1px);
        }
        </style>
        """,
        
        'landing_page': """
        <style>
        .legal-banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 4rem 2rem;
            border-radius: 1rem;
            margin-bottom: 3rem;
            text-align: center;
            color: white;
        }
        
        .banner-content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .banner-title {
            font-size: 3rem !important;
            font-weight: 700 !important;
            margin-bottom: 1rem !important;
            color: #0F172A !important;
        }
        
        .banner-subtitle {
            font-size: 1.25rem !important;
            margin-bottom: 2rem;
            line-height: 1.6;
            opacity: 0.9;
            color: #FACC15 !important;
        }
        
        .banner-features {
            display: flex;
            justify-content: center;
            gap: 3rem;
            margin-top: 2rem;
        }
        
        .banner-feature {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-weight: 500;
            color: white !important;
        }
        
        .banner-feature span {
            color: white !important;
        }
        
        .feature-icon {
            font-size: 1.5rem;
        }
        
        .landing-content {
            text-align: center;
            padding: 2rem;
        }
        
        .welcome-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 1rem;
        }
        
        .welcome-subtitle {
            font-size: 1.25rem;
            color: #64748b;
            margin-bottom: 2rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .legal-services-section {
            margin: 3rem 0;
        }
        
        .services-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        
        .service-section {
            background: white;
            padding: 2rem;
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .service-section:hover {
            transform: translateY(-4px);
        }
        
        .service-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .service-category {
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }
        
        .contract-category { color: #3b82f6; }
        .compliance-category { color: #10b981; }
        .risk-category { color: #f59e0b; }
        
        .service-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 1rem;
        }
        
        .service-description {
            color: #64748b;
            line-height: 1.6;
        }
        
        .bottom-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            margin-top: 3rem;
            padding: 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 0.75rem;
        }
        
        .legal-team-section {
            text-align: center;
        }
        
        .legal-team-title {
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: rgba(255, 255, 255, 0.8) !important;
            margin-bottom: 1rem;
        }
        
        .legal-team-content {
            font-size: 1.125rem;
            font-weight: 600;
            color: white;
        }
        
        .legal-team-item {
            padding: 0.25rem 0;
            color: white !important;
        }
        
        .trust-section {
            text-align: center;
        }
        
        .trust-title {
            font-size: 1.125rem;
            font-weight: 600;
            color: white !important;
            margin-bottom: 1rem;
        }
        
        .trust-features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
        }
        
        .trust-item {
            font-size: 0.875rem;
            color: rgba(255, 255, 255, 0.9) !important;
            padding: 0.25rem 0;
            text-align: center;
        }
        
        @media (max-width: 768px) {
            .bottom-section {
                grid-template-columns: 1fr;
                gap: 2rem;
                padding: 1.5rem;
            }
            
            .trust-features {
                grid-template-columns: 1fr;
                gap: 0.75rem;
            }
        }
        
        /* Call to Action Section */
        .cta-section {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 4rem 2rem;
            border-radius: 1rem;
            margin: 3rem 0;
        }
        
        .cta-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }
        
        .cta-content {
            text-align: left;
        }
        
        .cta-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 1rem;
            line-height: 1.2;
        }
        
        .cta-subtitle {
            font-size: 1.125rem;
            color: #64748b;
            margin-bottom: 2rem;
            line-height: 1.6;
        }
        
        .cta-features {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            margin-bottom: 2.5rem;
        }
        
        .cta-feature {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .cta-feature-icon {
            font-size: 2rem;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .cta-feature-text h4 {
            font-size: 1.125rem;
            font-weight: 600;
            color: #1e293b;
            margin: 0 0 0.25rem 0;
        }
        
        .cta-feature-text p {
            font-size: 0.875rem;
            color: #64748b;
            margin: 0;
        }
        
        .cta-button-container {
            text-align: left;
        }
        
        .cta-button {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            padding: 1rem 2rem;
            border-radius: 0.75rem;
            font-weight: 600;
            font-size: 1.125rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
            text-decoration: none;
            color: white;
        }
        
        .cta-button-icon {
            font-size: 1.25rem;
        }
        
        .cta-button-text {
            font-size: 1.125rem;
        }
        
        /* Supported Formats Section */
        .supported-formats {
            background: white;
            padding: 2.5rem;
            border-radius: 1rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .formats-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .formats-header h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 0.5rem;
        }
        
        .formats-header p {
            font-size: 0.875rem;
            color: #64748b;
            margin: 0;
        }
        
        .formats-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .format-card {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1.5rem;
            border-radius: 0.75rem;
            border: 2px solid #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .format-card:hover {
            border-color: #667eea;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        }
        
        .format-icon {
            font-size: 2rem;
            width: 60px;
            height: 60px;
            background: #f8fafc;
            border-radius: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        
        .format-info {
            flex: 1;
        }
        
        .format-info h4 {
            font-size: 1rem;
            font-weight: 600;
            color: #1e293b;
            margin: 0 0 0.25rem 0;
        }
        
        .format-info p {
            font-size: 0.875rem;
            color: #64748b;
            margin: 0 0 0.5rem 0;
        }
        
        .format-badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-size: 0.75rem;
            font-weight: 500;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
        }
        
        .formats-features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.75rem;
        }
        
        .format-feature {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
            color: #64748b;
        }
        
        .feature-check {
            color: #10b981;
            font-weight: bold;
            font-size: 1rem;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .cta-container {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            
            .cta-title {
                font-size: 2rem;
            }
            
            .formats-features {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        
        'document_analyzer': """
        <style>
        /* Upload Section Styles - Simplified */
        
        /* File Status Styles */
        .file-status {
            background: white;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #10b981;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .file-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .file-icon {
            font-size: 2rem;
        }
        
        .file-details h4 {
            margin: 0;
            font-size: 1.125rem;
            font-weight: 600;
            color: #1e293b;
        }
        
        .file-details p {
            margin: 0.25rem 0 0 0;
            font-size: 0.875rem;
            color: #64748b;
        }
        
        .file-status-badge {
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-weight: 500;
            font-size: 0.875rem;
        }
        
        .file-status-badge.success {
            background: #d1fae5;
            color: #065f46;
            border: 1px solid #a7f3d0;
        }
        
        /* Enhanced file uploader styling */
        .stFileUploader {
            background: white;
            border-radius: 0.75rem !important;
            padding: 1rem !important;
            border: 5px dashed #cbd5e1 !important;
            transition: all 0.3s ease !important;
        }
        
        .stFileUploader:hover {
            border-color: #667eea !important;
            background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%) !important;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .upload-features {
                flex-direction: column;
                gap: 1rem;
            }
            
            .file-status {
                flex-direction: column;
                gap: 1rem;
                text-align: center;
            }
            
            .upload-wrapper {
                padding: 1.5rem;
            }
        }
        
        .summary-container {
            background: #f8fafc;
            padding: 1.5rem;
            border-radius: 0.5rem;
            border-left: 4px solid #3b82f6;
        }
        
        .clause-card, .obligation-card, .risk-card, .missing-term-card {
            background: white;
            padding: 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 4px solid #3b82f6;
        }
        
        .clause-card h4, .obligation-card h4, .risk-card h4, .missing-term-card h4 {
            font-size: 1.125rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 1rem;
        }
        
        .clause-card p, .obligation-card p, .risk-card p, .missing-term-card p {
            margin: 0.5rem 0;
            color: #64748b;
        }
        
        .clause-card strong, .obligation-card strong, .risk-card strong, .missing-term-card strong {
            color: #374151;
        }
        
        /* Superwise Analysis Output Styling */
        .superwise-analysis {
            background: white;
            padding: 2rem;
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
        }
        
        .superwise-analysis h3 {
            color: #1e293b;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        .superwise-analysis h4 {
            color: #374151;
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }
        
        .superwise-analysis strong {
            color: #1e293b;
            font-weight: 600;
        }
        
        .superwise-analysis p {
            color: #64748b;
            line-height: 1.6;
            margin-bottom: 0.75rem;
        }
        
        .superwise-analysis ul, .superwise-analysis ol {
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .superwise-analysis li {
            color: #64748b;
            line-height: 1.6;
            margin-bottom: 0.5rem;
        }
        
        .superwise-analysis code {
            background: #f1f5f9;
            padding: 0.125rem 0.375rem;
            border-radius: 0.25rem;
            font-size: 0.875rem;
            color: #e11d48;
        }
        
        /* Analysis Results Metrics Styling */
        div[data-testid="stMetricValue"] {
            font-size: 0.875rem !important;
        }
        
        div[data-testid="stMetricLabel"] {
            font-size: 0.75rem !important;
        }
        
        /* ===== TAB CONTENT BORDERS ===== */
        /* Add borders to tab content panels - Left, Right, and Bottom */
        div[data-baseweb="tab-panel"] {
            border-left: 3px solid #e2e8f0 !important;
            border-right: 3px solid #e2e8f0 !important;
            border-bottom: 3px solid #e2e8f0 !important;
            padding: 2rem !important;
            background: #fafbfc !important;
            margin-top: 10px !important;
        }
        
        /* Add subtle rounded corners to bottom */
        div[data-baseweb="tabs"] {
            border-radius: 0 0 8px 8px;
        }
        
        /* Tab content area styling */
        .stTabs > div > div > div[role="tabpanel"] {
            border-left: 3px solid #e2e8f0;
            border-right: 3px solid #e2e8f0;
            border-bottom: 3px solid #e2e8f0;
            padding: 2rem !important;
            min-height: 400px;
        }
        
        /* Alternative selector for tab panels */
        [data-testid="stTabs"] [data-baseweb="tab-panel"] {
            border-left: 3px solid #e2e8f0 !important;
            border-right: 3px solid #e2e8f0 !important;
            border-bottom: 3px solid #e2e8f0 !important;
            padding: 2rem !important;
        }
        
        /* Custom Loader Styles */
        .page-overlay {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            background: rgba(255, 255, 255, 0.85) !important;
            backdrop-filter: blur(8px) !important;
            -webkit-backdrop-filter: blur(8px) !important;
            z-index: 999999 !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 1.5rem !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .spinner-container {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            gap: 1rem !important;
        }
        
        .spinner {
            width: 50px !important;
            height: 50px !important;
            border: 5px solid #f3f4f6 !important;
            border-top: 5px solid #667eea !important;
            border-radius: 50% !important;
            animation: spin 1s linear infinite !important;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .spinner-text {
            font-size: 1.25rem !important;
            font-weight: 600 !important;
            color: #1e293b !important;
            text-align: center !important;
        }
        
        .spinner-subtext {
            font-size: 0.875rem !important;
            color: #64748b !important;
            text-align: center !important;
        }
        </style>
        """
    }
    
    return styles.get(component_name, "")
