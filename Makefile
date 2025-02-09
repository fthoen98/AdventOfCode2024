# use Wildcarts to find all python files
run:
	uv run ruff check **/*.py
	uv run black **/*.py

# the alternative (wokring everywhere) is using "find" shell commands
# PYTHON_FILES := $(shell find . -type f -name "*.py")
# format:
# 	uv run ruff check $(PYTHON_FILES)
# 	uv run black $(PYTHON_FILES)