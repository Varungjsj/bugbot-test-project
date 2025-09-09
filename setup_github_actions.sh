#!/bin/bash
# Setup script for GitHub Actions workflow
# Run this script to create the necessary GitHub Actions workflow for Bugbot

echo "Setting up GitHub Actions workflow for Bugbot..."

# Create .github/workflows directory
mkdir -p .github/workflows

# Create the Bugbot workflow file
cat > .github/workflows/bugbot.yml << 'EOF'
name: Bugbot Analysis

on:
  pull_request:
    types: [opened, synchronize, reopened]
  issue_comment:
    types: [created]

permissions:
  contents: read
  pull-requests: write
  issues: write

jobs:
  bugbot:
    runs-on: ubuntu-latest
    if: |
      (github.event_name == 'pull_request') ||
      (github.event_name == 'issue_comment' && 
       github.event.issue.pull_request && 
       (contains(github.event.comment.body, '@bugbot run') || 
        contains(github.event.comment.body, '@cursor fix')))
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 mypy pylint black isort
      
      - name: Run static analysis
        run: |
          echo "Running static analysis on Python files..."
          
          # Run flake8
          echo "=== Flake8 Analysis ==="
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || true
          
          # Run pylint
          echo "=== Pylint Analysis ==="
          find . -name "*.py" -not -path "./venv/*" | xargs pylint --disable=all --enable=E || true
          
          # Check with mypy
          echo "=== Type Checking with mypy ==="
          mypy . --ignore-missing-imports || true
      
      - name: Comment PR
        if: github.event_name == 'issue_comment'
        uses: actions/github-script@v6
        with:
          script: |
            const comment = `## Bugbot Analysis Complete
            
            Static analysis has been performed on the Python files in this PR.
            Check the workflow logs for detailed results.
            
            *Note: This is a placeholder workflow. For full Bugbot functionality, please ensure the Cursor Bugbot GitHub App is installed on this repository.*`;
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
EOF

echo "GitHub Actions workflow has been created at .github/workflows/bugbot.yml"
echo ""
echo "To use this workflow:"
echo "1. Run 'git add .github' to stage the workflow"
echo "2. Commit and push to your repository"
echo "3. The workflow will run automatically on pull requests"
echo ""
echo "Note: For full Bugbot functionality, you still need to install the Cursor Bugbot GitHub App."