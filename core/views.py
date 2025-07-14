from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import LostItem
from .forms import LostItemForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

class LostItemCreateView(LoginRequiredMixin, CreateView):
    model = LostItem
    form_class = LostItemForm
    template_name = 'core/lostitem_form.html'
    success_url = reverse_lazy('lostitem_list')

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class LostItemListView(ListView):
    model = LostItem
    template_name = 'core/lostitem_list.html'
    paginate_by = 10
    ordering = ['-created_at']

class LostItemDetailView(DetailView):
    model = LostItem
    template_name = 'core/lostitem_detail.html'