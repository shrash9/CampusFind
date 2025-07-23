from django import forms
from .models import LostItem
from .models import Claim

class LostItemForm(forms.ModelForm):
    date_lost = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = LostItem
        fields = ['title', 'description', 'location', 'date_lost', 'photo']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['description', 'photo']
