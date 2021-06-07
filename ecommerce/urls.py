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

urlpatterns = [
    path('', include(router.urls)),
    path('product-rating-review/<int:id>', views.ProductRatingReviewAPI.as_view(), name='productratingreview'),

]
