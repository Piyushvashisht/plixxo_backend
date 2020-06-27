"""plixxo_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from User import views
import allauth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('brand/', include('Brand.urls')),
    path('platform/', include('Platform.urls')),
    path('user/', include('User.urls')),
    path('user/profile', include('User.views')),
    path('profile/edit/', views.edit_profile),name='edit_profile'),
    path('bank_details/', include('Bank_details.urls')),
    path('campaign/', include('Campaign.urls')),
    path('campaign_content/', include('Campaign_content.urls')),
    path('category/', include('Category.urls')),
    path('deliverable/', include('Deliverable.urls')),
    path('group/', include('Group.urls')),
    path('invoices/', include('Invoices.urls')),
    path('kyc/', include('Kyc.urls')),
    path('media_handles/', include('Media_handles.urls')),
    path('proposal/', include('Proposal.urls')),
    path('reevaluation/', include('Reevaluation.urls')),
    path('user_tags/', include('User_tags.urls')),
    path('rest_auth/',include('rest_auth.urls')),
    path('rest_auth/registration/',include('rest_auth.registration.urls')),
]
