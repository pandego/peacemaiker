"""Pytest configuration and shared fixtures."""
from typing import Dict

import pytest

from src.utils.example_answers import AMERICAN_EXAMPLE, PORTUGUESE_EXAMPLE


@pytest.fixture
def american_responses() -> Dict[str, str]:
    """Fixture providing sample American viewpoint responses."""
    return AMERICAN_EXAMPLE.copy()


@pytest.fixture
def portuguese_responses() -> Dict[str, str]:
    """Fixture providing sample Portuguese viewpoint responses."""
    return PORTUGUESE_EXAMPLE.copy()
