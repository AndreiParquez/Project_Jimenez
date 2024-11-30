from django.urls import path
from .views import (
    RoomListView, RoomDetailView, GuestCreateView, FacilityListView,
    ReservationCreateView, RoomUpdateView, RoomDeleteView, 
    FacilityUpdateView, FacilityDeleteView, homepage, book_room
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', homepage, name='home'),
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='view_room'),
    path('rooms/<int:pk>/update/', RoomUpdateView.as_view(), name='update_room'),
    path('rooms/<int:pk>/delete/', RoomDeleteView.as_view(), name='delete_room'),
    
    
    path('guests/create/', GuestCreateView.as_view(), name='create_guest'),
    path('facilities/', FacilityListView.as_view(), name='list_facility'),
    path('facilities/<int:pk>/update/', FacilityUpdateView.as_view(), name='update_facility'),
    path('facilities/<int:pk>/delete/', FacilityDeleteView.as_view(), name='delete_facility'),
    path('reservations/create/', ReservationCreateView.as_view(), name='book_room'),
    path('book-room/', book_room, name='book_room'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
