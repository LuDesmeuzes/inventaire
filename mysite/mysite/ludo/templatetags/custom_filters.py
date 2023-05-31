from django import template

register = template.Library()

@register.filter
def inventaire_split(station):
    return station.inventaire.split('\n')