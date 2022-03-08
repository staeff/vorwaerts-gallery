from django.urls import include, path
from django.views.generic.base import TemplateView  # import TemplateView

from vorwaerts.views import AdDetailView
from vorwaerts.views import PageDetailView
from vorwaerts.views import PageListView
from vorwaerts.views import SearchResultsView
from vorwaerts.views import TextQualityView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('page/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('textqa/', TextQualityView.as_view(), name='text_quality'),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
