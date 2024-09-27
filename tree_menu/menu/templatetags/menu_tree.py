from django import template
from django.shortcuts import get_object_or_404
from django.utils.html import format_html

from menu.models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(current_menu: str):
    """Рендеринг меню."""
    menu = get_object_or_404(
        Menu.objects.select_related("parent"),
        slug=current_menu,
    )
    return render_menu(menu)


def render_menu(menu: Menu) -> str:
    """Рендеринг меню с учётом выделенного элемента и вложенных пунктов."""
    selected_class = {menu.id: "selected"}
    nested_menu = {}
    while menu:
        children = menu.children.all()
        submenu = build_submenu(children, nested_menu, selected_class)
        nested_menu = {menu.id: submenu}
        list_item = build_menu_item(menu, nested_menu, selected_class)
        menu = menu.parent
    return format_html("<ul>{}</ul>", list_item)


def build_submenu(children, nested_menu, selected_class):
    """Создание подменю для пунктов меню."""
    menu_items = []
    for child in children:
        list_item = build_menu_item(child, nested_menu, selected_class)
        menu_items.append(list_item)
    return format_html("<ul>{}</ul>", format_html("".join(menu_items)))


def build_menu_item(menu: Menu, nested_menu: dict, selected_class: dict):
    """Создание элемента списка меню с учётом вложенности и выделения."""
    template = "<li><a class='{}' href='{}'>{}</a>{}</li>"
    url = menu.get_absolute_url()
    css_class = selected_class.get(menu.id, "unselected")
    nested_content = nested_menu.get(menu.id, "")
    return format_html(template, css_class, url, menu.name, nested_content)
