from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from .models import ChecklistItem, Play
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


class PlayDetailView(DetailView):
    model = Play
    template_name = 'pages/play_detail.html'
    pk_url_kwarg = 'play_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['checklists'] = ChecklistItem.objects.filter(play=self.object).all()
        return context
        
        
class ChecklistCreate(CreateView):
    model = ChecklistItem
    fields = ['content']
    success_url = '/play/'
    template_name = 'pages/checklist_create.html'
    
 
    def get_success_url(self) -> str:
        return self.success_url + str(self.kwargs['play_id']) + '/'
    def form_valid(self, form):
        data = form.save(commit=False)
        data.play = Play.objects.get(id=self.kwargs['play_id'])
        data.save()
        return redirect(self.get_success_url())


class ChecklistUpdateView(UpdateView):
    model = ChecklistItem
    pk_url_kwarg = 'check_id'
    fields = ['checked']
    success_url = '/play/'
    template_name = 'pages/checklist_update.html'
    
    def get(self, request, *args, **kwargs):
        data = super().get_object()
        data.checked = not data.checked
        data.save()
        return redirect(self.get_success_url())
        
        

    def get_success_url(self) -> str:
        # 'view-play' == 상세보기
        return reverse('view-play', kwargs={'play_id': str(self.kwargs['play_id'])})
        # return self.success_url + str(self.kwargs['play_id']) + '/'