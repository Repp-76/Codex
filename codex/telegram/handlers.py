FILE_REQUEST_PHRASES = (
    "as a file", "as a python file", "as a script", "send the file",
    "send this as", "give me the file", "export this", "create the zip",
    "project zip", "download this", "as a .py file", "as a document",
    "hantar sebagai fail", "hantar file",
)


def wants_file(message: str) -> bool:
    lowered = message.lower()
    return any(phrase in lowered for phrase in FILE_REQUEST_PHRASES)
