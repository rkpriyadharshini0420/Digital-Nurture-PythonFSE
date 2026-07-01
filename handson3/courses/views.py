from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Enrollment, Student
from .serializers import CourseSerializer, StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    # This replaces the need for separate List and Detail views
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # This is the "Custom Action" requested in Task 34
    # It creates the URL: /api/courses/{id}/students/
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        course = self.get_object() # Gets the specific course
        # Find all enrollments for this course and get the students
        enrollments = Enrollment.objects.filter(course=course)
        students = [e.student for e in enrollments]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)