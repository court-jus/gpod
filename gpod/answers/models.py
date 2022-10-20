from django.db import models

from pictures.models import POD


class Answer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    who = models.CharField(max_length=300)
    guess = models.CharField(max_length=300)
    pod = models.ForeignKey(POD, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return f"{self.date}: {self.who}: {self.guess}"
