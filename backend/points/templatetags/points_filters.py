from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/
    """
    d = context["request"].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.inclusion_tag("link.html", takes_context=True)
def jump_link(context):
    return {
        "link": context["home_link"],
        "title": context["home_title"],
    }
