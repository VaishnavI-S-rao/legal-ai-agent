"""
Analysis Utilities for Legal Document Analyzer

This module contains utility functions for analysis statistics and data management.
"""

import streamlit as st
from datetime import datetime
from typing import Dict, Any
from utils.logger import get_logger

def calculate_analysis_stats(analysis_results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate statistics from analysis results.
    
    Args:
        analysis_results: Dictionary containing analysis results
        
    Returns:
        Dict[str, Any]: Calculated statistics
    """
    stats = {
        "total_analyses": 1,
        "high_risk_count": 0,
        "medium_risk_count": 0,
        "low_risk_count": 0,
        "last_analysis_time": datetime.now()
    }
    
    # Count risks by level
    risks = analysis_results.get('risks', [])
    for risk in risks:
        risk_level = risk.get('level', 'Medium').lower()
        if risk_level == 'high':
            stats['high_risk_count'] += 1
        elif risk_level == 'medium':
            stats['medium_risk_count'] += 1
        elif risk_level == 'low':
            stats['low_risk_count'] += 1
    
    return stats

def update_analysis_stats(analysis_results: Dict[str, Any]):
    """
    Update session state analysis statistics.
    
    Args:
        analysis_results: Dictionary containing analysis results
    """
    logger = get_logger(__name__)
    
    # Calculate new stats
    new_stats = calculate_analysis_stats(analysis_results)
    
    # Update session state
    if 'analysis_stats' not in st.session_state:
        st.session_state.analysis_stats = {
            "total_analyses": 0,
            "high_risk_count": 0,
            "medium_risk_count": 0,
            "low_risk_count": 0,
            "last_analysis_time": None
        }
    
    # Add to existing stats
    st.session_state.analysis_stats['total_analyses'] += new_stats['total_analyses']
    st.session_state.analysis_stats['high_risk_count'] += new_stats['high_risk_count']
    st.session_state.analysis_stats['medium_risk_count'] += new_stats['medium_risk_count']
    st.session_state.analysis_stats['low_risk_count'] += new_stats['low_risk_count']
    st.session_state.analysis_stats['last_analysis_time'] = new_stats['last_analysis_time']
    
    logger.info(f"📊 Updated analysis stats: {st.session_state.analysis_stats}")

def get_analysis_stats() -> Dict[str, Any]:
    """
    Get current analysis statistics from session state.
    
    Returns:
        Dict[str, Any]: Current analysis statistics
    """
    return st.session_state.get('analysis_stats', {
        "total_analyses": 0,
        "high_risk_count": 0,
        "medium_risk_count": 0,
        "low_risk_count": 0,
        "last_analysis_time": None
    })

def get_analysis_count() -> int:
    """
    Get total number of analyses performed.
    
    Returns:
        int: Total analysis count
    """
    stats = get_analysis_stats()
    return stats.get('total_analyses', 0)
