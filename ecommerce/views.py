from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from core.models import User
from core.permissions import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import render, get_object_or_404

# Create your views here.


class ViewProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.user.is_admin is False:
            return Response({"error": "You are not Admin"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)


class RatingReviewViewSet(viewsets.ModelViewSet):
    queryset = RatingReview.objects.all()
    serializer_class = RatingReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def create(self, request, *args, **kwargs):
        # if request.user.is_admin is False:
        # return Response({"error": "You are not Admin"}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)


class ProductRatingReviewAPI(generics.RetrieveAPIView):
    queryset = RatingReview.objects.all()
    serializer_class = RatingReviewSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=self.kwargs["id"])
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "Product Does not exist"}, status=400)

        queryset = self.queryset.filter(product=product)
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = AddToCartSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer, IsOwner]

    

    def create(self, request, *args, **kwargs):
        # if request.user.is_admin is False:
        # return Response({"error": "You are not Admin"}, status=400)
        if Cart.objects.filter(product=request.data.get('product'), user=request.user).exists():
            return Response({"ALREADY_EXIST": "Item Already Exists in Cart"}, status=400)

        if not Product.objects.filter(product_name=request.data.get('product')).in_stock:
            return Response({"OUT_OF_STOCK": "Item currently not available in Stock"}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer.save(user=request.user))
        return Response(serializer.data, status=200)

    

class CartDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = ViewMyCartSerializer(queryset, context = {'request':request})
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ViewMyCartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = ViewMyCartSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer, IsOwner]

    
    def list(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.filter(user=user)
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"NO_ITEM": "Empty Cart"}, status=400)
    
    


class EditCartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = EditCartSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer, IsOwner]

class UpdatePriceView(APIView):
    # queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get(self, request, *args, **kwargs):
        try:
            queryset = Cart.objects.all().filter(user=request.user)
        except Cart.DoesNotExist:
            raise Http404
        total = 0
        for i in queryset:
            total += i.product.selling_price * i.quantity
        content = {'total_price':total}
        return Response(content)

from rest_framework import viewsets, permissions

class AddToWishlist(APIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get(self, request):
        try:
            queryset = self.queryset.get(user=request.user)
        except WishList.DoesNotExist:
            return Response({"DOESNT_EXIST": "Item Doesn't Exists in WishList"}, status=402)
        serializer = WishListSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if WishList.objects.filter(product=request.data.get('product'), user=request.user).exists():
            return Response({"ALREADY_EXIST": "Item Already Exists in WishList"}, status=400)
        
        if request.data['user'] is None:
            request.data['user'] = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DelWishListItem(APIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get_object(self, pk):
        try:
            return WishList.objects.get(id=pk)
        except WishList.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = self.serializer_class(snippet)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


