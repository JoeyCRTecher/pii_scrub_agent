"""Initial PII scanning functionality."""

from pathlib import Path

from pii_scrub_agent.paths import ProjectPaths
from pii_scrub_agent.llm_client import LLMClient


class PIIScanner:
    """Scanner for identifying PII in content using LLM."""
    
    def __init__(self, llm_client: LLMClient):
        """Initialize the PII scanner.
        
        Args:
            llm_client: LLM client for making requests
        """
        self.llm_client = llm_client
    
    def load_prompt_template(self) -> str:
        """Load the initial scan prompt template.
        
        Returns:
            The prompt template content
        """
        prompt_file = ProjectPaths.get_prompts_dir() / "initial_scan.txt"
        return prompt_file.read_text().strip()
    
    def scan_content(self, content: str, model_name: str) -> str:
        """Scan content for PII using the LLM.
        
        Args:
            content: The content to scan for PII
            model_name: Name of the model to use
            
        Returns:
            The LLM response identifying PII
        """
        template = self.load_prompt_template()
        prompt = template.format(content=content)
        
        return self.llm_client.prompt(prompt, model_name)


def perform_initial_scan() -> str:
    """Perform the initial PII scan with the specified parameters.
    
    Returns:
        The result of the PII scan
    """
    # Parameters from the issue description
    content = "Joey Corea - Developer Relation Specialist. Attendee."
    model_name = "google/gemma-3-12b"
    url = "http://127.0.0.1:1234"
    
    # Create LLM client and scanner
    llm_client = LLMClient(url)
    scanner = PIIScanner(llm_client)
    
    # Perform the scan
    result = scanner.scan_content(content, model_name)
    return result


if __name__ == "__main__":
    # Run the initial scan when executed directly
    result = perform_initial_scan()
    print("PII Scan Result:")
    print(result)