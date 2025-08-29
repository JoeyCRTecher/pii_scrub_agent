#!/usr/bin/env python3
"""Simple test to verify the initial scan functionality."""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pii_scrub_agent.initial_scan import PIIScanner
from pii_scrub_agent.llm_client import LLMClient
from pii_scrub_agent.paths import ProjectPaths


def test_prompt_template_loading():
    """Test that the prompt template can be loaded correctly."""
    print("Testing prompt template loading...")
    
    llm_client = LLMClient('http://127.0.0.1:1234')
    scanner = PIIScanner(llm_client)
    
    template = scanner.load_prompt_template()
    
    # Verify template content
    expected_template = "Scan the document and identify any PII in the list:\n{content}"
    assert template == expected_template, f"Expected '{expected_template}', got '{template}'"
    
    print("✓ Prompt template loaded correctly")


def test_content_interpolation():
    """Test that content is correctly interpolated into the template."""
    print("Testing content interpolation...")
    
    llm_client = LLMClient('http://127.0.0.1:1234')
    scanner = PIIScanner(llm_client)
    
    template = scanner.load_prompt_template()
    content = "Joey Corea - Developer Relation Specialist. Attendee."
    prompt = template.format(content=content)
    
    expected_prompt = "Scan the document and identify any PII in the list:\nJoey Corea - Developer Relation Specialist. Attendee."
    assert prompt == expected_prompt, f"Expected '{expected_prompt}', got '{prompt}'"
    
    print("✓ Content interpolation works correctly")


def test_paths():
    """Test that project paths are resolved correctly."""
    print("Testing project paths...")
    
    prompts_dir = ProjectPaths.get_prompts_dir()
    assert prompts_dir.exists(), f"Prompts directory should exist: {prompts_dir}"
    
    prompt_file = prompts_dir / "initial_scan.txt"
    assert prompt_file.exists(), f"Prompt file should exist: {prompt_file}"
    
    print("✓ Project paths resolved correctly")


def main():
    """Run all tests."""
    print("Running PII Scrub Agent Tests")
    print("=" * 40)
    
    try:
        test_paths()
        test_prompt_template_loading()
        test_content_interpolation()
        
        print("\n✓ All tests passed!")
        print("\nNote: The actual LLM API call would require a running server at http://127.0.0.1:1234")
        return 0
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())