from django.db import models

class GithubStatus(models.Model):
    Tipos_de_Eventos = models.CharField(max_length=50, help_text="Ej: Push, Pull_requuest, Issues")
    Repositorio = models.CharField(max_length=255, help_text="Nombre completo del repositorio")
    Autor = models.CharField(max_length=150, help_text="Usuario de Github que disparó el evento")
    payload = models.JSONField(help_text="Payload completo recibido de Github")
    Creado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"[{self.Tipos_de_Eventos} {self.Repositorio} by {self.Autor} ({self.Creado})]"
