from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SerConverter
from rest_framework.response import Response
from .models import*
# Create your views here.
class CreatUser(APIView):
    def post(self,request):
        d1=request.data
        ser_obj=SerConverter(data=d1)
        if ser_obj.is_valid():
            ser_obj.save()
            all_row=User.objects.all()
            ser_obj=SerConverter(all_row,many=True)
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)
        

class RetriveData(APIView):

    def get(self,request):
        all_rows=User.objects.all()
        ser_obj=SerConverter(all_rows, many=True)
        return Response(ser_obj.data)
    

class UpdateData(APIView):

    def put(self,request,pk):

        single_user=User.objects.get(id=pk)
        d1=request.data
        ser_obj=SerConverter(single_user,data=d1)
        if ser_obj.is_valid():
            ser_obj.save()

            all_rows=User.objects.all()
            ser_obj=SerConverter(all_rows,many=True)
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)


class DeleteData(APIView):

    def delete(self,request,pk):
        user1=User.objects.get(id=pk)
        user1.delete()

        all_rows=User.objects.all()
        ser_obj=SerConverter(all_rows,many=True)
        return Response(ser_obj.data)