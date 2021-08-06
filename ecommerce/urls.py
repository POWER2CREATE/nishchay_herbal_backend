from django.urls import path, include
from rest_framework import routers
from ecommerce import views


app_name = 'ecommerce'

router = routers.DefaultRouter()
router.register('view-all-product', views.ViewProductViewSet, basename='viewallproduct')
router.register('view-add-edit-product', views.ProductViewSet, basename='viewadddeditproduct')
router.register('view-add-rating-review', views.RatingReviewViewSet, basename='viewaddratingreview')
router.register('add-cart', views.CartViewSet, basename='viewaddcart')
router.register('view-my-cart', views.ViewMyCartViewSet, basename='viewmycart')
router.register('edit-cart', views.EditCartViewSet, basename='editcart')
# router.register('WishList', views.AddToWishlist, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
    path('product-rating-review/<int:id>', views.ProductRatingReviewAPI.as_view(), name='productratingreview'),
    path('cart-total-price/', views.UpdatePriceView.as_view(), name='cart-total'),
    path('cart/delete/<int:pk>/', views.CartDeleteView.as_view(), name='cart-item-delete'),
    path('wishlist/add/', views.AddToWishlist.as_view(), name='wishlist'),
    path('wishlist/delete/<int:pk>/', views.DelWishListItem.as_view(), name='DelWish'),
    path('My-order/', views.OrderNow.as_view({'get': 'list'})),
    path('Cancel-Order/<int:pk>/', views.OrderDel.as_view(), name='Cancel-My-Order'),
]
