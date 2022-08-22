from django.urls import path

from home.views import MorningGreetingView, HomeView, ContactView, CvView,PreviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacto', ContactView.as_view(), name='contact'),
    path('cv', CvView.as_view(), name='cv'),
    path('vistas', PreviewView.as_view(), name='preview'),
    #######
    path('salute', MorningGreetingView.as_view(text2='byee')),
]