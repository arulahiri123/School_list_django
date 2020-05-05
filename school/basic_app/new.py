from django.contrib import admin
from django.urls import path
from basic_app import views



app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolViewList.as_view(),name ='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDelete.as_view(),name='delete')
]
