from rusilomer.models import Event

from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from django.db.models import Case, When, IntegerField, F, DurationField

def index(request):
    context = {}
    # context['test_message'] = 'Test carousel_event!'
    now = timezone.now()

    passed = Event.objects.filter(event_date__lt=now).order_by('-event_date')
    col_upcoming = len(passed)

    # context['test_message'] = col_upcoming
    context['events'] = passed[:10]
    context['events1'] = passed[:3]
    context['events2'] = passed[3:7]
    context['events3'] = passed[7:10]



    return render(request, 'index.html', context)

def carousel_event(request):



    return render(request, 'index.html')




