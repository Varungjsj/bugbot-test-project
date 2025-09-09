# bugbot-test-project

A test repository for demonstrating Cursor's Bugbot functionality.

## About This Project

This repository contains a Python script (`buggy_script.py`) that was initially created with intentional bugs to test Bugbot's bug detection capabilities. The script has since been fixed and now demonstrates proper Python programming practices.

## Bug Detection System

This repository includes a comprehensive bug detection system that works through GitHub Actions.

### How It Works

The bug detection system consists of:

1. **Custom Bug Detector** (`bug_detector.py`) - A Python script that analyzes code for:
   - Syntax errors and code issues
   - Security vulnerabilities (hardcoded secrets, SQL injection risks)
   - Code quality problems (mutable defaults, bare excepts, missing returns)
   - Style issues (comparison with None, debug prints)
   - TODO/FIXME comments

2. **GitHub Actions Workflow** (`.github/workflows/bugbot.yml`) - Automatically runs on:
   - All pull requests
   - PR comments containing `@bugbot run`, `bugbot run`, or `@cursor fix`

3. **Configuration Files**:
   - `.bugbot.yml` - Bugbot configuration for Cursor app
   - `.cursorconfig` - Cursor IDE settings
   - `requirements-dev.txt` - Development dependencies

### Using the Bug Detection

In any pull request, you can trigger bug analysis by commenting:

- `@bugbot run` - Run full bug analysis
- `bugbot run` - Alternative trigger
- `@cursor fix` - Request bug detection

The system will analyze all Python files and post a detailed report as a PR comment.

### Running Locally

You can also run the bug detector locally:

```bash
# Analyze all Python files
python3 bug_detector.py

# Analyze specific files
python3 bug_detector.py file1.py file2.py

# Output as JSON
python3 bug_detector.py --format json

# Save report to file
python3 bug_detector.py --output report.md
```

### Cursor Bugbot App (Optional)

For enhanced features, you can also install the [Cursor Bugbot GitHub App](https://github.com/apps/cursor-bot). This repository's bug detection system works independently and doesn't require the app.

## Project Structure

```
.
├── .bugbot.yml              # Bugbot configuration
├── .cursorconfig            # Cursor IDE configuration
├── .github/
│   └── workflows/
│       └── bugbot.yml       # GitHub Actions workflow
├── bug_detector.py          # Custom bug detection script
├── buggy_script.py          # Python script (now fixed)
├── test_buggy_code.py       # Test file with intentional bugs
├── requirements-dev.txt     # Development dependencies
└── README.md                # This file
```

## Python Script

The `buggy_script.py` file demonstrates various Python programming patterns and best practices, including:

- Proper error handling
- Safe file operations
- Thread-safe operations
- Memory management
- Security best practices
- Type safety

## Development

To set up the development environment:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run the main script
python3 buggy_script.py

# Run bug detection on all files
python3 bug_detector.py

# Test bug detection on the test file
python3 bug_detector.py test_buggy_code.py

# Run traditional linting
flake8 . --exclude=venv,__pycache__
pylint *.py
mypy *.py
```

## Troubleshooting

### Bugbot Authentication Errors

If you see "Unable to authenticate your request" errors:

**Solution:** This repository now includes a working bug detection system that runs through GitHub Actions without requiring the Cursor Bugbot app. Simply comment `@bugbot run` or `@cursor fix` in any PR to trigger the analysis.

To use the official Cursor Bugbot (optional):
1. Install the [Cursor Bugbot GitHub App](https://github.com/apps/cursor-bot)
2. Grant necessary repository permissions
3. The app will work alongside our custom bug detection

### Common Issues

- **Bug detector not finding files**: Make sure you're running from the repository root
- **Missing dependencies**: Run `pip install -r requirements-dev.txt`
- **GitHub Actions not triggering**: Ensure the workflow file exists in `.github/workflows/`

## Contributing

This is a test repository for Bugbot functionality. Feel free to:

1. Create pull requests with intentionally buggy code to test Bugbot
2. Test different types of bugs and edge cases
3. Improve the Bugbot configuration

## License

This is a test project for demonstration purposes.