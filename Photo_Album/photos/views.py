from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from Photo_Album.photos.forms import AddPhotoForm, EditPhotoForm
from Photo_Album.photos.models import Photo


class PhotoGalleryView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['photos'] = Photo.objects.filter(user=user)
        return context


class PhotoAddView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Photo
    form_class = AddPhotoForm
    template_name = 'photos/add-photo-page.html'

    # TODO: HAVE TO figure a way to add the categories
    def get_context_data(self, **kwargs):
        pass

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()

        return super(PhotoAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home page')


class PhotoView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'photos/photo-view.html'
    model = Photo


class PhotoEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'photos/edit-photo-page.html'
    model = Photo
    form_class = EditPhotoForm

    def get_success_url(self):
        return reverse_lazy('home page')


class PhotoDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'photos/delete-photo-page.html'
    model = Photo
    success_url = reverse_lazy('home page')
