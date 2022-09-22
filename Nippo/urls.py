from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),

    path('',views.home,name='home'),
    path('list/',views.listPage,name='list'),
    path('report/',views.reportPage,name='report'),
    path('edit_report/<str:pk>', views.updateReport, name='edit_report')
]