import re

FILE_BLOCK_RE = re.compile(
    r"FILE:\s*(?P<path>\S+)\s*\n```[a-zA-Z0-9_+-]*\n(?P<content>.*?)\n```",
    re.DOTALL,
)

CODE_FENCE_RE = re.compile(r"```(?P<lang>[a-zA-Z0-9_+-]*)\n(?P<code>.*?)\n```", re.DOTALL)

LANG_EXTENSIONS = {
    "python": "py", "py": "py", "javascript": "js", "js": "js", "typescript": "ts",
    "ts": "ts", "tsx": "tsx", "jsx": "jsx", "html": "html", "css": "css",
    "java": "java", "kotlin": "kt", "go": "go", "rust": "rs", "ruby": "rb",
    "php": "php", "csharp": "cs", "c#": "cs", "cpp": "cpp", "c++": "cpp",
    "c": "c", "json": "json", "yaml": "yml", "yml": "yml", "toml": "toml",
    "ini": "ini", "bash": "sh", "sh": "sh", "shell": "sh", "powershell": "ps1",
    "sql": "sql", "markdown": "md", "md": "md", "text": "txt", "txt": "txt",
}


def parse_file_blocks(text: str) -> list[tuple[str, str]]:
    return [(m.group("path"), m.group("content")) for m in FILE_BLOCK_RE.finditer(text)]


def extract_code_blocks(text: str) -> list[tuple[str, str]]:
    """Fenced code blocks with no FILE: label, as (language, code)."""
    return [(m.group("lang").lower(), m.group("code")) for m in CODE_FENCE_RE.finditer(text)]


def guess_filename(language: str, index: int) -> str:
    ext = LANG_EXTENSIONS.get(language, "txt")
    suffix = "" if index == 0 else f"_{index + 1}"
    return f"codex_output{suffix}.{ext}"
