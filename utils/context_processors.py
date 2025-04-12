from products.models import ParrentCategory, Category

def category_context(request):
    parent_obj = ParrentCategory.objects.all()
    category_obj = Category.objects.all()
    return {
        'parent_category_list': parent_obj,
        'category_list': category_obj,
    }