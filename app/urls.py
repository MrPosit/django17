from django.urls import path
from .views import home, create, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('update/<int:book_id>/', update, name='update'),
    path('delete/<int:book_id>/', delete, name='delete'),
]
