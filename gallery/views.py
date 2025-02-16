from django.shortcuts import render
from django.views.generic import ListView
from gallery.models import Gallery, ImageType
from utils import utils
def gallery_page(request):
    return render(request, 'gallery.html')

from django.views.generic import ListView
from django.db.models import Prefetch
from .models import Gallery, ImageType

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    paginate_by = 10
    context_object_name = 'gallery_list'

    def get_queryset(self):
        return Gallery.objects.prefetch_related('image_type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(utils.get_context())
        context['image_types'] = ImageType.objects.all()
        return context
