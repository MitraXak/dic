from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Dict
from .forms import GetDict
import re
# Create your views here.
english = re.compile(r"[a-z]", re.I)
russha = re.compile(r"[а-я]", re.I)
def index(request):
    if(request.method =="POST"):
        gendr = request.POST.get("word").lower()
        if english.search(gendr):
            d = Dict.objects.get(englishWord=gendr);
            return render(request, 'base/content.html', {'d': d })
        if russha.search(gendr):
            d = Dict.objects.get(rush=gendr);
            return render(request, 'base/content.html', {'d': d.englishWord})
        
    else:
        d = Dict.objects.all()
        return render(request, 'base/content.html', {'d': d})

def send(request):
    try:
        if(request.method == "POST"):
            data = request.FILES['file'].readlines()
            import re
            temOne = re.compile(r"<k>(.*)</k>", re.I | re.S)
            temTwo = re.compile(r"(.*)</ar>", re.I | re.S)
            b = 1
            text = ''
            for s in data:
                s = s.decode("utf-8", "ignore")
                if b == 0 and temOne.search(s):
                    text = "".join(temOne.findall(s))
                    b = 1
                elif b==1 and temTwo.search(s) :
                    textTwo = "".join(temTwo.findall(s))
                    dict = Dict()
                    dict.rush = text
                    dict.englishWord = textTwo
                    dict.save()
                    b = 0
            return redirect("/")
    except OSError as exc:
        if exc.errno == 36:
            return HttpResponse('None')
        else:
            raise  # re-raise previously caught exceptions