from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='home'),
    path('home_adm', views.lista_produtos_admin, name='homeadm'),
    path('adicionar/', views.adc_produtos, name='adicionar_produto'),
    path('atualizar/<int:id>/', views.update_produtos, name='atualizar_produto'),
    path('deletar/<int:id>/', views.dell_produtos, name='deletar_produto'),
]

if settings.DEBUG:  # verificação para evitar servir arquivos estáticos em produção

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)