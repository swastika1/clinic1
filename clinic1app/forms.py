from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# -------- CLIENT FORMS ---------
# -------- CLIENT FORMS ---------
# -------- CLIENT FORMS ---------
# -------- CLIENT FORMS ---------


class ClientContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Enter Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Enter your Email',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
            }),
            'phone': forms.TextInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Enter contact number',
                'pattern': '[0-9]{10}'

            }),
            'message': forms.Textarea(attrs={
                'data-validation': 'required',
                'placeholder': 'Your Message'
            }),
        }


class ClientAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        autocomplete_fields = ['doctor']

        fields = ['patient_name', 'email', 'mobile', 'doctor', 'date',
                  'details']
        widgets = {
            'patient_name': forms.TextInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter your email',
            }),
            'mobile': forms.NumberInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Enter phone number',
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-doctor',
                'data-validation': 'required',

                # 'placeholder': 'Doctor',
            }),

            'date': forms.DateInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Appointment date',
                'id': 'datetimepicker1',


            }),
            'details': forms.Textarea(attrs={
                'placeholder': 'Details',
            }),
            # 'appointed_time': forms.TimeInput(attrs={
            #     'data-validation': 'required',
            #     'placeholder': 'Appointment time',
            #     'id': 'datetimepicker3'
            # }),

        }


class ClientSubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widget = {
            'email': forms.EmailInput(attrs={
                'data-validation': 'required',
                'placeholder': 'Enter your Email',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            print("Email exists")
            raise forms.ValidationError(
                "User already registered.", code="email",)
        else:
            # print("Email doesnot exist.")
        # 
            return email


# -------- ADMIN FORMS ---------
# -------- ADMIN FORMS ---------
# -------- ADMIN FORMS ---------
# -------- ADMIN FORMS ---------


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password'
    }))


# admin blog create form

class AdminBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        widgets = {

            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter blog title',
            }),
            'content': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter blog content',
            }),
            'image': forms.ClearableFileInput(attrs={
                # "class": "form-control",
                'data-validation': 'required',

            }),
            'content': SummernoteWidget(),
        }
# Admin doctor forms


class AdminDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'image',
                  'speciality', 'degree', 'details', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter doctor name',
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter doctor email',
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter doctor image',
            }),
            'speciality': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter doctor speciality',
            }),
            'degree': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter degree',
            }),
            'details': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter doctor Details'
            }),
            'experience': forms.NumberInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter doctor Experience',
            }),
            'details': SummernoteWidget(),
        }


# Admin event forms

class AdminEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'detail', 'date', 'venue']
        widgets = {


            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter event Title',
            }),

            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter event Image',
            }),
            'detail': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter event Details'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': 'Enter event date ',
                'id': 'datetimepicker1'
                # 'class': 'datepicker-f'
            }),
            'venue': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter event venue',
            }),
            'detail': SummernoteWidget(),

        }

# Admin Facility forms


class AdminFacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['title', 'image', 'detail']
        widgets = {


            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter facility title',
            }),

            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter facility image',
            }),
            'detail': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter facility details'
            }),
            'detail': SummernoteWidget(),
        }


# Admin ImageGallery forms


class AdminImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ['title', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Upload  image',
            }),
            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter image title',
            }),
        }


# Admin Notice forms

class AdminNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'detail']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter notice title',
            }),
            'detail': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter notice details'
            }),
            'detail': SummernoteWidget(),
        }

# Admin Page forms


class AdminPageDropdownForm(forms.ModelForm):
    class Meta:
        model = PageDropdown
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter Dropdown Name',
            }),
        }


class AdminPageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.Select(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter page title',
            }),

            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter page image',
            }),
            'content': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter page content'
            }),
            'content': SummernoteWidget(),
        }

# Admin Service forms


class AdminServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'image', 'detail']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter service title',
            }),

            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter service image',
            }),
            'detail': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter service detail'
            }),
            'detail': SummernoteWidget(),
        }


class AdminOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'slogan', 'logo','mission', 'vision', 'about', 'address',
                  'email', 'phone',
                  'mobile', 'favicon', 'facebook',
                  'twitter', 'youtube', 'map_location']
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization name',
            }),
            'slogan': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization slogan',
            }),
            'logo': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization logo',
            }),
            'mission': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization of mission'
            }),
            'vision': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization vision'
            }),
            'about': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter details about organization'
            }),
            'address': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization address',
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': 'Enter organizaiton email',
            }),
            'phone': forms.NumberInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization phone number',
            }),
            'mobile': forms.NumberInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization mobile number',
            }),
            'favicon': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization favicon',
            }),
            'facebook': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter facebook page link',
            }),
            'twitter': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter twitter page link ',
            }),
            'youtube': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter youtube channel link',
            }),
            'map_location': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter organization map link',
            }),
            'about': SummernoteWidget(),
            'mission': SummernoteWidget(),
            'vision': SummernoteWidget(),

        }


class AdminAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'mobile', 'email', 'doctor', 'date',
                  'verified', 'details']

        widgets = {
            'details': SummernoteWidget(),


            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': "Enter patient's name",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': "Enter patient's email",
            }),
            'mobile': forms.NumberInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': "Enter patient's phone number",
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'class': 'form-doctor',
                'placeholder': 'Enter doctor name',
            }),
            'date': forms.DateInput(attrs={

                'data-validation': 'required',
                'placeholder': 'Appointment date',
                'id': 'datetimepicker1'
                # 'class': 'datepicker-f'
            }),
            'verified': forms.Select(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': 'Status',
                'id': 'verify'
            }),
            # 'subject': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'data-validation': 'required',
            #     'placeholder': 'Enter appointment subject',
            # }),
            'details': forms.Textarea(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': 'Enter appointment details',
            }),
            # 'appointed_time': forms.TimeInput(attrs={
            #     'class': 'form-control',
            #     'data-validation': 'required',
            #     'placeholder': 'Enter appointed date',
            #     'id': 'datetimepicker2'
            #     # 'class': 'datepicker-f'
            # }),
            # 'note': forms.Textarea(attrs={
            #     'class': 'form-control',
            #     'data-validation': 'required',
            #     'placeholder': 'Enter appointment note',
            # }),
            'details': SummernoteWidget(),
        }


class AdminMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': "Sender's name",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': "Sender's email",
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': "Sender's phone number",
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'placeholder': "Sender's message",
            }),
        }


class AdminPopUpForm(forms.ModelForm):
    class Meta:
        model = PopUp
        fields = ['title', 'image', 'show']
        widgets = {

            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter popup title',
            }),

            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter popup image',
            }),
            'show': forms.CheckboxInput(attrs={

            })
        }


class AdminScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'day', 'arrival', 'departure']
        widgets = {
            'day': forms.Select(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter appointment day',
                "id": "day",
            }),
            'arrival': forms.TimeInput(attrs={
                'data-validation': 'required',
                'placeholder': "Enter doctor's arrival",
                'id': 'datetimepicker3'
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'class': 'form-doctor',
                'placeholder': 'Enter doctor name',
            }),
            'departure': forms.TimeInput(attrs={
                'data-validation': 'required',

                'placeholder': "Enter doctor's departure",
                'id': 'datetimepicker4'

            }),

        }


class AdminSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'about', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter slider title',
            }),
            'about': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Max 200 character'
            }),
            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter slider image',
            }),
        }


class AdminSubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'data-validation': 'required',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$',
                'placeholder': "Subscriber's email",
            }),
        }


class AdminTestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['written_by', 'image', 'relation', 'testimonial']
        widgets = {
            'written_by': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter writer',
            }),

            'image': forms.ClearableFileInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Upload image',
            }),
            'testimonial': forms.Textarea(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter testimonial (Max 400 characters)'
            }),
            'relation': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter relation',
            }),
            # 'testimonial': SummernoteWidget(),

        }


class AdminVideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = ['title', 'video_link']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter video title',
            }),
            'video_link': forms.TextInput(attrs={
                "class": "form-control",
                'data-validation': 'required',
                'placeholder': 'Enter video link',
            }),

        }
