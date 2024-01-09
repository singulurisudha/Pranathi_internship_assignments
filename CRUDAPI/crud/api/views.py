from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import F, ExpressionWrapper, fields
from crud.models import Students
from django.db.models import  Max , Min


class StudentAPIView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            try:
                
                obj=Students.objects.get(pk=pk)
                #using aggregate function
                
                max_marks=Students.objects.aggregate(max_marks=Max('obtained_marks'))['max_marks']
                min_marks=Students.objects.aggregate(min_marks=Min('obtained_marks'))['min_marks']

                student_with_max_marks = Students.objects.filter(obtained_marks=max_marks).values().first()
                student_with_min_marks = Students.objects.filter(obtained_marks=min_marks).values().first()
                
                data = [{"stu_id": obj.stu_id, "first_name": obj.first_name,
                          "last_name": obj.last_name, 
                         "email": obj.email,"obtained_marks":obj.obtained_marks,
                         "total_marks":obj.total_marks},
                         {
                             "MAXIMUM MARKS":student_with_max_marks
                         },
                         {
                             "MINIMUM MARKS":student_with_min_marks
                         }
                         
                         ]
                
                return Response(data, status=status.HTTP_200_OK)
            except Students.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
        else:
            obj = Students.objects.all()
            data = [{"stu_id": instance.stu_id, "first_name": instance.first_name, 
                     "last_name": instance.last_name,
                     "email": instance.email,"obtained_marks":instance.obtained_marks,
                     "total_marks":instance.total_marks} 
                    for instance in obj]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            new_obj = Students(**data)
            new_obj.save()
            return Response({"message": "Student Added successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg':'add first name , last name , email'})

    def put(self, request,pk, *args, **kwargs):
        try:
            data = request.data
            obj = Students.objects.get(pk=pk)
            obj.first_name = data.get('first_name', obj.first_name)
            obj.last_name = data.get('last_name', obj.last_name)
            obj.email = data.get('email', obj.email)
            obj.obtained_marks=data.get('obtained_marks',obj.obtained_marks)
            obj.total_marks=data.get('total_marks',obj.total_marks)
            obj.save()
            return Response({'msg':'Data Updated Successfully..!!!!'} ,
                             status=status.HTTP_200_OK)
        except:
            return Response({'msg':'Unable to update the student details check once...'})


    def delete(self, request, pk, *args, **kwargs):
        obj = Students.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Student deleted successfully'},status=status.HTTP_204_NO_CONTENT)
