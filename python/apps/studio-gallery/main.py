import flet as ft
import counter, to_do, calculator, drawing_tool, buttons, entry_form, charts, flet_animation, audio_player


class AppTile(ft.ListTile):
    def __init__(self, name, view, icon_name, file_name):
        super().__init__()
        self.view = view
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.title = ft.Text(name)
        self.leading = ft.Icon(icon_name)
        self.on_click = self.app_button_clicked
        self.name = name
        self.file_name = file_name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(
                        title=ft.Text(f"{e.control.name}"),
                        actions=[
                            ft.IconButton(
                                content=ft.Image(
                                    src="github-mark.svg", width=24, height=24
                                ),
                                url=f"https://github.com/flet-dev/examples/tree/main/python/apps/studio-gallery/{self.file_name}",
                                url_target="_blank",
                            )
                        ],
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    page.add(
        ft.ListView(
            controls=[
                AppTile(
                    name="Counter",
                    file_name="counter.py",
                    view=counter.example(),
                    icon_name=ft.icons.ADD,
                ),
                AppTile(
                    name="To-Do",
                    file_name="to_do.py",
                    view=to_do.example(),
                    icon_name=ft.icons.CHECK_BOX_OUTLINED,
                ),
                AppTile(
                    name="Calculator",
                    file_name="calculator.py",
                    view=calculator.example(),
                    icon_name=ft.icons.CALCULATE_OUTLINED,
                ),
                AppTile(
                    name="Drawing Tool",
                    file_name="drawing_tool.py",
                    view=drawing_tool.example(),
                    icon_name=ft.icons.DRAW_OUTLINED,
                ),
                AppTile(
                    name="Buttons",
                    file_name="buttons.py",
                    view=buttons.example(),
                    icon_name=ft.icons.SMART_BUTTON_OUTLINED,
                ),
                AppTile(
                    name="Entry Form",
                    file_name="entry_form.py",
                    view=entry_form.example(),
                    icon_name=ft.icons.LOGIN,
                ),
                AppTile(
                    name="Charts",
                    file_name="charts.py",
                    view=charts.example(),
                    icon_name=ft.icons.INSERT_CHART_OUTLINED,
                ),
                AppTile(
                    name="Flet Animation",
                    file_name="flet_animation.py",
                    view=flet_animation.example(page=page),
                    icon_name=ft.icons.ANIMATION,
                ),
                AppTile(
                    name="Audio Player",
                    file_name="audio_player.py",
                    view=audio_player.example(),
                    icon_name=ft.icons.AUDIOTRACK,
                ),
            ]
        )
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.window_width = 390
    page.window_height = 844
    page.update()


ft.app(target=main, assets_dir="assets")
