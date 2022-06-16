
from django.urls import path

from webapp.views import index_view, article_create_view


urlpatterns = [
    path('n/', article_create_view),
    # path('n/n/', index_view),
    # path('fr/', article_create_view)
]
