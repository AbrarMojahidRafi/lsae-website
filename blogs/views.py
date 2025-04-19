# blogs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogImage
from .forms import BlogForm, BlogImageForm
from django.forms import modelformset_factory

def blog_list(request):
    blogs = Blog.objects.filter(status='approved').order_by('-published_date')
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


@login_required
def blog_create(request):
    BlogImageFormSet = modelformset_factory(BlogImage, form=BlogImageForm, extra=10, max_num=10)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        formset = BlogImageFormSet(request.POST, request.FILES, queryset=BlogImage.objects.none())
        if form.is_valid() and formset.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user.username
            blog.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    BlogImage.objects.create(blog=blog, image=image)
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm()
        formset = BlogImageFormSet(queryset=BlogImage.objects.none())
    return render(request, 'blog_form.html', {'form': form, 'formset': formset})

@login_required
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    BlogImageFormSet = modelformset_factory(BlogImage, form=BlogImageForm, extra=10, max_num=10, can_delete=True)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        formset = BlogImageFormSet(request.POST, request.FILES, queryset=BlogImage.objects.filter(blog=blog))
        if form.is_valid() and formset.is_valid():
            form.save()
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    form.instance.delete()
                elif form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.blog = blog
                    image.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
        formset = BlogImageFormSet(queryset=BlogImage.objects.filter(blog=blog))
    return render(request, 'blog_form.html', {'form': form, 'formset': formset})
