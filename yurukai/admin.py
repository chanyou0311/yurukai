from django.contrib import admin

from .models import User, Area, Tag, Yurukai, Schedule, Entry


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "bio", "updated", "created"]


class AreaAdmin(admin.ModelAdmin):
    list_display = ["name", "updated", "created"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "updated", "created"]


class YurukaiAdmin(admin.ModelAdmin):
    list_display = ["name", "area", "updated", "created"]


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["yurukai", "start_time", "end_time", "updated", "created"]
    fields = ["yurukai", "start_time", "end_time"]


class EntryAdmin(admin.ModelAdmin):
    list_display = ["user", "schedule", "is_join", "is_teacher", "updated", "created"]


admin.site.register(User, UserAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Yurukai, YurukaiAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Entry, EntryAdmin)
