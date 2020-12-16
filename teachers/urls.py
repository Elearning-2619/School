from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('list/', views.teachers_list_view, name='teachers_list'),
    path('detail/<int:teacher_id>/', views.teachers_detail_view, name='teachers_detail'),
    path('delete/<int:teacher_id>/', views.teachers_delete_view, name='teachers_delete'),
    path('update/<int:teacher_id>/', views.teachers_update_view, name='teachers_update'),
]