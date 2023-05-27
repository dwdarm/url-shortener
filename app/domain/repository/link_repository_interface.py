from app.domain.model.link_model import Link

class LinkRepositoryInterface:

    def find_by_slug(self, slug: str):
        pass

    def create(self, data: Link):
        pass