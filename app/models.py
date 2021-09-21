import uuid
from django.db import models
#from django_mysql.models import Model

# Create your models here.

class Users(models.Model):
    user_id = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)
    
    __str__ = __repr__

class Colors(models.Model):
    name = models.CharField(max_length=50)
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)
    
    __str__ = __repr__

class Friends(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="my_id")
    friend_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="friend_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GroupNames(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GroupTags(models.Model):
    #name = models.CharField(max_length=50)
    groupname_id = models.ForeignKey(GroupNames, on_delete=models.CASCADE)
    create_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="create_user")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="grouptag_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)
    
    __str__ = __repr__

class Schedules(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    is_all_day = models.BooleanField(null=True)
    notifying_time = models.TimeField(null=True)
    collaborating_member_id = models.ForeignKey(Users, on_delete=models.CASCADE,null=True,related_name="collaborating_member")
    collaborating_group_id = models.ForeignKey(GroupTags,on_delete=models.CASCADE,null=True)
    memo = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="schedule_user")

class Subjects(models.Model):
    name = models.CharField(max_length=50)
    is_hidden = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Colors, on_delete=models.CASCADE)

class ToDoLists(models.Model):
    name = models.CharField(max_length=50)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    limited_time = models.DateTimeField()
    estimated_work_time = models.DateTimeField()
    notifying_time = models.TimeField(null=True)
    collaborating_member_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name="member_id")
    collaborating_group_id = models.ForeignKey(GroupTags, on_delete=models.CASCADE, null=True, related_name="group_id")
    memo = models.TextField(null=True)
    is_work_finished = models.BooleanField(null=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)
    
    __str__ = __repr__

class Assignments(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    #end_time = models.DateTimeField()
    is_finished = models.BooleanField(null=True)
    complete_time = models.DateTimeField()
    required_time = models.TimeField()
    notifying_time = models.TimeField(null=True)
    margin = models.IntegerField()
    collaborating_member_id = models.IntegerField(null=True)
    collaborating_group_id = models.IntegerField(null=True)
    memo = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    to_do_list_id = models.ForeignKey(ToDoLists, on_delete=models.CASCADE)

class TimeTables(models.Model):
    monday_timetable = models.TextField(null=True)
    tuesday_timetable = models.TextField(null=True)
    wednesday_timetable = models.TextField(null=True)
    thursday_timetable = models.TextField(null=True)
    friday_timetable = models.TextField(null=True)
    saturday_timetable = models.TextField(null=True)
    sunday_timetable = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class ToDoListTasks(models.Model):
    to_do_list_id = models.ForeignKey(ToDoLists, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_work_finished = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TimeTableTimes(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_time = models.TimeField()
    class_time = models.TimeField()
    break_time = models.TimeField()
    lunch_break_start_time = models.TimeField()
    lunch_break_end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
