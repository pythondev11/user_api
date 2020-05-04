from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from myapp.models import UserData, ActivityRecord

import datetime
from faker import Faker
from random import randint
from django.utils import timezone



class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        try:
            for i in range(int(total)):
                user_obj = UserData.objects.create(
                  real_name=fake.name(),
                  time_zone=fake.timezone()
                  )
                for j in range(randint(1, 3)):
                    current_time = timezone.now()
                    et = current_time + datetime.timedelta(hours=randint(1, 10))
                    this_activity = ActivityRecord.objects.create(
                        start_time=current_time,
                        end_time=et)
                    user_obj.activity_periods.add(this_activity)
                user_obj.save()
            self.stdout.write(self.style.SUCCESS(' {} users created successfully!!!'.format(total)))
        except:
            self.stdout.write(self.style.WARNING(' Sorry something went wrong'))

