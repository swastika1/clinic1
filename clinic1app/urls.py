from django.urls import path
from .views import *
from .utils import *


app_name = 'clinic1app'

urlpatterns = [


    # CLIENT PATHS ##
    # CLIENT PATHS ##
    # CLIENT PATHS ##
    # CLIENT PATHS ##

    # general pages

    path('', ClientHomeView.as_view(), name='clienthome'),
    path('about/', ClientAboutView.as_view(), name='clientabout'),
    path('contact/', ClientContactCreateView.as_view(), name='clientcontact'),
    path('makeanappointment/', ClientAppointmentCreateView.as_view(),
         name='clientappointmentcreate'),
    path('doctors/', ClientDoctorListView.as_view(), name='clientdoctorlist'),
    path('doctors/<slug:slug>/detail/', ClientDoctorDetailView.as_view(),
         name='clientdoctordetail'),
    path('services/', ClientServiceListView.as_view(),
         name='clientservicelist'),
    path('services/<slug:slug>/detail/',
         ClientServiceDetailView.as_view(), name='clientservicedetail'),
    path('schedule/<slug:slug>/detail/',
         ClientScheduleDetailView.as_view(), name='clientscheduledetail'),
    path('testimonial/',
         TestimonialListView.as_view(), name='testimoniallist'),
    # path('slider/',
    #      SliderListView.as_view(), name='sliderlist'),
    path('facilities/', ClientFacilityListView.as_view(),
         name='clientfacilitylist'),
    path('facilities/<slug:slug>/details',
         ClientFacilityDetailView.as_view(), name='clientfacilitydetail'),
    path('events/', ClientEventListView.as_view(),
         name='clienteventlist'),
    path('events/<slug:slug>/details',
         ClientEventDetailView.as_view(), name='clienteventdetail'),
    path('notices/', ClientNoticeListView.as_view(), name='clientnoticelist'),
    path('notices/<slug:slug>/details',
         ClientNoticeDetailView.as_view(), name='clientnoticedetail'),
    path('pages/<slug:slug>/details',
         ClientPageDetailView.as_view(), name='clientpagedetail'),
    path('images/', ClientImageListView.as_view(), name='clientimagelist'),
    path('videos/', ClientVideoListView.as_view(), name='clientvideolist'),
    path('blogs/', ClientBlogListView.as_view(), name='clientbloglist'),
    path('blogs/<slug:slug>/details',
         ClientBlogDetailView.as_view(), name='clientblogdetail'),
    path('schedules/', ClientScheduleListView.as_view(), name='clientschedulelist'),
    path('404/', ClientPageNotFoundView.as_view(), name='clientpagenotfound'),
    path('subscribe/', ClientSubscriberCreateView.as_view(),
         name='clientsubscribercreate'),
    path('search/result/', SearchResultView.as_view(), name="searchresult"),


    # ADMIN PATHS ##
    # ADMIN PATHS ##
    # ADMIN PATHS ##
    # ADMIN PATHS ##



    # Admin login logout urls start
    path('clinic1-admin/login/', AdminLoginView.as_view(), name='adminlogin'),
    path('clinic1-admin/logout/', AdminLogoutView.as_view(),
         name='adminlogout'),
    path('clinic1-admin/', AdminHomeView.as_view(),
         name='adminhome'),

    # Admin login logout urls start


    # # admin blog path


    # Admin blog path

    path('clinic1-admin/blog/', AdminBlogListView.as_view(),
         name='adminbloglist'),
    path('clinic1-admin/blog/create/',
         AdminBlogCreateView.as_view(), name='adminblogcreate'),
    path('clinic1-admin/blog/<slug:slug>/update/',
         AdminBlogUpdateView.as_view(), name='adminblogupdate'),
    path('clinic1-admin/blog/<slug:slug>/delete/',
         AdminBlogDeleteView.as_view(), name='adminblogdelete'),

    # Admin Doctor paths
    path('clinic1-admin/doctor/',
         AdminDoctorListView.as_view(), name='admindoctorlist'),
    path('clinic1-admin/doctor/create/',
         AdminDoctorCreateView.as_view(), name='admindoctorcreate'),
    path('clinic1-admin/doctor/<slug:slug>/update/',
         AdminDoctorUpdateView.as_view(), name='admindoctorupdate'),
    path('clinic1-admin/doctor/<slug:slug>/delete/',
         AdminDoctorDeleteView.as_view(), name='admindoctordelete'),

    # Admin Event paths
    path('clinic1-admin/event/', AdminEventListView.as_view(),
         name='admineventlist'),
    path('clinic1-admin/event/create/',
         AdminEventCreateView.as_view(), name='admineventcreate'),
    path('clinic1-admin/event/<slug:slug>/update/',
         AdminEventUpdateView.as_view(), name='admineventupdate'),
    path('clinic1-admin/event/<slug:slug>/delete/',
         AdminEventDeleteView.as_view(), name='admineventdelete'),

    # Admin Facility paths
    path('clinic1-admin/facility/', AdminFacilityListView.as_view(),
         name='adminfacilitylist'),
    path('clinic1-admin/facility/create/',
         AdminFacilityCreateView.as_view(), name='adminfacilitycreate'),
    path('clinic1-admin/facility/<slug:slug>/update/',
         AdminFacilityUpdateView.as_view(), name='adminfacilityupdate'),
    path('clinic1-admin/facility/<slug:slug>/delete/',
         AdminFacilityDeleteView.as_view(), name='adminfacilitydelete'),

    # Admin ImageGallery paths
    path('clinic1-admin/imagegallery/', AdminImageGalleryListView.as_view(),
         name='adminimagegallerylist'),
    path('clinic1-admin/imagegallery/create/',
         AdminImageGalleryCreateView.as_view(),
         name='adminimagegallerycreate'),
    path('clinic1-admin/imagegallery/<slug:slug>/update/',
         AdminImageGalleryUpdateView.as_view(),
         name='adminimagegalleryupdate'),
    path('clinic1-admin/imagegallery/<slug:slug>/delete/',
         AdminImageGalleryDeleteView.as_view(),
         name='adminimagegallerydelete'),

    # Admin Notice paths
    path('clinic1-admin/notice/', AdminNoticeListView.as_view(),
         name='adminnoticelist'),
    path('clinic1-admin/notice/create/',
         AdminNoticeCreateView.as_view(), name='adminnoticecreate'),
    path('clinic1-admin/notice/<slug:slug>/update/',
         AdminNoticeUpdateView.as_view(), name='adminnoticeupdate'),
    path('clinic1-admin/notice/<slug:slug>/delete/',
         AdminNoticeDeleteView.as_view(), name='adminnoticedelete'),


    # Admin pagedropdown paths
    path('clinic1-admin/pagedropdown/', AdminPageDropdownListView.as_view(),
         name='adminpagedropdownlist'),
    path('clinic1-admin/pagedropdown/create/',
         AdminPageDropdownCreateView.as_view(), name='adminpagedropdowncreate'),
    path('clinic1-admin/pagedropdown/<slug:slug>/update/',
         AdminPageDropdownUpdateView.as_view(), name='adminpagedropdownupdate'),
    path('clinic1-admin/pagedropdown/<slug:slug>/delete/',
         AdminPageDropdownDeleteView.as_view(), name='adminpagedropdowndelete'),

    # Admin page paths
    path('clinic1-admin/page/', AdminPageListView.as_view(),
         name='adminpagelist'),
    path('clinic1-admin/page/create/',
         AdminPageCreateView.as_view(), name='adminpagecreate'),
    path('clinic1-admin/page/<slug:slug>/update/',
         AdminPageUpdateView.as_view(), name='adminpageupdate'),
    path('clinic1-admin/page/<slug:slug>/delete/',
         AdminPageDeleteView.as_view(), name='adminpagedelete'),

    # Admin service paths
    path('clinic1-admin/service/', AdminServiceListView.as_view(),
         name='adminservicelist'),
    path('clinic1-admin/service/create/',
         AdminServiceCreateView.as_view(), name='adminservicecreate'),
    path('clinic1-admin/service/<slug:slug>/update/',
         AdminServiceUpdateView.as_view(), name='adminserviceupdate'),
    path('clinic1-admin/service/<slug:slug>/delete/',
         AdminServiceDeleteView.as_view(), name='adminservicedelete'),

    # Admin organization paths
    path('clinic1-admin/organization/<int:pk>/detail/', AdminOrganizationDetailView.as_view(),
         name='adminorganizationdetail'),

    path('clinic1-admin/organization/', AdminOrganizationListView.as_view(),
         name='adminorganizationlist'),

    path('clinic1-admin/organization/<int:pk>/update/',
         AdminOrganizationUpdateView.as_view(),
         name='adminorganizationupdate'),


    path('clinic1-admin/organization/<int:pk>/update/',
         AdminOrganizationUpdateView.as_view(), name='adminorganizationupdate'),


    # Admin appointment paths
    path('clinic1-admin/appointment/', AdminAppointmentListView.as_view(),
         name='adminappointmentlist'),
    path('clinic1-admin/appointment/create/',
         AdminAppointmentCreateView.as_view(), name='adminappointmentcreate'),
    path('clinic1-admin/appointment/<int:pk>/update/',
         AdminAppointmentUpdateView.as_view(), name='adminappointmentupdate'),
    path('clinic1-admin/appointment/<int:pk>/delete/',
         AdminAppointmentDeleteView.as_view(), name='adminappointmentdelete'),

    # Admin message paths
    path('clinic1-admin/message/', AdminMessageListView.as_view(),
         name='adminmessagelist'),

    path('clinic1-admin/message/<int:pk>/delete/',
         AdminMessageDeleteView.as_view(), name='adminmessagedelete'),

    # Admin popup paths
    path('clinic1-admin/popup/<int:pk>/detail/', AdminPopUpDetailView.as_view(),
         name='adminpopuplist'),
    path('clinic1-admin/popup/<int:pk>/update/',
         AdminPopUpUpdateView.as_view(), name='adminpopupupdate'),

    # Admin schedule paths
    path('clinic1-admin/schedule/', AdminScheduleListView.as_view(),
         name='adminschedulelist'),
    path('clinic1-admin/schedule/create/',
         AdminScheduleCreateView.as_view(), name='adminschedulecreate'),
    path('clinic1-admin/schedule/<int:pk>/update/',
         AdminScheduleUpdateView.as_view(), name='adminscheduleupdate'),
    path('clinic1-admin/schedule/<int:pk>/delete/',
         AdminScheduleDeleteView.as_view(), name='adminscheduledelete'),

    # Admin slider paths
    path('clinic1-admin/slider/', AdminSliderListView.as_view(),
         name='adminsliderlist'),
    path('clinic1-admin/slider/<int:pk>/update/',
         AdminSliderUpdateView.as_view(), name='adminsliderupdate'),
   
    # Admin subscriber paths
    path('clinic1-admin/subscriber/', AdminSubscriberListView.as_view(),
         name='adminsubscriberlist'),
    # path('clinic1-admin/subscriber/create/',
    #      AdminSubscriberCreateView.as_view(), name='adminsubscribercreate'),
    # path('clinic1-admin/subscriber/<int:pk>/update/',
    #      AdminSubscriberUpdateView.as_view(), name='adminsubscriberupdate'),
    path('clinic1-admin/subscriber/<int:pk>/delete/',
         AdminSubscriberDeleteView.as_view(), name='adminsubscriberdelete'),

    # Admin testimonial paths
    path('clinic1-admin/testimonial/', AdminTestimonialListView.as_view(),
         name='admintestimoniallist'),
    path('clinic1-admin/testimonial/create/',
         AdminTestimonialCreateView.as_view(), name='admintestimonialcreate'),
    path('clinic1-admin/testimonial/<int:pk>/update/',
         AdminTestimonialUpdateView.as_view(), name='admintestimonialupdate'),
    path('clinic1-admin/testimonial/<int:pk>/delete/',
         AdminTestimonialDeleteView.as_view(), name='admintestimonialdelete'),

    # Admin videogallery paths
    path('clinic1-admin/videogallery/', AdminVideoGalleryListView.as_view(),
         name='adminvideogallerylist'),
    path('clinic1-admin/videogallery/create/',
         AdminVideoGalleryCreateView.as_view(),
         name='adminvideogallerycreate'),
    path('clinic1-admin/videogallery/<int:pk>/update/',
         AdminVideoGalleryUpdateView.as_view(),
         name='adminvideogalleryupdate'),
    path('clinic1-admin/videogallery/<int:pk>/delete/',
         AdminVideoGalleryDeleteView.as_view(),
         name='adminvideogallerydelete'),
]
