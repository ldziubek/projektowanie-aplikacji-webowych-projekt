from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome", views.welcome_view),
    path("categories", views.category_list),
    path("categories/<int:id>", views.category_detail),
    path("topics", views.topic_list),
    path("topics/<int:id>", views.topic_detail),
    path("tags", views.tag_list),
    path("tags/<int:id>", views.tag_detail),
    path("posts", views.post_list),
    path("posts/<int:id>", views.post_detail),
    path("pages", views.page_list),
    path("pages/<int:id>", views.page_detail),
]