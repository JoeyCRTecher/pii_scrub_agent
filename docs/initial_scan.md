# PII Scrub Agent - Initial Scan

This document explains how to use the initial PII scanning functionality.

## Overview

The initial scan feature allows you to scan content for Personally Identifiable Information (PII) using a language model API.

## Usage

### Method 1: Direct Python Import

```python
from pii_scrub_agent.initial_scan import perform_initial_scan

# Perform the scan with predefined parameters
result = perform_initial_scan()
print(result)
```

### Method 2: CLI Script

```bash
# Run the CLI script
python scripts/initial_scan.py
```

### Method 3: Custom Parameters

```python
from pii_scrub_agent.llm_client import LLMClient
from pii_scrub_agent.initial_scan import PIIScanner

# Create custom configuration
llm_client = LLMClient("http://your-llm-server:port")
scanner = PIIScanner(llm_client)

# Scan custom content
result = scanner.scan_content("Your content here", "your-model-name")
print(result)
```

## Configuration

The default configuration uses:
- **Content**: "Joey Corea - Developer Relation Specialist. Attendee."
- **Model**: "google/gemma-3-12b"
- **API URL**: "http://127.0.0.1:1234"

## Requirements

1. A running LLM server at the specified endpoint
2. The server should support OpenAI-compatible API format
3. Python packages: `requests`

## API Format

The LLM client expects a standard OpenAI-compatible endpoint:

```
POST /v1/chat/completions
Content-Type: application/json

{
  "model": "google/gemma-3-12b",
  "messages": [
    {"role": "user", "content": "Scan the document and identify any PII in the list:\nJoey Corea - Developer Relation Specialist. Attendee."}
  ],
  "temperature": 0.1,
  "max_tokens": 1000
}
```