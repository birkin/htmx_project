from django.contrib import admin
from django.urls import path
from htmx_app import views


urlpatterns = [
    ## main ---------------------------------------------------------
    ## TODO

    ## other --------------------------------------------------------
    path( '', views.root, name='root_url' ),
    path( 'admin/', admin.site.urls ),
    path( 'error_check/', views.error_check, name='error_check_url' ),
    path( 'version/', views.version, name='version_url' ),

    ## htmx experimentation -----------------------------------------
    path( 'htmx_example/', views.htmx_example, name='htmx_example_url' ),
    path( 'htmx_f__new_content/', views.htmx_f__new_content, name='htmx_f__new_content_url' ),
    path( 'htmx_f__email_validator/', views.htmx_f__email_validator, name='htmx_f__email_validator_url' ),
    path( 'htmx_f__form_handler/', views.htmx_f__form_handler, name='htmx_f__form_handler_url' ),
    path( 'htmx_results/', views.htmx_results, name='htmx_results_url' ),

]
