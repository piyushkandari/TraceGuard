"""Basic scanner tests."""
from scanner.core import get_scanner_version

def test_version():
    """Ensure scanner version is correct."""
    assert get_scanner_version() == "0.1.0"