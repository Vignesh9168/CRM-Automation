from .models import Lead,Agent
from rest_framework import serializers



class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields  = "__all__"
        


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = AgentSerializer(read_only=False)

    class Meta:
        model = Lead
        fields  = "__all__"        