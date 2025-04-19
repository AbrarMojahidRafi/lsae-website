from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ProductLine
from about.models import Certification
from .forms import EnquiryForm
from django.contrib import messages
from django.http import JsonResponse

def home(request):
   product_lines = ProductLine.objects.all()
   certifications = Certification.objects.all()
   if request.method == 'POST':
       form = EnquiryForm(request.POST)
       if form.is_valid():
           form.save()
           if request.is_ajax():
               return JsonResponse({'success': True})
           messages.success(request, 'Thank you for your enquiry. We will get back to you soon!')
           return redirect('home')
       else:
           if request.is_ajax():
               return JsonResponse({'success': False, 'errors': form.errors})
   else:
       form = EnquiryForm()
   return render(request, 'home/home.html', {
       'product_lines': product_lines,
       'certifications': certifications,
       'form': form,
       'now': timezone.now()
   })
