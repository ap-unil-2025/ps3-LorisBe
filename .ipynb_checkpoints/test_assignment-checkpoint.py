"""
Automated tests for Problem Set 3.
These tests will be run by GitHub Classroom autograding.
"""

import pytest
import os
import sys
from io import StringIO


def test_problem2_imports():
    """Test that problem2.py can be imported."""
    try:
        import problem2
        assert hasattr(problem2, 'celsius_to_fahrenheit')
        assert hasattr(problem2, 'fahrenheit_to_celsius')
    except ImportError:
        pytest.fail("Could not import problem2.py")


def test_celsius_to_fahrenheit():
    """Test Celsius to Fahrenheit conversion."""
    from problem2 import celsius_to_fahrenheit

    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == 98.6


def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    from problem2 import fahrenheit_to_celsius

    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert abs(fahrenheit_to_celsius(98.6) - 37) < 0.1


def test_problem3_imports():
    """Test that problem3.py can be imported."""
    try:
        import problem3
        assert hasattr(problem3, 'analyze_numbers')
    except ImportError:
        pytest.fail("Could not import problem3.py")


def test_analyze_numbers():
    """Test number analysis function."""
    from problem3 import analyze_numbers

    # Test with sample data
    numbers = [1, 2, 3, 4, 5]
    result = analyze_numbers(numbers)

    assert result is not None
    assert result.get('count') == 5
    assert result.get('sum') == 15
    assert result.get('average') == 3.0
    assert result.get('minimum') == 1
    assert result.get('maximum') == 5

    # Test empty list
    assert analyze_numbers([]) is None


def test_problem4_imports():
    """Test that problem4.py can be imported."""
    try:
        import problem4
        assert hasattr(problem4, 'count_words')
        assert hasattr(problem4, 'count_lines')
    except ImportError:
        pytest.fail("Could not import problem4.py")


def test_file_operations():
    """Test file counting functions."""
    from problem4 import create_sample_file, count_words, count_lines

    # Create test file
    create_sample_file("test_file.txt")

    # Test that file was created
    assert os.path.exists("test_file.txt")

    # Test counting functions
    word_count = count_words("test_file.txt")
    line_count = count_lines("test_file.txt")

    assert word_count > 0
    assert line_count == 13  # Sample file has 4 lines

    # Cleanup
    os.remove("test_file.txt")


def test_git_log_exists():
    """Test that git_log.txt exists."""
    assert os.path.exists("git_log.txt"), "git_log.txt file is missing"


def test_git_log_has_commits():
    """Test that git_log.txt contains commit history."""
    with open("git_log.txt", "r") as f:
        content = f.read()
        lines = content.strip().split('\n')
        # Should have at least 4 commits as required
        assert len(lines) >= 4, "git_log.txt should contain at least 4 commits"


if __name__ == "__main__":
    # Run basic tests
    print("Running basic tests...")

    # Test imports
    try:
        import problem2
        import problem3
        import problem4
        print("✓ All problem files can be imported")
    except ImportError as e:
        print(f"✗ Import error: {e}")

    # Test basic functionality
    from problem2 import celsius_to_fahrenheit
    assert celsius_to_fahrenheit(0) == 32
    print("✓ Temperature conversion works")

    from problem3 import analyze_numbers
    result = analyze_numbers([1, 2, 3])
    assert result['count'] == 3
    print("✓ Number analysis works")

    print("\nAll basic tests passed!")
    print("Run 'pytest test_assignment.py -v' for full test suite")