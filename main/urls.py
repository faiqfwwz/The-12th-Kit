from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_slug, show_json_by_slug, add_employee

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('add_employee/', add_employee, name="add_employee"),
    path('product/<slug:slug>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<slug:slug>/', show_xml_by_slug, name='show_xml_by_slug'),
    path('json/<slug:slug>/', show_json_by_slug, name='show_json_by_slug'),
]