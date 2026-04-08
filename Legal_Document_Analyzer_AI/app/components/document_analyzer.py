"""
Document Analyzer Component for Legal Document Analyzer

This component handles document upload, processing, and analysis results.
"""

import streamlit as st
import os
import tempfile
import requests
from typing import Dict, List, Any

# Import utilities
from utils.logger import get_logger
from utils.css_styles import get_component_specific_styles
from utils.document_processor import DocumentProcessor
from utils.analysis_utils import update_analysis_stats
from config.settings import FILE_UPLOAD_CONFIG, SUPERWISE_API_CONFIG, API_CONFIG

# Initialize global logger
logger = get_logger(__name__)

def display_text_with_toggle(results: Dict, key_suffix: str = ""):
    """
    Display extracted text (always shows full text).
    
    Args:
        results: Dictionary containing extracted text data
        key_suffix: Unique suffix for Streamlit widget keys
    """
    # Always show full text
    text_to_display = results.get('extracted_text_full') or results.get('extracted_text_preview', '')
    text_length = results.get('text_length', len(text_to_display))
    
    st.caption(f"📝 Document Text ({text_length:,} total characters)")
    st.text_area("Document Text", text_to_display, height=600, key=f"full_text_{key_suffix}")

def show_custom_loader(message: str = "Processing...", submessage: str = "Please wait"):
    """
    Display a custom full-page loader with blur effect.
    
    Args:
        message: Main message to display (default: "Processing...")
        submessage: Sub-message to display below main message (default: "Please wait")
    """
    st.markdown(f"""
    <div class="page-overlay" id="custom-loader-overlay">
        <div class="spinner-container">
            <div class="spinner"></div>
            <div class="spinner-text">{message}</div>
            <div class="spinner-subtext">{submessage}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_document_analyzer():
    """
    Creates the document analyzer component with upload and analysis functionality.
    
    Returns:
        None: Renders the analyzer directly to the Streamlit app
    """
    logger.info("📄 Creating document analyzer component")
    
    # Load analyzer CSS styles
    st.markdown(get_component_specific_styles('document_analyzer'), unsafe_allow_html=True)
    
    # File upload section with enhanced styling
    st.markdown("## 📤 Upload Document")
    max_size_mb = FILE_UPLOAD_CONFIG["max_file_size"] / (1024 * 1024)
    allowed_extensions = ", ".join(FILE_UPLOAD_CONFIG["allowed_extensions"]).upper()
    st.markdown(f"**Supported formats:** {allowed_extensions} | **Maximum size:** {max_size_mb:.0f}MB")
    st.markdown("✅ Secure • 🔒 Private • ⚡ Fast Processing")
    
    uploaded_file = st.file_uploader(
        "Choose a legal document",
        type=['pdf', 'doc', 'docx'],
        help=f"Supported formats: {allowed_extensions} (Max size: {max_size_mb:.0f}MB)",
        key="document_upload"
    )
    
    # Add file status indicator if file is uploaded
    if uploaded_file is not None:
        # Validate uploaded file
        is_valid, error_msg = validate_uploaded_file(uploaded_file)
        
        if not is_valid:
            st.error(f"❌ {error_msg}")
            return
        
        file_size = len(uploaded_file.getvalue())
        st.markdown("""
        <div class="file-status">
            <div class="file-info">
                <span class="file-icon">📄</span>
                <div class="file-details">
                    <h4 class="file-name">{}</h4>
                    <p class="file-size">{:.1f} KB</p>
                </div>
            </div>
            <div class="file-status-badge success">
                ✅ Ready for Analysis
            </div>
        </div>
        """.format(uploaded_file.name, file_size / 1024), unsafe_allow_html=True)
    
        # Automatic processing - no button needed
        process_document_automatically(uploaded_file)
    
    # Display previous analysis results if available
    if 'analysis_results' in st.session_state and st.session_state.analysis_results:
        display_analysis_results(st.session_state.analysis_results)

def validate_uploaded_file(uploaded_file):
    """
    Validate uploaded file for size and other constraints.
    
    Args:
        uploaded_file: The uploaded file object
        
    Returns:
        tuple: (is_valid, error_message)
    """
    
    # Get configurable settings
    max_size = FILE_UPLOAD_CONFIG["max_file_size"]
    allowed_extensions = FILE_UPLOAD_CONFIG["allowed_extensions"]
    max_size_mb = max_size / (1024 * 1024)
    
    file_size = len(uploaded_file.getvalue())
    
    if file_size > max_size:
        error_msg = f"File size ({file_size / (1024*1024):.1f} MB) exceeds the {max_size_mb:.0f}MB limit. Please upload a smaller file."
        logger.error(f"File size validation failed: {uploaded_file.name} - {file_size} bytes (limit: {max_size} bytes)")
        return False, error_msg
    
    # Check file type
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    
    if file_extension not in allowed_extensions:
        error_msg = f"File type '{file_extension}' is not supported. Allowed types: {', '.join(allowed_extensions)}"
        logger.error(f"File type validation failed: {uploaded_file.name} - {file_extension}")
        return False, error_msg
    
    # Check if file is empty
    if file_size == 0:
        error_msg = "File is empty. Please upload a valid document."
        logger.error(f"Empty file validation failed: {uploaded_file.name}")
        return False, error_msg
    
    logger.info(f"✅ File validation passed: {uploaded_file.name} - {file_size / (1024*1024):.1f} MB (limit: {max_size_mb:.0f}MB)")
    return True, None

def clean_document_text(text: str) -> str:
    """
    Clean document text by removing unrecognized characters while preserving readable content.
    
    Args:
        text: Raw extracted text from document
        
    Returns:
        str: Cleaned text with unrecognized characters removed
    """
    if not text:
        return ""
    
    import re
    
    # Keep letters, numbers, spaces, and common punctuation
    # This regex keeps: a-z, A-Z, 0-9, spaces, and common punctuation
    cleaned_text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\[\]\{\}\"\'\/\@\#\$\%\&\*\+\=\<\>\|\\]', '', text)
    
    # Remove multiple consecutive spaces and normalize whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    # Remove leading/trailing whitespace
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

def process_document_automatically(uploaded_file):
    """
    Automatically process uploaded document: extract text → call Superwise API → show results
    
    Args:
        uploaded_file: The uploaded file object
    """
    logger.info(f"🚀 Starting automatic processing for: {uploaded_file.name}")
    
    # Create a placeholder for the loader
    loader_placeholder = st.empty()

    # Page-level loading spinner
    with loader_placeholder.container():
        show_custom_loader(message="Processing document...", submessage="Please wait while we analyze your document")

    # Show progress
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Step 1: Extract text
        status_text.text("📝 Extracting text from document...")
        progress_bar.progress(20)
        
        result_metadata = extract_document_text_only(uploaded_file)
        
        if result_metadata['processing_status'] != 'success':
            st.error(f"❌ Text extraction failed: {result_metadata['error_message']}")
            progress_bar.empty()
            status_text.empty()
            return
        
        # Step 2: Call Superwise API
        status_text.text("🤖 Calling Superwise API for analysis...")
        progress_bar.progress(60)
        
        extracted_text = result_metadata['extracted_text']
        analysis_options = {
            'extract_clauses': True,
            'identify_obligations': True,
            'assess_risks': True,
            'find_missing_terms': True,
            'generate_summary': True,
            'highlight_issues': True
        }
        
        # Call Superwise API
        superwise_results = call_superwise_api(extracted_text, analysis_options)
        
        # Step 3: Store results
        status_text.text("📊 Processing analysis results...")
        progress_bar.progress(80)
        
        st.session_state.analysis_results = {
            'filename': uploaded_file.name,
            'file_size': len(uploaded_file.getvalue()),
            'file_type': result_metadata['file_type'],
            'processing_status': 'success',
            'text_length': len(extracted_text),
            'analysis_options': analysis_options,
            'results': superwise_results,
            # Store both preview and full text for better UX
            'extracted_text_preview': extracted_text[:1000] + "..." if len(extracted_text) > 1000 else extracted_text,
            'extracted_text_full': extracted_text,
            'is_truncated': len(extracted_text) > 1000
        }
        
        # Complete
        progress_bar.progress(100)
        status_text.text("✅ Analysis completed successfully!")
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()

        # Clear the loader
        loader_placeholder.empty()

        
        logger.info(f"✅ Automatic processing completed for: {uploaded_file.name}")
        
    except Exception as e:
        logger.error(f"❌ Error during automatic processing: {str(e)}")
        st.error(f"Error processing document: {str(e)}")
        progress_bar.empty()
        status_text.empty()

        # Clear the loader
        loader_placeholder.empty()


def extract_document_text_only(uploaded_file):
    """
    Extract text from uploaded document only (no AI analysis).
    
    Args:
        uploaded_file: The uploaded file object
        
    Returns:
        Dict: Result metadata with extracted text
    """
    logger.info(f"📄 Extracting text from: {uploaded_file.name}")
    
    # Initialize result metadata
    result_metadata = {
        'filename': uploaded_file.name,
        'file_size': len(uploaded_file.getvalue()),
        'file_type': os.path.splitext(uploaded_file.name)[1].lower(),
        'processing_status': 'processing',
        'extracted_text': None,
        'text_length': 0,
        'error_message': None
    }
    
    try:
        # Save uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        # Extract text using document processor
        processor = DocumentProcessor()
        raw_text = processor.extract_text(tmp_file_path)
        
        # Clean the text - remove unrecognized characters
        cleaned_text = clean_document_text(raw_text)
        
        # Check if text extraction was successful
        if not cleaned_text or len(cleaned_text.strip()) == 0:
            result_metadata['processing_status'] = 'failed'
            result_metadata['error_message'] = 'No readable text found in document'
            logger.error(f"❌ No readable text found in: {uploaded_file.name}")
            return result_metadata
        
        # Update metadata with successful extraction
        result_metadata['extracted_text'] = cleaned_text
        result_metadata['text_length'] = len(cleaned_text)
        result_metadata['processing_status'] = 'success'
        
        # Clean up temporary file
        os.unlink(tmp_file_path)
        
        logger.info(f"✅ Text extraction completed for: {uploaded_file.name}")
        logger.info(f"📊 Extracted {len(cleaned_text)} characters of clean text")
        logger.info(f"result_metadata: {result_metadata}")
        
        return result_metadata
        
    except Exception as e:
        result_metadata['processing_status'] = 'failed'
        result_metadata['error_message'] = str(e)
        logger.error(f"❌ Error during text extraction: {str(e)}")
        return result_metadata

def call_superwise_api(extracted_text, analysis_options):
    """
    Call Superwise API with extracted text.
    
    Args:
        extracted_text: Cleaned text from document
        analysis_options: Analysis options
        
    Returns:
        Dict: Analysis results from Superwise API
    """
    logger.info("🤖 Calling Superwise API for analysis")
    logger.info(f"📊 Text length: {len(extracted_text)} characters")
    logger.info(f"⚙️ Analysis options: {analysis_options}")
    
    try:
        # Prepare Superwise API payload
        payload = {
            "input": extracted_text,
            "chat_history": []
        }
        
        # Get API configuration
        api_url = SUPERWISE_API_CONFIG["ask_endpoint"]
        timeout = API_CONFIG["timeout"]
        
        logger.info("🔗 Preparing Superwise API request")
        logger.info(f"📤 API URL: {api_url}")
        logger.info(f"📤 Payload prepared: {payload}")
        logger.info("📤 Sending request to Superwise API")
        
        # Make actual API call
        response = requests.post(
            url=api_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=timeout
        )
        
        # Check response status
        if response.status_code == 200:
            analysis_results = response.json()
            logger.info("✅ Superwise API analysis completed successfully")
            logger.info(f"📋 Analysis results: {analysis_results}")
            return analysis_results
        else:
            error_msg = f"API request failed with status {response.status_code}: {response.text}"
            logger.error(f"❌ {error_msg}")
            raise Exception(error_msg)
        
    except requests.exceptions.Timeout:
        error_msg = f"API request timed out after {timeout} seconds"
        logger.error(f"❌ {error_msg}")
        raise Exception(error_msg)
    except requests.exceptions.RequestException as e:
        error_msg = f"API request failed: {str(e)}"
        logger.error(f"❌ {error_msg}")
        raise Exception(error_msg)
    except Exception as e:
        logger.error(f"❌ Error calling Superwise API: {str(e)}")
        raise

def analyze_document(uploaded_file, analysis_options: Dict[str, bool]):
    """
    Analyze the uploaded document with the specified options.
    
    Args:
        uploaded_file: The uploaded file object
        analysis_options: Dictionary of analysis options
        
    Returns:
        Dict: Analysis results with metadata including file size, processing status, and cleaned text
    """
    logger.info(f"🔍 Starting document analysis for: {uploaded_file.name}")
    
    # Show progress
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Initialize result metadata
    result_metadata = {
        'filename': uploaded_file.name,
        'file_size': len(uploaded_file.getvalue()),
        'file_type': os.path.splitext(uploaded_file.name)[1].lower(),
        'processing_status': 'processing',
        'extracted_text': None,
        'text_length': 0,
        'error_message': None
    }
    
    try:
        # Step 1: Save uploaded file
        status_text.text("📁 Processing uploaded file...")
        progress_bar.progress(20)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
        
        # Step 2: Extract and clean text
        status_text.text("📝 Extracting and cleaning text from document...")
        progress_bar.progress(40)
        
        # Extract text using document processor
        processor = DocumentProcessor()
        raw_text = processor.extract_text(tmp_file_path)
        
        # Clean the text - remove unrecognized characters
        cleaned_text = clean_document_text(raw_text)
        
        # Check if text extraction was successful
        if not cleaned_text or len(cleaned_text.strip()) == 0:
            result_metadata['processing_status'] = 'failed'
            result_metadata['error_message'] = 'No readable text found in document'
            logger.error(f"❌ No readable text found in: {uploaded_file.name}")
            st.error("No readable text found in the document. Please try a different file.")
            progress_bar.empty()
            status_text.empty()
            return result_metadata
        
        # Update metadata with successful extraction
        result_metadata['extracted_text'] = cleaned_text
        result_metadata['text_length'] = len(cleaned_text)
        result_metadata['processing_status'] = 'success'
        
        logger.info(f"result_metadata: {result_metadata}")

        # Step 3: Perform analysis
        status_text.text("🤖 Running AI analysis...")
        progress_bar.progress(60)
        
        analysis_results = processor.analyze_document(cleaned_text, analysis_options)
        
        # Step 4: Generate results
        status_text.text("📊 Generating analysis results...")
        progress_bar.progress(80)
        
        # Store results in session state
        st.session_state.analysis_results = {
            'filename': uploaded_file.name,
            'file_size': len(uploaded_file.getvalue()),
            'file_type': result_metadata['file_type'],
            'processing_status': 'success',
            'text_length': len(cleaned_text),
            'analysis_options': analysis_options,
            'results': analysis_results,
            # Store both preview and full text for better UX
            'extracted_text_preview': cleaned_text[:1000] + "..." if len(cleaned_text) > 1000 else cleaned_text,
            'extracted_text_full': cleaned_text,
            'is_truncated': len(cleaned_text) > 1000
        }
        
        # Update analysis statistics
        update_analysis_stats(analysis_results)
        
        # Complete progress
        progress_bar.progress(100)
        status_text.text("✅ Analysis completed successfully!")
        
        # Clean up temporary file
        os.unlink(tmp_file_path)
        
        logger.info(f"✅ Document analysis completed successfully for: {uploaded_file.name}")
        logger.info(f"📊 Extracted {len(cleaned_text)} characters of clean text")
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        return result_metadata
        
    except Exception as e:
        result_metadata['processing_status'] = 'failed'
        result_metadata['error_message'] = str(e)
        logger.error(f"❌ Error during document analysis: {str(e)}")
        st.error(f"Error analyzing document: {str(e)}")
        progress_bar.empty()
        status_text.empty()
        return result_metadata

def parse_superwise_markdown(markdown_text: str) -> Dict[str, str]:
    """
    Parse Superwise markdown output into structured sections.
    
    Args:
        markdown_text: Raw markdown text from Superwise API
        
    Returns:
        Dict: Parsed sections with their content
    """
    import re
    
    sections = {}
    current_section = None
    current_content = []
    
    # Split by lines
    lines = markdown_text.split('\n')
    
    for line in lines:
        # Check if this is a section header (pattern: **Section Name:**)
        header_match = re.match(r'^\*\*([^*]+):\*\*\s*$', line.strip())
        
        if header_match:
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            
            # Start new section
            current_section = header_match.group(1).strip()
            current_content = []
        else:
            # Add content to current section
            if current_section:
                current_content.append(line)
    
    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections

def display_analysis_results(results: Dict[str, Any]):
    """
    Display the analysis results in a formatted way.
    
    Args:
        results: Dictionary containing analysis results
    """
    st.markdown("---")
    st.markdown("## 📊 Analysis Results")
    
    # Document info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📄 Document", results['filename'])
    
    with col2:
        st.metric("📏 File Size", f"{results['file_size'] / 1024:.1f} KB")
    
    with col3:
        file_type = results.get('file_type', 'Unknown')
        st.metric("📁 File Type", file_type.upper())
    
    with col4:
        text_length = results.get('text_length', 0)
        st.metric("📝 Text Length", f"{text_length:,} chars")
    
    # Processing status
    processing_status = results.get('processing_status', 'unknown')
    if processing_status == 'success':
        st.success("✅ Document processed successfully")
    elif processing_status == 'failed':
        st.error("❌ Document processing failed")
    else:
        st.info("ℹ️ Processing status unknown")
    
    # Check if Superwise API returned structured markdown output
    superwise_output = results.get('results', {}).get('output', '')
    
    # Always create tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📋 Summary", "🔍 Key Clauses", "📋 Obligations", 
        "⚠️ Risks", "🔎 Missing Terms", "📄 Full Text"
    ])
    
    if superwise_output:
        # Parse Superwise markdown output
        parsed_sections = parse_superwise_markdown(superwise_output)
        
        # Check if parsing resulted in empty sections (plain text response)
        if not parsed_sections:
            # Display raw output in Summary tab with warning
            with tab1:
                st.warning("⚠️ The AI could not analyze this document as a legal document.")
                st.markdown("**Response:**")
                st.markdown(superwise_output)
            
            # Show info in other tabs
            with tab2:
                st.info("Key clauses cannot be extracted from non-legal documents.")
            with tab3:
                st.info("Obligations cannot be identified from non-legal documents.")
            with tab4:
                st.info("Risk assessment not available for non-legal documents.")
            with tab5:
                st.info("Missing terms analysis not available for non-legal documents.")
            with tab6:
                st.markdown("### 📄 Extracted Text")
                display_text_with_toggle(results, key_suffix="non_legal")
        else:
            # Tab 1: Summary (combine Document Type, Summary, Final Summary Insight)
            with tab1:
                summary_content = []
                if 'Document Type' in parsed_sections:
                    summary_content.append(f"**Document Type:**\n{parsed_sections['Document Type']}")
                if 'Summary' in parsed_sections:
                    summary_content.append(f"**Summary:**\n{parsed_sections['Summary']}")
                if 'Final Summary Insight' in parsed_sections:
                    summary_content.append(f"**Final Summary Insight:**\n{parsed_sections['Final Summary Insight']}")
                
                if summary_content:
                    st.markdown('\n\n'.join(summary_content))
                else:
                    st.info("Summary information not available.")
            
            # Tab 2: Key Clauses
            with tab2:
                if 'Key Clauses' in parsed_sections:
                    st.markdown(parsed_sections['Key Clauses'])
                else:
                    st.info("Key clauses not identified.")
            
            # Tab 3: Obligations
            with tab3:
                if 'Identified Obligations' in parsed_sections:
                    st.markdown(parsed_sections['Identified Obligations'])
                else:
                    st.info("Obligations not identified.")
            
            # Tab 4: Risks
            with tab4:
                if 'Risk Assessment' in parsed_sections:
                    st.markdown(parsed_sections['Risk Assessment'])
                else:
                    st.info("Risk assessment not available.")
            
            # Tab 5: Missing Terms
            with tab5:
                if 'Missing Terms' in parsed_sections:
                    st.markdown(parsed_sections['Missing Terms'])
                else:
                    st.info("Missing terms not identified.")
            
            # Tab 6: Full Text
            with tab6:
                st.markdown("### 📄 Extracted Text")
                display_text_with_toggle(results, key_suffix="legal_with_details")
                
                # Show additional details if available
                additional_info = []
                if 'Parties / Entities Involved' in parsed_sections:
                    additional_info.append(("Parties / Entities Involved", parsed_sections['Parties / Entities Involved']))
                if 'Dates / Duration' in parsed_sections:
                    additional_info.append(("Dates / Duration", parsed_sections['Dates / Duration']))
                if 'Financial Terms (if applicable)' in parsed_sections:
                    additional_info.append(("Financial Terms", parsed_sections['Financial Terms (if applicable)']))
                if 'Compliance / Legal Observations' in parsed_sections:
                    additional_info.append(("Compliance / Legal Observations", parsed_sections['Compliance / Legal Observations']))
                
                if additional_info:
                    st.markdown("---")
                    st.markdown("### 📋 Additional Information")
                    for title, content in additional_info:
                        with st.expander(f"📎 {title}"):
                            st.markdown(content)
    else:
        # Fallback to original structured format for backward compatibility
        
        with tab1:
            if results['analysis_options']['generate_summary']:
                st.markdown("### 📊 Document Summary")
                summary = results['results'].get('summary', 'Summary not available')
                st.markdown(f"""
                <div class="summary-container">
                    <p>{summary}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.info("Summary analysis was not selected.")
        
        with tab2:
            if results['analysis_options']['extract_clauses']:
                st.markdown("### 🔍 Key Clauses")
                clauses = results['results'].get('key_clauses', [])
                if clauses:
                    for i, clause in enumerate(clauses, 1):
                        st.markdown(f"""
                        <div class="clause-card">
                            <h4>Clause {i}</h4>
                            <p><strong>Type:</strong> {clause.get('type', 'Unknown')}</p>
                            <p><strong>Content:</strong> {clause.get('content', 'No content')}</p>
                            <p><strong>Importance:</strong> {clause.get('importance', 'Medium')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No key clauses identified.")
            else:
                st.info("Key clauses extraction was not selected.")
        
        with tab3:
            if results['analysis_options']['identify_obligations']:
                st.markdown("### 📋 Identified Obligations")
                obligations = results['results'].get('obligations', [])
                if obligations:
                    for i, obligation in enumerate(obligations, 1):
                        st.markdown(f"""
                        <div class="obligation-card">
                            <h4>Obligation {i}</h4>
                            <p><strong>Party:</strong> {obligation.get('party', 'Unknown')}</p>
                            <p><strong>Description:</strong> {obligation.get('description', 'No description')}</p>
                            <p><strong>Deadline:</strong> {obligation.get('deadline', 'Not specified')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No obligations identified.")
            else:
                st.info("Obligations identification was not selected.")
        
        with tab4:
            if results['analysis_options']['assess_risks']:
                st.markdown("### ⚠️ Risk Assessment")
                risks = results['results'].get('risks', [])
                if risks:
                    for i, risk in enumerate(risks, 1):
                        risk_level = risk.get('level', 'Medium')
                        risk_color = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}.get(risk_level, '🟡')
                        
                        st.markdown(f"""
                        <div class="risk-card">
                            <h4>{risk_color} Risk {i} - {risk_level}</h4>
                            <p><strong>Type:</strong> {risk.get('type', 'Unknown')}</p>
                            <p><strong>Description:</strong> {risk.get('description', 'No description')}</p>
                            <p><strong>Recommendation:</strong> {risk.get('recommendation', 'No recommendation')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No risks identified.")
            else:
                st.info("Risk assessment was not selected.")
        
        with tab5:
            if results['analysis_options']['find_missing_terms']:
                st.markdown("### 🔎 Missing Terms")
                missing_terms = results['results'].get('missing_terms', [])
                if missing_terms:
                    for i, term in enumerate(missing_terms, 1):
                        st.markdown(f"""
                        <div class="missing-term-card">
                            <h4>Missing Term {i}</h4>
                            <p><strong>Term:</strong> {term.get('term', 'Unknown')}</p>
                            <p><strong>Category:</strong> {term.get('category', 'General')}</p>
                            <p><strong>Importance:</strong> {term.get('importance', 'Medium')}</p>
                            <p><strong>Suggestion:</strong> {term.get('suggestion', 'Consider adding this term')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No missing terms identified.")
            else:
                st.info("Missing terms detection was not selected.")
        
        with tab6:
            st.markdown("### 📄 Extracted Text")
            display_text_with_toggle(results, key_suffix="fallback")
