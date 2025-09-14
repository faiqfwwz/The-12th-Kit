from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product, Employee
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()
    context = {
        'npm' : '2406397706',
        'name': 'Ahmad Faiq Fawwaz Abdussalam',
        'class': 'PBP C',
        'product_list': product_list
    }

    return render(request, "main.html", context)

def add_employee(request):
    new_employee = Employee.objects.create(name="Budi",age=25,persona="Pacil 26")
    context = {
        'new_employee' : new_employee
    }
    return render(request, "add_employee.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

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
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_slug(request, slug):
    product = get_object_or_404(Product, slug=slug)
    xml_data = serializers.serialize("xml", [product])
    return HttpResponse(xml_data, content_type="application/xml")
   
def show_json_by_slug(request, slug):
    product = get_object_or_404(Product, slug=slug)
    json_data = serializers.serialize("json", [product])
    return HttpResponse(json_data, content_type="application/json")