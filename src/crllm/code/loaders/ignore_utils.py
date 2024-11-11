import os
import fnmatch
from typing import List


def read_crllm_ignore(project_root: str) -> List[str]:
    """
    Read .crllm_ignore file and return a list of ignore patterns.

    Args:
        project_root (str): Root directory of the project

    Returns:
        List[str]: List of ignore patterns
    """
    ignore_file_path = os.path.join(project_root, ".crllm_ignore")

    if not os.path.exists(ignore_file_path):
        return []

    with open(ignore_file_path, "r", encoding="utf8") as file:
        # Strip whitespace and remove comments and empty lines
        return [
            line.strip()
            for line in file.readlines()
            if line.strip() and not line.strip().startswith("#")
        ]


def should_ignore_file(
    file_path: str, project_root: str, ignore_patterns: List[str] = None
) -> bool:

    if ignore_patterns is None:
        ignore_patterns = read_crllm_ignore(project_root)

    relative_path = os.path.relpath(file_path, project_root).replace(os.path.sep, "/")

    return any(
        fnmatch.fnmatch(relative_path, pattern)
        or fnmatch.fnmatch(os.path.basename(file_path), pattern)
        for pattern in ignore_patterns
    )
