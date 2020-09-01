from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "Test"

# 여기서 넘어갈 url 설정해주는 것임
urlpatterns = [
    path('', main, name='main'),
    path('test/<int:pk>', test_page, name='test'),
    path('loading/<int:pk>', loading, name='loading'),
    path('result01/<int:pk>', result_01, name='re01'),
    path('result02/<int:pk>', result_02, name='re02'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
