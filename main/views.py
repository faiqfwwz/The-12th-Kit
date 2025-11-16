import json
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
import requests
from django.utils.html import strip_tags

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406397706',
        'name': request.user.username,
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'product' : product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'is_featured': p.is_featured,
            'stock': p.stock,
            'brand': p.brand,
            'league': p.league,
            'team': p.team,
            'season': p.season,
            'user_id': p.user_id,
        }
        for p in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        p = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            
            'is_featured': p.is_featured,
            'stock': p.stock,
            'brand': p.brand,
            'league': p.league,
            'team': p.team,
            'season': p.season,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def _is_ajax(request):
    # anggap request AJAX bila ada X-Requested-With atau minta JSON
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest' \
        or 'application/json' in request.headers.get('Accept', '')

@csrf_protect
def login_ajax(request):
    if request.method == 'GET':
        # render halaman login
        return render(request, 'login.html')

    if request.method != 'POST':
        return HttpResponseNotAllowed(['GET', 'POST'])

    if not _is_ajax(request):
        return JsonResponse({'ok': False, 'errors': {'__all__': ['AJAX required']}}, status=400)

    data = json.loads(request.body or '{}')
    username = data.get('username', '')
    password = data.get('password', '')
    user = authenticate(request, username=username, password=password)
    if not user:
        return JsonResponse({'ok': False, 'errors': {'__all__': ['Invalid credentials']}}, status=400)

    login(request, user)
    return JsonResponse({'ok': True})


@csrf_protect
def register_ajax(request):
    if request.method == 'GET':
        # render halaman register
        return render(request, 'register.html')

    if request.method != 'POST':
        return HttpResponseNotAllowed(['GET', 'POST'])

    if not _is_ajax(request):
        return JsonResponse({'ok': False, 'errors': {'__all__': ['AJAX required']}}, status=400)

    data = json.loads(request.body or '{}')
    u  = (data.get('username') or '').strip()
    p1 = data.get('password1') or ''
    p2 = data.get('password2') or ''

    errs = {}
    if not u:  errs.setdefault('username', []).append('Required')
    if not p1: errs.setdefault('password1', []).append('Required')
    if p1 != p2: errs.setdefault('password2', []).append('Passwords do not match')
    if User.objects.filter(username=u).exists():
        errs.setdefault('username', []).append('Already taken')

    if errs:
        return JsonResponse({'ok': False, 'errors': errs}, status=400)

    User.objects.create_user(username=u, password=p1)
    return JsonResponse({'ok': True})

@csrf_protect
def logout_ajax(request):
    if request.method != 'POST' or not _is_ajax(request):
        return JsonResponse({'ok': False, 'errors': {'__all__': ['Method not allowed']}}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'errors': {'__all__': ['Not logged in']}}, status=400)

    logout(request)
    return JsonResponse({'ok': True}, status=200)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

VALID_CATEGORIES = {
    "club_home","club_away","club_third","club_gk","club_special",
    "national_home","national_away","national_third","national_gk","national_special",
    "retro","limited",
}

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        d = request.POST
        name        = (d.get("name") or "").strip()
        price_raw   = d.get("price") or "0"
        description = d.get("description") or ""
        thumbnail   = d.get("thumbnail") or ""
        category    = d.get("category") or "club_home"
        is_featured = (d.get("is_featured") in ["on","true","1","yes"])
        stock_raw   = d.get("stock") or "0"
        brand       = d.get("brand") or ""
        league      = d.get("league") or ""
        team        = d.get("team") or ""
        season      = d.get("season") or ""
        user        = request.user if request.user.is_authenticated else None

        if not name:
            return JsonResponse({"ok": False, "errors": {"name": ["This field is required."]}}, status=400)

        try:
            price = int(price_raw)
            stock = int(stock_raw)
        except ValueError:
            return JsonResponse({"ok": False, "errors": {"price/stock": ["Must be integers."]}}, status=400)

        if category not in VALID_CATEGORIES:
            return JsonResponse({"ok": False, "errors": {"category": ["Invalid category."]}}, status=400)

        p = Product.objects.create(
            user=user, name=name, price=price, description=description,
            thumbnail=thumbnail, category=category, is_featured=is_featured,
            stock=stock, brand=brand, league=league, team=team, season=season
        )
        return JsonResponse({"ok": True, "id": str(p.id)}, status=201)

    except Exception as e:
        return JsonResponse({"ok": False, "errors": {"__all__": [str(e)]}}, status=500)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product.user_id and request.user.is_authenticated and product.user_id != request.user.id:
        return HttpResponseForbidden(b"FORBIDDEN")

    name        = request.POST.get("name")
    price       = request.POST.get("price") or "0"
    description = request.POST.get("description") or ""
    thumbnail   = request.POST.get("thumbnail") or ""
    category    = request.POST.get("category") or product.category
    is_featured = (request.POST.get("is_featured") == "on")
    stock       = request.POST.get("stock") or "0"
    brand       = request.POST.get("brand") or ""
    league      = request.POST.get("league") or ""
    team        = request.POST.get("team") or ""
    season      = request.POST.get("season") or ""

    if not name:
        return HttpResponseBadRequest(b"NAME_REQUIRED")
    try:
        price = int(price); stock = int(stock)
    except ValueError:
        return HttpResponseBadRequest(b"INVALID_NUMBER")

    product.name        = name
    product.price       = price
    product.description = description
    product.thumbnail   = thumbnail
    product.category    = category
    product.is_featured = is_featured
    product.stock       = stock
    product.brand       = brand
    product.league      = league
    product.team        = team
    product.season      = season
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_entry_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if product.user_id and request.user.is_authenticated and product.user_id != request.user.id:
        return HttpResponseForbidden(b"FORBIDDEN")
    product.delete()
    return HttpResponse(b"DELETED", status=200)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({"status": "error", "message": "User not authenticated"}, status=401)

        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        thumbnail = data.get("thumbnail", "") or ""
        category = data.get("category", "club_home")
        is_featured = data.get("is_featured", False)
        brand = strip_tags(data.get("brand", ""))
        league = strip_tags(data.get("league", ""))
        team = strip_tags(data.get("team", ""))
        season = strip_tags(data.get("season", ""))

        try:
            price = int(data.get("price", 0))
            stock = int(data.get("stock", 0))
        except ValueError:
            return JsonResponse({"status": "error", "message": "Price and stock must be numbers"}, status=400)

        if not name:
            return JsonResponse({"status": "error", "message": "Name is required"}, status=400)

        if price < 0:
            return JsonResponse({"status": "error", "message": "Price cannot be negative"}, status=400)

        if stock < 0:
            return JsonResponse({"status": "error", "message": "Stock cannot be negative"}, status=400)

        product = Product(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            stock=stock,
            brand=brand,
            league=league,
            team=team,
            season=season,
            user=request.user,
        )
        product.save()

        return JsonResponse({"status": "success", "message": "Product created"}, status=200)

    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)
