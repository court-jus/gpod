import datetime
from django.shortcuts import render


from answers.models import Answer
from .models import Picture, POD


def main_view(request):
    context = {
        "imageurl": None,
        "last_guesses": [],
        "errors": [],
        "messages": [],
    }
    today = datetime.date.today()
    pod = POD.objects.filter(day=today).first()
    if pod:
        picture_to_show = Picture.objects.filter(order=0, pod=pod).first()
        if picture_to_show:
            context["imageurl"] = picture_to_show.asset.url
        context["last_guesses"] = Answer.objects.filter(pod=pod).order_by("-date")[:10]

    if request.method == "POST":
        print("GUESS", request.POST)
        data = request.POST
        if not "name" in data or not data["name"]:
            context["errors"].append("Please enter your name")
        if not "guess" in data or not data["guess"]:
            context["errors"].append("Please enter your guess")
        if pod and not context["errors"]:
            answer = Answer.objects.create(
                who=data["name"], guess=data["guess"], pod=pod
            )
            print("Answer", answer, "recorded")
    return render(request, "pictures/main.html", context)
