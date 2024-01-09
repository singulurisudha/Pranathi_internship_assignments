from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from library.models import Student , Books

class BookStatusAPIView(APIView):
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                
                obj=Books.objects.get(pk=pk)
                data = [{"b_id": obj.b_id, "b_name": obj.b_name,
                         "author":obj.author
                         }
                        ]
                return Response(data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'error': 'book not found'}, status=404)
        else:
            obj = Books.objects.all()
            data = [
                    {"b_id": instance.b_id, "b_name": instance.b_name,
                         "author":instance.author
                    } for instance in obj
                   ]
        return Response(data, status=status.HTTP_200_OK)
    def post(self, request,*args,**kwargs):
        try:
            data = request.data
            new_obj = Books.objects.create(**data)
            new_obj.save()
            return Response({"message": "Book Added successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg':'add book name , author'})
    def put(self, request,pk, *args, **kwargs):
        try:
            data = request.data
            obj = Books.objects.get(pk=pk)
            obj.b_name = data.get('b_name', obj.b_name)
            obj.author = data.get('author', obj.author)
            obj.save()
            return Response({'msg':'Book Updated Successfully..!!!!'} ,
                             status=status.HTTP_200_OK)
        except:
            return Response({'msg':'Unable to update the Book details check once...'})
        
    def delete(self, request, pk, *args, **kwargs):
        obj = Books.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Book deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        
class StudentStatusAPIView(APIView):
    
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            try:
                
                obj=Student.objects.get(pk=pk)
                
                s_data = [{"s_id": obj.s_id, "s_name": obj.s_name,
                         "book_name":obj.book_name.b_name,"taken":obj.taken,"returned":obj.returned
                         }
                        ]
                return Response(s_data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
        else:
            obj = Student.objects.all()
            data = [{"s_id": instance.s_id, "s_name": instance.s_name,
                         "book_name":instance.book_name.b_name,"taken":instance.taken,"returned":instance.returned
                    } for instance in obj
                    ]
        return Response(data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        try:
            data = request.data
            b_id = data.get('b_id')  # Assuming 'b_id' is sent in the request data

            # Check if the book with the provided ID exists
            try:
                book = Books.objects.get(pk=b_id)
            except Books.DoesNotExist:
                return Response({"message": "Book does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new student with the associated book
            student = Student.objects.create(
                s_name=data['s_name'],
                taken=data['taken'],
                returned=data['returned'],
                book_name=Books.objects.get(pk=b_id)  # Assign the book object to the student's foreign key field
            )

            return Response({"message": "Student Added successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request,pk, *args, **kwargs):
        try:
            data = request.data

            obj2=Books.objects.get(pk=pk)
            obj2.author=data.get('author',obj2.author)
            obj2.b_name=data.get('b_name',obj2.b_name)

            obj = Student.objects.get(pk=pk)
            obj.s_name = data.get('s_name', obj.s_name)
            obj.taken=data.get('taken',obj.taken)
            obj.returned=data.get('returned',obj.returned)
            obj.save()
            return Response({'msg':'Student Updated Successfully..!!!!'} ,
                             status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk, *args, **kwargs):
        obj = Student.objects.get(pk=pk)
        obj.delete()
        return Response({'message': 'Student deleted successfully'},status=status.HTTP_204_NO_CONTENT)







