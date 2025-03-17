# use Wildcarts to find all python files
checks:
	uv run flake8 1 2 4 5 --extend-ignore=E501,W191,E265,E203
	uv run black . -l 79
# the alternative (wokring everywhere) is using "find" shell commands
# PYTHON_FILES := $(shell find . -type f -name "*.py")
# format:
# 	uv run ruff check $(PYTHON_FILES)
# 	uv run black $(PYTHON_FILES)