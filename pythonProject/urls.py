"""
URL configuration for pythonProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pythonProject import views
from django.conf import settings
from django.conf.urls.static import static

# for profile

from django.contrib.auth import views as auth_views
# from django.urls import path, include
# from pythonProject.views import ProfileUpdateView

#####
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage,name="homepage"),

    path('signup/',views.signup,name="signup"),
    path('login/',views.login_page),
    path("sell/",views.sell,name="sell"),
    path("deleteitem/<id>/",views.deleteitem,name="deleteitem"),
    path("updateitem/<id>/",views.updateitem,name="updateitem"),
    path("log_out/",views.log_out,name="log_out"),
    path("item/<id>",views.item,name="item"),
    path("category/<id>",views.category,name="category"),
    #  path('upload/',views.upload_images, name='upload_images'),
    path("myads/",views.myads,name="myads"),
    path("updateitem/<id>",views.updateitem,name="updateitem"),
    path("requests/",views.requests,name="requests"),
    path('approve/<id>/', views.approve, name='approve'),
    # for profile
    path('profile/',views.ProfileView, name='profile'),
#     path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('change-password',auth_views.PasswordChangeView.as_view(
        template_name='changePassword.html',
        success_url='/'
        ),
        name='change-password'
),
#     # path("get/",views.get,name="get"),
    path('profileUpdate/',views.profileUpdate,name="profileUpdate"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset/password_reset.html',
             subject_template_name='password-reset/password_reset_subject.txt',
             email_template_name='password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('show-image/', views.show_image, name='show_image'),

]
if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
