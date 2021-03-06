# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

# Create your urls here.

urlpatterns = [
	url(r'^Step1$',views.Step1,name='Step1'),
    
    url(r'^Step2$',views.Step2,name='step2'),
    url(r'^Step3$',views.Step3,name='step3'),
    url(r'^Step4$',views.Step4,name='step4'),
    url(r'^Step5$',views.Step5,name='step5'),
    url(r'^Step6$',views.Step6,name='step6'),
    url(r'^Step7$',views.Step7,name='step7'),
    url(r'^common$',views.Step9,name='step9'),
    url(r'^cart$',views.Step8,name='cart'),
    url(r'^motherboard_details', views.motherboard_details, name='motherboard_details'),
    url(r'^gpu_details$', views.gpu_details, name='gpu_details'),
    url(r'^cpu_details$',views.cpu_details,name='cpu_details'),
    url(r'^memory_details$',views.memory_details,name='memory_details'),
    url(r'^storage_details', views.storage_details, name='storage_details'),
    url(r'^',views.index,name='index')
    ]
