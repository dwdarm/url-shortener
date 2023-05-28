from flask import jsonify, request, render_template, redirect

from dependency_injector.wiring import inject, Provide

from app.usecase.link_usecase import LinkUsecase
from app.registry.container import Container

@inject
def get_link_by_slug_view(
    slug: str,
    link_usecase: LinkUsecase = Provide[Container.link_usecase]
):
    link = link_usecase.getLink(slug=slug)
    if link == None:
        return redirect('/', code=302)
    
    return redirect(link.href, code=302)

@inject
def create_link_view(
    base_domain: str = Provide[Container.config.base_domain],
    link_usecase: LinkUsecase = Provide[Container.link_usecase]
):
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        link = link_usecase.createLink(
            slug=None,
            href=request.form['url'],
        )

        data = {
            'base_domain': base_domain,
            'link': link
        }

        return render_template('index.html', data=data)