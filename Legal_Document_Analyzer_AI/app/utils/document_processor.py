"""
Document Processor for Legal Document Analyzer

This module handles document text extraction and AI-powered analysis.
"""

import os
import tempfile
from typing import Dict, List, Any
import PyPDF2
import docx
from utils.logger import get_logger

class DocumentProcessor:
    """Handles document processing and analysis."""
    
    def __init__(self):
        self.logger = get_logger(__name__)
    
    def extract_text(self, file_path: str) -> str:
        """
        Extract text from uploaded document.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            str: Extracted text content
        """
        try:
            file_extension = os.path.splitext(file_path)[1].lower()
            
            if file_extension == '.pdf':
                return self._extract_pdf_text(file_path)
            elif file_extension in ['.doc', '.docx']:
                return self._extract_docx_text(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
                
        except Exception as e:
            self.logger.error(f"Error extracting text: {str(e)}")
            raise
    
    def _extract_pdf_text(self, file_path: str) -> str:
        """Extract text from PDF file."""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return text
        except Exception as e:
            self.logger.error(f"Error extracting PDF text: {str(e)}")
            raise
    
    def _extract_docx_text(self, file_path: str) -> str:
        """Extract text from DOCX file."""
        try:
            doc = docx.Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            self.logger.error(f"Error extracting DOCX text: {str(e)}")
            raise
    
    def analyze_document(self, text: str, analysis_options: Dict[str, bool]) -> Dict[str, Any]:
        """
        Analyze document text with AI-powered analysis.
        
        Args:
            text: Document text content
            analysis_options: Dictionary of analysis options
            
        Returns:
            Dict[str, Any]: Analysis results
        """
        self.logger.info("🤖 Starting AI document analysis")
        
        results = {}
        
        # Generate summary
        if analysis_options.get('generate_summary', False):
            results['summary'] = self._generate_summary(text)
        
        # Extract key clauses
        if analysis_options.get('extract_clauses', False):
            results['key_clauses'] = self._extract_key_clauses(text)
        
        # Identify obligations
        if analysis_options.get('identify_obligations', False):
            results['obligations'] = self._identify_obligations(text)
        
        # Assess risks
        if analysis_options.get('assess_risks', False):
            results['risks'] = self._assess_risks(text)
        
        # Find missing terms
        if analysis_options.get('find_missing_terms', False):
            results['missing_terms'] = self._find_missing_terms(text)
        
        return results
    
    def _generate_summary(self, text: str) -> str:
        """Generate document summary."""
        # This would integrate with an AI service like OpenAI, Anthropic, etc.
        # For demo purposes, returning a mock summary
        return """
        This legal document appears to be a standard service agreement between two parties. 
        The document outlines the terms and conditions for the provision of services, including 
        payment terms, delivery schedules, and liability limitations. Key areas of focus include 
        intellectual property rights, confidentiality clauses, and dispute resolution mechanisms.
        """
    
    def _extract_key_clauses(self, text: str) -> List[Dict[str, str]]:
        """Extract key clauses from the document."""
        # Mock implementation - in real app, this would use AI
        return [
            {
                'type': 'Payment Terms',
                'content': 'Payment shall be made within 30 days of invoice receipt',
                'importance': 'High'
            },
            {
                'type': 'Confidentiality',
                'content': 'Both parties agree to maintain confidentiality of proprietary information',
                'importance': 'High'
            },
            {
                'type': 'Termination',
                'content': 'Either party may terminate this agreement with 30 days written notice',
                'importance': 'Medium'
            }
        ]
    
    def _identify_obligations(self, text: str) -> List[Dict[str, str]]:
        """Identify obligations in the document."""
        # Mock implementation
        return [
            {
                'party': 'Service Provider',
                'description': 'Deliver services according to agreed specifications',
                'deadline': 'As per project timeline'
            },
            {
                'party': 'Client',
                'description': 'Make payment within 30 days of invoice',
                'deadline': '30 days from invoice date'
            }
        ]
    
    def _assess_risks(self, text: str) -> List[Dict[str, str]]:
        """Assess risks in the document."""
        # Mock implementation
        return [
            {
                'level': 'Medium',
                'type': 'Payment Risk',
                'description': 'No late payment penalties specified',
                'recommendation': 'Consider adding late payment fees and interest charges'
            },
            {
                'level': 'Low',
                'type': 'Liability Risk',
                'description': 'Limited liability clause present',
                'recommendation': 'Review liability limitations for adequacy'
            }
        ]
    
    def _find_missing_terms(self, text: str) -> List[Dict[str, str]]:
        """Find missing terms in the document."""
        # Mock implementation
        return [
            {
                'term': 'Force Majeure Clause',
                'category': 'Risk Management',
                'importance': 'High',
                'suggestion': 'Add force majeure clause to protect against unforeseen circumstances'
            },
            {
                'term': 'Data Protection Clause',
                'category': 'Compliance',
                'importance': 'Medium',
                'suggestion': 'Include GDPR/data protection compliance terms'
            }
        ]
