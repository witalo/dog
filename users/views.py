import os
from datetime import datetime
from http import HTTPStatus

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from users.forms import FormLogin, UserForm
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


def modal_user(request):
    if request.method == 'GET':
        pk = request.GET.get('pk', 0)
        try:
            pk = int(pk)
        except (ValueError, TypeError):
            return JsonResponse({
                'success': False,
                'message': 'Valor invalido',
            }, status=HTTPStatus.OK)
        try:
            if pk > 0:
                user = User.objects.get(id=int(pk))
            else:
                user = None
        except User.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'El empleado no existe',
            }, status=HTTPStatus.OK)
        t = loader.get_template('users/modal_user.html')
        c = ({
            'user': user,
            'role_set': User._meta.get_field('role').choices,
        })
        return JsonResponse({
            'success': True,
            'form': t.render(c, request),
        })


def user_create_update(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        if pk:
            user = get_object_or_404(User, pk=pk)
            form = UserForm(request.POST, request.FILES, instance=user)
        else:
            form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                if user.photo and user.photo != request.FILES['photo']:
                    if os.path.isfile(user.photo.path):
                        os.remove(user.photo.path)
                print(request.FILES['photo'])
                form.instance.photo = request.FILES['photo']
            form.save()
            user_set = User.objects.all()
            tpl = loader.get_template('users/user_grid.html')
            context = ({
                'user_set': user_set
            })
            return JsonResponse({
                'success': True,
                'message': 'Proceso con éxito',
                'grid': tpl.render(context)
            }, status=HTTPStatus.OK)
        else:
            return JsonResponse({'success': False, 'message': 'Datos invalidos', 'errors': form.errors})
