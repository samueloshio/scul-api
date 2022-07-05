from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class Gender(str, Enum):
    male = "Male"
    female = "Female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    editor = "editor"

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


class User(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    # role: List[Role]
    #post: List[Post]