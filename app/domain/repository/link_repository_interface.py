from app.domain.model.link_model import Link, LinkCreate

class LinkRepositoryInterface:

    def find_by_slug(self, slug: str):
        pass

    def create(self, data: LinkCreate):
        pass