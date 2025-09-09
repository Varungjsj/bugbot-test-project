#!/usr/bin/env python3
"""
Bug Detector - A Python script to analyze code for common bugs and issues.
This simulates Bugbot functionality for repositories without the Cursor app.
"""

import ast
import sys
import os
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple
import argparse


class BugDetector:
    def __init__(self):
        self.issues = []
        self.file_path = None
        
    def add_issue(self, issue_type: str, message: str, line: int = None, column: int = None, severity: str = "warning"):
        """Add an issue to the list."""
        issue = {
            "type": issue_type,
            "message": message,
            "file": self.file_path,
            "severity": severity
        }
        if line:
            issue["line"] = line
        if column:
            issue["column"] = column
        self.issues.append(issue)
    
    def analyze_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Analyze a Python file for bugs."""
        self.file_path = file_path
        self.issues = []
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Parse the AST
            try:
                tree = ast.parse(content, filename=file_path)
                self.visit_ast(tree)
            except SyntaxError as e:
                self.add_issue("syntax_error", f"Syntax error: {e.msg}", e.lineno, e.offset, "error")
                
            # Additional pattern-based checks
            self.check_common_patterns(content)
            
        except Exception as e:
            self.add_issue("file_error", f"Could not analyze file: {str(e)}", severity="error")
            
        return self.issues
    
    def visit_ast(self, tree):
        """Visit AST nodes to find issues."""
        for node in ast.walk(tree):
            # Check for various bug patterns
            self.check_division_by_zero(node)
            self.check_mutable_defaults(node)
            self.check_unused_variables(node, tree)
            self.check_undefined_variables(node, tree)
            self.check_comparison_with_none(node)
            self.check_bare_except(node)
            self.check_missing_return(node)
            
    def check_division_by_zero(self, node):
        """Check for potential division by zero."""
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            if isinstance(node.right, ast.Constant) and node.right.value == 0:
                self.add_issue(
                    "division_by_zero",
                    "Division by zero detected",
                    node.lineno,
                    node.col_offset,
                    "error"
                )
                
    def check_mutable_defaults(self, node):
        """Check for mutable default arguments."""
        if isinstance(node, ast.FunctionDef):
            for i, default in enumerate(node.args.defaults):
                if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                    param_index = len(node.args.args) - len(node.args.defaults) + i
                    param_name = node.args.args[param_index].arg
                    self.add_issue(
                        "mutable_default_argument",
                        f"Mutable default argument '{param_name}' in function '{node.name}'",
                        default.lineno,
                        default.col_offset
                    )
                    
    def check_comparison_with_none(self, node):
        """Check for == None instead of is None."""
        if isinstance(node, ast.Compare):
            for op, comparator in zip(node.ops, node.comparators):
                if isinstance(op, ast.Eq) and isinstance(comparator, ast.Constant) and comparator.value is None:
                    self.add_issue(
                        "comparison_with_none",
                        "Use 'is None' instead of '== None'",
                        node.lineno,
                        node.col_offset
                    )
                    
    def check_bare_except(self, node):
        """Check for bare except clauses."""
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            self.add_issue(
                "bare_except",
                "Bare 'except:' clause found - consider catching specific exceptions",
                node.lineno,
                node.col_offset
            )
            
    def check_missing_return(self, node):
        """Check for functions that might be missing return statements."""
        if isinstance(node, ast.FunctionDef):
            # Skip __init__ methods
            if node.name == "__init__":
                return
                
            # Check if function has any return statements
            has_return = any(isinstance(n, ast.Return) and n.value is not None 
                           for n in ast.walk(node))
            
            # If function has assignment but no return, it might be missing return
            has_assignment = any(isinstance(n, ast.Assign) for n in ast.walk(node))
            
            if has_assignment and not has_return and node.returns is None:
                self.add_issue(
                    "missing_return",
                    f"Function '{node.name}' might be missing a return statement",
                    node.lineno,
                    node.col_offset,
                    "info"
                )
                
    def check_unused_variables(self, node, tree):
        """Check for unused variables (simplified check)."""
        # This is a simplified check - a full implementation would need more context
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    # Check if variable name starts with underscore (convention for unused)
                    if not target.id.startswith('_'):
                        # This is where we'd check if the variable is used later
                        # For now, just flag variables that look suspicious
                        if target.id in ['temp', 'tmp', 'unused', 'x', 'y', 'z']:
                            self.add_issue(
                                "possibly_unused_variable",
                                f"Variable '{target.id}' might be unused",
                                target.lineno,
                                target.col_offset,
                                "info"
                            )
                            
    def check_undefined_variables(self, node, tree):
        """Check for potentially undefined variables."""
        # Simplified check - looks for Name nodes in Load context
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            # Common undefined variable names from bugs
            suspicious_names = ['undefined_var', 'undefined', 'not_defined']
            if node.id in suspicious_names:
                self.add_issue(
                    "undefined_variable",
                    f"Variable '{node.id}' appears to be undefined",
                    node.lineno,
                    node.col_offset,
                    "error"
                )
                
    def check_common_patterns(self, content: str):
        """Check for common bug patterns using string matching."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for print debugging left in code
            if 'print(' in line and '# debug' not in line.lower() and '# todo' not in line.lower():
                if any(debug_word in line.lower() for debug_word in ['debug', 'test', 'xxx', 'todo']):
                    self.add_issue(
                        "debug_print",
                        "Debug print statement found",
                        i,
                        severity="info"
                    )
                    
            # Check for hardcoded passwords or secrets
            if any(secret in line.lower() for secret in ['password =', 'secret =', 'api_key =', 'token =']):
                if any(bad in line for bad in ["'", '"', 'True', 'False']) and '=' in line:
                    self.add_issue(
                        "hardcoded_secret",
                        "Possible hardcoded secret or password",
                        i,
                        severity="error"
                    )
                    
            # Check for TODO comments
            if 'TODO' in line or 'FIXME' in line or 'XXX' in line:
                self.add_issue(
                    "todo_comment",
                    f"TODO/FIXME comment found: {line.strip()}",
                    i,
                    severity="info"
                )


