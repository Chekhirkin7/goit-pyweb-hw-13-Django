from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views import View


class RegistrationView(View):
    template_name = 'app_auth/registration.html'
    form_class = RegistrationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('quotes:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})