import asyncio
from abc import ABC, abstractmethod
from typing import Optional

from .models import *
from .session import SessionMetadata

class BaseBot(ABC):
    def __init__(self, session_metadata: SessionMetadata):
        self.session_metadata = session_metadata

    @abstractmethod
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        pass

    @abstractmethod
    async def on_chat(self, user: User, message: str) -> None:
        pass

    @abstractmethod
    async def on_user_join(self, user: User) -> None:
        pass

    @abstractmethod
    async def on_user_leave(self, user: User) -> None:
        pass
