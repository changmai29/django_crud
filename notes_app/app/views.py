from django.shortcuts import render

from rest_framework import viewsets
from app.models import Notes
from app.serializers import NotesSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset= Notes.objects.all()
    serializer_class=NotesSerializer
    
    #companies/{companyId}/emplyees
    # @action(detail=True,methods=['get'])
    # def employees(self,request,pk=None):   
    #     try:                
    #         company=Company.objects.get(pk=pk)
    #         emps=Employee.objects.filter(company=company)
    #         emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
    #         return Response(emps_serializer.data)
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'message':'Company might not exists !! Error'
    #         })

# Create your views here.
# class NotesList(APIView):

#     def post(self, request, format=None):
#         serializer = NotesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request, format=None):
#         snippets = Notes.objects.all()
#         serializer = NotesSerializer(snippets, many=True)
#         return Response(serializer.data)
