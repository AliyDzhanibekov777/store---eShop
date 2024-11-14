from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-2'
    }))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Введите отзыв о товаре'
    }))

    class Meta:
        model = Reviews
        fields = ('rating', 'comment')