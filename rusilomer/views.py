from rusilomer.models import Event

from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from django.db.models import Case, When, IntegerField, F, DurationField

def index(request):
    # return redirect('index')
    return render(request, 'index.html')

def carousel_event(request):
    context = {}
    context['test_message'] = 'Test carousel_event!'
    now = timezone.now()

    passed = Event.objects.filter(event_date__lt=now).order_by('-event_date')
    col_upcoming = len(passed)

    context['test_message'] = col_upcoming
    context['events'] = passed[:10]





    return render(request, 'index.html', context)




