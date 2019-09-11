from django import template

register = template.Library()

@register.filter
def who_is_my_followed(user, my_followed):
    if user.username in my_followed:
        return True
    return False