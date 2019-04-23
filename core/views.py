from django.shortcuts import render, redirect

from django.views.generic import ListView, TemplateView
from .forms import PostForm
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'

class UploadView(TemplateView):
    template_name = 'core/upload.html'

    def upload_image(request):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PostForm()
        return render(request, 'core/upload.html', {
            'form': form
        })
