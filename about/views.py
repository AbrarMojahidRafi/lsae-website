from django.shortcuts import render
from django.utils import timezone
from .models import SpecialMachinery, Certification

def about(request):
    special_machineries = SpecialMachinery.objects.all()
    certifications = Certification.objects.all()
    current_date = timezone.now()
    return render(request, 'about/about.html', {
        'special_machineries': special_machineries,
        'certifications': certifications,
        'now': current_date
    })
