from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts off all value of args from the String
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
