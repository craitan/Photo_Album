from django.shortcuts import render
from django.views import generic as views

from Photo_Album.common.forms import ContactUsForm
from Photo_Album.common.models import ContactUs


class HomePageView(views.TemplateView):
    template_name = 'common/home-page.html'


class ContactView(views.FormView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'common/contact-us.html'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'common/contact-submitted.html')
