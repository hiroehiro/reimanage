from django.shortcuts import render
from django.views.generic import TemplateView,ListView

class TopView(TemplateView):
    template_name = "top.html"

