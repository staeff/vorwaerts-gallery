from django.views.generic import DetailView
from django.views.generic import ListView

from vorwaerts.models import ClassifiedAd
from vorwaerts.models import NewspaperPage


class PageListView(ListView):
    model = NewspaperPage
    paginate_by = 6
    template_name = 'home.html'


class PageDetailView(DetailView):
    model = NewspaperPage
    template_name = 'page.html'


class AdDetailView(DetailView):
    model = ClassifiedAd
    template_name = 'ad.html'
