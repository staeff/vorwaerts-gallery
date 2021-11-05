from random import randint

from django import template


register = template.Library()

### FILTERS ###
# .. your filters go here..

### TAGS ###
@register.simple_tag
def random_pk():
    return randint(1, 12281)
