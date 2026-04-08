# Superwise API Integration Guide

This guide explains how to set up and use the Superwise API integration in Legal Document Analyzer.

## 🔑 Prerequisites & Account Setup

### **Step 1: Create Superwise Account**

1. **Sign Up**: Visit [Superwise Platform](https://platform.superwise.ai/) and create a free account
2. **Verify Email**: Complete email verification process
3. **Access Dashboard**: Log in to your Superwise dashboard

**Note**: You'll also need an **OpenAI API key** for the model setup (Step 7). If you don't have one, create an account at [OpenAI Platform](https://platform.openai.com/) and generate an API key.

### **Step 2: Create Agent**

1. **Navigate to Agents**: In your Superwise dashboard, go to "Agents" section
2. **Create New Agent**: Click "Create" button from top right corner
3. **Agent Creation Dialog**: A dialog will open with the following fields:
   - **Name**: Enter `Legal Document Analyzer` (or your preferred name)
   - **Agent source**: Choose **"Build with Superwise Studio"** (not Integrate with Flowise) and click on **Next** button
4. **Agent Type**: Select **"Basic LLM Assistant"** (option 1)
     - Available options:
       - **Basic LLM Assistant (option 1)** ← Select this one
       - AI-Assistant Retrieval (option 2)
       - Advanced Agent (option 3)
5. **Complete Creation**: Click "Create" to create the agent
6. **Agent Dashboard**: After clicking "Done", you'll see the agent dashboard with:
   - **Top Left**: Agent name
   - **Top Right**: Three dots menu: click on and select **Copy ID** (this is for your `.env` file)
   - **Top Center**: There are 3 tabs:
      - **Overview**: In this tab you can see **Agent Details**, **Description** and **Metrics** section
      - **Builder**: In this tab you can see **Setup** and **Guardrails** menu on the left side and **Chat playground** on the right side
         - **Setup**:
            - **"+Model"**: Add AI models to your agent
            - **"Prompt"**: Configure prompts and instructions
            - **Chat Playground**: Interactive testing area for your agent
         - **Guardrails**: Configure safety and compliance rules
            - **+ Rule**: Add Guardrail Rules for input and output
      - **Settings**:
         - **"Authentication"**: Set up API authentication
         - **Observability**: Integrate your agent with Superwise observability to gain real-time data about your agent's behavior, usage, and potential feedback.
      - **"Publish"**: Publish your agent

### **Step 3: Configure Model**
   - **Click "+Model" Button**: Located in the top right of the dashboard
   - **Model Provider Dialog**: A dialog will open with provider options:
     - OpenAI
     - Google AI
     - Anthropic
     - Other providers
   - **Select Provider**: Choose **"OpenAI"** as the model provider
   - **Prerequisites**: Ensure you have an OpenAI API key/token
   - **Model Selection**: Select **"gpt-4"** (recommended model)
   - **API Configuration**:
     - **API Token Box**: Enter your OpenAI API key/token
     - **Click "Save"**: Complete the model setup

### **Step 4: Configure Prompt**
   - **Navigate to Prompt Section**: Click on "Prompt" under Builder->Setup tab
   - **Add System Prompt**: Copy and paste the following prompt into the prompt dialog box:

   ```
   You are a Legal Document Analysis Agent.  
You are not a lawyer and do not provide legal advice, opinions, or enforceable interpretations.  
You provide educational, analytical, and informational insights derived from legal text using AI language understanding.

### 🎯 Objective:
Analyze the provided legal or corporate document content and generate a structured summary with extracted insights, key clauses, identified obligations, risks, and compliance observations.

### 🧾 Document Categories You Can Handle:
1. **Contracts / Agreements**
   - Examples: NDA, Employment Contract, Service Agreement, Vendor Agreement
   - Extract: Key clauses (Termination, Confidentiality, Payment Terms, Liability), parties, dates, risks, and missing clauses.

2. **Corporate Documents**
   - Examples: MOU, Partnership Agreement, Shareholder Agreement
   - Extract: Parties involved, ownership structures, responsibilities, duration, renewal conditions, and risks.

3. **Financial / Loan Documents**
   - Examples: Loan Agreement, Term Sheet, Repayment Schedule
   - Extract: Principal amount, interest rate, repayment terms, tenure, default conditions, collateral, and risks.

4. **Legal Filings / Judgments**
   - Examples: Court Orders, Case Summaries
   - Extract: Case title, parties, background, legal issue, judgment summary, decision, and key precedents.

5. **Compliance Policies**
   - Examples: Privacy Policy, Data Sharing Agreement, Regulatory Compliance Document
   - Extract: Policy sections, compliance obligations, missing regulatory clauses (e.g., GDPR, IT Act), and gaps.

### ⚙️ Output Format:
Return the analysis in the following structured text format:

**Document Type:**  
(e.g., Contract / MOU / Loan Agreement / Compliance Policy / Judgment)

**Summary:**  
(A concise 4–6 sentence overview in plain English)

**Key Clauses:**  
- Clause 1: Title → Summary  
- Clause 2: Title → Summary  
- Clause 3: Title → Summary  

**Identified Obligations:**  
- (List all obligations of each party — payment duties, service commitments, confidentiality, etc.)

**Parties / Entities Involved:**  
- Party A:  
- Party B:  

**Dates / Duration:**  
- Effective Date:  
- Expiry / Renewal:  

**Financial Terms (if applicable):**  
- Principal Amount:  
- Interest Rate:  
- Repayment Schedule:  
- Penalties:  

**Risk Assessment:**  
- (List potential risks, vague terms, or one-sided clauses)

**Missing Terms:**  
- (Mention any standard clauses not found, e.g., termination, indemnity, confidentiality)

**Compliance / Legal Observations:**  
- (List compliance gaps, missing obligations, or non-standard terms)

**Final Summary Insight:**  
(A concise paragraph summarizing the document’s purpose, major risks, and overall compliance health)

### 🧩 Instructions:
- Automatically infer the document type based on the input text.  
- Focus on clarity and precision — highlight meaningful insights for quick review.  
- Be neutral and factual; avoid giving legal advice or definitive judgments.  
- If the text doesn’t appear to be a legal or formal document, respond with:  
  “The provided text does not appear to be a legal or formal document.”
   ```

   - **Save Prompt**: Click "Save" to save the prompt configuration

### **Step 5: Configure Guardrails**

Set up safety and compliance rules to protect sensitive legal document information:

1. **Navigate to Guardrails**: Click on "Guardrails" under Builder tab
2. **Add Input Rule**: Click "+ Rule" button to add a new guardrail rule
3. **Select Rule Type**: Choose **"Restricted topics input"** from the available rule types
4. **Configure Input Rule**:
   - **Name**: Enter `Sensitive Legal Information Input`
   - **Configuration**: Select **"Legal Document Privacy"** or **"Confidential Information"** from the dropdown
   - **Specific Fields**: Configure protection for:
     - Client Names and Identifiers
     - Financial Information
     - Confidential Business Terms
     - Personal Identifiable Information (PII)
     - Trade Secrets
   - **Model**: Select **"OpenAI"** as the model provider
   - **Model Version**: Choose **"gpt-4o"** (or your preferred model)
   - **API Token**: Enter your OpenAI API key/token
   - **Save Rule**: Click "Save" to create the input guardrail rule

5. **Add Output Rule**: Click "+ Rule" button again to add an output guardrail
6. **Configure Output Rule**:
   - **Rule Type**: Select **"Restricted topics output"**
   - **Name**: Enter `Sensitive Legal Information Output`
   - **Configuration**: Select **"Legal Document Privacy"** or **"Confidential Information"** from the dropdown
   - **Specific Fields**: Configure protection for:
     - Client Names and Identifiers
     - Financial Information
     - Confidential Business Terms
     - Personal Identifiable Information (PII)
     - Trade Secrets
   - **Model**: Select **"OpenAI"** as the model provider
   - **Model Version**: Choose **"gpt-4o"** (or your preferred model)
   - **API Token**: Enter your OpenAI API key/token
   - **Save Rule**: Click "Save" to create the output guardrail rule

**Purpose**: These guardrails ensure that:
- **Input Protection**: Prevents sensitive legal information from being exposed during processing
- **Output Protection**: Ensures the AI doesn't generate or expose sensitive legal data
- **Compliance**: Helps maintain legal compliance and attorney-client privilege standards
- **Confidentiality**: Protects client information and confidential business terms

### **Step 6: Publish Application**
   - **Click "Publish" Button**: Located in the top right of the dashboard
   - **Wait for Processing**: The system will process your configuration (may take a few minutes)
   - **Check Status**: Monitor the application status on the right side top near "Created at"
   - **Status Confirmation**: Once ready, you'll see status change to **"Available"**

✅ **Congratulations! Your Superwise application is now ready to use.**

### **Step 7: Get Credentials**
   - **App ID**: Located in three dots menu: click on and select **Copy ID** (top left) - **Copy this for your project**
   - **API URL**: Base URL for API calls (usually `https://api.superwise.ai/`)
   - **API Version**: Current API version (usually `v1`)

## 🔧 Configuration Setup

### **Step 8: Configure Project Environment Variables**

Now that your Superwise application is ready, you need to configure it in your Legal Document Analyzer project:

1. **Copy Template**: 
   
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

2. **Edit Configuration**:
   ```bash
   # Superwise API Settings
   SUPERWISE_API_URL=https://api.superwise.ai/
   SUPERWISE_API_VERSION=v1
   SUPERWISE_APP_ID=your_app_id_here
   
   # API Timeout Settings (in seconds)
   API_TIMEOUT=30
   
   # Retry Settings
   MAX_RETRIES=3
   RETRY_DELAY=1
   
   # File Upload Settings
   MAX_FILE_SIZE_MB=10
   ```

3. **Replace App ID**: Update `SUPERWISE_APP_ID` with your actual App ID from Step 7 (the one you copied from the Superwise dashboard)

### **Step 9: Test Integration**

1. **Start Application**: Run the application using Docker or local Python
2. **Navigate to Document Analyzer**: Go to the main document analysis page
3. **Test AI Analysis**: Upload a document and click "Analyze Document" button
4. **Verify Connection**: Check for successful API response or error messages

### **Troubleshooting**

**Common Issues:**
- **Wrong Framework Selected**: Ensure you selected "Superwise Framework" (not Flowise Framework) during app creation
- **Wrong Application Type**: Make sure you selected "Basic LLM Assistant" (option 1) in the application type dialog
- **Invalid App ID**: Double-check your App ID in Superwise dashboard
- **API URL Issues**: Ensure `SUPERWISE_API_URL` matches your Superwise region
- **Timeout Errors**: Increase `API_TIMEOUT` value if experiencing slow responses
- **Authentication Errors**: Verify your Superwise account is active and has proper permissions

**Need Help?**
- Review Superwise documentation: [Superwise Docs](https://docs.superwise.ai/)
- Contact Superwise support for API-related issues

## 🚀 Usage

### How it Works

1. **Document Upload**: User uploads a legal document (PDF, DOC, DOCX)
2. **Text Extraction**: System extracts text from the document
3. **API Call**: System calls the Superwise API with document text
4. **Analysis**: AI processes the document and provides comprehensive analysis
5. **Response**: Displays analysis results including clauses, risks, obligations, and recommendations

### API Payload Structure

The system sends document text to Superwise for legal document analysis:

```json
{
  "input": "Here is the legal document content: [extracted document text]",
  "chat_history": []
}
```

**Fields Sent to Superwise:**
- **Document Text**: Extracted text content from uploaded document
- **Document Type**: Type of legal document (contract, agreement, etc.)
- **Analysis Options**: Selected analysis categories (clauses, risks, obligations, etc.)

**Privacy Note**: The system only sends document text required for analysis. Sensitive client information is protected through guardrails, but users should be cautious with highly confidential documents in demo environments.

## 🔍 Error Handling

The system handles various error scenarios:

- **Configuration Error**: Missing API key or URL
- **Timeout**: API request takes too long
- **Network Error**: Connection issues
- **API Error**: Server returns error status
- **Document Processing Error**: Issues with document extraction
- **Unexpected Error**: Other unexpected issues

## 📝 Logging

All API calls are logged with:
- Request details
- Response status
- Error messages (if any)
- Document processing information
- Session ID for tracking

## 🛠️ Customization

### Modify API Endpoint

Edit `app/config/api_config.py` to change:
- API URL
- Headers
- Timeout settings
- Retry logic

### Custom Payload

Modify the `payload` structure in document processing functions to send different data to Superwise.

### Response Formatting

Update the response formatting in the document analyzer component to display different information from the API response.

## 🔒 Security Notes

- API keys are stored in environment variables
- Never hardcode API keys in source code
- Use HTTPS for all API communications
- Implement rate limiting if needed
- Monitor API usage and costs
- Protect sensitive legal documents
- Follow attorney-client privilege guidelines

## 🧪 Testing

### Test API Connection

```python
# Test the API configuration
from app.config.api_config import validate_api_config
print(validate_api_config())  # Should return True if configured correctly
```

### Mock API for Development

For development without real API calls, you can modify the document processing function to return mock data:

```python
def analyze_document_with_ai(document_text):
    # Mock response for development
    return {
        "success": True,
        "data": {
            "summary": "Sample contract analysis...",
            "clauses": ["Clause 1: Payment Terms", "Clause 2: Delivery Terms"],
            "risks": ["Risk 1: Limited liability cap", "Risk 2: Unclear termination terms"],
            "obligations": ["Obligation 1: Payment within 30 days", "Obligation 2: Delivery guarantee"],
            "missing_terms": ["Missing: Force majeure clause", "Missing: Dispute resolution mechanism"]
        },
        "message": "Mock analysis completed"
    }
```

## ⚠️ Important Disclaimers

**Legal Compliance:**
- This application uses MOCK DATA for demonstration purposes only
- All analysis results are artificially generated for demo purposes
- This is a demonstration/educational project, not a production legal system
- DO NOT USE WITH REAL LEGAL DOCUMENTS - FOR DEMONSTRATION ONLY

**For Production Use:**
- Ensure proper legal compliance before handling real legal documents
- Implement proper safeguards for sensitive legal information
- Ensure all AI analysis is reviewed by qualified legal professionals
- Maintain attorney-client privilege requirements
- Follow data protection regulations (GDPR, CCPA, etc.)

