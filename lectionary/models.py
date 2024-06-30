from django.db import models


class Day(models.Model):
    """A model representing a specific holy day within the three-year
    liturgical calendar.
    """

    class Year(models.TextChoices):
        A = ("A", "Year A")
        B = ("B", "Year B")
        C = ("C", "Year C")

    class Season(models.TextChoices):
        ADVENT = ("AD", "Advent")
        CHRISTMAS = ("CH", "Christmas")
        EPIPHANY = ("EP", "Epiphany")
        LENT = ("LE", "Lent")
        EASTER = ("EA", "Easter")
        PENTECOST = ("PE", "Pentecost")

    class Color(models.TextChoices):
        WHITE = ("WH", "White")
        RED = ("RD", "Red")
        GREEN = ("GR", "Green")
        VIOLET = ("VI", "Violet")

    class Rank(models.IntegerChoices):
        MINOR = (0, "Minor")
        MAJOR = (1, "Major")
        SUNDAY = (2, "Sunday")
        FIXED = (3, "Fixed")
        PRINCIPAL = (4, "Principal")

    name = models.CharField(max_length=100)
    alt_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=1, choices=Year)
    season = models.CharField(max_length=2, choices=Season, null=True, blank=True)
    color = models.CharField(max_length=2, choices=Color, null=True, blank=True)
    rank = models.IntegerField(choices=Rank, null=True, blank=True)
    lessons = models.ManyToManyField("Lesson")

    class Meta:
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return f"{self.name} ({self.year})"


class Lesson(models.Model):
    """A model representing a specific lesson appointed in the
    lectionary for one or more holy days. Note that the scripture field
    may have alternate readings separated by " or ".
    """

    scripture = models.CharField(max_length=300)
    days = models.ManyToManyField("Day")

    def __str__(self):
        return f"{self.scripture}"
