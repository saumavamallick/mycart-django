#takes request as a argument and returns dictionary
#context processors are available for each template regardless
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
