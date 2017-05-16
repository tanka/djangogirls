from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Guest


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'tours/index.html'
    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """ Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    """ Return the last five published questions (not including those set to be
    published in the future). """

    def get_queryset(self):
        return Guest.objects.all()
