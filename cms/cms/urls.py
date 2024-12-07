from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(('organization.urls', 'organization'), namespace='organization')),
    path('member/', include(('member.urls', 'member'), namespace='member')),
    path('dues/', include(('dues.urls', 'dues'), namespace='dues')),
    path('song/', include(('song.urls', 'song'), namespace='song')),
    path('tithe/', include(('tithe.urls', 'tithe'), namespace='tithe')),
    path('announcement/', include(('announcement.urls', 'announcement'), namespace='announcement')),
    path('expenditure/', include(('expenditure.urls', 'expenditure'), namespace='expenditures')),
    path('manage_content/', include(('manage_content.urls', 'manage_content'), namespace='manage_content')),
    path('activity/', include(('activity.urls', 'activity'), namespace='activity')),
    path('attendance/', include(('attendance.urls', 'attendance'), namespace='attendance')),
    path('custom_group/', include(('custom_group.urls', 'custom_group'), namespace='custom_group')),
    path('custom_user/', include(('custom_user.urls', 'custom_user'), namespace='custom_user')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
