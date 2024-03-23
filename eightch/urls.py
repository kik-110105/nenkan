from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

app_name="eightch"
urlpatterns = [
    path('',views.ThreadView.as_view(), name='threadview'),
    path('thread_toukou/',views.ThreadToukouView.as_view(), name='threadtoukouview'),
    path('thread_toukou/thread_ok/', views.threadpost, name='thread_ok'),
    
    path('thread_list/', views.threadListView, name='threadListView'),
    path('<int:threadid>/', views.ThreadTextView.as_view(), name='threadtextview'),
    path('<int:threadid>/toukou_ok/', views.toukoupost, name='toukou_ok'),

    path('otoiawase/',views.OtoiawaseView.as_view(), name='otoiawase'),
    path('otoiawase/otoiawase_ok/',views.otoiawasepost, name='otoiawase_ok'),

]