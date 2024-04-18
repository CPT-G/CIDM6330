from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearningPath',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('progress', models.TimeField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
