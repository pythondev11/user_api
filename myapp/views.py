from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from datetime import timedelta
import datetime
import pytz
from django.utils import timezone

from myapp.models import UserData


class ProfileApiCreateRead(ViewSet):

    def get_all_user_details(self, request):
        from pytz import timezone
        response = {"ok": False, 'members': [],
                    "message": '!!! Ops something went wrong '}
        status_code = status.HTTP_400_BAD_REQUEST
        data = list()
        all_members = UserData.objects.all()
        for member in all_members:
            member_details = {
                'id': member.id,
                'real_name': member.real_name,
                'tz': member.time_zone,
                'activity_periods': []
            }

            for activity in member.activity_periods.all():
                activity_data = {
                    'start_time': activity.start_time.astimezone(
                    timezone((member_details['tz']))).strftime("%d %B, %Y, %I%p "),
                    'end_time': activity.end_time.astimezone(
                    timezone((member_details['tz']))).strftime("%d %B, %Y, %I%p ")}
                member_details['activity_periods'].append(activity_data)

            data.append(member_details)

        if len(data) > 0:
            response.update({'members': data, 'ok': True})
            response.update({'message': 'data recived from db '})
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
