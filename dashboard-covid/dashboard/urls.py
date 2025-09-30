from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Remova estas linhas - as APIs são chamadas diretamente pelo JavaScript
    # path('api/global-stats/', views.get_global_stats, name='global_stats'),
    # path('api/country-timeline/<str:country_code>/', views.get_country_timeline, name='country_timeline'),
    # path('api/heatmap-data/', views.get_heatmap_data, name='heatmap_data'),
]