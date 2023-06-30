from doctest import debug_script
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Listing, Bid, Comment, Watchlist


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings,  
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='login')
def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        starting_bid = request.POST["starting_bid"]
        category = request.POST["category"]
        url = request.POST["url"]
        description = request.POST["description"]
        seller = request.user
        if not title or not starting_bid or not description:
            return render(request, "auctions/createlistings.html", {
                "message": "Title, starting bid and descripton are required"
            })
        else:
            listing = Listing(title = title, starting_bid = starting_bid, category = category, url = url, description = description, seller = seller)
            listing.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/createlistings.html")

@login_required(login_url='login')
def listing(request, listing_id):
    uname = request.user
    listing = Listing.objects.get(id=listing_id)
    comment = Comment.objects.filter(item=listing)
    x=listing_id
    print(request)
    try:
        watch = Watchlist.objects.get(item=listing,username=uname)
    except ObjectDoesNotExist:
        watch = False
        
    try:
        bids = Bid.objects.get(bid_item=listing_id)
    except ObjectDoesNotExist:
        bids = None

    if request.method == "GET":
        if listing.active == False:
            message = "The auction has ended."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "message":message,
            "bids":bids,
            "username":uname,
            "comment":comment,
            "watch":watch,
            
        })
        else:
            return render(request, "auctions/listings.html", {
                "list":listing,
                "bids":bids,
                "username":uname,
                "comment":comment,
                "watch":watch,
                
            })
    else:
        try:
            bid = int(request.POST["bid"])
        except ValueError:
            bid = 0 
        
        if not bid or bid < listing.starting_bid:
            message = "Bid must be higher or equal starting bid."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "message":message,
            "bids":bids,
            "username":uname,
            "comment":comment,
            "watch":watch,
        })
        elif not bids and (bid >= listing.starting_bid):
            bids = Bid(actual_bid = bid, winner = request.user, bid_item = listing)
            bids.save()
            Listing.objects.filter(id=x).update(actual_price = bid)
            print("test")
            message = "Bid has been placed successfully."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "message":message,
            "bids":bids,
            "username":uname,
            "comment":comment,
            "watch":watch,
        })
        elif bids and (bid <= bids.actual_bid):
            message = "Bid must be higher."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "message":message,
            "bids":bids,
            "username":uname,
            "comment":comment,
            "watch":watch,
        })
        else:
            bids.actual_bid = bid
            bids.winner = request.user
            Listing.objects.filter(id=x).update(actual_price = bid)
            #bids.save()
            Bid.objects.filter(bid_item=listing).update(actual_bid=bid, winner=bids.winner)
            message = "Bid has been placed successfully."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "message":message,
            "bids":bids,
            "username":uname,
            "comment":comment,
            "watch":watch,
        })
        
def closed(request, listing_id):
    x=listing_id
    uname = request.user
    listing = Listing.objects.get(id=listing_id)
    try:
        comment = Comment.objects.filter(item=listing)
        bids = Bid.objects.get(bid_item=listing_id)
    except ObjectDoesNotExist:
        Listing.objects.filter(id=listing_id).update(active = False)
        listing = Listing.objects.get(id=listing_id)
        message = "The auction has ended."
        return HttpResponseRedirect(reverse("list", args=(listing_id,)))
    comment = Comment.objects.filter(item=listing)
    watch = Watchlist.objects.get(item=listing,username=uname)
    x=listing_id
    uname = request.user
    if request.method == "GET":
        if listing.active == False:
            if bids.winner == uname:
                message = "Congratulations, You won this auction!"
            else:
                message = "The auction has ended."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "message":message,
            "username":uname,
            "bids":bids,
            "comment":comment,
            "watch":watch,
        })
    else:
        if request.POST["act"]:
            Listing.objects.filter(id=x).update(active = False)
            listing = Listing.objects.get(id=listing_id)
            if bids.winner == uname:
                message = "Congratulations, You won this auction!"
            else:
                message = "The auction has ended."
            return render(request, "auctions/listings.html", {
            "list":listing,
            "username":uname,
            "message":message,
            "bids":bids,
            "comment":comment,
            "watch":watch,
            })


def comment(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    uname = request.user
    if request.POST["comm"]:
            comm = Comment(com=request.POST["comm"], item=listing, username=uname)
            comm.save()
            listing = Listing.objects.get(id=listing_id)
            return HttpResponseRedirect(reverse("list", args=(listing_id,)))
    else:
         return HttpResponseRedirect(reverse("list", args=(listing_id,)))


def watch(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    uname = request.user
    watch = Watchlist.objects.filter(item=listing,username=uname)
    if request.POST["watch"] == "Watch":
        if len(watch) == 0:
            watch = Watchlist(watched=True, item=listing, username=uname)
            watch.save()
        else:
            Watchlist.objects.filter(item=listing, username=uname).update(watched = True)
    else:
        Watchlist.objects.filter(item=listing, username=uname).update(watched = False)
    
    listing = Listing.objects.get(id=listing_id)
    return HttpResponseRedirect(reverse("list", args=(listing_id,)))

@login_required(login_url='login')
def listwatch(request):
    uname = request.user
    watch = Watchlist.objects.filter(username=uname)
    listing = Listing.objects.all()
    return render(request, "auctions/watched.html", {
        "watch": watch,  
        "listings":listing,
        "uname":uname,
    })
@login_required(login_url='login')
def categories(request):
    cats = Listing.objects.order_by('category')[:]
    catset = set()
    for cat in cats:
        try:
            catset.add(cat.category)
        except AttributeError:
            pass
    catset = sorted(catset)
    return render(request, "auctions/categories.html", { 
        "listings":listing,
        "cats":cats,
        "catset":catset
    })

@login_required(login_url='login')
def categorylist(request, category):
    listing = Listing.objects.filter(category=category, active=True)
    if len(listing) == 0:
        message = "No active listings in this category"
    else:
        message = ""
    return render(request, "auctions/categorylisting.html", { 
        "listings":listing,
        "message":message,
        "category":category
    })