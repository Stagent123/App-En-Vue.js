from rest_framework import serializers
from .models import GithubStatus

class GitHubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubStatus
        fields = ['id', 'Tipos_de_Eventos', 'Repositorio', 'Autor', 'Payload', 'Creado']