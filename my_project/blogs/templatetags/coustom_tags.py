from django import template

register=template.Library()

@register.simple_tag

def get_half_contant(description):
    return description[:int(len(description)/2)]
    """total=len(description)
    half=total/2
    half=int(half)
    return description[:half]"""
"""
def get_next_half(complete_post):
    return """