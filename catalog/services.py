from catalog.models import Product
from config.settings import CASHE_ENABLED
from django.core.cache import cache


def get_products_from_cache():
    if not CASHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
      return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
