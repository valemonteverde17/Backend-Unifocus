from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Modelo para el curso
class Curso(models.Model):
    MATERIA_CHOICES = [
        ('Matemáticas', 'Matemáticas'),
        ('Español', 'Español'),
    ]
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=20, choices=MATERIA_CHOICES)
    cupo_maximo = models.PositiveIntegerField(default=20)
    docente = models.ForeignKey('Docente', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para el docente
class Docente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# Modelo para el alumno
class Alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, through='Inscripcion')

    def __str__(self):
        return self.usuario.username

# Modelo para las inscripciones
class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('alumno', 'curso')

# Modelo para las tareas
class Tarea(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return self.titulo

# Modelo para los pagos
class Pago(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago de {self.alumno.usuario.username} por {self.curso.nombre}'

