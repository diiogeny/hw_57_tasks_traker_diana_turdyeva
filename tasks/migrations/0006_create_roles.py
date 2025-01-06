from django.db import migrations

def create_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='Project Manager')
    Group.objects.get_or_create(name='Team Lead')
    Group.objects.get_or_create(name='Developer')

class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0005_project_members'),
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]
