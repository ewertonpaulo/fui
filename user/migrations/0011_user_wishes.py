# Generated by Django 2.1 on 2018-10-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_wishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(blank=True, choices=[('1', '1 vez por semana'), ('2', '2 vezes por semana'), ('3', '3 vezes por semana'), ('>3', 'Mais de 3 vezes')], max_length=4, null=True)),
                ('type', models.CharField(blank=True, choices=[('C', 'Cultural'), ('F', 'Festas'), ('S', 'Shows'), ('E', 'Exposições')], max_length=2, null=True)),
                ('music_taste', models.CharField(blank=True, choices=[('S', 'Sertanejo'), ('F', 'Funk'), ('R', 'Rock'), ('O', 'Outros')], max_length=2, null=True)),
                ('drink', models.CharField(blank=True, choices=[('Y', 'Sim'), ('N', 'Não')], max_length=2, null=True)),
                ('price', models.CharField(blank=True, choices=[('free', 'Sim'), ('10~20', 'De R$10 até R$20'), ('20~30', 'De R$20 até R$30'), ('>30', 'Mais de R$30')], max_length=2, null=True)),
                ('distance', models.CharField(blank=True, choices=[('Y', 'Sim'), ('N', 'Não')], max_length=2, null=True)),
            ],
        ),
    ]
