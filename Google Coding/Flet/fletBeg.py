import flet as ft

def page (page: ft.Page):
    page.window_height = 500
    page.window_width = 500
    page.window_center()
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greeetings = ft.Ref[ft.Column]()

    def sending_greet(e):
        greeetings.current.controls.append(ft.Text(f"Hello! {first_name.current.value} {last_name.current.value}", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.JUSTIFY))
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()
    
    page.add(
        ft.Column([
        ft.TextField(ref=first_name, label= "Firstname", autofocus=True),
        ft.TextField(ref=last_name, label= "Lastname"),
        ft.ElevatedButton("say hello!", on_click=sending_greet)
        ],height=400, alignment=ft.MainAxisAlignment.END
        ),
        ft.Column(ref=greeetings),
    )

ft.app(target=page)