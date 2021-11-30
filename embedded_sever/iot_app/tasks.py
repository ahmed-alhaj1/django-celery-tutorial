import random
import string
from django.contrib.auth.models import User  
from django.utils.crypto import get_random_string
from celery.utils.log import get_task_logger 
from celery import shared_task


logger = get_task_logger(__name__)

@shared_task(name="sum_two_numbers")
def add(x,y):
    return x+y 

@shared_task(name="multiply_two_number")
def mul(x,y):
    tot = x * (y * random.randint(3,1000))
    return tot 
@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)

@shared_task

def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email =  '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password )
        return '{} random user creaetd with success !'.format(total)

@shared_task
def debug_task():
    logger.info("task executed .")