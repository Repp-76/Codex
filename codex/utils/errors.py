class CodexError(Exception):
    pass


_SUGGESTIONS = {
    "auth": "Check the API key in your .env file.",
    "rate_limit": "Wait a moment and try again, or reduce request frequency.",
    "timeout": "Check your network connection and retry.",
    "connection": "Check your network connection and retry.",
    "model_not_found": "Verify the model name with /model.",
    "not_configured": "Add the provider's API key to .env.",
    "server_error": "The provider is likely having issues. Try again shortly.",
    "empty_response": "Try rephrasing the request or switching models.",
}


def error_suggestion(code: str) -> str:
    return _SUGGESTIONS.get(code, "Review the request and try again.")
