# Generated by Django 2.0.7 on 2018-07-10 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='nome')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='título')),
                ('content', tinymce.models.HTMLField(verbose_name='texto')),
                ('backside_title', models.CharField(blank=True, max_length=64, verbose_name='título do verso')),
                ('backside_content', tinymce.models.HTMLField(blank=True, verbose_name='texto do verso')),
                ('background', models.ImageField(blank=True, help_text='\n        A imagem de fundo deverá ter 3508 pixels de largura e 2480 pixels de altura, correspondendo a uma \n        folha A4 na orientação de paisagem.\n        ', upload_to='backgrounds', verbose_name='imagem de fundo')),
                ('font', models.CharField(choices=[('a', 'Arial'), ('t', 'Times New Roman')], default='a', max_length=1, verbose_name='fonte')),
                ('title_top_distance', models.PositiveIntegerField(blank=True, default=0, verbose_name='distância do topo ao título')),
                ('title_section_align', models.CharField(choices=[('left', 'Alinhar seção à esquerda'), ('center', 'Seção centralizada'), ('right', 'Alinhar seção à direita')], default='left', max_length=10, verbose_name='alinhamento da seção')),
                ('title_align', models.CharField(choices=[('left', 'Alinhar texto à esquerda'), ('center', 'Texto centralizado'), ('right', 'Alinhar texto à direita'), ('justify', 'Texto justificado')], default='left', max_length=10, verbose_name='alinhamento do título')),
                ('title_color', models.CharField(choices=[('#000', 'Preto'), ('#FFF', 'Preto'), ('#CCC', 'Cinza claro'), ('#999', 'Cinza escuro')], default='#000', max_length=10, verbose_name='cor do título')),
                ('title_font_size', models.PositiveIntegerField(default=30, verbose_name='tamanho da fonte do título')),
                ('content_title_distance', models.PositiveIntegerField(blank=True, default=0, verbose_name='distância do título ao texto')),
                ('content_section_align', models.CharField(choices=[('left', 'Alinhar seção à esquerda'), ('center', 'Seção centralizada'), ('right', 'Alinhar seção à direita')], default='left', max_length=10, verbose_name='alinhamento da seção')),
                ('content_text_align', models.CharField(choices=[('left', 'Alinhar texto à esquerda'), ('center', 'Texto centralizado'), ('right', 'Alinhar texto à direita'), ('justify', 'Texto justificado')], default='left', max_length=10, verbose_name='alinhmento do texto')),
                ('content_text_color', models.CharField(choices=[('#000', 'Preto'), ('#FFF', 'Preto'), ('#CCC', 'Cinza claro'), ('#999', 'Cinza escuro')], default='#000', max_length=10, verbose_name='cor do texto')),
                ('content_font_size', models.PositiveIntegerField(default=12, verbose_name='tamanho da fonte do texto')),
                ('footer_title_distance', models.PositiveIntegerField(blank=True, default=0, verbose_name='distância do texto ao rodapé')),
                ('footer_section_align', models.CharField(blank=True, choices=[('left', 'Alinhar seção à esquerda'), ('center', 'Seção centralizada'), ('right', 'Alinhar seção à direita')], default='left', max_length=10, verbose_name='alinhamento da seção')),
                ('footer_text_align', models.CharField(choices=[('left', 'Alinhar texto à esquerda'), ('center', 'Texto centralizado'), ('right', 'Alinhar texto à direita'), ('justify', 'Texto justificado')], default='left', max_length=10, verbose_name='alinhamento do rodapé')),
                ('footer_text_color', models.CharField(choices=[('#000', 'Preto'), ('#FFF', 'Preto'), ('#CCC', 'Cinza claro'), ('#999', 'Cinza escuro')], default='#000', max_length=10, verbose_name='cor do rodapé')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Event', verbose_name='evento')),
            ],
        ),
    ]
