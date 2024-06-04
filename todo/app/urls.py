from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.log,name="log"),
    path('',views.signup,name="signup"),
    path('index/', views.index, name = 'index'),
    path('add_task/', views.add_task, name='add_task'),
    path('logout/', views.logout_view, name='logout'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),  
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),  
    path('change_status/<int:task_id>/', views.change_status, name='change_status'),      
]