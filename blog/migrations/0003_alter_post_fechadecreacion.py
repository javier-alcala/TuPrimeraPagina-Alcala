# Generated by Django 5.2.3 on 2025-06-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_perfil_edad_alter_post_fechadecreacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fechaDeCreacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
