from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingItemSerializer



# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingItemSerializer
    permission_classes  = [permissions.IsAuthenticated]
    