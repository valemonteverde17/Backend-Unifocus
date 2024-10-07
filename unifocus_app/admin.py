from django.contrib import admin
from .models import Curso, Docente, Alumno, Inscripcion, Tarea, Pago

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'materia', 'cupo_maximo', 'docente')
    search_fields = ('nombre', 'materia')
    list_filter = ('materia',)
    fields = ('nombre', 'materia', 'cupo_maximo', 'docente', 'descripcion')
    # Esto oculta algunos campos para no mostrarlos en la lista de visualización

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    search_fields = ('usuario__username',)

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'fecha_inscripcion')
    list_filter = ('curso',)
    search_fields = ('alumno__usuario__username',)

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'fecha_entrega')
    list_filter = ('curso',)
    search_fields = ('titulo',)

class PagoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'monto', 'fecha_pago')
    list_filter = ('curso',)
    search_fields = ('alumno__usuario__username', 'curso__nombre')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Pago, PagoAdmin)


