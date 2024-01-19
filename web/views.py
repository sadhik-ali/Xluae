import json

from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import EducationalPrograms, Feature, Team, WeOffer, Magazine


def index(request):
    weoffers = WeOffer.objects.all()
    programs = EducationalPrograms.objects.all()

    form = ContactForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)

            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {"weoffers": weoffers, "programs": programs, "form": form}
    return render(request, "web/index.html", context)


def football_academy(request):
    features = Feature.objects.all()
    teams = Team.objects.all()
    context = {"features": features, "teams": teams}
    return render(request, "web/football_academy.html", context)


def programs(request, slug):
    program_details = EducationalPrograms.objects.get(slug=slug)
    context = {"program_details": program_details}
    return render(request, "web/programs.html", context)


def contact(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)

            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Thank You, Our Team Will Contact you Soon",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "form2 validation error",
                "message": repr(form.errors),
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {"form": form}
    return render(request, "web/contact.html", context)

def magazine(request):
    magazines = Magazine.objects.all()
    return render (request, 'web/magazine.html', {'magazines': magazines})  

def magazine_detail(request):
    return render (request, 'web/magazine_detail.html')

