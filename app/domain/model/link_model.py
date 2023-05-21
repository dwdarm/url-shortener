from pydantic import BaseModel
from pydantic import HttpUrl
from typing import Any

class Link(BaseModel):
    slug: str
    href: HttpUrl
    create_at: Any
    qr_code: Any

class LinkCreate(BaseModel):
    slug: str
    href: HttpUrl
    qr_code: Any