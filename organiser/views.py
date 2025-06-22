from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from organiser.forms import OrganizerForm
from organiser.models import Organizer


# Create your views here.
class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'create-organizer.html'
    success_url = reverse_lazy('details-organizer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = Organizer.objects.first()
        return context

# def create_organizer(request):
#     if request.method == 'POST':
#         form = OrganizerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('details-organiser')
#     context = {'form': form}
#     return render(request, 'create-organiser.html', context)

class OrganizerDetailView(DetailView):
    model = Organizer
    template_name = 'details-organizer.html'
    context_object_name = 'organizer'

    def get_object(self, queryset=None):
        return Organizer.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = Organizer.objects.first()
        return context

# def organizer_details(request):
#     organizer = Organizer.objects.first()
#     context = {'organizer': organizer}
#     return render(request, 'details-organiser.html', context)

class OrganizerUpdateView(UpdateView):
    model = Organizer
    form_class = OrganizerForm
    template_name = 'edit-organizer.html'
    success_url = reverse_lazy('details-organizer')

    def get_object(self):
        return Organizer.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = Organizer.objects.first()
        return context

# def edit_organizer(request):
#     organizer = Organizer.objects.first()
#     form = OrganizerForm(instance=organizer)
#     if request.method == 'POST':
#         form = OrganizerForm(request.POST, instance=organizer)
#         if form.is_valid():
#             form.save()
#             return redirect('details-organiser')
#     context = {'form': form}
#     return render(request, 'edit-organizer.html', context)

class OrganizerDeleteView(DeleteView):
    model = Organizer
    template_name = 'delete-organizer.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return Organizer.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer'] = Organizer.objects.first()
        return context

# def delete_organizer(request):
#     organizer = Organizer.objects.first()
#     if request.method == 'POST':
#         organizer.delete()
#         return redirect('index')
#     context = {'organizer': organizer}
#     return render(request, 'delete-organiser.html', context)