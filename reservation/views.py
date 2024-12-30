

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Guest, Room, Reservation, Facility
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse






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
    fields = ['guest', 'room', 'checkIn','checkOut', 'status']
    template_name = 'booking.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.filter(is_available=True)
        context['guests'] = Guest.objects.all()
        context['checkIn'] = Guest.objects.all()
        context['checkOut'] = Guest.objects.all()
        context['total_cost'] = Guest.objects.all()
        context['status'] = ['Pending','Complete']
        return context

    def form_valid(self, form):
        check_in = form.cleaned_data['checkIn']
        check_out = form.cleaned_data['checkOut']
        room = form.cleaned_data['room']
        total_days = (check_out - check_in).days
        total_cost = total_days * room.price
        form.instance.total_cost = total_cost
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors})
        return super().form_invalid(form)



class RoomUpdateView(UpdateView):
    model = Room
    fields = ['name', 'description', 'image', 'price', 'is_available']
    template_name = 'update_room.html'
    success_url = reverse_lazy('room_list')

class FacilityUpdateView(UpdateView):
    model = Facility
    fields = ['name', 'description']
    template_name = 'facility_form.html'
    success_url = reverse_lazy('list_facility')



class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'room_delete.html'
    success_url = reverse_lazy('room_list')

class FacilityDeleteView(DeleteView):
    model = Facility
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list_facility')
