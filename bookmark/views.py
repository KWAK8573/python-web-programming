from django.shortcuts import render ,redirect
from django.utils import timezone
from django.views.generic import ListView,DetailView
from .models import Bookmark
from .form import BlogUpdate

# Create your views here.

def create(request):
    return render(request, 'bookmark/create.html')

def postcreate(request):
    model = Bookmark()
    model.title = request.GET['title']
    model.url = request.GET['url']
    model.pub_date = timezone.datetime.now()
    model.save()
    return redirect('/bookmark/' + str(model.id))


def update(request, model_id):
    model = Bookmark.objects.get(id=model_id)

    if request.method == "POST":
        form = BlogUpdate(request.POST) 
        if form.is_valid():
            model.title = request.POST['title']
            model.url = request.POST['url']
            model.pub_date = timezone.datetime.now()
            model.save()
            return redirect('/bookmark/' + str(model.id))

    else:
        form = BlogUpdate(instance = model)
        return render(request, 'bookmark/update.html', {'form':form})
    
    
def delete(request, model_id):
        model = Bookmark.objects.get(id=model_id)
        model.delete()
        return redirect('/bookmark/')

class BookmarkLV(ListView):
    model = Bookmark
    pagenate_by = 2
    
    def get_queryset(self):
        return Bookmark.objects.order_by('-id')
    
class BookmarkDV(DetailView):
    model = Bookmark
