from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import LostItem, Claim
from .forms import LostItemForm,ClaimForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import django_filters
from django_filters.views import FilterView


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
    
class LostItemFilter(django_filters.FilterSet):
    date_lost = django_filters.DateFromToRangeFilter()
    location = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.ChoiceFilter(choices=LostItem.STATUS_CHOICES)

    class Meta:
        model = LostItem
        fields = ['date_lost', 'location', 'status']

class HomeLostItemListView(ListView):
    model = LostItem
    template_name = 'core/home.html'
    paginate_by = 10
    ordering = ['-created_at']

class LostItemListView(FilterView):
    model = LostItem
    template_name = 'core/lostitem_list.html'
    paginate_by = 10
    filterset_class = LostItemFilter
    ordering = ['-created_at']

class LostItemDetailView(DetailView):
    model = LostItem
    template_name = 'core/lostitem_detail.html'

class LostItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LostItem
    fields = ['title', 'description', 'location', 'date_lost', 'photo', 'status']
    template_name = 'core/lostitem_form.html'
    success_url = reverse_lazy('lostitem_list')

    def test_func(self):
        lost_item = self.get_object()
        return lost_item.reporter == self.request.user  # Only reporter can edit

class LostItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LostItem
    template_name = 'core/lostitem_confirm_delete.html'
    success_url = reverse_lazy('lostitem_list')

    def test_func(self):
        lost_item = self.get_object()
        return lost_item.reporter == self.request.user  # Only reporter can delete
    
class ClaimCreateView(LoginRequiredMixin, CreateView):
    model = Claim
    form_class = ClaimForm
    template_name = 'core/claim_form.html'

    def get_success_url(self):
        return reverse_lazy('claim_list')

    def form_valid(self, form):
        form.instance.claimant = self.request.user
        lost_item_id = self.kwargs.get('lost_item_id')
        form.instance.lost_item_id = lost_item_id
        return super().form_valid(form)
    
class ClaimListView(LoginRequiredMixin, ListView):
    model = Claim
    template_name = 'core/claim_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Claim.objects.filter(claimant=self.request.user).order_by('-submitted_at')

class ClaimDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Claim
    template_name = 'core/claim_detail.html'

    def test_func(self):
        claim = self.get_object()
        return claim.claimant == self.request.user or self.request.user.is_staff
