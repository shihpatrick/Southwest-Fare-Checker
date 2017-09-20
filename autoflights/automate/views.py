# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {
		'name': 'Patrick'
	}

	return render(request, 'index.html', context)
