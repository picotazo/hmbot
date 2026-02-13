from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_lorem():
    print("=== Test: lorem.txt truncation ===")
    result = get_file_content("calculator", "lorem.txt")

    # Check length is at least MAX_CHARS
    print("Length:", len(result))

    # Check truncation message
    expected_suffix = f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
    print("Ends with truncation message:", result.endswith(expected_suffix))


def test_main_py():
    print("\n=== Test: main.py ===")
    print(get_file_content("calculator", "main.py"))


def test_pkg_calculator():
    print("\n=== Test: pkg/calculator.py ===")
    print(get_file_content("calculator", "pkg/calculator.py"))


def test_outside_dir():
    print("\n=== Test: outside directory (/bin/cat) ===")
    print(get_file_content("calculator", "/bin/cat"))


def test_missing_file():
    print("\n=== Test: missing file ===")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    test_lorem()
    test_main_py()
    test_pkg_calculator()
    test_outside_dir()
    test_missing_file()

