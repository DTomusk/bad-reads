import pytest
from src.infrastructure.utilities.text_normalizer import normalize_text


def test_normalize_text_basic():
    """Test basic text normalization"""
    assert normalize_text("Hello World") == "hello world"
    assert normalize_text("  Multiple   Spaces  ") == "multiple spaces"


def test_normalize_text_unicode():
    """Test unicode normalization"""
    assert normalize_text("José García") == "jose garcia"
    assert normalize_text("François") == "francois"


def test_normalize_text_punctuation():
    """Test punctuation removal"""
    assert normalize_text("Dr. J.K. Rowling") == "dr jk rowling"
    assert normalize_text("O'Connor") == "oconnor"
    assert normalize_text("Smith & Jones") == "smith jones"


def test_normalize_text_initials():
    """Test single letter initial combination"""
    assert normalize_text("J K Rowling") == "jk rowling"
    assert normalize_text("A B C") == "abc"


def test_normalize_text_edge_cases():
    """Test edge cases"""
    assert normalize_text("") == ""
    assert normalize_text("   ") == ""
    assert normalize_text("123") == "123"
    assert normalize_text("!@#$%") == "" 