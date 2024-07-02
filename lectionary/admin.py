from django.contrib import admin

from lectionary.models import Day, Lesson


class PropersInline(admin.TabularInline):
    model = Day.lessons.through
    extra = 0


class DayAdmin(admin.ModelAdmin):
    inlines = [
        PropersInline,
    ]
    exclude = ["lessons"]


class LessonAdmin(admin.ModelAdmin):
    inlines = [
        PropersInline,
    ]
    exclude = ["days"]


admin.site.register(Day, DayAdmin)
admin.site.register(Lesson, LessonAdmin)
