from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Exam Portal Admin"
admin.site.site_title = "Exam Portal Admin Portal"
admin.site.index_title = "Welcome to Exam Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('prof/', include('prof.urls')), 
    path('student/', include('student.urls')),
]
