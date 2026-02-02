from django.urls import path
from .views import report_page, top10_page

app_name = 'report_app'

urlpatterns = [
    path('', report_page, name='dashboard'),
    path('top10/', top10_page, name='top10'),
]
