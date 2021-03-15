from django.urls import path
from . import views

app_name = 'wishes'


# URL pattern for...
urlpatterns = [
    # wishes page
    path('', views.index, name='index'),

    # new wish page
    path('post_wish/', views.post_wish, name='post_wish'),

    # edit wish page
    path('edit_wish/<int:wish_id>', views.edit_wish, name='edit_wish'),

    # delete wish page
    path('delete_wish/<int:wish_id>', views.delete_wish, name='delete_wish')
]