# Generated by Django 2.2.16 on 2020-10-21 11:31

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading_h1', models.CharField(blank=True, max_length=100)),
                ('heading_h1_pt', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_h1_es', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_h1_fr', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_h2', models.CharField(blank=True, max_length=100)),
                ('heading_h2_pt', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_h2_es', models.CharField(blank=True, max_length=100, null=True)),
                ('heading_h2_fr', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SkiResortPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('top_destination_first_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.HomePage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
