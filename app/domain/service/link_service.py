import qrcode
import base64
import io

from app.domain.repository.link_repository_interface import LinkRepositoryInterface
from app.domain.model.link_model import Link
from config.setting import BASE_DOMAIN

class LinkService:

    link_repository: LinkRepositoryInterface = None

    def __init__(self, link_repository: LinkRepositoryInterface) -> None:
        self.link_repository =  link_repository

    def check_slug(self, slug: str) -> bool:
        link = self.link_repository.find_by_slug(slug=slug)
        if link != None:
            return True
        
        return False
    
    def generate_qr_code(self, slug: str) -> str:
        img = qrcode.make(BASE_DOMAIN + '/' + slug)
        buf = io.BytesIO()
        img.save(buf)

        return 'data: image/gif;base64, '+ base64.b64encode(buf.getvalue()).decode('utf-8')
