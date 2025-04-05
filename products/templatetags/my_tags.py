from django import template

register = template.Library()


@register.filter()
def products_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/products/image_not_found.png'
