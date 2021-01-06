from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Article


def view(req, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(req, "articles/detail.html",
                            {'article': article})


@login_required
def edit(req, slug):
    return render(req, "articles/edit.html")


@login_required
def create(req):
    return render(req, "articles/edit.html")