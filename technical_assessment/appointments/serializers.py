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

    def validate(self, attrs):
        if attrs["end_time"] <= attrs["start_time"]:
            raise serializers.ValidationError("End time must be later than start time.")
        return attrs
