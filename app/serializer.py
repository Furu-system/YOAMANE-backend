from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('title', 'start_time', 'end_time', 'is_all_day', 'notifying_time', 'collaborating_member_id', 'collaborating_group_id', 'memo', 'user_id')
        
