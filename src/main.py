import flet as ft

def main(page: ft.Page):
    # Текст для отображения результата
    result = ft.Text(size=50)

    def button_click(e):
        result.value = e.control.text  # Получаем текст
        result.update()

    # Три кнопки
    btn1 = ft.ElevatedButton("1", on_click=button_click)
    btn2 = ft.ElevatedButton("2", on_click=button_click)
    btn3 = ft.ElevatedButton("3", on_click=button_click)

    # Расположение элементов
    page.add(
        ft.Container(result, alignment=ft.alignment.center, expand=True),
        ft.Row([btn1, btn2, btn3], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(main)