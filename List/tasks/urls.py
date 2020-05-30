from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='tasks'),
    path('add/',views.add,name='add-task'),
    path('edit/<int:id>',views.edit,name='edit-task'),
    path('delete/<int:id>',views.delete,name='delete-task'),
    path('delete-all/',views.delete_all,name='delete-all-task'),

]