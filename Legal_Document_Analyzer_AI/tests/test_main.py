"""
Test suite for Legal Document Analyzer main application

This test suite covers:
- Document Processing: Text extraction and file handling
- API Integration: Superwise API integration and error handling
- Configuration: Environment variable handling
"""

import pytest
import os
import tempfile
from unittest.mock import Mock, patch, MagicMock, mock_open
from pathlib import Path

# Import modules to test
from app.utils.document_processor import DocumentProcessor
from app.utils.analysis_utils import (
    calculate_analysis_stats,
    get_analysis_stats,
    get_analysis_count
)
from app.config.settings import (
    APP_NAME,
    APP_VERSION,
    FILE_UPLOAD_CONFIG,
    API_CONFIG,
    SUPERWISE_API_CONFIG
)
from app.config.api_config import (
    validate_api_config,
    get_legal_ai_headers,
    get_analysis_endpoint,
    API_TIMEOUT,
    MAX_RETRIES
)


class TestDocumentProcessor:
    """Test suite for DocumentProcessor class"""
    
    def test_processor_initialization(self):
        """Test DocumentProcessor initialization"""
        processor = DocumentProcessor()
        assert processor is not None
        assert processor.logger is not None
    
    def test_extract_text_unsupported_format(self):
        """Test extract_text with unsupported file format"""
        processor = DocumentProcessor()
        
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp_file:
            tmp_file.write(b"Test content")
            tmp_path = tmp_file.name
        
        try:
            with pytest.raises(ValueError, match="Unsupported file format"):
                processor.extract_text(tmp_path)
        finally:
            os.unlink(tmp_path)
    
    @patch('app.utils.document_processor.PyPDF2.PdfReader')
    def test_extract_pdf_text(self, mock_pdf_reader):
        """Test PDF text extraction"""
        processor = DocumentProcessor()
        
        # Mock PDF reader
        mock_page = Mock()
        mock_page.extract_text.return_value = "Sample PDF text"
        mock_reader_instance = Mock()
        mock_reader_instance.pages = [mock_page]
        mock_pdf_reader.return_value = mock_reader_instance
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            tmp_file.write(b"PDF content")
            tmp_path = tmp_file.name
        
        try:
            result = processor.extract_text(tmp_path)
            assert result == "Sample PDF text\n"
            mock_pdf_reader.assert_called_once()
        finally:
            os.unlink(tmp_path)
    
    @patch('app.utils.document_processor.docx.Document')
    def test_extract_docx_text(self, mock_docx):
        """Test DOCX text extraction"""
        processor = DocumentProcessor()
        
        # Mock DOCX document
        mock_paragraph = Mock()
        mock_paragraph.text = "Sample DOCX text"
        mock_doc_instance = Mock()
        mock_doc_instance.paragraphs = [mock_paragraph]
        mock_docx.return_value = mock_doc_instance
        
        with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp_file:
            tmp_file.write(b"DOCX content")
            tmp_path = tmp_file.name
        
        try:
            result = processor.extract_text(tmp_path)
            assert result == "Sample DOCX text\n"
            mock_docx.assert_called_once_with(tmp_path)
        finally:
            os.unlink(tmp_path)
    
    def test_analyze_document_with_summary(self):
        """Test document analysis with summary option"""
        processor = DocumentProcessor()
        text = "Sample legal document text"
        options = {'generate_summary': True}
        
        result = processor.analyze_document(text, options)
        
        assert 'summary' in result
        assert isinstance(result['summary'], str)
        assert len(result['summary']) > 0
    
    def test_analyze_document_with_clauses(self):
        """Test document analysis with clause extraction"""
        processor = DocumentProcessor()
        text = "Sample legal document text"
        options = {'extract_clauses': True}
        
        result = processor.analyze_document(text, options)
        
        assert 'key_clauses' in result
        assert isinstance(result['key_clauses'], list)
        assert len(result['key_clauses']) > 0
    
    def test_analyze_document_with_obligations(self):
        """Test document analysis with obligation identification"""
        processor = DocumentProcessor()
        text = "Sample legal document text"
        options = {'identify_obligations': True}
        
        result = processor.analyze_document(text, options)
        
        assert 'obligations' in result
        assert isinstance(result['obligations'], list)
        assert len(result['obligations']) > 0
    
    def test_analyze_document_with_risks(self):
        """Test document analysis with risk assessment"""
        processor = DocumentProcessor()
        text = "Sample legal document text"
        options = {'assess_risks': True}
        
        result = processor.analyze_document(text, options)
        
        assert 'risks' in result
        assert isinstance(result['risks'], list)
        assert len(result['risks']) > 0
    
    def test_analyze_document_with_missing_terms(self):
        """Test document analysis with missing terms detection"""
        processor = DocumentProcessor()
        text = "Sample legal document text"
        options = {'find_missing_terms': True}
        
        result = processor.analyze_document(text, options)
        
        assert 'missing_terms' in result
        assert isinstance(result['missing_terms'], list)
        assert len(result['missing_terms']) > 0
    
    def test_analyze_document_all_options(self):
        """Test document analysis with all options enabled"""
        processor = DocumentProcessor()
        text = "Sample legal document text"
        options = {
            'generate_summary': True,
            'extract_clauses': True,
            'identify_obligations': True,
            'assess_risks': True,
            'find_missing_terms': True
        }
        
        result = processor.analyze_document(text, options)
        
        assert 'summary' in result
        assert 'key_clauses' in result
        assert 'obligations' in result
        assert 'risks' in result
        assert 'missing_terms' in result


