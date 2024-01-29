# Generated by Django 3.2.7 on 2021-12-02 21:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('titulo_principal', models.CharField(help_text='Titulo principal. Maximo 30 caracteres. ', max_length=30)),
                ('fecha_proyecto', models.DateField(blank=True, help_text='Fecha de incio o terminacion del Proyecto', null=True)),
                ('funciones_cargo', models.CharField(help_text='Funciones del Cargo. Ej: Diseño, Edicion Video, Grabacion. Maximo 30 caracteres.', max_length=30)),
                ('cliente', models.CharField(help_text='Nombre del Cliente. Maximo 20 caracteres.', max_length=20)),
                ('web_cliente', models.URLField(blank=True, help_text='Si el cliente posee sitio web la URL va aqui', null=True)),
                ('descripcion', wagtail.core.fields.RichTextField(blank=True, help_text='Describa aqui el proyecto y sus labores. Maximo 1500 caracteres', max_length=1500)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PublicarImagen',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PublicarVideo',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('titulo_imagen', models.CharField(blank=True, help_text='Titulo opcional de la imagen. Maximo 100 caracteres', max_length=100, null=True)),
                ('subtitulo_imagen', models.CharField(blank=True, help_text='Subtitulo opcional de la imagen. Maximo 75 caracteres', max_length=75, null=True)),
                ('imagen_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagen_portafolio', to='portfolio.publicarimagen')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagenesPorfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('imagen_portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_portfolio', to='portfolio.portfolioitem')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoverVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('url_video', models.URLField(help_text='Inserte aqui la url del video')),
                ('titulo_video', models.CharField(blank=True, help_text='Titulo opcional de la imagen. Maximo 100 caracteres', max_length=100, null=True)),
                ('subtitulo_video', models.CharField(blank=True, help_text='Subtitulo opcional de la imagen. Maximo 75 caracteres', max_length=75, null=True)),
                ('cover_video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='covers_video', to='portfolio.publicarvideo')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]