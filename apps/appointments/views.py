from rest_framework import status
from rest_framework.views import APIView
from apps.appointments.serializers import AppointmentSerializer
from apps.shared.response import CustomResponse


class AppointmentCreateView(APIView):
    def post(self,request):
        serializer = AppointmentSerializer(data=request.data)
        if not serializer.is_valid():
            return CustomResponse.error(
                message="Validation error",
                errors=serializer.errors,
            )
        serializer.save()
        return CustomResponse.success(
            data=serializer.data,
            message="Your appointment has been booked successfully!",
            status_code=status.HTTP_201_CREATED
        )