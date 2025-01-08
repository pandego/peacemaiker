"""Main module for the PEACEMAiKER Streamlit application."""
import asyncio
from typing import Any

import streamlit as st
from dotenv import load_dotenv

from src.models.viewpoint import Questions
from src.services.summary import generate_summary_async
from src.utils.example_answers import AMERICAN_EXAMPLE, PORTUGUESE_EXAMPLE

# Load environment variables
load_dotenv()


def main() -> None:
    """Main function to run the Streamlit application."""
    st.markdown(
        """
    <h1 style='text-align: center;'>PEACEMAiKER</h1>
    """,
        unsafe_allow_html=True,
    )

    # Create two columns
    col1, col2 = st.columns(2)

    # Initialize session state for storing responses
    if "viewpoint1_responses" not in st.session_state:
        st.session_state.viewpoint1_responses = AMERICAN_EXAMPLE.copy()
    if "viewpoint2_responses" not in st.session_state:
        st.session_state.viewpoint2_responses = PORTUGUESE_EXAMPLE.copy()

    questions = Questions()

    # Viewpoint 1 inputs
    with col1:
        st.markdown(
            "<h3 style='text-align: center;'>Viewpoint 1</h3>", unsafe_allow_html=True
        )
        for i, question in enumerate(questions.QUESTIONS, 1):
            key = f"Q{i}"
            response = st.text_area(
                question,
                key=f"vp1_{key}",
                value=st.session_state.viewpoint1_responses.get(key, ""),
                height=100,
            )
            st.session_state.viewpoint1_responses[key] = response

    # Viewpoint 2 inputs
    with col2:
        st.markdown(
            "<h3 style='text-align: center;'>Viewpoint 2</h3>", unsafe_allow_html=True
        )
        for i, question in enumerate(questions.QUESTIONS, 1):
            key = f"Q{i}"
            response = st.text_area(
                question,
                key=f"vp2_{key}",
                value=st.session_state.viewpoint2_responses.get(key, ""),
                height=100,
            )
            st.session_state.viewpoint2_responses[key] = response

    # Generate summaries button
    if st.button("Generate Summaries"):
        if all(st.session_state.viewpoint1_responses.values()) and all(
            st.session_state.viewpoint2_responses.values()
        ):
            # Generate both summaries in parallel
            with st.spinner("Generating summaries in parallel..."):

                async def generate_both_summaries() -> Any:
                    """Generate both summaries in parallel."""
                    return await asyncio.gather(
                        generate_summary_async(st.session_state.viewpoint1_responses),
                        generate_summary_async(st.session_state.viewpoint2_responses),
                    )

                # Create a new event loop and run the coroutine
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    summary1, summary2 = loop.run_until_complete(
                        generate_both_summaries()
                    )
                finally:
                    loop.close()

            # Create columns for displaying summaries
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(
                    "<h3 style='text-align: center;'>Viewpoint 1 Summary</h3>",
                    unsafe_allow_html=True,
                )
                st.write(summary1)

            with col2:
                st.markdown(
                    "<h3 style='text-align: center;'>Viewpoint 2 Summary</h3>",
                    unsafe_allow_html=True,
                )
                st.write(summary2)
        else:
            st.error("Please fill in all fields before generating summaries.")


if __name__ == "__main__":
    main()
