from django.urls import path
from . import views

app_name = 'diarys'

urlpatterns = [
    path('practice/', views.index2, name='practice'),
    path('', views.main, name='main'),
    path('<int:year>/<int:month>/<int:date>/', views.daily_workout),
    path('<int:year>/<int:month>/<int:date>/<int:routine_id>/', views.add_routine, name='add_routine'),
    path('edit/<int:year>/<int:month>/<int:date>/<int:routine_id>/', views.edit_routine, name='edit_routine')
]
