import pytest

if __name__ == "__main__":
    print("Starting tests...\n")
    exit_code = pytest.main(["-v", "tests.py"])
    print(f"\nTests finished with exit code: {exit_code}")
