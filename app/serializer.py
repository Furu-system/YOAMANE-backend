from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'user_id', 'name', 'password')

    def create(self, validated_data):
        user = Users(
            user_id = validated_data["user_id"],
            name = validated_data["name"],
            password = make_password(validated_data["password"])
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.name = validated_data.get("name", instance.name)
        instance.password = make_password(validated_data.get("password", instance.password))
        instance.save()
        return instance

class GroupTagSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()

    class Meta:
        model = GroupTags
        fields = ('id', 'name', 'user_id')

class ScheduleSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # collaborating_group_id = GroupTagSerializer()
    # collaborating_member_id = UserSerializer()

    class Meta:
        model = Schedules
        fields = ('id', 'title', 'start_time', 'end_time', 'is_all_day', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')
       
class FriendSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # friend_user_id = UserSerializer()

    class Meta:
        model = Friends
        fields = ('id', 'user_id', 'friend_user_id')

class AssignmentSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # collaborating_group_id = GroupTagSerializer()
    # collaborating_member_id = UserSerializer()

    class Meta:
        model = Assignments
        fields = ('id', 'name', 'start_time', 'end_time', 'is_finished', 'complete_time', 'required_time', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')

class TimeTableTimeSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    
    class Meta:
        model = TimeTableTimes
        fields = ('id', 'user_id', 'start_time', 'class_time', 'break_time', 'lunch_break_start_time', 'lunch_break_end_time')

class TimeTableSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()

    class Meta:
        model = TimeTables
        fields = ('id', 'monday_timetable', 'tuesday_timetable', 'wednesday_timetable', 'thursday_timetable', 'friday_timetable', 'saturday_timetable', 'sunday_timetable', 'user_id')

class ToDoListSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # subjects_id = SubjectSerializer()

    class Meta:
        model = ToDoLists
        fields = ('id', 'name', 'subjects_id', 'limited_time', 'estimated_work_time', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'is_work_finished', 'user_id')

class ToDoListTaskSerializer(serializers.ModelSerializer):
    # to_do_list_id = ToDoListSerializer()

    class Meta:
        model = ToDoListTasks
        fields = ('id', 'to_do_list_id', 'name', 'is_work_finished')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'name', 'red', 'green', 'blue')

class SubjectSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # color_id = ColorSerializer()

    class Meta:
        model = Subjects
        fields = ('id', 'name', 'is_hidden', 'user_id', 'color_id')

