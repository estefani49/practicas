import flet as ft


def main(page: ft.Page):
    page.title="App03"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="grey"
    
    lbl1=ft.Text("",
                style=ft.TextStyle(size=40,weight="bold"))
    
    Img1=ft.Image(src="shinobu.png", width=300,height=300)
    
    
    btnSi=ft.ElevatedButton("Sumar",
                            color="green",
                            width=110,
                            height=50)
    
    btnNo=ft.ElevatedButton("Limpiar",
                            color="red",
                            width=110,
                            height=50)
    
    def no(e):
    

        page.update()
        
    def si(e):
        Img1.src="shinobu.png"
        page.update()
        
    btnSi.on_click=si
    btnNo.on_click=no
    
    
    
    page.add(
        ft.Column(
            [
                lbl1,
                Img1,
                ft.Row([btnSi,btnNo],
                        alignment=ft.MainAxisAlignment.CENTER,
                        )
            ],
            
            
        )
    )
    
ft.app(main)