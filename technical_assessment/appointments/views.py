from rest_framework import viewsets, exceptions
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        from_date = self.request.query_params.get("from_date")
        to_date = self.request.query_params.get("to_date")

        if from_date:
            queryset = queryset.filter(start_time__gte=from_date)

        if to_date:
            queryset = queryset.filter(end_time__lte=to_date)

        return queryset

    def create(self, request, *args, **kwargs):
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")

        if self.check_for_conflicts(start_time, end_time):
            raise exceptions.ValidationError(
                "The appointment time conflicts with an existing appointment."
            )

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        instance = self.get_object()

        if self.check_for_conflicts(start_time, end_time, instance.id):
            raise exceptions.ValidationError(
                "The appointment time conflicts with an existing appointment."
            )

        return super().update(request, *args, **kwargs)

    def check_for_conflicts(self, start_time, end_time, instance_id=None):
        conflicting_appointments = Appointment.objects.filter(
            start_time__lt=end_time, end_time__gt=start_time
        )
        if instance_id:
            conflicting_appointments = conflicting_appointments.exclude(id=instance_id)
        return conflicting_appointments.exists()
