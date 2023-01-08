from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from Photo_Album.photos.forms import EditPhotoForm
from Photo_Album.photos.models import Photo, Category


class PhotoGalleryView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'photos/user-gallery-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        category = self.request.GET.get('category')
        if category == None:
            context['photos'] = Photo.objects.filter(user=user)
        else:
            context['photos'] = Photo.objects.filter(category__name=category, category__user=user)

        context['categories'] = Category.objects.filter(user=user)
        return context


def add_photo(request):
    user = request.user
    categories = Category.objects.filter(user=user)

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                user=user,
                description=data['description'],
                image=image,
            )

        return redirect('photo gallery')

    context = {
        'categories': categories,
    }
    return render(request, 'photos/add-photo-page.html', context)


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
    success_url = reverse_lazy('photo gallery')
