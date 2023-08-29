import flet as ft

def main(page: ft.Page):
                    page.add(
                        ft.Row([
                            ft.Column(
                                [ft.Container(ft.Text(f"{i}")) for i in range(3)], height=500, alignment=ft.MainAxisAlignment.START
                                ),
                            ft.Container(ft.Text("Game field"), width=500, height=500, bgcolor=ft.colors.TEAL,
                                        alignment=ft.alignment.center),
                            ft.Column([ft.Container(ft.Text(f"{i}")) for i in range(3)], height=500, alignment=ft.MainAxisAlignment.END
                                    )
                                    
                        ])
                        
                    )

ft.app(main, "Layout example")
