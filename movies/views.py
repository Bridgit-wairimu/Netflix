from django.shortcuts  import render
from .forms import MoviesLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import MoviesLetterRecipients
from django.contrib.auth.decorators import login_required
from .models import Image,Category



# Create your views here.


@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()

    if request.method == 'POST':
        form = MoviesLetterForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            
            recipient = MoviesLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('welcome')
    else:
        form = MoviesLetterForm()

    return render(request, 'welcome.html',{"letterForm":form , 'images': images[::-1]})
