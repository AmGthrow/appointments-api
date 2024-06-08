from datetime import time
from zoneinfo import ZoneInfo
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

    @staticmethod
    def is_disallowed_day(dt):
        DISALLOWED_DAYS = [6]
        return dt.weekday() in DISALLOWED_DAYS

    @staticmethod
    def is_within_allowed_time(dt):
        ALLOWED_TIME_START = time(9, 0)
        ALLOWED_TIME_END = time(17, 0)
        return ALLOWED_TIME_START <= dt.time() <= ALLOWED_TIME_END

    def validate(self, attrs):
        start_datetime = attrs["start_time"].astimezone()
        end_datetime = attrs["end_time"].astimezone()

        # Check if the start or end time is on a disallowed day
        if self.is_disallowed_day(start_datetime) or self.is_disallowed_day(
            end_datetime
        ):
            raise serializers.ValidationError(
                "Appointments are not allowed on Sundays."
            )

        # Check if the start or end time is outside the allowed time range
        if not self.is_within_allowed_time(
            start_datetime
        ) or not self.is_within_allowed_time(end_datetime):
            raise serializers.ValidationError(
                "Appointments are only available 9AM-5PM Monday to Saturday."
            )

        # Check if the end time is not after the start time
        if end_datetime <= start_datetime:
            raise serializers.ValidationError("End time must be later than start time.")

        return attrs
