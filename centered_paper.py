# ============================================================
# Autor: kamowski & AI
# Názov: centered_paper
# Verzia: 26.09.2026–07:20
# SPDX-License-Identifier: MIT
#
# Popis:
# Centered Paper – Xed plugin
#
# Jednoduchý plugin pre Xed 3.8.9, ktorý zmení editor na
# príjemnú „papierovú“ plochu uprostred obrazovky.
#
# Text je automaticky vystredený podľa šírky 80 znakov.
# Okolo bieleho listu zostáva jemné sivé pozadie.
# Obsah dokumentu sa nijako nemení.
#
# Vlastnosti:
# - biely papier uprostred okna
# - automatické centrovanie
# - jemné okraje
# - prispôsobenie pri zmene veľkosti okna a fontu
# - žiadne vkladanie medzier ani úprava obsahu dokumentu
#
# Testované na Xed 3.8.9 / GTK3 / GtkSourceView 4.
#
# Because sometimes you just want your text editor
# to look like a piece of paper. 😄
# ============================================================.

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("GtkSource", "4")
gi.require_version("Xed", "1.0")

from gi.repository import Gtk, GtkSource, GObject, Pango, Gdk, Xed


class CenteredPaperPlugin(GObject.Object, Xed.WindowActivatable):

    __gtype_name__ = "CenteredPaperPlugin"

    window = GObject.Property(type=Xed.Window)

    PAPER_COLUMNS = 80
    PAPER_PADDING = 20

    OUTER_COLOR = (0.91, 0.91, 0.91)
    BORDER_COLOR = (0.78, 0.78, 0.78)

    def __init__(self):
        super().__init__()

        self.enabled = False
        self.accel_group = None

        self.view = None

        self.old_left_margin = 0
        self.old_right_margin = 0

        self._size_handler = None
        self._font_handler = None
        self._draw_handler = None
        self._tab_handler = None

    # ---------------------------------------------------------
    # Aktivácia pluginu
    # ---------------------------------------------------------

    def do_activate(self):
        self._install_action()

        self._tab_handler = self.window.connect(
            "active-tab-changed",
            self._on_active_tab_changed
        )

    def do_deactivate(self):

        if self._tab_handler is not None:
            try:
                self.window.disconnect(
                    self._tab_handler
                )
            except Exception:
                pass

            self._tab_handler = None

        self._detach()

        if self.accel_group is not None:
            try:
                self.window.remove_accel_group(
                    self.accel_group
                )
            except Exception:
                pass

            self.accel_group = None

    # ---------------------------------------------------------
    # Klávesová skratka F10
    # ---------------------------------------------------------

    def _install_action(self):

        self.accel_group = Gtk.AccelGroup()

        self.accel_group.connect(
            Gdk.KEY_F10,
            0,
            Gtk.AccelFlags.VISIBLE,
            self._on_f10
        )

        self.window.add_accel_group(
            self.accel_group
        )

    def _on_f10(
        self,
        accel_group,
        acceleratable,
        keyval,
        modifier
    ):

        self.enabled = not self.enabled

        if self.enabled:
            self._attach_to_current_view()
        else:
            self._detach()

        return True

    # ---------------------------------------------------------
    # Aktuálny editor
    # ---------------------------------------------------------

    def _get_current_view(self):

        try:

            tab = self.window.get_active_tab()

            if tab is None:
                return None

            view = tab.get_view()

            if isinstance(view, GtkSource.View):
                return view

        except Exception:
            pass

        return None

    def _on_active_tab_changed(
        self,
        window,
        tab
    ):

        if not self.enabled:
            return

        self._detach()
        self._attach_to_current_view()

    # ---------------------------------------------------------
    # Pripojenie k editoru
    # ---------------------------------------------------------

    def _attach_to_current_view(self):

        if not self.enabled:
            return

        if self.view is not None:
            return

        view = self._get_current_view()

        if view is None:
            return

        self.view = view

        self.old_left_margin = (
            view.get_left_margin()
        )

        self.old_right_margin = (
            view.get_right_margin()
        )

        self._size_handler = view.connect(
            "size-allocate",
            self._on_size_allocate
        )

        self._font_handler = view.connect(
            "notify::font-desc",
            self._on_font_changed
        )

        # Dôležité:
        # Sivé okraje kreslíme AŽ PO vykreslení textu.
        self._draw_handler = view.connect_after(
            "draw",
            self._on_draw
        )

        self._update_layout()

    # ---------------------------------------------------------
    # Odpojenie od editora
    # ---------------------------------------------------------

    def _detach(self):

        if self.view is None:
            return

        try:

            if self._size_handler is not None:
                self.view.disconnect(
                    self._size_handler
                )

            if self._font_handler is not None:
                self.view.disconnect(
                    self._font_handler
                )

            if self._draw_handler is not None:
                self.view.disconnect(
                    self._draw_handler
                )

            # Obnovíme pôvodné nastavenia Xed.
            self.view.set_left_margin(
                self.old_left_margin
            )

            self.view.set_right_margin(
                self.old_right_margin
            )

            self.view.queue_draw()

        except Exception:
            pass

        self.view = None

        self._size_handler = None
        self._font_handler = None
        self._draw_handler = None

    # ---------------------------------------------------------
    # Výpočet šírky papiera
    # ---------------------------------------------------------

    def _get_paper_width(self):

        view = self.view

        if view is None:
            return 640

        try:

            context = view.get_pango_context()

            font = (
                view
                .get_style_context()
                .get_font(
                    Gtk.StateFlags.NORMAL
                )
            )

            layout = Pango.Layout.new(
                context
            )

            layout.set_font_description(
                font
            )

            # Šírka 80 znakov.
            layout.set_text(
                "M" * self.PAPER_COLUMNS,
                -1
            )

            width, _ = (
                layout.get_pixel_size()
            )

            return width

        except Exception:

            return 640

    # ---------------------------------------------------------
    # Rozloženie textu
    # ---------------------------------------------------------

    def _update_layout(self):

        if self.view is None:
            return

        allocation = (
            self.view.get_allocation()
        )

        viewport_width = allocation.width

        if viewport_width <= 0:
            return

        paper_width = (
            self._get_paper_width()
        )

        paper_width = min(
            paper_width,
            viewport_width
        )

        side = int(
            max(
                0,
                (
                    viewport_width
                    - paper_width
                ) / 2
            )
        )

        self.view.set_left_margin(
            side
        )

        self.view.set_right_margin(
            side + self.PAPER_PADDING
        )

        self.view.queue_draw()

    # ---------------------------------------------------------
    # Zmena veľkosti okna
    # ---------------------------------------------------------

    def _on_size_allocate(
        self,
        widget,
        allocation
    ):

        self._update_layout()

    # ---------------------------------------------------------
    # Zmena fontu
    # ---------------------------------------------------------

    def _on_font_changed(
        self,
        widget,
        pspec
    ):

        self._update_layout()

    # ---------------------------------------------------------
    # Sivé okraje
    # ---------------------------------------------------------

    def _on_draw(
        self,
        view,
        cr
    ):

        allocation = (
            view.get_allocation()
        )

        width = allocation.width
        height = allocation.height

        paper_width = (
            self._get_paper_width()
        )

        paper_width = min(
            paper_width,
            width
        )

        left = int(
            max(
                0,
                (
                    width
                    - paper_width
                ) / 2
            )
        )

        right = (
            left + paper_width
        )

        cr.save()

        # -----------------------------------------------------
        # Sivá plocha VĽAVO od papiera
        # -----------------------------------------------------

        cr.set_source_rgb(
            *self.OUTER_COLOR
        )

        cr.rectangle(
            0,
            0,
            left,
            height
        )

        cr.fill()

        # -----------------------------------------------------
        # Sivá plocha VPRAVO od papiera
        # -----------------------------------------------------

        cr.rectangle(
            right,
            0,
            width - right,
            height
        )

        cr.fill()

        # -----------------------------------------------------
        # Ľavý okraj papiera
        # -----------------------------------------------------

        cr.set_source_rgb(
            *self.BORDER_COLOR
        )

        cr.set_line_width(1)

        cr.move_to(
            left + 0.5,
            0
        )

        cr.line_to(
            left + 0.5,
            height
        )

        # -----------------------------------------------------
        # Pravý okraj papiera
        # -----------------------------------------------------

        cr.move_to(
            right - 0.5,
            0
        )

        cr.line_to(
            right - 0.5,
            height
        )

        cr.stroke()

        cr.restore()

        # Text už Xed vykreslil.
        return False

