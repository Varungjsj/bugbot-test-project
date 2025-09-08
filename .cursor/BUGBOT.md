# BugBot Rules for This Project

## General Guidelines
- Enforce PEP8 style (for Python) or project coding standards.
- Do not allow unused imports or dead code.
- Flag hardcoded secrets, API keys, or credentials.
- Encourage writing clear commit messages.

## Pull Request Review
- Ensure PRs are small and focused (≤ 300 lines ideally).
- Check that tests are added/updated for new features or bug fixes.
- Verify that code is properly documented (docstrings, inline comments).
- Suggest performance improvements when possible.

## Security Rules
- Reject use of `eval` or other unsafe functions.
- Ensure proper input validation and sanitization.
- Check for outdated dependencies in requirements/config files.

## Folder-specific Rules
- `src/`: Code must be modular, no duplication.
- `tests/`: Every function should have test coverage