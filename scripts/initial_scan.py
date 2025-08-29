#!/usr/bin/env python3
"""CLI script for performing initial PII scan."""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pii_scrub_agent.initial_scan import perform_initial_scan


def main():
    """Main entry point for the CLI script."""
    print("Starting PII initial scan...")
    print("Content: 'Joey Corea - Developer Relation Specialist. Attendee.'")
    print("Model: google/gemma-3-12b")
    print("URL: http://127.0.0.1:1234")
    print()
    
    try:
        result = perform_initial_scan()
        print("PII Scan Result:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        print("\nNote: Make sure the LLM server is running at http://127.0.0.1:1234")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())