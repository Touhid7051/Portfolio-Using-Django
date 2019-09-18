from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = reversed(Service.objects.all())
        context['works'] = RecentWork.objects.all()
        context['clients'] = Client.objects.all()
        context['contact'] = Contact.objects.first()
        context['contactT'] = contactTitle.objects.first()
        context['aboutT'] = aboutTitle.objects.first()
        context['clientsT'] = testimonialTitle.objects.first()
        context['servicesT'] = serviceTitle.objects.first()
        context['portfolioT'] = portfolioTitle.objects.first()
        context['addressT'] = adressTitle.objects.first()



        return context
