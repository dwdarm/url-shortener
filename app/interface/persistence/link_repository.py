import datetime

from pymongo import MongoClient

from app.domain.repository.link_repository_interface import LinkRepositoryInterface
from app.domain.model.link_model import Link, LinkCreate

class LinkRepository(LinkRepositoryInterface):
    
    def __init__(self, db: MongoClient) -> None:
        self.col = db.link_short['link']

    def make_link(self, data) -> Link:
        return Link(
            slug=data['slug'],
            href=data['href'],
            qr_code=data['qr_code'],
            create_at=data['create_at']
        )

    def find_by_slug(self, slug: str) -> Link | None:
        result = self.col.find_one({'slug': slug})
        if result == None:
            return None
        
        return self.make_link(result)
    
    def create(self, data: LinkCreate) -> Link | None:
        result = self.col.insert_one({
            **data.dict(),
            'create_at': datetime.datetime.utcnow(),
        })
        if result.acknowledged == False:
            return None
        
        return self.find_by_slug(slug=data.slug)