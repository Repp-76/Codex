from dataclasses import dataclass, field
from typing import Optional

from core.history import History
from project.manager import Project
from project.editor import Editor


@dataclass
class Session:
    provider: str
    model: str
    project: Optional[Project] = None
    editor: Optional[Editor] = None
    history: History = field(default_factory=History)
    last_response: str = ""
