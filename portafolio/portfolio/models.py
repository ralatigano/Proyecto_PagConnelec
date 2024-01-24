from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=75)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='projects',blank=True)
    link = models.URLField(max_length=180,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class  Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']