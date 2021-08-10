from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import *
from core.models import User
from core.permissions import *
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.views import APIView
from digitalprofile import models as digipromodel
from django.db.models import Q
import datetime
from ecommerce import models as ecomodel



class CouponView(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    today = datetime.date.today()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.queryset.filter(active=True, valid_from__lte=self.today, valid_to__gte=self.today)
        except Coupon.DoesNotExist:
            return Response({"DOESNT_EXIST": "No object in Coupon list"}, status=402)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=200)

class RedeemCoupon(APIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get_object(self, pk):
        try:
            return Coupon.objects.get(id=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        if snippet.filter(user=request.user) is not None:
            return Response({"CANT USE":"U can't use same coupon again"}, status=400)
        serializer = CouponSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            coupon = Coupon.objects.get(id=pk)
        except Coupon.DoesNotExist:
            return Response({"DOES_NOT_EXIST":"No coupon exist by this id"}, status=402)
        for i in coupon.user:
            if i == request.user:
                return Response({"CANT USE":"U can't use same coupon again"}, status=400)
        coupon.user = request.user

        serializer = CouponSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class rewardcodeList(viewsets.ModelViewSet):
    queryset = RewardCode.objects.all()
    serializer_class = RewardCodeSerializer
    permission_classes =[permissions.IsAuthenticated,]

    def list(self,request,*args,**kwargs):
        print("here")
        try:
            student = User.objects.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response("error",status=400)
        print(student)

        queryset =self.queryset.filter(user=student)

        claim = self.request.query_params.get('claim', None)
        if claim is not None:
            if claim == "false":
                queryset = queryset.filter(claimed=False)
            elif claim == "true":
                queryset = queryset.filter(claimed=True)
        else:
            queryset = queryset.filter(claimed=False)
        
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=200)


class ReferralcodeAPI(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self,request):
        try:
            student = RewardCode.objects.get(code=request.data["referralcode"])
        except ObjectDoesNotExist:
            return Response({"error":"Referral code invalid"},status=400)
        
        sys = RewardSystem.objects.get(user=student)

        sys.points = sys.points + 50
        sys.totalReferral = sys.totalReferral + 1

        sys.save()

        return Response({"Successful"},status=200)

