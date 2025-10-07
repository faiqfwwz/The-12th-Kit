from django.urls import path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),

    path('product/add-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('product/<uuid:product_id>/edit-ajax/', edit_product_entry_ajax, name='edit_product_entry_ajax'),
    path('product/<uuid:product_id>/delete-ajax/', delete_product_entry_ajax, name='delete_product_entry_ajax'),

    path('product/<uuid:id>/', show_product, name='show_product'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register_ajax, name='register'),
    path('login/', login_ajax, name='login'),
    path('logout/', logout_ajax, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
]
