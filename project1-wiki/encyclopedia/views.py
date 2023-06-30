from logging import PlaceHolder
from re import search
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import markdown2
from django import forms
from django.urls import reverse
from . import util
from random import randint

class SearchForm(forms.Form):
    search = forms.CharField(label='', required=False, widget=forms.TextInput({ "placeholder": "Search Encyclopedia"}))

class AddForm(forms.Form):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'name':'title', 'style':"width:40vw; height:40px;"}))
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'name':'content', 'style':"width:80vw; height:60vh;" }))

def index(request):
    search = SearchForm(request.POST)
    return render(request, "encyclopedia/index.html", {
        
        "entries": util.list_entries(),
        "form": search
    })


def title(request, name):
    search = SearchForm(request.POST)
    if name in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "name": name,
            "entry":  markdown2.markdown(util.get_entry(name)),
            "form": search
        })
    else:
        search = SearchForm(request.POST)
        return render(request, "encyclopedia/error.html", {
            "form": search,
            "name": name
        })



def searc(request):
    if request.method == "POST":
        search = SearchForm(request.POST)
        if search.is_valid():
            x = request.POST.get("search")
            #print(x)
            l = []
            for i in util.list_entries():
                if x in i:
                    l.append(i)
            
            #print(request.POST.get("search")
            #print(l)
            if len(l) != 0 and l[0] == x:
                
                #return title(request, l[0])
                return HttpResponseRedirect(f"wiki/{x}")
               
            else:
                return render(request, "encyclopedia/search.html",{
                    "form": search,
                    "entries": l
                })
        else:
            return render(request, "encyclopedia/search.html", {
                "form": search
            })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    search = SearchForm(request.POST)
    add = AddForm(request.POST)
    if request.method == "POST":
        if add.is_valid():
            x = request.POST.get("title")
            t = request.POST.get("content")
            if x in util.list_entries():
                return render(request, "encyclopedia/addpage.html",{
                    "title":x,
                    "form": search,
                    "add": AddForm()
                })
            else:
                util.save_entry(x, t)
                return HttpResponseRedirect(f"wiki/{x}")
                
    else:
        return render(request, "encyclopedia/addpage.html",{
            "form": search,
            "add": add
        })


def edit(request, name):
    search = SearchForm(request.POST)
    cont = util.get_entry(name)
    if name in util.list_entries():
        if request.method == "POST":
            x = request.POST.get("edd")
            print(x)
            util.save_entry(name, x)
            return HttpResponseRedirect(f"/wiki/{name}")
        else:
            return render(request, "encyclopedia/edit.html",{
                "cont":cont,
                "name":name,
                "form": search,
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "form": search,
            "name": name
        })
def random(request):
    x = util.list_entries()
    i = randint(0, (len(x)-1))
    x = x[i]
    return HttpResponseRedirect(f"/wiki/{x}")