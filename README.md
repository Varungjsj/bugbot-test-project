# bugbot-test-project

A test repository for demonstrating Cursor's Bugbot functionality.

## About This Project

This repository contains a Python script (`buggy_script.py`) that was initially created with intentional bugs to test Bugbot's bug detection capabilities. The script has since been fixed and now demonstrates proper Python programming practices.

## Bugbot Setup

To enable Cursor's Bugbot on this repository:

### 1. Install the Cursor Bugbot GitHub App

1. Go to the [Cursor Bugbot GitHub App page](https://github.com/apps/cursor-bot)
2. Click "Install" or "Configure"
3. Select this repository from your list of repositories
4. Grant the necessary permissions

### 2. Repository Configuration

This repository includes the following configuration files for Bugbot:

- `.bugbot.yml` - Main Bugbot configuration
- `.github/workflows/bugbot.yml` - GitHub Actions workflow for automated analysis
- `.cursorconfig` - Cursor-specific configuration
- `requirements-dev.txt` - Python development dependencies

### 3. Using Bugbot

Once installed, you can trigger Bugbot in pull requests by commenting:

- `@bugbot run` - Run bug analysis on the PR
- `@cursor fix` - Request automated fixes for detected issues

## Project Structure

```
.
├── .bugbot.yml              # Bugbot configuration
├── .cursorconfig            # Cursor IDE configuration
├── .github/
│   └── workflows/
│       └── bugbot.yml       # GitHub Actions workflow
├── buggy_script.py          # Python script (now fixed)
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

# Run the script
python buggy_script.py

# Run linting
flake8 buggy_script.py
pylint buggy_script.py
mypy buggy_script.py
```

## Troubleshooting

If you see "Unable to authenticate your request" errors from Bugbot:

1. Ensure the Cursor Bugbot GitHub App is installed on this repository
2. Check that the repository has the proper permissions granted
3. Verify that the configuration files are properly formatted
4. Contact Cursor support if issues persist

## Contributing

This is a test repository for Bugbot functionality. Feel free to:

1. Create pull requests with intentionally buggy code to test Bugbot
2. Test different types of bugs and edge cases
3. Improve the Bugbot configuration

## License

This is a test project for demonstration purposes.