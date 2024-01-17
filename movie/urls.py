from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>',views.detail,name='detail'),
    path('movieform/',views.ModelFormView,name='ModelFormView')
]