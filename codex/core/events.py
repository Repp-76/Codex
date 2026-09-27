from dataclasses import dataclass


@dataclass
class FileCreatedEvent:
    path: str


@dataclass
class FileModifiedEvent:
    path: str


@dataclass
class ProjectCreatedEvent:
    root: str
    files: list[str]
    project_name: str


@dataclass
class ConversationExportedEvent:
    path: str
