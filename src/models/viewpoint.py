"""Models for viewpoint data structures."""
from typing import ClassVar, List

from pydantic import BaseModel, Field


class ViewpointResponse(BaseModel):
    """Pydantic model for storing viewpoint responses."""

    situation: str = Field(..., description="One sentence description of the situation")
    involved_parties: str = Field(..., description="People involved in the situation")
    disagreement: str = Field(..., description="Description of the disagreement")
    potential_losses: str = Field(..., description="What would be lost in compromise")
    compromise_stance: str = Field(
        ..., description="Negotiable and non-negotiable aspects"
    )


class Questions:
    """Predefined questions for viewpoint analysis."""

    QUESTIONS: ClassVar[List[str]] = [
        "Q1. Describe the situation in one sentence.",
        "Q2. Who is involved?",
        "Q3. What is the disagreement about?",
        "Q4. What do you think would be lost if we did things the other person's way?",
        "Q5. If you had to compromise, what parts of your stance are non-negotiable, "
        "and where are you flexible?",
    ]
