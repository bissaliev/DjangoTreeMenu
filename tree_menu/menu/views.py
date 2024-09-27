from django.shortcuts import get_object_or_404, render

from .models import Menu


def index(request):
    """Главная страница."""
    menu_items = Menu.objects.filter(parent=None)
    title = "Главная страница"
    return render(
        request, "menu/index.html", {"menu_items": menu_items, "title": title}
    )


def menu(request, menu_slug):
    """Страница меню."""
    current_menu = get_object_or_404(Menu, slug=menu_slug)
    return render(request, "menu/menu.html", {"current_menu": current_menu})
