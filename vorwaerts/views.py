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

class SearchResultsView(ListView):
    model = ClassifiedAd
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = ClassifiedAd.objects.filter(text__icontains=query)
        return object_list

class TextQualityView(ListView):
    model = ClassifiedAd
    paginate_by = 300
    template_name = 'text_quality.html'
    ordering = ['-ocr_confidence']
