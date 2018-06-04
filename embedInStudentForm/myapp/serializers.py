from rest_framework.serializers import ModelSerializer
from .models import StudentForm

class PostSerializer(ModelSerializer):
    class Meta:
        model=StudentForm
        fields=[
            'first_name',
            'last_name',
            'picture'

        ]