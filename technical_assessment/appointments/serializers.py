from rest_framework import serializers
from appointments.models import Appointment
from patients.models import Patient
from patients.serializers import PatientSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True, read_only=True)
    patient_ids = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Appointment
        fields = (
            "id",
            "start_time",
            "end_time",
            "patients",
            "patient_ids",
            "comments",
        )

    def create(self, validated_data):
        patient_ids = validated_data.pop("patient_ids")
        appointment = Appointment.objects.create(**validated_data)
        appointment.patients.set(patient_ids)
        return appointment

    def update(self, instance, validated_data):
        patient_ids = validated_data.pop("patient_ids", None)
        if patient_ids is not None:
            instance.patients.set(patient_ids)
        return super().update(instance, validated_data)
