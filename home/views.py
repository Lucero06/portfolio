from django.shortcuts import render
from  django.views import View
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import MailForm
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings
from decouple import config
from smtplib import SMTPException

class HomeView(View):
    def get(self,request):
        template_name='portfolio/base.html'
        return render(request, template_name)

class CvView(View):
    def get(self,request):
        template_name='cv.html'
        return render(request, template_name)

class PreviewView(View):
    def get(self, request):
        template_name='previews.html'
        return render(request, template_name)

class ContactView(HomeView):
    form_class=MailForm
    template_name='contact.html'

    def get(self, request):
        #print(request)
        form= self.form_class()
        return render(request, self.template_name, {'form':form,'number':config('CEL_NUMBER'), 'mail':config('EMAIL')})
    
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            data = form.cleaned_data
            try:
                send_mail(
                    'Portfolio message',
                    'Nombre: '+data['name']+'\n'
                    +'Celular: '+data['cellphone_number']+'\n'
                    +'Tel.Fijo: '+data['phone_number']+'\n\n'
                    +'Mensaje:\n'+data['body'],
                    config('EMAIL_HOST_USER'),
                    [config('SEND_EMAIL')],
                    fail_silently=False,
                )
            except SMTPException as e:
                return render(request, self.template_name, 
                        {'form': form, 
                        'status':'fail',
                        'number':config('CEL_NUMBER'), 
                        'mail':config('EMAIL')})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            form=self.form_class()
            return render(request, self.template_name, 
                            {'form': form, 'status':'success',
                            'number':config('CEL_NUMBER'), 
                            'mail':config('EMAIL')})
            
        return render(request, self.template_name, 
                        {'form': form, 'status':'false', 
                        'number':config('CEL_NUMBER'), 
                        'mail':config('EMAIL')})

#################
class TestView(View):
    text='Hi'
    text2='Bye'
    text3=' :D'
    def get(self, request):
        # <view logic>
        return HttpResponse(self.text+' result <h1>HOla</h1>'+self.text2+self.text3)

class MorningGreetingView(TestView):
    text = "Morning to ya"
    def get(self, request):
        # <view logic>
        return HttpResponse(self.text+' result <h1>HOla</h1>'+self.text2+self.text3)

