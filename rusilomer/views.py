from rusilomer.models import Event

from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone

def index(request):
    # return redirect('index')
    return render(request, 'index.html')

def carousel_event(request):
    context = {}

    now = timezone.now()
    # upcoming = Event.objects.filter(event_date__gte=now).order_by('event_date')
    # passed = Event.objects.filter(event_date__lt=now).order_by('-date')
    context['test'] = 'testing'

              # + list(passed)
    return render(request, 'test.html', context)



    # context = {}
    #
    # now = datetime.today()
    # now = now.strftime('%y-%m-%d')
    # event_array = Event.objects.filter('pub_date')
    # Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3))

    # future_event = Event.objects.filter( Q(event_date__incontants > now))
    # past_event =

    # from django.utils import timezone
    # from myapp.models import Event

    # class EventListView(generics.ListView):
    #     def get_queryset(self):
    #         now = timezone.now()
    #         upcoming = Event.objects.filter(date__gte=now).order_by('date')
    #         passed = Event.objects.filter(date__lt=now).order_by('-date')
    #         return list(upcoming) + list(passed)
    #
    # # now = timezone.now()
    # (Event.objects.annotate(
    #     relevance=models.Case(
    #         models.When(date__gte=now, then=1),
    #         models.When(date__lt=now, then=2),
    #         output_field=models.IntegerField(),
    #     )).order_by('relevance'))

    # now = datetime.today()
    # print(now)



