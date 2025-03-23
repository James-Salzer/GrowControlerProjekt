import socket
import netifaces
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.conf import settings
from .models import Sensor, SensorData, Actor

## @brief Checks if the required database tables exist.
#  @return True if all tables exist, False otherwise.
def check_database_tables():
    table_names = connection.introspection.table_names()
    required_tables = ['webinterface_sensordata', 'webinterface_wificonfig']
    for table in required_tables:
        if table not in table_names:
            print(f"Error: Table '{table}' is missing from the database.")
            return False
    return True

## @brief Gets the IP address of the system, prioritizing Ethernet over WLAN.
#  @return The IP address as a string, or '127.0.0.1' if no IP address is found.
def get_ip_address():
    try:
        # Prioritize Ethernet interface
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            if 'eth' in interface:
                addresses = netifaces.ifaddresses(interface)
                if socket.AF_INET in addresses:
                    return addresses[socket.AF_INET][0]['addr']
        # If no Ethernet, try WLAN interface
        for interface in interfaces:
            if 'wlan' in interface:
                addresses = netifaces.ifaddresses(interface)
                if socket.AF_INET in addresses:
                    return addresses[socket.AF_INET][0]['addr']
    except Exception as e:
        print(f"Error getting IP address: {e}")
    return '127.0.0.1'

## @brief Renders the index page with the IP address and a welcome message.
#  @param request The HTTP request object.
#  @return An HTTP response with the rendered index page.
def index(request):
    if not check_database_tables():
        return render(request, 'error.html', {'message': 'Database tables are missing.'})
    ip_address = get_ip_address()
    sensors = Sensor.objects.all()
    actors = Actor.objects.all()
    return render(
        request,
        'index.html',
        {'message': 'Hallo, GrowController!', 'ip_address': ip_address, 'sensors': sensors, 'actors': actors}
    )

## @brief Handles button click events.
#  @param request The HTTP request object.
#  @return A JSON response indicating the status of the button click.
def button_click(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'Button-Klick empfangen'})
    return JsonResponse({'status': 'Invalid request'})

