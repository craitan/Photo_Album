from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views

from Photo_Album.common.forms import ContactUsForm
from Photo_Album.common.models import ContactUs
from Photo_Album.photos.models import Photo


class HomePageView(views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = Photo.objects.all()
        page = self.request.GET.get('page')
        context['photos'] = Paginator(photos, 3).get_page(page)

        return context


class ContactView(views.FormView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'common/contact-us.html'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'common/contact-submitted.html')
