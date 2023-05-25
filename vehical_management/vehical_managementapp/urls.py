from django.urls import path
from vehical_managementapp import views
urlpatterns = [
    path('home',views.infopage),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('dashboard',views.dashboard),

]