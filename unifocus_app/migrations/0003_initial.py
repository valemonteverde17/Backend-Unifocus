# Generated by Django 5.1.1 on 2024-10-07 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unifocus_app', '0002_delete_alumno_delete_materia_delete_profesor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('materia', models.CharField(choices=[('Matemáticas', 'Matemáticas'), ('Español', 'Español')], max_length=20)),
                ('cupo_maximo', models.PositiveIntegerField(default=20)),
                ('descripcion', models.TextField()),
                ('docente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unifocus_app.docente')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateTimeField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unifocus_app.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unifocus_app.curso')),
            ],
            options={
                'unique_together': {('alumno', 'curso')},
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='cursos',
            field=models.ManyToManyField(through='unifocus_app.Inscripcion', to='unifocus_app.curso'),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unifocus_app.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unifocus_app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_entrega', models.DateTimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unifocus_app.curso')),
            ],
        ),
    ]
