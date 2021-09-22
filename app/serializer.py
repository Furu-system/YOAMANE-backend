from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *

class UserSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source

    id = serializers.IntegerField(
        read_only=True
    )
    user_id=serializers.IntegerField(
        read_only=True
    )
    
    def validate_username(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value
    
    class Meta:
        model = Users
        fields = ('id', 'user_id', 'username', 'password')
        #read_only_fields = ('id','user_id','updated_at','created_at')


    def create(self, validated_data):
        user = Users(
            user_id = validated_data["user_id"],
            username = validated_data["username"],
            password = make_password(validated_data["password"])
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.username = validated_data.get("username", instance.name)
        instance.password = make_password(validated_data.get("password", instance.password))
        instance.save()
        return instance


class GroupNameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True
    )

    def validate_name(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value

    class Meta:
        model = GroupNames
        fields = ('id','name')


class GroupTagSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()

    id = serializers.IntegerField(
        read_only=True
    )
    user_id=serializers.IntegerField(
        read_only=True
    )
    groupname_id = serializers.IntegerField(
        read_only=True
    )
    create_user_id=serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = GroupTags
        fields = ('id','user_id','groupname_id','create_user_id')


class ScheduleSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # collaborating_group_id = GroupTagSerializer()
    # collaborating_member_id = UserSerializer()

    id = serializers.IntegerField(
        read_only=True
    )
    user_id=serializers.IntegerField(
        read_only=True
    )

    def validate_title(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value

    class Meta:
        model = Schedules
        fields = ('id', 'title', 'start_time', 'end_time', 'is_all_day', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')


class FriendSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # friend_user_id = UserSerializer()

    id = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Friends
        fields = ('id', 'user_id', 'friend_user_id')


class AssignmentSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # collaborating_group_id = GroupTagSerializer()
    # collaborating_member_id = UserSerializer()

    id = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Assignments
        fields = ('id', 'name', 'start_time', 'is_finished', 'complete_time', 'required_time', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')


class TimeTableTimeSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()

    id = serializers.IntegerField(
        read_only=True
    )
    user_id = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = TimeTableTimes
        fields = ('id', 'user_id', 'start_time', 'class_time', 'break_time', 'lunch_break_start_time', 'lunch_break_end_time')


class TimeTableSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()

    id = serializers.IntegerField(
        read_only=True
    )
    user_id=serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = TimeTables
        fields = ('id', 'monday_timetable', 'tuesday_timetable', 'wednesday_timetable', 'thursday_timetable', 'friday_timetable', 'saturday_timetable', 'sunday_timetable', 'user_id')
    

class ToDoListSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # subjects_id = SubjectSerializer()

    id = serializers.IntegerField(
        read_only=True
    )
    subject_id = serializers.IntegerField(
        read_only = True
    )
    user_id = serializers.IntegerField(
        read_only=True
    )

    def validate_name(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value

    class Meta:
        model = ToDoLists
        fields = ('id', 'name', 'subject_id', 'limited_time', 'estimated_work_time', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'is_work_finished', 'user_id')


class ToDoListTaskSerializer(serializers.ModelSerializer):
    # to_do_list_id = ToDoListSerializer()

    id = serializers.IntegerField(
        read_only=True
    )

    def validate_name(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value

    class Meta:
        model = ToDoListTasks
        fields = ('id', 'to_do_list_id', 'name', 'is_work_finished')


class ColorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True
    )

    def validate_name(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value

    def validate_red(self,value):
        if value > 255 or value<0:
            raise serializers.ValidationError("The value has to be within 255 - 0")
        return value

    def validate_green(self,value):
        if value > 255 or value<0:
            raise serializers.ValidationError("The value has to be within 255 - 0")
        return value

    def validate_blue(self,value):
        if value > 255 or value<0:
            raise serializers.ValidationError("The value has to be within 255 - 0")
        return value

    class Meta:
        model = Colors
        fields = ('id', 'name', 'red', 'green', 'blue')


class SubjectSerializer(serializers.ModelSerializer):
    # user_id = UserSerializer()
    # color_id = ColorSerializer()
    id = serializers.IntegerField(
        read_only=True
    )
    user_id=serializers.IntegerField(
        read_only=True
    )

    def validate_name(self,value):
        if len(value) > 50:
            raise serializers.ValidationError("The name has to be within 50 charactor")
        return value
    
    class Meta:
        model = Subjects
        fields = ('id', 'name', 'is_hidden', 'user_id', 'color_id')
