from django import template
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from menu.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(current_menu: str):
    menu = get_object_or_404(
        Menu.objects.select_related("parent"),
        slug=current_menu,
    )
    return render_menu(menu)


def render_menu(menu: Menu) -> str:
    selected_id = {menu.id: "selected"}
    insertion_menu = {}
    while menu:
        children = menu.children.all()
        items = building_list(children, insertion_menu)  # li's
        insertion_item = formatting_html(menu, items, selected_id)  # li_insert
        insertion_menu = {menu.id: insertion_item}
        menu = menu.parent
    return format_html("<ul>{}</ul>", insertion_item)


def building_list(queryset, insertion_menu: dict):
    items = []
    pattern = '<li><a href="{}">{}</a></li>'
    for item in queryset:
        url = item.get_absolute_url()
        text = insertion_menu.get(
            item.id, format_html(pattern, url, item.name)
        )
        items.append(text)
    return "".join(items)


def formatting_html(menu, text: str, selected_id: dict) -> str:
    pattern = "<li><a class='{}' href='{}'>{}</a><ul>{}</ul></li>"
    class_css = selected_id.get(menu.id, "unselected")
    url = menu.get_absolute_url()
    return format_html(pattern, class_css, url, menu.name, format_html(text))
