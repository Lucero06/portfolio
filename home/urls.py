from django.urls import path

from home.views import MorningGreetingView, HomeView, ContactView, CvView,PreviewView, robots_txt
from django.views.generic.base import TemplateView


urlpatterns = [
    # path('robots.txt', Robots.as_view(), name='robots'),
    # path("robots.txt",
    #     TemplateView.as_view(
    #         template_name="robots.txt", 
    #         content_type="text/plain")),
    path("robots.txt", robots_txt),
    path('', HomeView.as_view(), name='home',),
    path('contacto', ContactView.as_view(), name='contact'),
    path('cv', CvView.as_view(), name='cv'),
    path('vistas', PreviewView.as_view(), name='preview'),
    #######
    path('salute', MorningGreetingView.as_view(text2='byee')),
]