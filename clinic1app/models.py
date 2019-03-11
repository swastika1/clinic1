from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .utils import unique_slug_generator


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Organization(models.Model):
    name = models.CharField(max_length=200)
    slogan = models.CharField(null=True, blank=True, max_length=200)
    logo = models.ImageField(upload_to='organizationdetails')
    about = models.TextField()
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    favicon = models.ImageField(upload_to='organizationdetails')
    facebook = models.URLField()
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    map_location = models.CharField(max_length=50)
    mission = models.TextField(null=True, blank=True)
    vision = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        validate_only_one_instance(self)


DAY = (
    ('sunday', 'sunday'),
    ('monday', 'monday'),
    ('tuesday', 'tuesday'),
    ('wednesday', 'wednesday'),
    ('thursday', 'thursday'),
    ('friday', 'friday'),
    ('saturday', 'saturday'),
)

VerificationStatus = (
    ('verified', 'verified'),
    ('pending', 'pending'),
    ('cancelled', 'cancelled'),

)
POSITION = (
    ('Header ad', 'Header ad'),
    ('Banner ad', 'Banner ad'),
    ('Side ad1', 'Side ad1'),
    ('Side ad2', 'Side ad2'),
    ('Inner ad1', 'Inner ad1'),
    ('Inner ad2', 'Inner ad2'),

)


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        abstract = True


class Message(TimeStamp):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Doctor(TimeStamp):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='doctors/')
    speciality = models.CharField(max_length=512)
    degree = models.CharField(max_length=512)
    details = models.TextField(max_length=512)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.name + " (" + self.speciality + ")"

    @property
    def title(self):
        return self.name


class Appointment(TimeStamp):
    patient_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    doctor = models.ForeignKey(Doctor,
                               on_delete=models.CASCADE,
                               related_name='appointments', null=True,
                               blank=True)
    date = models.DateField()
    verified = models.CharField(
        max_length=100, choices=VerificationStatus,
        verbose_name='Verification Status')
    subject = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    appointed_time = models.TimeField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.patient_name


class Subscriber(TimeStamp):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']


class Blog(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    email = models.ManyToManyField(Subscriber)

    def __str__(self):
        return self.title


class Event(TimeStamp):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='events/')
    detail = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Facility(TimeStamp):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='facility/')
    detail = models.TextField()

    def __str__(self):
        return self.title


class ImageGallery(TimeStamp):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.image.url

    class Meta:
        ordering = ['-id']


class Notice(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    detail = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class PageDropdown(TimeStamp):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Page(TimeStamp):
    title = models.ForeignKey(
        PageDropdown, on_delete=models.CASCADE, related_name="pages")
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='pages')
    content = models.TextField()

    def __str__(self):
        return self.slug


class PopUp(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='popup/')
    message = models.TextField()
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Service(TimeStamp):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='services/')
    detail = models.TextField()

    def __str__(self):
        return self.title


class Schedule(TimeStamp):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=20, choices=DAY)
    arrival = models.TimeField(max_length=30)
    departure = models.TimeField(max_length=30)
    details = models.CharField(max_length=512)

    def __str__(self):
        return self.doctor.name


class Slider(TimeStamp):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.title


class Testimonial(TimeStamp):
    written_by = models.CharField(max_length=200)
    relation = models.CharField(max_length=100)
    testimonial = models.TextField(max_length=400)
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.written_by

    class Meta:
        ordering = ['-id']


class VideoGallery(TimeStamp):
    title = models.CharField(max_length=200)
    video_link = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


def all_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(all_pre_save, sender=Notice)
pre_save.connect(all_pre_save, sender=Page)
pre_save.connect(all_pre_save, sender=Doctor)
pre_save.connect(all_pre_save, sender=Service)
pre_save.connect(all_pre_save, sender=Blog)
pre_save.connect(all_pre_save, sender=Event)
pre_save.connect(all_pre_save, sender=Facility)
pre_save.connect(all_pre_save, sender=ImageGallery)
pre_save.connect(all_pre_save, sender=PageDropdown)

