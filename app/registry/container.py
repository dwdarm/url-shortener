from typing import Any, Optional, Sequence, Type, Union
from bson.codec_options import TypeRegistry
from dependency_injector import containers, providers
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from app.interface.persistence.link_repository import LinkRepository
from app.domain.service.link_service import LinkService
from app.usecase.link_usecase import LinkUsecase

class Database(MongoClient):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.link_short['link'].create_index([('slug', 1)], unique=True)

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['app.interface.views.link_view'])

    config = providers.Configuration()

    client = providers.Singleton(Database, config.mongodb_uri, server_api=ServerApi('1'))

    link_repository = providers.Factory(
        LinkRepository,
        client=client,
        db=config.db_name
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