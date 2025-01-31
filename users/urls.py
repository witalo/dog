from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('users/', login_required(ListUser.as_view()), name='users'),
    path('modal_user/', login_required(modal_user), name='modal_user'),
    path('user_create_update/', login_required(user_create_update), name='user_create_update'),
    # path('user_update/<int:pk>/', login_required(UpdateUser.as_view()), name='user_update'),
    # path('user_delete/<int:pk>/', login_required(DeleteUser.as_view()), name='user_delete'),
    # path('save_permission/', login_required(save_permission), name='save_permission'),
    # path('create_permission/', login_required(create_permission), name='create_permission'),
]
