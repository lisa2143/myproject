from django.urls import path
from . import views
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, BoardCreate, updatefunc, BoardDelete, CommentView, ReplyView

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
    path('good/<int:pk>/', goodfunc, name='good'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('update/<int:pk>/', updatefunc, name='update'),
    path('delete/<int:pk>/', BoardDelete.as_view(), name='delete'),
    path('', views.index, name='index'),
    path('comment/<int:pk>/', views.CommentView.as_view(),name='comment'),
    path('reply/<int:pk>/', views.ReplyView.as_view(),name='reply'),
]