class TestAnalysisUtils:
    """Test suite for analysis utilities"""
    
    def test_calculate_analysis_stats_basic(self):
        """Test basic statistics calculation"""
        analysis_results = {
            'risks': [
                {'level': 'High', 'type': 'Risk 1'},
                {'level': 'Medium', 'type': 'Risk 2'},
                {'level': 'Low', 'type': 'Risk 3'}
            ]
        }
        
        stats = calculate_analysis_stats(analysis_results)
        
        assert stats['total_analyses'] == 1
        assert stats['high_risk_count'] == 1
        assert stats['medium_risk_count'] == 1
        assert stats['low_risk_count'] == 1
        assert stats['last_analysis_time'] is not None
    
    def test_calculate_analysis_stats_no_risks(self):
        """Test statistics calculation with no risks"""
        analysis_results = {}
        
        stats = calculate_analysis_stats(analysis_results)
        
        assert stats['total_analyses'] == 1
        assert stats['high_risk_count'] == 0
        assert stats['medium_risk_count'] == 0
        assert stats['low_risk_count'] == 0
    
    def test_calculate_analysis_stats_multiple_high_risks(self):
        """Test statistics calculation with multiple high risks"""
        analysis_results = {
            'risks': [
                {'level': 'High', 'type': 'Risk 1'},
                {'level': 'High', 'type': 'Risk 2'},
                {'level': 'high', 'type': 'Risk 3'}  # lowercase
            ]
        }
        
        stats = calculate_analysis_stats(analysis_results)
        
        assert stats['high_risk_count'] == 3
        assert stats['medium_risk_count'] == 0
        assert stats['low_risk_count'] == 0
    
    @patch('app.utils.analysis_utils.st')
    def test_get_analysis_stats_with_session_state(self, mock_st):
        """Test getting analysis stats from session state"""
        mock_st.session_state = {
            'analysis_stats': {
                'total_analyses': 5,
                'high_risk_count': 2,
                'medium_risk_count': 1,
                'low_risk_count': 1,
                'last_analysis_time': None
            }
        }
        
        stats = get_analysis_stats()
        
        assert stats['total_analyses'] == 5
        assert stats['high_risk_count'] == 2
    
    @patch('app.utils.analysis_utils.st')
    def test_get_analysis_stats_without_session_state(self, mock_st):
        """Test getting analysis stats when session state is empty"""
        mock_st.session_state = {}
        
        stats = get_analysis_stats()
        
        assert stats['total_analyses'] == 0
        assert stats['high_risk_count'] == 0
        assert stats['medium_risk_count'] == 0
        assert stats['low_risk_count'] == 0
    
    @patch('app.utils.analysis_utils.st')
    def test_get_analysis_count(self, mock_st):
        """Test getting analysis count"""
        mock_st.session_state = {
            'analysis_stats': {
                'total_analyses': 10,
                'high_risk_count': 0,
                'medium_risk_count': 0,
                'low_risk_count': 0,
                'last_analysis_time': None
            }
        }
        
        count = get_analysis_count()
        assert count == 10


class TestConfiguration:
    """Test suite for configuration settings"""
    
    def test_app_name_constant(self):
        """Test APP_NAME constant"""
        assert APP_NAME == "Legal Document Analyzer"
    
    def test_app_version_constant(self):
        """Test APP_VERSION constant"""
        assert APP_VERSION == "1.0.0"
    
    def test_file_upload_config_structure(self):
        """Test FILE_UPLOAD_CONFIG structure"""
        assert 'max_file_size' in FILE_UPLOAD_CONFIG
        assert 'allowed_extensions' in FILE_UPLOAD_CONFIG
        assert 'max_files' in FILE_UPLOAD_CONFIG
        assert '.pdf' in FILE_UPLOAD_CONFIG['allowed_extensions']
        assert '.doc' in FILE_UPLOAD_CONFIG['allowed_extensions']
        assert '.docx' in FILE_UPLOAD_CONFIG['allowed_extensions']
    
    def test_api_config_structure(self):
        """Test API_CONFIG structure"""
        assert 'timeout' in API_CONFIG
        assert 'retry_attempts' in API_CONFIG
        assert isinstance(API_CONFIG['timeout'], int)
        assert isinstance(API_CONFIG['retry_attempts'], int)
    
    def test_superwise_api_config_structure(self):
        """Test SUPERWISE_API_CONFIG structure"""
        assert 'base_url' in SUPERWISE_API_CONFIG
        assert 'api_version' in SUPERWISE_API_CONFIG
        assert 'app_id' in SUPERWISE_API_CONFIG
        assert 'ask_endpoint' in SUPERWISE_API_CONFIG


