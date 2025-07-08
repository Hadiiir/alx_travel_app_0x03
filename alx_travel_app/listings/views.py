from .tasks import send_booking_confirmation

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def perform_create(self, serializer):
        booking = serializer.save()
        # Trigger email task
        send_booking_confirmation.delay(
            recipient_email=booking.user.email,
            booking_details=str(booking)
        )