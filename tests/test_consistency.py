import pytest
from mock_llm import mock_llm_response



def test_response_consistency():
    """
    Verifies that repeated calls with the same prompt
    do not produce wildly different responses.
    """

    prompt = "What is artificial intelligence?"
    responses = []

    for _ in range(5):
        result = mock_llm_response(prompt)
        responses.append(result["response"])

    unique_responses = set(responses)

    # Allow minor variation but not excessive inconsistency
    assert len(unique_responses) <= 2, (
        f"Inconsistent responses detected: {unique_responses}"
    )
