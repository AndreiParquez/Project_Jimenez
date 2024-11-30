

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Guest, Room, Reservation, Facility
from django.shortcuts import render




def book_room(request):
    rooms = Room.objects.filter(is_available=True) 
    if request.method == 'POST':
       
        pass
    return render(request, 'booking.html', {'rooms': rooms})

def homepage(request):
    rooms = Room.objects.filter(is_available=True)
    facilities = Facility.objects.all()
    return render(request, 'homepage.html', {'rooms': rooms, 'facilities': facilities})


class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'

class FacilityListView(ListView):
    model = Facility
    template_name = 'list_facility.html'
    context_object_name = 'facilities'



class RoomDetailView(DetailView):
    model = Room
    template_name = 'view_room.html'


class GuestCreateView(CreateView):
    model = Guest
    fields = ['name', 'email', 'contact_number']
    template_name = 'guest_form.html'
    success_url = reverse_lazy('home')

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ['guest', 'room', 'date_of_booking', 'status']
    template_name = 'booking.html'
    success_url = reverse_lazy('home')



class RoomUpdateView(UpdateView):
    model = Room
    fields = ['name', 'is_available', 'price', 'description']
    template_name = 'room_form.html'
    success_url = reverse_lazy('room_list')

class FacilityUpdateView(UpdateView):
    model = Facility
    fields = ['name', 'description']
    template_name = 'facility_form.html'
    success_url = reverse_lazy('list_facility')



class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('room_list')

class FacilityDeleteView(DeleteView):
    model = Facility
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list_facility')
