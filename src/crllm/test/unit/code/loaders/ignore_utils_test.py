import os
import tempfile
from crllm.code.loaders.ignore_utils import read_crllm_ignore, should_ignore_file


def test_empty_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        ignore_path = os.path.join(tmpdir, ".crllm_ignore")
        with open(ignore_path, "w", encoding="utf8") as file:
            file.close()
        assert read_crllm_ignore(tmpdir) == []


def test_comments_and_whitespace():
    with tempfile.TemporaryDirectory() as tmpdir:
        ignore_path = os.path.join(tmpdir, ".crllm_ignore")
        with open(ignore_path, "w", encoding="utf8") as file:
            file.write(
                """
# This is a comment
*.log
 temp/  
# Another comment
.env
"""
            )
        patterns = read_crllm_ignore(tmpdir)
        assert patterns == ["*.log", "temp/", ".env"]


def test_read_crllm_ignore_no_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        assert read_crllm_ignore(tmpdir) == []


def test_ignore_relative_path():
    with tempfile.TemporaryDirectory() as tmpdir:

        os.makedirs(os.path.join(tmpdir, "src", "logs"))
        ignore_path = os.path.join(tmpdir, ".crllm_ignore")
        with open(ignore_path, "w", encoding="utf8") as file:
            file.write("*.log\nsrc/logs/\n*.pyc\ntemp/")

        assert should_ignore_file(os.path.join(tmpdir, "app.log"), tmpdir)
        assert should_ignore_file(
            os.path.join(tmpdir, "src", "logs", "debug.log"), tmpdir
        )
        assert not should_ignore_file(os.path.join(tmpdir, "src", "main.py"), tmpdir)


def test_basename_patterns():
    with tempfile.TemporaryDirectory() as tmpdir:
        ignore_path = os.path.join(tmpdir, ".crllm_ignore")
        with open(ignore_path, "w", encoding="utf8") as file:
            file.write(".env\n*.log")

        assert should_ignore_file(os.path.join(tmpdir, "src", ".env"), tmpdir)
        assert should_ignore_file(os.path.join(tmpdir, "app.log"), tmpdir)
        assert should_ignore_file(os.path.join(tmpdir, "src", "app.log"), tmpdir)


def test_custom_patterns():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.makedirs(os.path.join(tmpdir, "src"))

        custom_patterns = ["*.txt", "secret/"]
        file_path = os.path.join(tmpdir, "src", "notes.txt")
        assert should_ignore_file(file_path, tmpdir, custom_patterns)

        file_path = os.path.join(tmpdir, "src", "code.py")
        assert not should_ignore_file(file_path, tmpdir, custom_patterns)


def test_edge_cases():
    with tempfile.TemporaryDirectory() as tmpdir:
        assert not should_ignore_file(os.path.join(tmpdir, "test.py"), tmpdir, [])

        ignore_path = os.path.join(tmpdir, ".crllm_ignore")
        with open(ignore_path, "w", encoding="utf8") as file:
            file.write("*.tmp")

        assert should_ignore_file(os.path.join(tmpdir, "test.tmp"), tmpdir)
