MAX_CONTEXT_CHARS = 20000


def build_project_context(project, focus_files: list[str] | None = None) -> str:
    if project is None:
        return ""

    files = focus_files or project.list_files()
    chunks = []
    used = 0
    for rel_path in files:
        content = project.read_file(rel_path)
        if content is None:
            continue
        chunk = f"FILE: {rel_path}\n```\n{content}\n```\n"
        if used + len(chunk) > MAX_CONTEXT_CHARS:
            break
        chunks.append(chunk)
        used += len(chunk)

    return "\n".join(chunks)
