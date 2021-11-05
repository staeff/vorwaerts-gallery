from django import template
from random import randint

register = template.Library()

### FILTERS ###
# .. your filters go here..

### TAGS ###
@register.simple_tag
def random_pk():
    return randint(1,12281)
