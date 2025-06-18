
from django.contrib import admin
from django.urls import path
from resume.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',resume_list,name='resumelist'),
    path('addresume',resume_add,name='resumeadd'),
    path('viewresume/<int:id>',resume_view,name='resumeview'),
    path('deleteresume/<int:id>',resume_delete,name='resumedelete'),
     path('editresume/<int:id>',resume_edit,name='resumeedit'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
