from cProfile import Profile
from dataclasses import field, fields
from re import template
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, CreateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from members.forms import EditProfileForm, PasswordChangingForm, ProfilePageForm, SignUpForm
from theblog.models import Profile



class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile.html'

    # If you use form_class you can not use fields = "__all__". It will cause 'form_class is not permitted' error.
    # fields = '__all__'

    # This will pass the user to the form. So we can know which user is creating the profile.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePage(generic.UpdateView):
    model =Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio',
        'profile_pic',
        'website_url',
        'facebook_url',
        'twitter_url',
        'instagram_url',
        'pinterest_url'
        ]
    success_url = reverse_lazy('home')



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success.html')

def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

