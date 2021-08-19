from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name', 'password')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('title', 'start_time', 'end_time', 'is_all_day', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')
       
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('user_id', 'friend_user_id')

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = ('name', 'start_time', 'end_time', 'is_finished', 'complete_time', 'required_time', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')

class TimeTableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTableTimes
        fields = ('user_id', 'start_time', 'class_time', 'break_time', 'lunch_break_start_time', 'lunch_break_end_time')

class GroupTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTags
        fields = ('name', 'user_id')

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTables
        fields = ('monday_timetable', 'tuesday_timetable', 'wednesday_timetable', 'thursday_timetable', 'friday_timetable', 'saturday_timetable', 'sunday_timetable', 'user_id')

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoLists
        fields = ('name', 'subjects_id', 'limited_time', 'estimated_work_time', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'is_work_finished', 'user_id')

class ToDoListTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoListTasks
        fields = ('to_do_list_id', 'name', 'is_work_finished')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('name', 'is_hidden', 'user_id', 'color_id')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('name', 'red', 'green', 'blue')
