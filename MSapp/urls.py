from django.urls import re_path

from . import views

urlpatterns = [
        re_path(

        r'^analytical_review_detail_raw/(?P<aid>\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b)/$',

        #MSapp.
        views.analytical_review_detail_raw, name='analytical_review_detail_raw'),

]
