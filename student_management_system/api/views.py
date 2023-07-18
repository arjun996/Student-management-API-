from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Student, Staff
from .serializers import CourseSerializer, StudentSerializer, StaffSerializer

@api_view(['GET'])
def student_list(request):
    queryset = Student.objects.all()
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def staff_list(request):
    queryset = Staff.objects.all()
    serializer = StaffSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_list(request):
    queryset = Course.objects.all()
    serializer = CourseSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_staff(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def staff_detail(request, staff_id):
    try:
        staff = Staff.objects.get(id=staff_id)
    except Staff.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        staff.delete()
        return Response(status=204)


