from .CommonSelectors import css, partial_link, link_text


class MainPage:
    class menu:
        class desktops:
            link = (link_text, "Desktops")
            show_all = (partial_link, "Show All Desktops")

    promoblock = "#slideshow0"
    nav_links = "ul.nav > li"
