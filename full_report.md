# 🐛 Bug Detection Report

## ❌ Errors (5)

- **hardcoded_secret** at `bug_detector.py:193`: Possible hardcoded secret or password
- **division_by_zero** at `test_buggy_code.py:8`: Division by zero detected
- **undefined_variable** at `test_buggy_code.py:24`: Variable 'undefined_var' appears to be undefined
- **hardcoded_secret** at `test_buggy_code.py:39`: Possible hardcoded secret or password
- **hardcoded_secret** at `test_buggy_code.py:40`: Possible hardcoded secret or password

## ⚠️  Warnings (3)

- **mutable_default_argument** at `test_buggy_code.py:11`: Mutable default argument 'my_list' in function 'append_to_list'
- **comparison_with_none** at `test_buggy_code.py:17`: Use 'is None' instead of '== None'
- **bare_except** at `test_buggy_code.py:25`: Bare 'except:' clause found - consider catching specific exceptions

## ℹ️  Information (18)

- **missing_return** at `buggy_script.py:49`: Function 'count_to_ten' might be missing a return statement
- **missing_return** at `buggy_script.py:131`: Function 'main' might be missing a return statement
- **missing_return** at `buggy_script.py:123`: Function 'parent' might be missing a return statement
- **missing_return** at `buggy_script.py:126`: Function 'add_child' might be missing a return statement
- **possibly_unused_variable** at `buggy_script.py:163`: Variable 'x' might be unused
- **missing_return** at `bug_detector.py:22`: Function 'add_issue' might be missing a return statement
- **missing_return** at `bug_detector.py:84`: Function 'check_mutable_defaults' might be missing a return statement
- **missing_return** at `bug_detector.py:120`: Function 'check_missing_return' might be missing a return statement
- **missing_return** at `bug_detector.py:162`: Function 'check_undefined_variables' might be missing a return statement
- **missing_return** at `bug_detector.py:177`: Function 'check_common_patterns' might be missing a return statement
- **todo_comment** at `bug_detector.py:202`: TODO/FIXME comment found: # Check for TODO comments
- **todo_comment** at `bug_detector.py:203`: TODO/FIXME comment found: if 'TODO' in line or 'FIXME' in line or 'XXX' in line:
- **todo_comment** at `bug_detector.py:206`: TODO/FIXME comment found: f"TODO/FIXME comment found: {line.strip()}",
- **missing_return** at `test_buggy_code.py:29`: Function 'get_sum' might be missing a return statement
- **debug_print** at `test_buggy_code.py:35`: Debug print statement found
- **todo_comment** at `test_buggy_code.py:42`: TODO/FIXME comment found: # TODO: Fix this function
- **todo_comment** at `test_buggy_code.py:44`: TODO/FIXME comment found: # FIXME: This needs implementation
- **debug_print** at `test_buggy_code.py:50`: Debug print statement found
