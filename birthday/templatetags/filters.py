from django import template
import jdatetime

register = template.Library()


@register.filter
def to_jalali(value):
    if not value:
        return ""

    try:
        jdate = jdatetime.datetime.fromgregorian(datetime=value)
        return jdate.strftime("%Y/%m/%d")
    except:
        return value
