# views.py

from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Agent, Lead
from .serializers import AgentSerializer, LeadSerializer

from .services.assignment_services import assign_lead


class AgentCreateAPIView(APIView):

    @swagger_auto_schema(
        request_body=AgentSerializer
    )
    def post(self, request):

        serializer = AgentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Agent created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class LeadCreateAPIView(APIView):

    @swagger_auto_schema(
        request_body=LeadSerializer
    )
    def post(self, request):

        serializer = LeadSerializer(data=request.data)

        if serializer.is_valid():

            # Save lead

            lead = serializer.save()

            # Auto assignment
            assign_lead(lead)

            # Refresh updated lead
            lead.refresh_from_db()

            response_serializer = LeadSerializer(lead)

            return Response(
                {
                    "message": "Lead created and assigned successfully",
                    "data": response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class AgentListAPIView(APIView):

    def get(self, request):

        agents = Agent.objects.all()

        serializer = AgentSerializer(
            agents,
            many=True
        )

        return Response(serializer.data)



class LeadListAPIView(APIView):

    def get(self, request):

        leads = Lead.objects.all()

        serializer = LeadSerializer(
            leads,
            many=True
        )

        return Response(serializer.data)