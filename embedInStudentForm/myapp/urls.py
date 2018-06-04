from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
   path('register/',views.saveStudentForm,name='register'),
    path('showinfo',views.showInfo.as_view(),name='showinfo'),
    path('showstudent(?P<student_id>\d+)/$',views.showStudent,name='showstudent'),
    path('api',views.PostListAPIView.as_view(),name='api'),
path('',include('messenger.urls')),
]
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)