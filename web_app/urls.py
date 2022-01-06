from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('save_info', views.save_info, name='save_info'),
    path('move_value/<int:pk>', views.move_value, name='move_value'),
    path('back_value/<int:pk>', views.back_value, name='back_value'),

    path('pdf_file', views.pdf_file, name='pdf_file'),
    path('csv_file', views.csv_file, name='csv_file'),
    path('txt_file', views.txt_file, name='txt_file'),


    path('json_def', views.json_def, name='json_def'),
    path('click_to_send', views.click_to_send, name='click_to_send'),



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()

