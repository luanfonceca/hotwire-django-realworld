from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import Profile
from articles.models import Article
from django.contrib.auth import get_user_model


def view(req, profile):
    user = get_object_or_404(get_user_model(), username=profile)
    articles = Article.objects.filter(author=user.profile)
    return render(
        req, "profile/detail.html", context={"article_user": user, "articles": articles}
    )


@login_required
def edit(request):
    status = 200
    initial = {
        "image": request.user.profile.image,
        "bio": request.user.profile.bio,
    }

    if request.method == "POST":
        form = EditProfileForm(request.POST, initial=initial)
        if form.is_valid():
            form.save(request.user)
            a = redirect("profile_view", profile=request.user.username)
            # Turbo expects a 303 response on form success
            a.status_code = 303
            return a
        else:
            # Turbo expects a 422 response on form errors
            status = 422
    else:
        form = EditProfileForm(initial=initial)

    return render(request, "profile/edit.html", {"form": form}, status=status)