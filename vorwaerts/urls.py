from django.urls import path

from vorwaerts.views import PageListView
from vorwaerts.views import PageDetailView

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail')
]
