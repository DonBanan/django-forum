# coding: utf-8
import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ChatForm

from .models import Chat


def chat_form(request):
	context = {}
	context['chat_list'] = Chat.objects.all().order_by('-created_at')
	return render(request, 'chat/chat.html', context)