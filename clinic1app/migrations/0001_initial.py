# Generated by Django 2.1.5 on 2019-01-08 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('patient_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('verified', models.CharField(choices=[('verified', 'verified'), ('pending', 'pending'), ('cancelled', 'cancelled')], max_length=100, verbose_name='Verification Status')),
                ('subject', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('appointed_date', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blogs/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='doctors/')),
                ('speciality', models.CharField(max_length=512)),
                ('degree', models.CharField(max_length=512)),
                ('details', models.TextField(max_length=512)),
                ('experience', models.PositiveIntegerField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events')),
                ('detail', models.TextField()),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='facility')),
                ('detail', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('caption', models.CharField(blank=True, max_length=250, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('detail', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slogan', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(upload_to='organizationdetails')),
                ('about', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('favicon', models.ImageField(upload_to='organizationdetails')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('map_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(upload_to='pages')),
                ('content', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='popup/')),
                ('message', models.TextField()),
                ('show', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('day', models.CharField(choices=[('sunday', 'sunday'), ('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday')], max_length=20)),
                ('arrival', models.CharField(max_length=30)),
                ('departure', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=512)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='clinic1app.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='services')),
                ('detail', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='sliders/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('written_by', models.CharField(max_length=200)),
                ('relation', models.CharField(max_length=100)),
                ('testimonial', models.TextField(max_length=400)),
                ('image', models.ImageField(upload_to='testimonials/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VideoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('video_link', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='clinic1app.Doctor'),
        ),
    ]
