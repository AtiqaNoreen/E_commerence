
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('shop/', views.shop, name='shop'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('shoppingcart/', views.shoppingcart, name='shopping-cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('wishlist/', views.wishlist, name='wishlist'),
    path('login/', views.login_view, name='login'),
    path("update-cart/<int:item_id>/", views.update_cart, name="update_cart"),
    path("remove-cart-item/<int:item_id>/", views.remove_cart_item, name="remove_cart_item"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)