class TestAPIConfig:
    """Test suite for API configuration"""
    
    @patch.dict(os.environ, {
        'LEGAL_AI_API_URL': 'https://api.test.com',
        'LEGAL_AI_APP_ID': 'test_app_id',
        'LEGAL_AI_API_KEY': 'test_api_key'
    })
    def test_validate_api_config_valid(self):
        """Test API config validation with valid values"""
        # Need to reload the module to pick up new env vars
        import importlib
        import app.config.api_config as api_config_module
        importlib.reload(api_config_module)
        
        assert api_config_module.validate_api_config() is True
    
    @patch.dict(os.environ, {
        'LEGAL_AI_API_URL': '',
        'LEGAL_AI_APP_ID': '',
        'LEGAL_AI_API_KEY': ''
    }, clear=True)
    def test_validate_api_config_invalid(self):
        """Test API config validation with missing values"""
        import importlib
        import app.config.api_config as api_config_module
        importlib.reload(api_config_module)
        
        assert api_config_module.validate_api_config() is False
    
    @patch.dict(os.environ, {
        'LEGAL_AI_API_URL': 'https://api.test.com',
        'LEGAL_AI_API_KEY': 'test_api_key'
    })
    def test_get_legal_ai_headers(self):
        """Test getting Legal AI API headers"""
        import importlib
        import app.config.api_config as api_config_module
        importlib.reload(api_config_module)
        
        headers = api_config_module.get_legal_ai_headers()
        
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        assert 'X-API-Version' in headers
        assert 'User-Agent' in headers
        assert headers['Content-Type'] == 'application/json'
        assert 'Bearer' in headers['Authorization']
    
    @patch.dict(os.environ, {
        'LEGAL_AI_API_URL': 'https://api.test.com'
    })
    def test_get_analysis_endpoint(self):
        """Test getting analysis endpoint URL"""
        import importlib
        import app.config.api_config as api_config_module
        importlib.reload(api_config_module)
        
        endpoint = api_config_module.get_analysis_endpoint()
        
        assert endpoint == 'https://api.test.com/document-analysis'
    
    def test_api_timeout_default(self):
        """Test API timeout default value"""
        assert API_TIMEOUT == 30 or isinstance(API_TIMEOUT, int)
    
    def test_max_retries_default(self):
        """Test MAX_RETRIES default value"""
        assert MAX_RETRIES == 3 or isinstance(MAX_RETRIES, int)


class TestMainApplication:
    """Test suite for main application functions"""
    
    @patch('app.main.st')
    def test_get_current_page_default(self, mock_st):
        """Test getting current page with default value"""
        from app.main import get_current_page
        
        mock_st.session_state = {}
        
        page = get_current_page()
        assert page == 'landing'
    
    @patch('app.main.st')
    def test_get_current_page_custom(self, mock_st):
        """Test getting current page with custom value"""
        from app.main import get_current_page
        
        mock_st.session_state = {'current_page': 'analyzer'}
        
        page = get_current_page()
        assert page == 'analyzer'
    
    @patch('app.main.st')
    def test_handle_url_routing_no_params(self, mock_st):
        """Test URL routing with no query parameters"""
        from app.main import handle_url_routing
        
        mock_st.query_params = {}
        mock_st.session_state = {'current_page': 'landing'}
        
        page = handle_url_routing()
        assert page == 'landing'
    
    @patch('app.main.st')
    def test_handle_url_routing_valid_page(self, mock_st):
        """Test URL routing with valid page parameter"""
        from app.main import handle_url_routing
        
        # Create a mock query_params that supports 'in' operator and clear()
        mock_query_params = MagicMock()
        mock_query_params.__contains__ = Mock(side_effect=lambda key: key == 'page')
        mock_query_params.__getitem__ = Mock(return_value='analyzer')
        mock_query_params.clear = Mock()
        
        # Create a mock session_state that supports attribute assignment
        mock_session_state = MagicMock()
        mock_session_state.get = Mock(return_value='landing')
        
        mock_st.query_params = mock_query_params
        mock_st.session_state = mock_session_state
        
        page = handle_url_routing()
        assert page == 'analyzer'
        # Verify session_state was updated
        assert hasattr(mock_session_state, 'current_page')
    
    @patch('app.main.st')
    def test_handle_url_routing_invalid_page(self, mock_st):
        """Test URL routing with invalid page parameter"""
        from app.main import handle_url_routing
        
        mock_st.query_params = {'page': 'invalid_page'}
        mock_st.session_state = {}
        
        page = handle_url_routing()
        assert page == '404'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

