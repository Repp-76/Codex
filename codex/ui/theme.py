from rich.theme import Theme
from rich.console import Console

CODEX_THEME = Theme({
    "codex.red": "bold red",
    "codex.dim": "grey58",
    "codex.ok": "bold green",
    "codex.warn": "bold yellow",
    "codex.err": "bold red",
})

console = Console(theme=CODEX_THEME)
