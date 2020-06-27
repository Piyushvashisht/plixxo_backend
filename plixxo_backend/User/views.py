from rest_framework import routers
from django.shortcuts import render redirect
from User.api import UserProfileViewSet
from django.contrib.auth.forms import UserChangeForm
def edit_profile(request):
    if request.method == 'POST':
        form=UserChangeForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user/profile')