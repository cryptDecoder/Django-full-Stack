from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.


def home_page(request):
    leads = Lead.objects.all()

    context = {
        "leads": leads
    }
    return render(request, "leads/home_page.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse("Here is detailed view")
