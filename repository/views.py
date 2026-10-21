from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from repository.models import QuestionDB
from repository.serializers import QuestionSerializer
from repository.models import SubmissionDb
from repository.serializers import SubmissionSerializer


# Create your views here.

class QuestionListCreateView(APIView):

    def get(self, request):
        qs = QuestionDB.objects.all()
        serializer_instance = QuestionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data =  request.data
        serializer_instance = QuestionSerializer(data = form_data)
        if  serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionDB.objects.create(**actual_data)
            return Response(data = {"message": "Question added successfully."})
        else:
            return Response(data ={"errors":serializer_instance.errors})

class QuestionsRetrieveUpdateDeleteVeiw(APIView):
    def get(self,request,pk):
        qs = QuestionDB.objects.get(id =pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(data = serializer_instance.data)
    def put(self,request,pk):
        form_data = request.data #get data from client
        serializer_instance = QuestionSerializer(data = form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionDB.objects.filter(id=pk).update(**actual_data)
            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)
    def delete(self, request, pk):
        QuestionDB.objects.filter(id=pk).delete()
        return Response({
            "Message": "Question deleted successfully..!"
    })
class SubmissionsListCreateView(APIView):
    def get(self, request):
        qs = SubmissionDb.objects.all()
        submission_instance = SubmissionSerializer(qs, many=True)
        return Response(data=submission_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            SubmissionDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
class SubmissionsRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        #qs=SubmissionDb.objects.get(id=pk)##if the id is already there it will show otherwise it will show error
        qs = get_object_or_404(SubmissionDb,id=pk)#this will show that no matches in submission db instead of error when wrong id is given
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    
class EvaluateSubmissionView(APIView):
    
    def put(self, request, pk):
        form_data = request.data

        SubmissionDb.objects.filter(id=pk).update(**form_data)

        return Response(data={
            "Message": "Updated..!"
        })
        
