"""End-to-end tests for the PEACEMAiKER application."""
import streamlit as st

from src.app import main
from src.utils.example_answers import AMERICAN_EXAMPLE, PORTUGUESE_EXAMPLE


def test_app_initialization() -> None:
    """Test that the app initializes with correct session state."""
    main()
    assert "viewpoint1_responses" in st.session_state
    assert "viewpoint2_responses" in st.session_state
    assert st.session_state.viewpoint1_responses == AMERICAN_EXAMPLE
    assert st.session_state.viewpoint2_responses == PORTUGUESE_EXAMPLE
