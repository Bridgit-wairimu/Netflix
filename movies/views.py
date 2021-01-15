from django.shortcuts  import render
from .forms import MoviesLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import MoviesLetterRecipients
from django.contrib.auth.decorators import login_required
from .models import Image,Category



# Create your views here.
def welcome(request,category):
    url = 'https://api.themoviedb.org/3/movie/550?api_key=fc3a024559a41bf4c9130f6e3345d852'
    key = config('API_KEY')
    url = config('url')
    url1 = url.format(category,key)
    url2 = requests.get(url1)
    url3 = url2.json()
    return url3

def Welcome (request):
    popular = welcome(request, 'popular')
    upcoming = welcome(request, 'upcoming')
    airingToday = welcome(request, 'airing_today')
    trending = welcome(request, 'trending')

    return render (request, 'welcome.html', {'popular': popular, 'upcoming': upcoming, 'airing_today': airingToday, 'trending': trending})

def youtube(request,id):
    youTubeKey = config('youTubeKey')
    popular = welcome(request, 'popular')
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']

    youtube = build('youtube', 'v3', developerKey= youTubeKey)
    request = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video')
    res = request.execute()
    return render(request,'youtube.html',{'response':res})



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


def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
                
        message = 'No searches yet'
        return render(request, 'search.html',{"message": message})


