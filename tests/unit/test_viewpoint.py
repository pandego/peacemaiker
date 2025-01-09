"""Unit tests for viewpoint models and summary generation."""
from typing import Dict

import pytest
from pydantic_ai import Agent

from src.models.viewpoint import Questions, ViewpointResponse
from src.utils.example_answers import AMERICAN_EXAMPLE, PORTUGUESE_EXAMPLE


@pytest.fixture
def american_responses() -> Dict[str, str]:
    """Fixture providing sample American viewpoint responses."""
    return AMERICAN_EXAMPLE.copy()


@pytest.fixture
def portuguese_responses() -> Dict[str, str]:
    """Fixture providing sample Portuguese viewpoint responses."""
    return PORTUGUESE_EXAMPLE.copy()


def test_viewpoint_response_model(american_responses: Dict[str, str]) -> None:
    """Test ViewpointResponse Pydantic model validation."""
    viewpoint = ViewpointResponse(
        situation=american_responses["Q1"],
        involved_parties=american_responses["Q2"],
        disagreement=american_responses["Q3"],
        potential_losses=american_responses["Q4"],
        compromise_stance=american_responses["Q5"],
    )
    assert isinstance(viewpoint, ViewpointResponse)


def test_questions_structure() -> None:
    """Test that Questions class contains the correct number of predefined questions."""
    questions = Questions()
    assert len(questions.QUESTIONS) == 5
    assert all(q.startswith("Q") for q in questions.QUESTIONS)


def test_agent_creation() -> None:
    """Test that we can create a Pydantic.AI agent with our configuration."""
    agent = Agent(model="openai:gpt-4", system_prompt="Test prompt")
    assert agent is not None
