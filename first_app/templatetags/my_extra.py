from django import template


register = template.Library()


def cut(val, arg):
    return val.replace(arg, '')

register.filter('cut',cut)
