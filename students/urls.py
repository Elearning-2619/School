from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.students_list_view, name='students_list_page'),
    path('detail/<slug:student_slug>/', views.students_detail_view, name='students_detail'),
    path('delete/<slug:student_slug>/', views.students_delete_view, name='students_delete'),
    path('update/<slug:student_slug>/', views.students_update_view, name='students_update'),
]

