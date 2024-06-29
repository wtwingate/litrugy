from django.db import models


class Years(models.IntegerChoices):
    """A model representing years in the three-year liturgical cycle.
    Year A starts on the first Sunday of Advent in years evenly
    divisible by 3.
    """

    A = 0
    B = 1
    C = 2


class Seasons(models.TextChoices):
    """A model representing the various liturgical seasons."""

    ADVENT = ("AD", "Advent")
    CHRISTMAS = ("CH", "Christmas")
    EPIPHANY = ("EP", "Epiphany")
    LENT = ("LE", "Lent")
    EASTER = ("EA", "Easter")
    PENTECOST = ("PE", "Pentecost")


class Colors(models.TextChoices):
    """A model representing the various liturgical colors associated
    with seasons and holy days.
    """

    WHITE = ("WH", "White")
    RED = ("RD", "Red")
    GREEN = ("GR", "Green")
    VIOLET = ("VI", "Violet")


class Ranks(models.IntegerChoices):
    """A model representing ranks of precedence for holy days in the
    liturgical calendar.
    """

    MINOR = 0
    MAJOR = 1
    SUNDAY = 2
    FIXED = 3
    PRINCIPAL = 4


class Day(models.Model):
    """A model representing a specific holy day within the three-year
    liturgical calendar.
    """

    name = models.CharField(max_length=100)
    alt_name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(choices=Years)
    season = models.CharField(max_length=2, choices=Seasons, null=True, blank=True)
    color = models.CharField(max_length=2, choices=Colors)
    lessons = models.ManyToManyField("Lesson")

    class Meta:
        indexes = [models.Index(fields=["name", "alt_name"])]

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
