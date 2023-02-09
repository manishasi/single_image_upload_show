from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect # new
from .models import Image
from .forms import ImageUploadForm # new 

# def index(request):
#     data = Image.objects.all()
#     context = {
#         'data' : data
#     }
#     return render(request,"display.html", context)
# new
def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
            form = ImageUploadForm()
            data = Image.objects.all()
    return render(request, 'upload.html', {'form': form, 'data': data})