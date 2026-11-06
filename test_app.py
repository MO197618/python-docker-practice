import pytest
from app import analyze_issue


def test_detect_error():
    assert analyze_issue("Application error") == ["error"]


def test_detect_multiple_keywords():
    result = analyze_issue("Application crashes with an error")
    assert result == ["error", "crash"]


def test_no_keywords():
    assert analyze_issue("Everything works correctly") == []


def test_case_insensitive():
    assert analyze_issue("SYSTEM CRASH") == ["crash"]


def test_empty_input():
    assert analyze_issue("") == []


def test_invalid_input():
    with pytest.raises(TypeError):
        analyze_issue(None)