import os
from dataclasses import dataclass


@dataclass
class Credential:
    username: str
    password: str


@dataclass
class Token:
    auth_token: str = None


@dataclass
class Section:
    title: str
    credential: Credential = None
    token: Token = None

    def __init__(self, title: str):
        self.title = title
        self.credential = Credential(
            username=os.environ.get(f"{title}_username", "default_username"),
            password=os.environ.get(f"{title}_password", "default_password")
        )

    # def __str__(self) -> str:
    #     return self.title