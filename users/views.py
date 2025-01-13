from datetime import datetime

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from users.forms import FormLogin
from users.models import User


class Login(FormView):
    template_name = 'login.html'
    form_class = FormLogin
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # return redirect(settings.LOGIN_REDIRECT_URL)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        user_set = User.objects.filter(is_active=True)
        my_date = datetime.now()
        if user is not None:
            context = {
                'date': my_date,
                'user_set': user_set
            }
            return context
        else:
            context = {
                'user_set': user_set,
            }
            return context


class ListUser(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'user_set'
    queryset = User.objects.filter(is_active=True)
