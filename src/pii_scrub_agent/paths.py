import os
from pathlib import Path

class ProjectPaths:
    """
    Helper class to provide source of truth for important project paths.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    SRC_DIR = BASE_DIR / "src"
    PACKAGE_DIR = SRC_DIR / "pii_scrub_agent"
    PROMPTS_DIR = PACKAGE_DIR / "prompts"
    TMP_DIR = BASE_DIR / "tmp"
    GITHUB_DIR = BASE_DIR / ".github"

    @classmethod
    def get_base_dir(cls) -> Path:
        return cls.BASE_DIR

    @classmethod
    def get_src_dir(cls) -> Path:
        return cls.SRC_DIR

    @classmethod
    def get_package_dir(cls) -> Path:
        return cls.PACKAGE_DIR

    @classmethod
    def get_prompts_dir(cls) -> Path:
        return cls.PROMPTS_DIR

    @classmethod
    def get_tmp_dir(cls) -> Path:
        return cls.TMP_DIR

    @classmethod
    def get_github_dir(cls) -> Path:
        return cls.GITHUB_DIR
