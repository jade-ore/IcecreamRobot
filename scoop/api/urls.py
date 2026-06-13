from django.urls import path
import api.views as views

urlpatterns = [
    path('get-orders/', views.get_orders),
    path('add-order/', views.add_order),
    path('finish-order/', views.finish_order),
]
