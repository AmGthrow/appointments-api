from rest_framework import serializers

from appointments.models import Appointment
from patients.serializers import PatientSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True)

    class Meta:
        model = Appointment
        fields = (
            "id",
            "start_time",
            "end_time",
            "patients",
            "comments",
        )
