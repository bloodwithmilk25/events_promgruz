from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.shortcuts import render

from datetime import datetime
from .models import Event, Location


class UpcomingEventsView(ListView):
    template_name = 'events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.published(date_end__gte=datetime.today()).order_by('date_start')


class PastEventsView(TemplateView):
    queryset = Event.objects.published(date_end__lt=datetime.today()).order_by('-date_start')
    template_name = 'events.html'
    items_on_page = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_list = self.queryset
        paginator = Paginator(event_list, self.items_on_page)
        page = self.request.GET.get('page', 1)

        if self.request.is_ajax():
            query = self.request.GET.get('page')
            if query is not None:
                page = query
        try:
            events = paginator.get_page(page)
        except (EmptyPage, InvalidPage):
            events = paginator.page(paginator.num_pages)
        context['events'] = events
        context['page'] = page
        return context


class ArchiveEventsView(PastEventsView):
    template_name = 'search_archive_results.html'
    items_on_page = 10


class EventDetailView(DetailView):
    model = Event


class LocationDetailView(DetailView):
    model = Location


def search(request):
    event_list = Event.objects.published().order_by('-date_start')
    q = request.GET.get("q")
    if q:
        q = q.lower()  # uppercase the first letter of query
        event_list = event_list.filter(name__icontains=q) | event_list.filter(name__icontains=q.title())

    if len(event_list) == 0:
        return render(request, 'search_archive_results.html', {'message': "Поиск не дал результатов"})

    paginator = Paginator(event_list, 6)

    page = request.GET.get('page', 1)
    events = paginator.get_page(page)
    return render(request, 'search_archive_results.html', {'events': events})
