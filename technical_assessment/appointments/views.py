from rest_framework import viewsets, exceptions
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        if self.check_for_conflicts(start_time, end_time):
            raise exceptions.ValidationError(
                "The appointment time conflicts with an existing appointment."
            )

        return super().create(request, *args, **kwargs)

    def check_for_conflicts(self, start_time, end_time):
        conflicting_appointments = Appointment.objects.filter(
            start_time__lt=end_time, end_time__gt=start_time
        )
        return conflicting_appointments.exists()
