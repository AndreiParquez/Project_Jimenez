from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

@login_required
def user_profile(request):
    if request.method == 'POST':
        if 'profile_form' in request.POST:
            profile_form = CustomUserChangeForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('user_profile')
            else:
                messages.error(request, 'Please correct the error below.')
        elif 'password_form' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('user_profile')
            else:
                messages.error(request, 'Please correct the error below.')
    else:
        profile_form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
    
    return render(request, 'user_profile.html', {
        'profile_form': profile_form,
        'password_form': password_form
    })