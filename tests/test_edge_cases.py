from mock_llm import mock_llm_response

from utils.input_generator import generate_edge_inputs


def test_edge_case_handling():
    """
    Tests AI responses against various edge-case inputs
    to ensure graceful handling and no crashes.
    """

    edge_inputs = generate_edge_inputs()

    for prompt in edge_inputs:
        result = mock_llm_response(prompt)

        assert "response" in result, "Missing response field"
        assert result["response"] is not None, "Response is None"
        assert isinstance(result["response"], str), "Response is not a string"
