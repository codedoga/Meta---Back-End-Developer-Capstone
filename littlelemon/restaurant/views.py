from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Menu, Booking
from restaurant.serializers import BookingSerializer, MenuSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
