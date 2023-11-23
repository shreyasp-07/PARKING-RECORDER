from django import forms
from .models import Vehicle

class ImageCaptureForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'image']
