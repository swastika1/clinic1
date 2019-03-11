from django.views.generic import *
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from urllib.parse import urlparse, parse_qs
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.db.models import signals
from django.core.exceptions import ValidationError
from django.contrib import messages
from urllib.parse import urlparse
# CLIENT VIEWS
# CLIENT VIEWS
# CLIENT VIEWS
# CLIENT VIEWS


# class DoctorsMixin(object):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['clientdoctorlist'] = Doctor.objects.all()
#         return context


class ClientMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['organization'] = Organization.objects.get(id=1)
        context['clienttestimoniallist'] = Testimonial.objects.all()
        context['clientdoctorlist'] = Doctor.objects.all()
        context['clienteventlist'] = Event.objects.all()
        context['clientappointmentform'] = ClientAppointmentForm
        context['clientsubscriberform'] = ClientSubscriberForm
        context['clientschedulelist'] = Schedule.objects.all()
        context['clientpagedropdown'] = PageDropdown.objects.all()
        return context


class ClientPageNotFoundView(ClientMixin, TemplateView):
    template_name = "clienttemplates/404.html"


class ClientHomeView(ClientMixin, SuccessMessageMixin, TemplateView):
    template_name = "clienttemplates/clienthome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientservicelist'] = Service.objects.all()
        context['clientsliderlist'] = Slider.objects.all()
        context['clientpopup'] = PopUp.objects.first()
        return context


class ClientAboutView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clientabout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientdoctorlist'] = Doctor.objects.all()
        context['testimoniallist'] = Testimonial.objects.all()
        return context


class ClientContactCreateView(ClientMixin, SuccessMessageMixin, CreateView):
    template_name = "clienttemplates/clientcontact.html"
    form_class = ClientContactForm
    success_url = '/'
    success_message = 'We will be in contact with you soon'


class ClientAppointmentCreateView(ClientMixin, SuccessMessageMixin, CreateView):
    template_name = "clienttemplates/clientbase.html"
    form_class = ClientAppointmentForm
    success_url = reverse_lazy("clinic1app:clienthome")
    success_message = 'Your Appointment is Booked.'

    def form_valid(self, form):
        if self.request.POST.get('selects'):
            form.instance.doctor = Doctor.objects.get(
                slug=self.request.POST.get('selects'))

        return super().form_valid(form)


class ClientSubscriberCreateView(ClientMixin, SuccessMessageMixin, CreateView):
    template_name = "clienttemplates/clienthome.html"
    form_class = ClientSubscriberForm
    success_url = reverse_lazy("clinic1app:clienthome")
    success_message = 'You have been Subscribed'

    def form_valid(self, form):
        # self.object = form.save()
        subject = 'Registration Confirmation'
        message = 'Thank you for registering.'
        email_from = 'settings.EMAIL_HOST_USER'
        recipient_list = [form.instance.email]
        send_mail(subject, message, email_from,
                  recipient_list, fail_silently=False)
        return super().form_valid(form)


class ClientDoctorListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientdoctorlist.html"
    model = Doctor
    context_object_name = 'clientdoctorlist'


class ClientScheduleListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientschedulelist.html"
    model = Schedule
    context_object_name = 'clientschedulelist'


class SearchResultView(ClientMixin, TemplateView):
    template_name = 'clienttemplates/clientsearchresult.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            lookup = Q(title__icontains=query)
            slist = Blog.objects.filter(lookup)
            context["slist"] = slist
        return context


class ClientDoctorDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientdoctordetail.html"
    model = Doctor
    context_object_name = 'clientdoctordetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientdoctorlist'] = Doctor.objects.all()
        context['sundayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="sunday")
        context['mondayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="monday")
        context['tuesdayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="tuesday")
        context['wednesdayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="wednesday")
        context['thursdayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="thursday")
        context['fridayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="friday")
        context['saturdayschedules'] = Schedule.objects.filter(
            doctor__slug=self.kwargs['slug'], day="saturday")
        return context


class ClientScheduleDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientscheduledetail.html"
    model = Schedule
    context_object_name = 'clientscheduledetail'


class ClientPageDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientpagedetail.html"
    model = Page
    context_object_name = 'clientpagedetail'


class ClientServiceListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientservicelist.html"
    paginate_by = 3
    model = Service
    context_object_name = 'clientservicelist'


class ClientServiceDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientservicedetail.html"
    model = Service
    context_object_name = 'clientservicedetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientservicelist'] = Service.objects.all()
        return context


class TestimonialListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientabout.html"
    model = Testimonial
    context_object_name = 'testimoniallist'


# class SliderListView(ClientMixin, ListView):
#     template_name = "clienttemplates/clienthome.html"
#     model = Slider
#     context_object_name = 'clientsliderlist'


class ClientFacilityListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientfacilitylist.html"
    model = Facility
    paginate_by = 3
    context_object_name = 'clientfacilitylist'


class ClientFacilityDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientfacilitydetail.html"
    model = Facility
    context_object_name = 'clientfacilitydetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientfacilitylist'] = Facility.objects.all()
        return context


class ClientNoticeListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientnoticelist.html"
    model = Notice
    context_object_name = 'clientnoticelist'


class ClientNoticeDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientnoticedetail.html"
    model = Notice
    context_object_name = 'clientnoticedetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientnoticelist'] = Notice.objects.all()
        return context


class ClientEventListView(ClientMixin, ListView):
    template_name = "clienttemplates/clienteventlist.html"
    model = Event
    context_object_name = 'clienteventlist'


class ClientEventDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clienteventdetail.html"
    model = Event
    context_object_name = 'clienteventdetail'


class ClientImageListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientimagelist.html"
    model = ImageGallery
    context_object_name = 'clientimagelist'


class ClientVideoListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientvideolist.html"
    model = VideoGallery
    context_object_name = 'clientvideolist'


class ClientBlogListView(ClientMixin, ListView):
    template_name = "clienttemplates/clientbloglist.html"
    model = Blog
    paginate_by = 3
    context_object_name = 'clientbloglist'


class ClientBlogDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientblogdetail.html"
    model = Blog
    context_object_name = 'clientblogdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientbloglist'] = Blog.objects.all()
        return context


# ADMIN VIEWS
# ADMIN VIEWS
# ADMIN VIEWS
# ADMIN VIEWS

# Admin Login, Logout and Home

class AdminMixin(SuccessMessageMixin, LoginRequiredMixin, object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizationl'] = Organization.objects.first()
        context['adminpopuplist'] = PopUp.objects.first()
        return context


class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('clinic1app:clienthome')


class AdminLoginView(FormView):
    template_name = 'admintemplates/adminlogin.html'
    form_class = AdminLoginForm
    success_url = reverse_lazy("clinic1app:adminhome")

    def get(self, request):
        if request.user.is_authenticated:
            return render(self.request, 'admintemplates/base.html')
        return super().get(request)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,
                            password=password)
        if user is not None and user.is_staff:
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'errors': "Please correct username or password"})
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        self.next_url = self.request.POST.get('next')
        if self.next_url is not None:
            return self.next_url
        else:
            return self.success_url


class AdminHomeView(AdminMixin, TemplateView):
    login_url = reverse_lazy("clinic1app:adminlogin")
    template_name = 'admintemplates/adminhome.html'

# Admin Blog Views


class AdminBlogListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminbloglist.html'
    model = Blog
    context_object_name = 'bloglist'


class AdminBlogCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminblogcreate.html'
    form_class = AdminBlogForm
    success_url = reverse_lazy('clinic1app:adminbloglist')
    success_message = "Blog created succesfully"

    def form_valid(self, form):
        self.object = form.save()
        subject = 'Blog'
        text_content = 'New Blog is up. Please visit our site.'
        html_content = render_to_string(
            'clienttemplates/clientbloglist.html')
        strip_tags(html_content)
        email_from = 'ankitbaral9@gmail.com'
        recipient_list = []
        for users in Subscriber.objects.all():
            recipient_list.append(users.email)
        msg = EmailMultiAlternatives(
            subject, text_content, email_from, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponseRedirect(reverse_lazy('clinic1app:adminbloglist'))


class AdminBlogUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminblogcreate.html'
    model = Blog
    form_class = AdminBlogForm
    success_url = reverse_lazy("clinic1app:adminbloglist")
    success_message = "Blog updated succesfully"


class AdminBlogDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminblogdelete.html'
    model = Blog
    success_url = reverse_lazy('clinic1app:adminbloglist')
    success_message = "Blog  deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminBlogDeleteView, self).delete(request, *args, **kwargs)


# Admin Doctor View
class AdminDoctorListView(AdminMixin, ListView):
    template_name = 'admintemplates/admindoctorlist.html'
    model = Doctor
    context_object_name = 'doctorlist'


class AdminDoctorCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/admindoctorcreate.html'
    form_class = AdminDoctorForm
    success_url = reverse_lazy('clinic1app:admindoctorlist')
    success_message = "Doctor created successfully"


class AdminDoctorUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/admindoctorcreate.html'
    model = Doctor
    form_class = AdminDoctorForm
    success_url = reverse_lazy('clinic1app:admindoctorlist')
    success_message = "Doctor created successfully"


class AdminDoctorDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/admindoctordelete.html'
    model = Doctor
    success_url = reverse_lazy('clinic1app:admindoctorlist')
    success_message = "Doctor was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminDoctorDeleteView, self).delete(request, *args, **kwargs)


# Admin Event View

class AdminEventListView(AdminMixin, ListView):
    template_name = 'admintemplates/admineventlist.html'
    model = Event
    context_object_name = 'eventlist'


class AdminEventCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/admineventcreate.html'
    form_class = AdminEventForm
    success_url = reverse_lazy('clinic1app:admineventlist')
    success_message = "Event created successfully"


class AdminEventUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/admineventcreate.html'
    model = Event
    form_class = AdminEventForm
    success_url = reverse_lazy('clinic1app:admineventlist')
    success_message = "Event updatedss successfully"


class AdminEventDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/admineventdelete.html'
    model = Event
    success_url = reverse_lazy('clinic1app:admineventlist')
    success_message = "Event deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminEventDeleteView, self).delete(request, *args, **kwargs)


# Admin facility View

class AdminFacilityListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminfacilitylist.html'
    model = Facility
    context_object_name = 'facilitylist'


class AdminFacilityCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminfacilitycreate.html'
    form_class = AdminFacilityForm
    success_url = reverse_lazy('clinic1app:adminfacilitylist')
    success_message = "Facility created successfully"


class AdminFacilityUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminfacilitycreate.html'
    model = Facility
    form_class = AdminFacilityForm
    success_url = reverse_lazy('clinic1app:adminfacilitylist')
    success_message = "Facility updated successfully"


class AdminFacilityDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminfacilitydelete.html'
    model = Facility
    success_url = reverse_lazy('clinic1app:adminfacilitylist')
    success_message = "Facility was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminFacilityDeleteView, self).delete(request, *args, **kwargs)

    # def get_success_message(self,cleaned_data):
    #     print(cleaned_data)
    #     return "Facility deleted successfully"


# Admin ImageGallery View

class AdminImageGalleryListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminimagegallerylist.html'
    model = ImageGallery
    context_object_name = 'imagegallerylist'


class AdminImageGalleryCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminimagegallerycreate.html'
    form_class = AdminImageGalleryForm
    success_url = reverse_lazy('clinic1app:adminimagegallerylist')
    success_message = "ImageGallery created succesfully"


class AdminImageGalleryUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminimagegallerycreate.html'
    model = ImageGallery
    form_class = AdminImageGalleryForm
    success_url = reverse_lazy('clinic1app:adminimagegallerylist')
    success_message = "ImageGallery updated succesfully"


class AdminImageGalleryDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminimagegallerydelete.html'
    model = ImageGallery
    success_url = reverse_lazy('clinic1app:adminimagegallerylist')
    success_message = "Image was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminImageGalleryDeleteView, self).delete(request, *args, **kwargs)


# Admin Notice View
class AdminNoticeListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminnoticelist.html'
    model = Notice
    context_object_name = 'noticelist'


class AdminNoticeCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminnoticecreate.html'
    form_class = AdminNoticeForm
    success_url = reverse_lazy('clinic1app:adminnoticelist')
    success_message = "Notice created succesfully"


class AdminNoticeUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminnoticecreate.html'
    model = Notice
    form_class = AdminNoticeForm
    success_url = reverse_lazy('clinic1app:adminnoticelist')
    success_message = "Notice updated succesfully"


class AdminNoticeDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminnoticedelete.html'
    model = Notice
    success_url = reverse_lazy('clinic1app:adminnoticelist')
    success_message = "Notice was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminNoticeDeleteView, self).delete(request, *args, **kwargs)


# Admin PageDropdown View

class AdminPageDropdownListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminpagedropdownlist.html'
    model = PageDropdown
    context_object_name = 'PageDropdownlist'


class AdminPageDropdownCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminpagedropdowncreate.html'
    form_class = AdminPageDropdownForm
    success_url = reverse_lazy('clinic1app:adminpagedropdownlist')
    success_message = "PageDropdown created succesfully"


class AdminPageDropdownUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminpagedropdowncreate.html'
    model = PageDropdown
    form_class = AdminPageDropdownForm
    success_url = reverse_lazy('clinic1app:adminpagedropdownlist')
    success_message = "PageDropdown updated succesfully"


class AdminPageDropdownDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminpagedropdowndelete.html'
    model = PageDropdown
    success_url = reverse_lazy('clinic1app:adminpagedropdownlist')
    success_message = "PageDropdown was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminPageDropdownDeleteView, self).delete(request, *args, **kwargs)


# Admin Page View
class AdminPageListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminpagelist.html'
    model = Page
    context_object_name = 'pagelist'


class AdminPageCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminpagecreate.html'
    form_class = AdminPageForm
    success_url = reverse_lazy('clinic1app:adminpagelist')
    success_message = "Page created succesfully"


class AdminPageUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminpagecreate.html'
    model = Page
    form_class = AdminPageForm
    success_url = reverse_lazy('clinic1app:adminpagelist')
    success_message = "Page updated succesfully"


class AdminPageDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminpagedelete.html'
    model = Page
    success_url = reverse_lazy('clinic1app:adminpagelist')
    success_message = "Page was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminPageDeleteView, self).delete(request, *args, **kwargs)


# Admin Service View
class AdminServiceListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminservicelist.html'
    model = Service
    context_object_name = 'servicelist'


class AdminServiceCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminservicecreate.html'
    form_class = AdminServiceForm
    success_url = reverse_lazy('clinic1app:adminservicelist')
    success_message = "Service created succesfully"


class AdminServiceUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminservicecreate.html'
    model = Service
    form_class = AdminServiceForm
    success_url = reverse_lazy('clinic1app:adminservicelist')
    success_message = "Service updated succesfully"


class AdminServiceDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminservicedelete.html'
    model = Service
    success_url = reverse_lazy('clinic1app:adminservicelist')
    success_message = "Service was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminServiceDeleteView, self).delete(request, *args, **kwargs)


# Admin organization View
class AdminOrganizationListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminorganizationlist.html'
    model = Organization
    context_object_name = 'organizationlist'


class AdminOrganizationDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminorganizationdetail.html'
    model = Organization
    context_object_name = 'adminorganizationdetail'


class AdminOrganizationUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminorganizationcreate.html'
    model = Organization
    form_class = AdminOrganizationForm
    success_url = reverse_lazy('clinic1app:adminorganizationlist')
    success_message = "Organization details edited succesfully"

    def get_success_url(self, **kwargs):
        return reverse_lazy('clinic1app:adminorganizationdetail', kwargs={'pk': self.object.pk})


# Admin appointment View
class AdminAppointmentCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminappointmentcreate.html'
    form_class = AdminAppointmentForm
    success_url = reverse_lazy('clinic1app:adminappointmentlist')
    success_message = "Appointment created succesfully"


class AdminAppointmentListView(AdminMixin, ListView):
    template_name = "admintemplates/adminappointmentlist.html"
    model = Appointment
    context_object_name = 'appointmentlist'


class AdminAppointmentUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminappointmentcreate.html'
    model = Appointment
    form_class = AdminAppointmentForm
    success_url = reverse_lazy('clinic1app:adminappointmentlist')
    success_message = "Appointment updated succesfully"

    def email_view(request):
        if request.method == 'POST':
            form = AdminAppointmentForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
        return email

    def pre_user_save(sender, instance, *args, **kwargs):
        if Appointment.objects.filter(verified=instance.verified):
            send_mail(
                'Appointment Confirmation Mail',
                'Your appointment is verified',
                'settings.EMAIL_HOST_USER',
                [instance.email],
                fail_silently=False,
            )
    signals.pre_save.connect(pre_user_save, sender=Appointment,
                             dispatch_uid='pre_user_save')


class AdminAppointmentDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminappointmentdelete.html'
    model = Appointment
    success_url = reverse_lazy('clinic1app:adminappointmentlist')
    success_message = "Appointment was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminAppointmentDeleteView, self).delete(request, *args, **kwargs)


# Admin message View
class AdminMessageListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminmessagelist.html'
    model = Message
    context_object_name = 'messagelist'


class AdminMessageDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminmessagedelete.html'
    model = Message
    success_url = reverse_lazy('clinic1app:adminmessagelist')
    success_message = "Message was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminMessageDeleteView, self).delete(request, *args, **kwargs)


# Admin popup View
class AdminPopUpDetailView(AdminMixin, DetailView):
    template_name = 'admintemplates/adminpopupdetail.html'
    model = PopUp
    context_object_name = 'adminpopuplist'


# class AdminPopUpCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
#     form_class = AdminPopUpForm
#     success_url = reverse_lazy('clinic1app:adminpopuplist')
#     success_message = "PopUp created succesfully"


class AdminPopUpUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminpopupcreate.html'
    form_class = AdminPopUpForm
    model = PopUp
    success_message = "PopUp updated succesfully"

    def get_success_url(self, **kwargs):
        return reverse_lazy('clinic1app:adminpopuplist', kwargs={'pk': self.object.pk})


#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return super(AdminPopUpDeleteView, self).delete(request, *args, **kwargs)


# Admin schedule View
class AdminScheduleListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminschedulelist.html'
    model = Schedule
    context_object_name = 'schedulelist'


class AdminScheduleCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminschedulecreate.html'
    form_class = AdminScheduleForm
    success_url = reverse_lazy('clinic1app:adminschedulelist')
    success_message = "Schedule created succesfully"


class AdminScheduleUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminschedulecreate.html'
    model = Schedule
    form_class = AdminScheduleForm
    success_url = reverse_lazy('clinic1app:adminschedulelist')
    success_message = "Schedule updated succesfully"


class AdminScheduleDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminscheduledelete.html'
    model = Schedule
    success_url = reverse_lazy('clinic1app:adminschedulelist')
    success_message = "Schedule was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminScheduleDeleteView, self).delete(request, *args, **kwargs)


# Admin slider View
class AdminSliderListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminsliderlist.html'
    model = Slider
    context_object_name = 'sliderlist'


# class AdminSliderCreateView(AdminMixin, CreateView):
#     template_name = 'admintemplates/adminslidercreate.html'
#     form_class = AdminSliderForm
#     success_url = reverse_lazy('clinic1app:adminsliderlist')
#     success_message = "Slider created succesfully"


class AdminSliderUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminslidercreate.html'
    model = Slider
    form_class = AdminSliderForm
    success_url = reverse_lazy('clinic1app:adminsliderlist')
    success_message = "Slider updated succesfully"


# class AdminSliderDeleteView(AdminMixin, DeleteView):
#     template_name = 'admintemplates/adminsliderdelete.html'
#     model = Slider
#     success_url = reverse_lazy('clinic1app:adminsliderlist')
#     success_message = "Slider was deleted successfully."

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return super(AdminSliderDeleteView, self).delete(request, *args, **kwargs)


# Admin subscriber View
class AdminSubscriberListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminsubscriberlist.html'
    model = Subscriber
    context_object_name = 'subscriberlist'


# class AdminSubscriberCreateView(AdminMixin, CreateView):
#     template_name = 'admintemplates/adminsubscribercreate.html'
#     form_class = AdminSubscriberForm
#     success_url = reverse_lazy('clinic1app:adminsubscriberlist')
#     success_message = "Subscriber created succesfully"

#     def form_valid(self, form):
#         subject = 'Thank you for registering to our site'
#         message = ' It  means a world to us. '
#         email_from = 'mzitx.ml@gmail.com'
#         recipient_list = [form.instance.email]
#         send_mail(subject, message, email_from,
#                   recipient_list, fail_silently=False)
#         return super().form_valid(form)


# class AdminSubscriberUpdateView(AdminMixin, UpdateView):
#     template_name = 'admintemplates/adminsubscribercreate.html'
#     model = Subscriber
#     form_class = AdminSubscriberForm
#     success_url = reverse_lazy('clinic1app:adminsubscriberlist')
#     success_message = "Subscriber updated succesfully"


class AdminSubscriberDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminsubscriberdelete.html'
    model = Subscriber
    success_url = reverse_lazy('clinic1app:adminsubscriberlist')
    success_message = "Subscriber was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminSubscriberDeleteView, self).delete(request, *args, **kwargs)


# Admin testimonial View
class AdminTestimonialListView(AdminMixin, ListView):
    template_name = 'admintemplates/admintestimoniallist.html'
    model = Testimonial
    context_object_name = 'testimoniallist'


class AdminTestimonialCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/admintestimonialcreate.html'
    form_class = AdminTestimonialForm
    success_url = reverse_lazy('clinic1app:admintestimoniallist')
    success_message = "Testimonial created succesfully"


class AdminTestimonialUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/admintestimonialcreate.html'
    model = Testimonial
    form_class = AdminTestimonialForm
    success_url = reverse_lazy('clinic1app:admintestimoniallist')
    success_message = "Testimonial updated succesfully"


class AdminTestimonialDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/admintestimonialdelete.html'
    model = Testimonial
    success_url = reverse_lazy('clinic1app:admintestimoniallist')
    success_message = "Testimonial was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminTestimonialDeleteView, self).delete(request, *args, **kwargs)

# Admin videogallery View


class AdminVideoGalleryListView(AdminMixin, ListView):
    template_name = 'admintemplates/adminvideogallerylist.html'
    model = VideoGallery
    context_object_name = 'videogallerylist'


class AdminVideoGalleryCreateView(AdminMixin, CreateView):
    template_name = 'admintemplates/adminvideogallerycreate.html'
    form_class = AdminVideoGalleryForm
    success_url = reverse_lazy('clinic1app:adminvideogallerylist')
    success_message = "VideoGallery created succesfully"

    def form_valid(self, form):
        link = form.cleaned_data['video_link']
        url_data = urlparse(link)
        query = parse_qs(url_data.query)
        video = query["v"][0]
        form.instance.video_link = video
        return super().form_valid(form)


class AdminVideoGalleryUpdateView(AdminMixin, UpdateView):
    template_name = 'admintemplates/adminvideogallerycreate.html'
    model = VideoGallery
    form_class = AdminVideoGalleryForm
    success_url = reverse_lazy('clinic1app:adminvideogallerylist')
    success_message = "VideoGallery updated succesfully"

    def form_valid(self, form):
        link = form.cleaned_data['video_link']
        url_data = urlparse(link)
        query = parse_qs(url_data.query)
        video = query["v"][0]
        form.instance.video_link = video
        return super().form_valid(form)


class AdminVideoGalleryDeleteView(AdminMixin, DeleteView):
    template_name = 'admintemplates/adminvideogallerydelete.html'
    model = VideoGallery
    success_url = reverse_lazy('clinic1app:adminvideogallerylist')
    success_message = "Video was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AdminVideoGalleryDeleteView, self).delete(request, *args, **kwargs)
