from django.contrib import admin

from .models import *

@admin.register(Users)
class User(admin.ModelAdmin):
    pass

@admin.register(Schedules)
class Schedule(admin.ModelAdmin):
    pass

@admin.register(Assignments)
class Assignment(admin.ModelAdmin):
    pass

@admin.register(GroupTag)
class GroupTag(admin.ModelAdmin):
    pass

@admin.register(ToDoList)
class ToDoList(admin.ModelAdmin):
    pass

@admin.register(Timetable)
class Timetable(admin.ModelAdmin):
    pass

@admin.register(Friends)
class Friend(admin.ModelAdmin):
    pass

@admin.register(Color)
class Color(admin.ModelAdmin):
    pass

@admin.register(ToDoListTask)
class ToDoListTask(admin.ModelAdmin):
    pass

@admin.register(Subjects)
class Subject(admin.ModelAdmin):
    pass

@admin.register(TimetableTimes)
class TimetableTimes(admin.ModelAdmin):
    pass
