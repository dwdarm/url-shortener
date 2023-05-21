from typing import Any, Optional, Sequence, Type, Union
from bson.codec_options import TypeRegistry
from dependency_injector import containers, providers
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from app.interface.persistence.link_repository import LinkRepository
from app.domain.service.link_service import LinkService
from app.usecase.link_usecase import LinkUsecase
from config.setting import MONGODB_URI

class Database(MongoClient):
    def __init__(self, host: str | Sequence[str] | None = None, port: int | None = None, document_class: type | None = None, tz_aware: bool | None = None, connect: bool | None = None, type_registry: TypeRegistry | None = None, **kwargs: Any) -> None:
        super().__init__(host, port, document_class, tz_aware, connect, type_registry, **kwargs)
        self.link_short['link'].create_index([('slug', 1)], unique=True)

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['app.interface.views.link_view'])

    db = providers.Singleton(Database, MONGODB_URI, server_api=ServerApi('1'))

    link_repository = providers.Factory(
        LinkRepository,
        db=db
    )
    link_service = providers.Factory(
        LinkService,
        link_repository=link_repository
    )
    link_usecase = providers.Factory(
        LinkUsecase,
        repository=link_repository,
        service=link_service
    )