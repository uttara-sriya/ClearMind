# ClearMind

**ClearMind** is an AI-powered accessibility assistant built with **Google ADK (Agent Development Kit)** and the **Gemini 2.5 Flash** model. It simplifies complex corporate, legal, and technical jargon into clear, actionable insights—reducing cognitive load and improving accessibility for everyone.

## Features

- **Text Simplification**: Breaks down complex corporate and legal terminology into plain language
- **Smart Summarization**: Extracts concise summaries of dense documents
- **Action Item Extraction**: Identifies what needs to be done in a clear, bulleted format
- **Deadline Detection**: Automatically identifies and lists all deadlines mentioned
- **Priority Assessment**: Calculates urgency levels based on deadlines and document importance
- **REST API**: Easy-to-use FastAPI endpoint for programmatic access
- **Google ADK Powered**: Leverages Google's Agent Development Kit with Gemini model for advanced reasoning

## Use Cases

- Summarizing employment contracts or policy documents
- Simplifying financial statements and banking terms
- Breaking down technical compliance notices
- Extracting deadlines from legal correspondence
- Prioritizing multiple complex tasks from email or documents

---

## Quick Start

### Prerequisites

- **Python 3.14+** (as specified in pyproject.toml)
- **pip** or **uv** (package manager)
- **Google API Key** with Gemini access

### Installation

1. **Clone the repository** 
2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows (PowerShell):
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```bash
     .venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -e .
   ```

   Or using individual packages:
   ```bash
   pip install fastapi uvicorn pydantic google-adk google-genai python-dotenv
   ```

### Configuration

1. **Set up your Google API Key**:
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your-google-api-key-here
   ```

   Or set it directly in your terminal:
   - Windows (PowerShell):
     ```bash
     $env:GOOGLE_API_KEY = "your-google-api-key-here"
     ```
   - Windows (Command Prompt):
     ```bash
     set GOOGLE_API_KEY=your-google-api-key-here
     ```
   - macOS/Linux:
     ```bash
     export GOOGLE_API_KEY=your-google-api-key-here
     ```

   > **Note**: You need a Google API key with Gemini 2.5 Flash model access. Get one at [Google Cloud Console](https://console.cloud.google.com/)

---

## How to Run

### Start the API Server

With the virtual environment activated, run:

```bash
adk run clearMind
```

You should see output like:
```
Starting ClearMind API Server...
INFO:     Uvicorn running on http://0.0.0.0:8080
INFO:     Application startup complete
```

The API will be available at `http://localhost:8080`

### Access the API

#### 1. **Interactive API Documentation** (Swagger UI)
   - Open your browser and go to: `http://localhost:8080/docs`
   - Test the `/simplify` endpoint directly from the UI

#### 2. **Using cURL** (Command Line)

```bash
curl -X POST "http://localhost:8080/simplify" \
  -H "Content-Type: application/json" \
  -d '{"text": "Pursuant to Section 3.1(a) of the Service Level Agreement dated January 1st, 2024, failure to maintain 99.9% uptime will result in service credits..."}'
```

#### 3. **Using Python Requests**

```python
import requests

url = "http://localhost:8080/simplify"
payload = {
    "text": "Your complex text here..."
}

response = requests.post(url, json=payload)
print(response.json())
```

#### 4. **Using JavaScript/Fetch**

```javascript
fetch('http://localhost:8080/simplify', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    text: 'Your complex text here...' 
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## Example Usage & Response

### Request

```json
{
  "text": "Dear Employee, Per the recent executive directive effective March 15, 2024, all employees are required to complete mandatory compliance training within 30 days or face disciplinary action including potential termination. Failure to comply constitutes a violation of our corporate governance protocols."
}
```

### Response

```json
{
  "simplified_response": "**SUMMARY:**\nAll employees must finish compliance training by April 14, 2024. Not doing so may lead to discipline or job loss.\n\n**ACTION ITEMS:**\n• Complete compliance training\n• Submit completion certificate to HR\n\n**DEADLINES:**\n• April 14, 2024 (30 days from March 15, 2024)\n\n**URGENCY:**\nCRITICAL - Immediate Action Required"
}
```

---

## Project Structure

```
clearmind/
├── __init__.py           # Package initialization
├── agent.py              # Google ADK Agent definition with custom tools
├── app.py                # FastAPI application and endpoints
main.py                  # Server entry point
pyproject.toml           # Project dependencies and metadata
README.md                # This file
.env                     # Environment variables (create this locally)
```

---

## Project Components

### **1. Agent (`clearmind/agent.py`)**
- Defines the ClearMind agent using Google ADK
- Implements `calculate_priority_score()` custom tool
- Configures Gemini 2.5 Flash model with system instructions
- Handles text processing and priority calculation

### **2. API (`clearmind/app.py`)**
- FastAPI web server with `/simplify` endpoint
- Accepts complex text as input
- Returns structured JSON response with simplified content

### **3. Main Entry Point (`main.py`)**
- Initializes Uvicorn server
- Validates Google API key configuration
- Runs the FastAPI application on port 8080

---

## Troubleshooting

### **Issue: "GOOGLE_API_KEY environment variable is not set"**
- Ensure you've set the environment variable before running the server
- Check your `.env` file exists and has the correct key format
- Restart the server after setting the key

### **Issue: Module not found errors**
- Verify virtual environment is activated
- Run `pip install -e .` to install dependencies in editable mode

### **Issue: Port 8080 already in use**
- Modify `main.py` to use a different port:
  ```python
  uvicorn.run("clearmind.app:app", host="0.0.0.0", port=8081, reload=True)
  ```

### **Issue: API returns timeout or error**
- Verify you have internet access (for Google Gemini API calls)
- Check your Google API credits are available
- Ensure your API key has the correct permissions

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | >=0.104.1 | Web framework for API |
| `uvicorn` | >=0.24.0 | ASGI server |
| `pydantic` | >=2.5.2 | Data validation |
| `google-adk` | >=1.27.3 | Google Agent Development Kit |
| `google-genai` | Latest | Google Generative AI SDK |
| `python-dotenv` | Latest | Environment variable management |

---

## Learn More

- [Google ADK Documentation](https://ai.google.dev/docs)
- [Gemini API Documentation](https://ai.google.dev/docs/gemini-api)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Made for accessibility and simplicity**
