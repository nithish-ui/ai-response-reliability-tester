from mock_llm import mock_llm_response



def test_response_latency_under_threshold():
    """
    Ensures the AI response latency stays under 1 second.
    """

    prompt = "Test response latency"
    result = mock_llm_response(prompt)

    latency = result["latency"]

    assert latency < 1.0, (
        f"Response latency too high: {latency} seconds"
    )
