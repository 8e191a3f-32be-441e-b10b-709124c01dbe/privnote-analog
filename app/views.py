from django.shortcuts import render
from django.contrib import messages
from .models import Content
from django.utils import timezone
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def makenote(request):
    content = request.POST.get('text')
    if not content:
        # Error
        messages.error(request, 'Textfield is null!')
        return render(request, 'index.html')
    else:
        # Success
        c = Content(content=str(content))
        c.save()
        messages.success(request, str(c.id))
        return render(request, 'index.html')

def shownote(request, indef):
    now = datetime.datetime.now(tz=timezone.utc)
    c = Content.objects.get(id=indef)

    if not c.fire_date:
        c.fire_date = now
        c.save()
        return render(request, "watch.html", {'content': c.content})
    else:
        return render(request, "watch.html", {'firetime': c.fire_date})