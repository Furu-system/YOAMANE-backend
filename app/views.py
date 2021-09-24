from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *
from .common_schedule import CommonSchedule

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignments.objects.all()
    serializer_class = AssignmentSerializer

class TimeTableTimeViewSet(viewsets.ModelViewSet):
    queryset = TimeTableTimes.objects.all()
    serializer_class = TimeTableTimeSerializer

class GroupTagViewSet(viewsets.ModelViewSet):
    queryset = GroupTags.objects.all()
    serializer_class = GroupTagSerializer

class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTables.objects.all()
    serializer_class = TimeTableSerializer

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoLists.objects.all()
    serializer_class = ToDoListSerializer

    def list(self, request, pk=None):
        print(request)
        todolists = ToDoLists.objects.filter(user_id=request.POST.get("user_id"), subject_id=request.POST.get("subject_id"))
        serializer = ToDoListSerializer(todolists, many=True)
        return Response(serializer.data)

class ToDoListTaskViewSet(viewsets.ModelViewSet):
    queryset = ToDoListTasks.objects.all()
    serializer_class = ToDoListTaskSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    serializer_class = ColorSerializer

class CommonScheduleAPIView(APIView):
    def get(self, request, format=None):
        common_schedule = CommonSchedule(request)
        return Response({"message":common_schedule.helloworld()})