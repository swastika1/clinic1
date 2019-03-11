from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# apply summernote to some textfields in models
# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)

# admin.site.register(Post, PostAdmin)


admin.site.register([Organization, Message, Doctor, Appointment, Blog,
                     Event, Facility, ImageGallery, Notice,
                     Slider, Page, PopUp,
                     Service, Schedule, Subscriber, Testimonial,
                     VideoGallery, PageDropdown, ], SomeModelAdmin)
