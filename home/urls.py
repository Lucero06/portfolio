from django.urls import path

from home.views import MorningGreetingView, HomeView, ContactView, CvView

urlpatterns = [
    path('', HomeView.as_view()),
    path('contacto', ContactView.as_view()),
    path('cv', CvView.as_view()),
    #######
    path('salute', MorningGreetingView.as_view(text2='byee')),
]