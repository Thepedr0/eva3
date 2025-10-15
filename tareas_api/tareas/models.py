from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    hecho = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} - {self.titulo}"
