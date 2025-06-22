from organiser.models import Organizer

def organizer_context(request):
    return {
        'organizer': Organizer.objects.first()
    }
