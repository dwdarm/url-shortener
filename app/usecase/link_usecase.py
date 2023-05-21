from secrets import token_urlsafe
from slugify import slugify

from app.domain.model.link_model import Link, LinkCreate
from app.domain.repository.link_repository_interface import LinkRepositoryInterface
from app.domain.service.link_service import LinkService

class LinkUsecaseInterface:
    def getLink(self, slug: str) -> Link|None:
        pass
    def createLink(self, slug: str|None, href: str) -> Link|None:
        pass

class LinkUsecase(LinkUsecaseInterface):
    repository: LinkRepositoryInterface = None
    service: LinkService = None

    def __init__(self, repository: LinkRepositoryInterface, service: LinkService) -> None:
        self.repository = repository
        self.service = service

    def getLink(self, slug: str) -> Link|None:
        return self.repository.find_by_slug(slug=slug)
    
    def createLink(self, slug: str|None, href: str) -> Link|None:
        ts = slug
        if ts == None:
            ts = token_urlsafe(6)
            while True:
                if self.service.check_slug(ts):
                    ts = token_urlsafe(6)
                else:
                    break
        else:
            ts = slugify(ts)

        return self.repository.create(LinkCreate(
            slug=ts, 
            href=href, 
            qr_code=self.service.generate_qr_code(ts)
        ))