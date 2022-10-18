import datetime
from django.shortcuts import render

from .models import Picture


def main_view(request):
    today = datetime.date.today()
    picture_to_show = Picture.objects.filter(order=0, pod__day=today).first()
    if picture_to_show:
        url = picture_to_show.asset.url
    return render(request, "pictures/main.html", {"picture": url})
