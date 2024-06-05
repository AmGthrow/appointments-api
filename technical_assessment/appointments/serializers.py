from rest_framework import serializers

from appointments.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    patients = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = (
            "id",
            "start_time",
            "end_time",
            "patients",
            "comments",
        )

    def get_patients(self, obj):
        return [patient.name for patient in obj.patients.all()]
