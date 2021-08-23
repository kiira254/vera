from vera import views
from django.urls import path
from .views import SignUpView

urlpatterns = [
    # Leave as empty string for base url
    
    path('store', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    
  
     path('signup/', SignUpView.as_view(), name='signup'),
       path("contact", views.contact, name="contact"),
path('', views.home, name='home'),
]
