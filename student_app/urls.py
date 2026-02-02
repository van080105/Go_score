from django.urls import path
from .views import check_score
app_name = 'student_app'
urlpatterns = [
    path('', check_score, name='students'),
]