def run_external_linters(file_path: str) -> Dict[str, Any]:
    """Run external linting tools if available."""
    results = {}
    
    # Try to run flake8
    try:
        result = subprocess.run(
            ['flake8', '--format=json', file_path],
            capture_output=True,
            text=True
        )
        if result.stdout:
            results['flake8'] = json.loads(result.stdout)
    except (subprocess.SubprocessError, FileNotFoundError, json.JSONDecodeError):
        pass
        
    # Try to run pylint
    try:
        result = subprocess.run(
            ['pylint', '--output-format=json', file_path],
            capture_output=True,
            text=True
        )
        if result.stdout:
            results['pylint'] = json.loads(result.stdout)
    except (subprocess.SubprocessError, FileNotFoundError, json.JSONDecodeError):
        pass
        
    return results


def format_report(all_issues: List[Dict[str, Any]], external_results: Dict[str, Any]) -> str:
    """Format the bug report."""
    report = []
    report.append("# 🐛 Bug Detection Report\n")
    
    if not all_issues and not external_results:
        report.append("✅ No issues found!")
        return '\n'.join(report)
    
    # Group issues by severity
    errors = [i for i in all_issues if i['severity'] == 'error']
    warnings = [i for i in all_issues if i['severity'] == 'warning']
    info = [i for i in all_issues if i['severity'] == 'info']
    
    if errors:
        report.append(f"## ❌ Errors ({len(errors)})\n")
        for issue in errors:
            location = f"{issue['file']}:{issue.get('line', '?')}"
            report.append(f"- **{issue['type']}** at `{location}`: {issue['message']}")
        report.append("")
        
    if warnings:
        report.append(f"## ⚠️  Warnings ({len(warnings)})\n")
        for issue in warnings:
            location = f"{issue['file']}:{issue.get('line', '?')}"
            report.append(f"- **{issue['type']}** at `{location}`: {issue['message']}")
        report.append("")
        
    if info:
        report.append(f"## ℹ️  Information ({len(info)})\n")
        for issue in info:
            location = f"{issue['file']}:{issue.get('line', '?')}"
            report.append(f"- **{issue['type']}** at `{location}`: {issue['message']}")
        report.append("")
        
    # Add external linter results
    if external_results:
        report.append("## 🔍 External Linter Results\n")
        for linter, results in external_results.items():
            report.append(f"### {linter.title()}")
            if isinstance(results, list) and results:
                report.append(f"Found {len(results)} issues")
            else:
                report.append("No additional issues found")
            report.append("")
            
    return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(description='Detect bugs in Python files')
    parser.add_argument('files', nargs='*', help='Python files to analyze')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')
    parser.add_argument('--output', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    # If no files specified, find all Python files
    if not args.files:
        args.files = [str(p) for p in Path('.').rglob('*.py') if 'venv' not in str(p) and '__pycache__' not in str(p)]
        
    if not args.files:
        print("No Python files found to analyze")
        return 1
        
    detector = BugDetector()
    all_issues = []
    external_results = {}
    
    for file_path in args.files:
        if os.path.exists(file_path):
            issues = detector.analyze_file(file_path)
            all_issues.extend(issues)
            
            # Run external linters
            file_external = run_external_linters(file_path)
            if file_external:
                external_results[file_path] = file_external
                
    # Format output
    if args.format == 'json':
        output = json.dumps({
            'issues': all_issues,
            'external': external_results
        }, indent=2)
    else:
        output = format_report(all_issues, external_results)
        
    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
    else:
        print(output)
        
    # Return exit code based on errors
    return 1 if any(i['severity'] == 'error' for i in all_issues) else 0


if __name__ == '__main__':
    sys.exit(main())