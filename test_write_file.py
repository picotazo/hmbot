from functions.write_file import write_file

def test_overwrite_lorem():
    print("=== Test: overwrite lorem.txt ===")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

def test_write_new_file():
    print("\n=== Test: write pkg/morelorem.txt ===")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

def test_outside_directory():
    print("\n=== Test: attempt to write outside directory ===")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    test_overwrite_lorem()
    test_write_new_file()
    test_outside_directory()
