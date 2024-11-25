import flet as ft


def main(page: ft.Page) -> None:
    def add_clicked(e):
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        view.update()

    new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
    tasks_view = ft.Column()
    view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

if __name__ == '__main__':
    ft.app(main)
    