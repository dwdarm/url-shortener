from secrets import token_urlsafe
from slugify import slugify

from app.domain.model.link_model import Link
from app.domain.repository.link_repository_interface import LinkRepositoryInterface
from app.domain.service.link_service import LinkService

class LinkUsecaseInterface:
    def getLink(self, slug: str):
        pass
    def createLink(self, slug: str, href: str):
        pass

class LinkUsecase(LinkUsecaseInterface):
    repository: LinkRepositoryInterface = None
    service: LinkService = None

    def __init__(self, repository: LinkRepositoryInterface, service: LinkService) -> None:
        self.repository = repository
        self.service = service

    def getLink(self, slug: str):
        return self.repository.find_by_slug(slug=slug)
    
    def createLink(self, slug: str, href: str):
        ts = slug
        if not ts:
            ts = token_urlsafe(6)
            while True:
                if self.service.check_slug(ts):
                    ts = token_urlsafe(6)
                else:
                    break
        else:
            ts = slugify(ts)

        return self.repository.create(Link(
            slug=ts, 
            href=href, 
            qr_code=self.service.generate_qr_code(ts)
        ))