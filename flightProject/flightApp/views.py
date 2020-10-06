from django.shortcuts import render
from .models import Flight,Passanger,Reservation
from .serializers import FlightSerializer,PassangerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def find_flight(request):
    flights = Flight.objects.filter(departure_city=request.data['departure_city'],arrival_city=request.data['arrival_city'],deate_departure=request.data['deate_departure'])
    serializer = FlightSerializer(flights,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def flight_reservation(request):
    postdata = request.data.copy()
    firstname = postdata.get('FirstName')
    data = {
        'name':firstname,
    }

    jsonResponse = {
        'status':'200',
        'message': 'ffd',
        'data':data,
    }
    return Response(status=status.HTTP_200_OK,data=data)
    # return Response(jsonResponse)

class FightViewset(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassangerViewset(viewsets.ModelViewSet):
    queryset = Passanger.objects.all()
    serializer_class = PassangerSerializer

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
