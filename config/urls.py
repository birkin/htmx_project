from django.contrib import admin
from django.urls import path
from htmx_app import views


urlpatterns = [
    ## main ---------------------------------------------------------
    path( 'htmx_examples/', views.htmx_examples, name='htmx_examples_url' ),

    ## support fragments --------------------------------------------
    path( 'htmx_f__new_content/', views.htmx_f__new_content, name='htmx_f__new_content_url' ),
    
    path( 'htmx_f__form_handler/', views.htmx_f__form_handler, name='htmx_f__form_handler_url' ),
    path( 'htmx_f__example_7_invalid/', views.htmx_f__example_7_invalid, name='htmx_f__example_7_invalid_url' ),
    path( 'htmx_f__example_7_success/', views.htmx_f__example_7_success, name='htmx_f__example_7_success_url' ),

    ## other --------------------------------------------------------
    path( '', views.root, name='root_url' ),
    path( 'admin/', admin.site.urls ),
    path( 'error_check/', views.error_check, name='error_check_url' ),
    path( 'version/', views.version, name='version_url' ),


]
