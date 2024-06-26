from django.db import models


class Years(models.IntegerChoices):
    A = 0
    B = 1
    C = 2


class Ranks(models.IntegerChoices):
    pass


class Colors(models.TextChoices):
    WHITE = ("WH", "White")
    RED = ("RD", "Red")
    GREEN = ("GR", "Green")
    VIOLET = ("VI", "Violet")
    ROSE = ("RO", "Rose")
    BLACK = ("BK", "Black")
    BLUE = ("BL", "Blue")


class Day(models.Model):
    name = models.CharField(max_length=200)
    alt_name = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(choices=Years)
    season = models.ForeignKey("Season", on_delete=models.PROTECT)
    rank = models.IntegerField(choices=Ranks)
    color = models.Choices(choices=Colors, default=Colors.WHITE)
    lessons = models.ManyToManyField("Lesson")

    def __str__(self):
        return self.name


class Lesson(models.Model):
    # A lesson may provide alternate readings
    scripture = models.CharField(max_length=100)
    alt_scripture = models.CharField(max_length=100, null=True, blank=True)
    alt_alt_scripture = models.CharField(max_length=100, null=True, blank=True)
    days = models.ManyToManyField("Day")
