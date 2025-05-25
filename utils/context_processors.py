from django.shortcuts import get_object_or_404

from products.models import ParentCategory, Category, Product


def category_context(request):
    parent_obj = ParentCategory.objects.all()
    category_obj = Category.objects.all()
    return {
        'parent_category_list': parent_obj,
        'category_list': category_obj,
    }


def cart_context(request):
        if "cart" in request.session:
            return {"cart_products": request.session['cart']}

        return {}


