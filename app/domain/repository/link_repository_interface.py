from app.domain.model.link_model import Link, LinkCreate

class LinkRepositoryInterface:

    def find_by_slug(self, slug: str) -> Link|None:
        pass

    def create(self, data: LinkCreate) -> Link|None:
        pass