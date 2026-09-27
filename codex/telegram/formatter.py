from pathlib import Path


def document_caption(rel_path: str) -> str:
    return f"Codex \u2014 {Path(rel_path).name}"


def zip_caption(project_name: str, file_count: int) -> str:
    return f"Codex \u2014 {project_name} ({file_count} files)"


def chat_export_caption() -> str:
    return "Codex \u2014 conversation export"
