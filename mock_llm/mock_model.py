import random
import time

def mock_llm_response(prompt: str) -> dict:
    """
    Simulates an LLM response with random latency and occasional failures
    """
    start_time = time.time()

    # Simulated latency
    time.sleep(random.uniform(0.1, 0.6))

    if not prompt.strip():
        response = "I'm sorry, I didn't understand your query."
    elif len(prompt) > 300:
        response = "Your input is too long. Please shorten it."
    elif "???" in prompt:
        response = random.choice([
            "Could you clarify your question?",
            "I'm not sure I understand."
        ])
    else:
        response = f"Processed response for: {prompt[:50]}"

    latency = round(time.time() - start_time, 3)

    return {
        "response": response,
        "latency": latency
    }
