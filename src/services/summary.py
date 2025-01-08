"""Service for generating summaries using AI."""
import asyncio
import os
from typing import Any, Dict

from pydantic_ai import Agent


def get_model(provider: str, model_name: str) -> str:
    """Get the full model name for Pydantic.AI.

    Args:
        provider: The AI provider (e.g., 'openai')
        model_name: The model name (e.g., 'gpt-4')

    Returns:
        str: Full model name in provider:model format
    """
    return f"{provider}:{model_name}"


async def generate_summary_async(responses: Dict[str, str]) -> Any:
    """Generate a summary of viewpoint responses using Pydantic.AI Agent.

    Args:
        responses: Dictionary of question responses

    Returns:
        str: Generated summary of the viewpoint
    """
    # Initialize the AI agent with our configuration
    agent = Agent(
        model=get_model(
            os.getenv("PROVIDER", "openai"),
            os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini-2024-07-18"),
        ),
        system_prompt="""
        You are a skilled mediator who helps understand different viewpoints.
        Based on the responses provided,
        create a concise and empathetic summary of this viewpoint.
        Focus on understanding the core concerns and values expressed.
        """,
    )

    prompt = f"""
    Based on the following responses, provide a concise summary of this viewpoint:
    Situation: {responses['Q1']}
    Involved Parties: {responses['Q2']}
    Disagreement: {responses['Q3']}
    Potential Losses: {responses['Q4']}
    Compromise Stance: {responses['Q5']}
    """

    # pylint: disable=no-member
    result = await agent.run(prompt)
    return result.data


def generate_summary(responses: Dict[str, str]) -> Any:
    """Synchronous wrapper for generate_summary_async.

    Args:
        responses: Dictionary of question responses

    Returns:
        str: Generated summary of the viewpoint
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(generate_summary_async(responses))
    finally:
        loop.close()
