<div align="left">



<a href="https://superwise.ai/" target="_blank">
<img src="app/assets/superwise_logo.svg" alt="SUPERWISE® Logo" width="350"/></a>

**Powered by SUPERWISE® — Leading Agentic Governance & Operations Solutions**

[![Powered by SUPERWISE®](https://img.shields.io/badge/Powered%20by-SUPERWISE®-0052CC?style=for-the-badge&logo=superuser)](https://superwise.ai)
[![AI Legal Tech](https://img.shields.io/badge/AI%20Legal-Document%20Analysis-8B5CF6?style=for-the-badge&logo=scale)](https://superwise.ai)
[![Enterprise Ready](https://img.shields.io/badge/Enterprise-Ready-gold?style=for-the-badge&logo=enterprise)](https://superwise.ai)

</div>
<h2>Legal Document Analyzer</h2>
A modern AI-powered legal document analysis application built with Streamlit, featuring intelligent document review, clause extraction, and risk assessment with Superwise AI integration.

**Legal Document Analyzer** is an intelligent system designed to help lawyers, compliance officers, and business teams analyze legal documents efficiently.

The system analyzes **legal documents** — including contracts, agreements, corporate documents, compliance policies, and legal filings — and provides **AI-driven insights** including key clauses, obligations, risks, and missing terms to help users understand document implications quickly.

The solution integrates **Superwise AI** to provide intelligent legal document analysis while maintaining responsible AI governance and safety standards.

As this is a **demo project**, the analysis data used is **synthetic and non-real**, meaning it does **not contain any actual legal case data or client information**.  
For production environments, encryption and data security measures are **strongly recommended** to meet legal document privacy requirements.

### **Key Benefits**
- Provides intelligent legal document analysis with comprehensive insights.  
- Saves hours of manual review time with automated clause extraction.  
- Demonstrates responsible AI usage with built-in safety guardrails.  
- Offers professional interface for legal document review.  

## 🏢 **Ready for Business?**

**Transform your business operations with Superwise AI**: [Get Started with Superwise](https://docs.superwise.ai/docs/introduction-to-superwise) - Enterprise-grade AI governance, risk & compliance solutions for legal and other businesses.

<h3>🚀 Quick Start</h3>


### Prerequisites

- **Superwise Account**: Create account and application (see [Superwise Agent Setup Guide](docs/SUPERWISE_AGENT_SETUP_GUIDE.md#prerequisites--account-setup))

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd legal-document-analyzer-ai
   ```

2. **Set up environment variables**:
   
   **Linux/Mac:**
   ```bash
   cp .env.example .env
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   copy .env.example .env
   ```
   
   **Windows (PowerShell):**
   ```powershell
   Copy-Item .env.example .env
   ```
   
   **All Systems:** Edit the `.env` file with your Superwise Agent credentials (see [Superwise Agent Setup Guide](docs/SUPERWISE_AGENT_SETUP_GUIDE.md))

### Option 1: Docker (Recommended)

1. **Prerequisites**: 
   - Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. **Quick Launch**:
   ```bash
   # Build and run
   docker-compose up --build
   
   # Run in background
   docker-compose up -d
   
   # Stop
   docker-compose down
   ```

3. Open your browser and navigate to `http://localhost:9000`

### Option 2: Local Python Installation

1. **Prerequisites**:
   - Python 3.11+ installed

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app/main.py --server.port 9000
   ```

4. Open your browser and navigate to `http://localhost:9000`

## ✨ Features

- **🔍 Smart Clause Extraction**: Superwise AI automatically identifies and extracts key legal clauses from documents
- **⚠️ Risk Assessment**: AI-powered risk analysis to identify potential legal risks and one-sided terms
- **📋 Obligation Identification**: Extract and categorize contractual obligations for all parties
- **🔎 Missing Terms Detection**: Identify missing or incomplete standard clauses
- **📊 Comprehensive Summaries**: Generate detailed document summaries with structured insights
- **📄 Multi-Format Support**: Support for PDF, DOC, and DOCX files (up to 10MB)
- **🔄 Real-time Analysis**: Immediate document analysis and recommendations with confidence scoring

## 🛡️ Guardrails & Safety

### **Safety System**
- **Confidential Information Protection**: Automatic identification and protection of sensitive legal information
- **Document Classification**: Intelligent categorization into appropriate document types (contracts, agreements, policies, etc.)
- **Privacy Validation**: Built-in privacy checks and validation alerts
- **Context Awareness**: Maintains document context for accurate analysis

**Where to Find Safety Features:**
- **Document Analyzer Interface**: Real-time privacy alerts during document upload
- **Analysis Results**: Clear risk indicators and missing terms identification
- **Review Tracking**: Privacy alerts and sensitive information detection in analysis history
- **Analytics**: Risk metrics and compliance gap patterns

### **AI Governance & Monitoring**
- **Response Quality**: AI confidence scoring and response validation
- **Error Handling**: Graceful handling of API failures and timeouts
- **Logging System**: Comprehensive logging with file and console output
- **Health Checks**: Docker health monitoring with Streamlit health endpoints

**Where to Find Monitoring:**
- **Logs**: Check `logs/` directory for detailed application logs
- **Docker Health**: Monitor container health via `docker-compose ps`
- **Analysis History**: View AI confidence scores and response quality
- **Error Handling**: Monitor API failures and system events

## 🏗️ Project Structure

```
legal-document-analyzer-ai/
├── app/
│   ├── components/              # Reusable UI components
│   │   ├── header.py            # Application header
│   │   ├── landing_page.py      # Landing page component
│   │   ├── document_analyzer.py # Document analysis interface
│   │   └── error_404.py         # Error page component
│   ├── config/                  # Configuration settings
│   │   ├── settings.py          # Application settings
│   │   └── api_config.py        # Superwise API configuration
│   ├── utils/                   # Utility functions
│   │   ├── css_styles.py        # Custom CSS styles
│   │   ├── logger.py            # Logging utilities
│   │   ├── document_processor.py # Document processing and analysis
│   │   └── analysis_utils.py    # Analysis statistics utilities
│   ├── assets/                  # Static assets
│   │   ├── legal_analyzer_logo.svg # Legal analyzer branding
│   │   └── legal_icon.svg       # Application icon
│   └── main.py                  # Main application entry point
├── tests/                       # Test files
│   ├── __init__.py             # Test package initialization
│   └── test_main.py            # Main application tests
├── docs/                        # Documentation files
│   ├── DOCKER_README.md         # Docker setup guide
│   ├── PROJECT_OVERVIEW.md      # Project architecture overview
│   └── SUPERWISE_AGENT_SETUP_GUIDE.md # Superwise Agent setup guide
├── logs/                        # Application logs
├── requirements.txt             # Python dependencies
├── docker-compose.yml          # Docker configuration
├── Dockerfile                  # Docker image definition
├── .env.example                # Environment variables template
├── LICENSE                     # MIT License
└── README.md                   # This file
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Document Processing**: PyPDF2, python-docx
- **Data Processing**: Pandas, NumPy
- **AI Integration**: Superwise API
- **Styling**: Custom CSS with Streamlit components
- **Containerization**: Docker & Docker Compose
- **Environment**: Python 3.11+

## 📚 Documentation

For detailed information about specific aspects of the project, please refer to:

- **[Docker Setup Guide](docs/DOCKER_README.md)** - Comprehensive Docker deployment instructions
- **[Project Overview](docs/PROJECT_OVERVIEW.md)** - Detailed architecture and feature descriptions
- **[Superwise Agent Setup Guide](docs/SUPERWISE_AGENT_SETUP_GUIDE.md)** - AI integration setup and usage

## 🔧 Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# Superwise API Configuration
SUPERWISE_API_URL=https://api.superwise.ai/
SUPERWISE_API_VERSION=v1
SUPERWISE_APP_ID=YOUR_SUPERWISE_APP_ID

# API Timeout Settings
API_TIMEOUT=30
MAX_RETRIES=3
RETRY_DELAY=1

# File Upload Settings
MAX_FILE_SIZE_MB=10
```

**Note**: The Superwise API configuration is required for AI features to work properly.

## 🔒 Data Privacy & Compliance

### **Important Disclaimers**

⚠️ **This application uses SYNTHETIC DUMMY DATA for demonstration purposes only.**

- **No Real Legal Data**: All analysis results in this application are artificially generated
- **Educational Purpose**: This is a demonstration/educational project, not a production legal system
- **Data Sources**: Analysis data is generated through mock data generators

🚨 **CRITICAL SECURITY LIMITATIONS - NOT PRODUCTION READY:**

- **No Authentication**: Application has no user login or authentication system
- **No Authorization**: No access controls or user permission management
- **No Data Encryption**: Legal document data is stored and transmitted without encryption
- **No Session Management**: No secure session handling or user state management
- **No Access Logging**: No audit trails for data access or user activities
- **No Input Validation**: Limited input sanitization and validation
- **No HTTPS Enforcement**: No SSL/TLS encryption for data transmission

**⚠️ DO NOT USE WITH REAL LEGAL DOCUMENTS - FOR DEMONSTRATION ONLY**

### **Legal Compliance & Attorney-Client Privilege Considerations**

**For Production Use:**
- **Legal Compliance**: Ensure proper legal compliance before handling real legal documents
- **Attorney-Client Privilege**: Implement proper safeguards to maintain attorney-client privilege
- **Data Encryption**: Use encryption for data at rest and in transit
- **Access Controls**: Implement proper user authentication and authorization
- **Audit Logging**: Maintain comprehensive audit trails for all data access
- **Business Associate Agreements**: Ensure all third-party services (like Superwise API) have proper data processing agreements
- **Professional Review**: Ensure all AI analysis is reviewed by qualified legal professionals

**Current Implementation:**
- ✅ **Synthetic Data Only**: No real legal documents are processed
- ✅ **Local Processing**: Data stays within your local environment
- ✅ **No External Storage**: No data is sent to external databases
- ⚠️ **API Integration**: Superwise API calls may transmit document text (configure accordingly)

### **Legal Advice Disclaimer**

**This application is NOT a substitute for legal counsel.** It provides document analysis and informational insights only. Legal advice requires the expertise of qualified legal professionals who can consider all relevant facts, laws, and circumstances. This application serves as an analytical tool for educational purposes and should not be used as the sole basis for legal decisions.

### **Security Best Practices**

1. **Environment Variables**: Never commit real API keys or sensitive data
2. **Data Validation**: Implement proper input validation and sanitization
3. **Error Handling**: Avoid exposing sensitive information in error messages
4. **Logging**: Be cautious about logging sensitive legal data
5. **Network Security**: Use HTTPS in production environments

**Note**: This application is for educational/demonstration purposes. For production legal applications, consult with legal and compliance experts regarding data protection and attorney-client privilege requirements.


## 🧪 Testing & Code Quality

### **Linting & Code Formatting**

This project uses automated code quality tools to maintain consistent code style and catch potential issues.

**Run Linting:**
```bash
# Check code style and catch issues
flake8 app/

# Format code automatically
black app/
```

### **Running Tests**

#### **Option 1: With Docker (Recommended)**

```bash
# Run all tests in Docker container
docker-compose exec legal-analyzer pytest tests/ -v

# Run tests with coverage
docker-compose exec legal-analyzer pytest tests/ --cov=app --cov-report=html

# Run specific test file
docker-compose exec legal-analyzer pytest tests/test_main.py -v
```

#### **Option 2: Local Python Installation**

```bash
# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_main.py -v
```

### **Test Coverage**

The test suite covers:
- **Document Processing**: Text extraction and file handling
- **API Integration**: Superwise API integration and error handling
- **Configuration**: Environment variable handling

**View Coverage Report:**
```bash
# Generate HTML coverage report
pytest tests/ --cov=app --cov-report=html
# Open htmlcov/index.html in your browser
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. **Run tests**: `pytest tests/ -v`
5. **Check code quality**: `flake8 app/ && black app/`
6. Add tests for new functionality
7. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the [documentation files](#-documentation) above
- Review the [Docker Setup Guide](docs/DOCKER_README.md) for deployment issues
- Consult the [Superwise Agent Setup Guide](docs/SUPERWISE_AGENT_SETUP_GUIDE.md) for AI integration help
