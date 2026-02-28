from .models import Category, Advertising

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def advertising_processor(request):
    adverts = Advertising.objects.all()[:6]
    return {'adverts': adverts}
