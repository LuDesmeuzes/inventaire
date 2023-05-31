from django import template

register = template.Library()

@register.filter
def inventaire_split(station):
    if  "inventaire" in station._meta.get_fields():
        return station.inventaire.split('\n')
    else:
        return []