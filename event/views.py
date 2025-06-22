from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from event.models import Event
from event.forms import EventForm
from organiser.models import Organizer


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

# def index(request):
#     return render(request, 'index.html')

class EventListView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all().order_by('-start_time')

# def event_list(request):
#     events = Event.objects.all()
#     context = {'events': events}
#     return render(request, 'events.html', context)

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'create-event.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.organizer = Organizer.objects.first()
        return super().form_valid(form)

# def create_event(request):
#     organizer = Organizer.objects.first()
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.organizer = organizer
#             event.save()
#             return redirect('events')
#     context = {'form': form}
#     return render(request, 'create-event.html', context)

class EventDetailView(DetailView):
    model = Event
    template_name = 'details-event.html'
    context_object_name = 'event'
    pk_url_kwarg = 'event_pk'

# def event_details(request, event_pk):
#     event = get_object_or_404(Event, pk=event_pk)
#     context = {'event': event}
#     return render(request, 'details-event.html', context)

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'edit-event.html'
    pk_url_kwarg = 'event_pk'

    def get_success_url(self):
        return reverse_lazy('details-event', kwargs={'event_pk': self.object.pk})

# def edit_event(request, event_pk):
#     event = get_object_or_404(Event, pk=event_pk)
#     if request.method == 'POST':
#         form = EventForm(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('details-event', event_pk=event.pk)
#     context = {
#         'form': form,
#         'event': event,
#     }
#     return render(request, 'edit-event.html', context)

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'delete-event.html'
    pk_url_kwarg = 'event_pk'
    success_url = reverse_lazy('events')

# def delete_event(request, event_pk):
#     event = get_object_or_404(Event, pk=event_pk)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('event-list')
#     context = {'event': event}
#     return render(request, 'delete-event.html', context)