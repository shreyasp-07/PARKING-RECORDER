import cv2
import pytesseract
from django.shortcuts import render, redirect
from .forms import ImageCaptureForm
from .models import Vehicle

def capture_image(request):
    if request.method == 'POST':
        form = ImageCaptureForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            image = vehicle.image.path
            
            # Your image processing logic using OpenCV and Tesseract here
            
            vehicle.save()
            return redirect('success_page')  # Redirect to success page
    else:
        form = ImageCaptureForm()
    
    return render(request, 'capture.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')
