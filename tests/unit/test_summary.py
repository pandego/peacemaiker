"""Unit tests for summary generation."""
import asyncio
from typing import Dict

import pytest

from src.services.summary import generate_summary_async
from src.utils.example_answers import AMERICAN_EXAMPLE, PORTUGUESE_EXAMPLE


@pytest.fixture
def american_responses() -> Dict[str, str]:
    """Fixture providing sample American viewpoint responses."""
    return AMERICAN_EXAMPLE.copy()


@pytest.fixture
def portuguese_responses() -> Dict[str, str]:
    """Fixture providing sample Portuguese viewpoint responses."""
    return PORTUGUESE_EXAMPLE.copy()


@pytest.mark.asyncio
async def test_generate_summary_async(american_responses: Dict[str, str]) -> None:
    """Test async summary generation with sample responses using Pydantic.AI."""
    summary = await generate_summary_async(american_responses)
    assert isinstance(summary, str)
    assert len(summary) > 0


@pytest.mark.asyncio
async def test_parallel_summary_generation(
    american_responses: Dict[str, str], portuguese_responses: Dict[str, str]
) -> None:
    """Test that summaries can be generated in parallel using asyncio.

    Args:
        american_responses: Sample American viewpoint responses
        portuguese_responses: Sample Portuguese viewpoint responses
    """
    # Create tasks for both summaries
    summary1_task = asyncio.create_task(generate_summary_async(american_responses))
    summary2_task = asyncio.create_task(generate_summary_async(portuguese_responses))

    # Wait for both summaries to complete
    summary1, summary2 = await asyncio.gather(summary1_task, summary2_task)

    # Verify both summaries were generated
    assert isinstance(summary1, str) and len(summary1) > 0
    assert isinstance(summary2, str) and len(summary2) > 0
