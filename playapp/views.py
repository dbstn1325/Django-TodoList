from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Play
from .forms import PlayForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    context = {}
    return render(request, 'pages/index.html', context)


class PlaylistView(TemplateView):
    template_name = 'pages/play_list.html'

    def get_context_data(self, **kwargs):
        plays = Play.objects.filter(dead_line__gte=timezone.now()).order_by('-dead_line').all()
        paginator = Paginator(plays, 1)
        page_number = self.request.GET.get('page','1')
        paging = paginator.get_page(page_number)
        return {
            'paging': paging
        }

class PlayCreateView(CreateView):
    template_name = 'pages/play_create.html' 
    success_url='/'
    form_class = PlayForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PlayPreviousListView(ListView):
    model = Play
    template_name = 'pages/play_previous_list.html'
    queryset = Play.objects.filter(dead_line__lt=timezone.now()).order_by('-dead_line')
    paginate_by = 1




