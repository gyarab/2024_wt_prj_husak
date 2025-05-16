from django import template

register = template.Library()

@register.filter
def smart_truncate(value, max_length=100):
    if not isinstance(value, str):
        return value
    if len(value) <= max_length:
        return value

    truncated = value[:max_length].rstrip()

    for i in reversed(range(len(truncated))):
        if not truncated[i].isalnum():
            return truncated[:i+1].rstrip() + ' ...'
        
    return truncated + ' ...'