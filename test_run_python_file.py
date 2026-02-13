from functions.run_python_file import run_python_file

def test_usage():
    print("=== Test: main.py (usage) ===")
    print(run_python_file("calculator", "main.py"))

def test_calculation():
    print("\n=== Test: main.py with args ===")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

def test_tests_py():
    print("\n=== Test: tests.py ===")
    print(run_python_file("calculator", "tests.py"))

def test_outside():
    print("\n=== Test: outside directory ===")
    print(run_python_file("calculator", "../main.py"))

def test_missing():
    print("\n=== Test: nonexistent file ===")
    print(run_python_file("calculator", "nonexistent.py"))

def test_not_python():
    print("\n=== Test: not a Python file ===")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    test_usage()
    test_calculation()
    test_tests_py()
    test_outside()
    test_missing()
    test_not_python()
