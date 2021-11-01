from django.urls import path
from django.views.generic.base import TemplateView  # import TemplateView

from vorwaerts.views import PageDetailView
from vorwaerts.views import PageListView


urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
