from django import template

register = template.Library()

@register.filter
def get_price(sequence, position):
    return sequence[position].price
