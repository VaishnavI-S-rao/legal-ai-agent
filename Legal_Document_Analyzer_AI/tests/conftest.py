"""
Pytest configuration file for Legal Document Analyzer tests

This file sets up the Python path so that imports work correctly.
"""

import sys
from pathlib import Path

# Add the project root and app directory to Python path
project_root = Path(__file__).parent.parent
app_dir = project_root / "app"

# Add app directory first so relative imports work
if str(app_dir) not in sys.path:
    sys.path.insert(0, str(app_dir))

# Add project root for absolute imports
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

