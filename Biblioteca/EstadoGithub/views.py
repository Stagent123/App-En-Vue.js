

import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .tasks import process_github_event  # Tu tarea asíncrona
from .serializer import GitHubEventSerializer
from .models import GithubStatus
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .utils import VerificarFirma

class GitHubEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GithubStatus.objects.all().order_by('-Creado')
    serializer_class = GitHubEventSerializer
    permission_classes = [IsAuthenticated]  # O AllowAny si es un panel público

@csrf_exempt
@require_POST
def github_webhook_view(request):
    if not VerificarFirma(request):
        return HttpResponseBadRequest("Firma inválida")
    
    event_type = request.META.get("HTTP_X_GITHUB_EVENT", "ping")
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("JSON inválido")
    
    # Encolar de forma asíncrona para responder en < 10s
    process_github_event.delay(event_type, payload)
    
    return JsonResponse({"status": "recibido"}, status=200)


