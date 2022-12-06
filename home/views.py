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

from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.views.decorators.http import require_GET
from decouple import config

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: Googlebot",
        "Disallow: ",
        "User-agent: googlebot-image",
        "Disallow: ",
        "User-agent: googlebot-mobile",
        "Disallow: ",
        "User-agent: *",
        "Disallow: ",
        "Disallow: /cgi-bin/",
        "Sitemap: http://monse66.pythonanywhere.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def variables():
    return {
        'number':config('CEL_NUMBER'),
        'mail':config('EMAIL')
    }

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['preview', 'contact', 'cv', 'home']
    
    def location(self, item):
        return reverse(item)

class HomeView(View):
    def get(self,request):
        variables_o=variables()
        template_name='portfolio/base.html'
        return render(request, template_name,variables_o)

class CvView(View):
    def get(self,request):
        variables_o=variables()
        template_name='cv.html'
        return render(request, template_name)

class PreviewView(View):
    def get(self, request):
        variables_o=variables()
        template_name='previews.html'
        return render(request, template_name, variables_o)

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

