from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('', include('todo.urls')),   # Includes URLs from the 'todo' app
]
