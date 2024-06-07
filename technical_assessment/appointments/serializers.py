from rest_framework import serializers

from appointments.models import Appointment
from patients.models import Patient


class AppointmentSerializer(serializers.ModelSerializer):
    patients = serializers.SlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Patient.objects.all(),
    )

    class Meta:
        model = Appointment
        fields = (
            "id",
            "start_time",
            "end_time",
            "patients",
            "comments",
        )
