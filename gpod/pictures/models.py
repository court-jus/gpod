from django.db import models


class POD(models.Model):
    day = models.DateField()
    answer = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.day}: {self.answer}"


class Picture(models.Model):
    asset = models.ImageField()
    order = models.IntegerField()
    pod = models.ForeignKey("POD", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pod} - {self.order}"
