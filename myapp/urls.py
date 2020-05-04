from django.conf.urls import url
from myapp import views

urlpatterns = [

    url(r'^profiles/$', views.ProfileApiCreateRead.as_view({
        "get": "get_all_user_details"}), name='get_profiles'),
  ]
