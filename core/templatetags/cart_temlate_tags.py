from django import template
from core.models import Category

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Category.objects.filter(user=user)
        if qs.exists():
            return qs[0].items.count()
        return 0
