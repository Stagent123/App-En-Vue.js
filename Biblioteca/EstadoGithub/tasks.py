from celery import shared_task
from .models import GithubStatus

@shared_task
def process_github_event(event_type, payload):
    # Extraer metadatos comunes de forma segura
    repo_name = payload.get("repository", {}).get("full_name", "desconocido")
    sender_name = payload.get("sender", {}).get("login", "sistema")
    
    # Guardar en base de datos
    GithubStatus.objects.create(
        event_type=event_type,
        repository=repo_name,
        sender=sender_name,
        payload=payload
    )