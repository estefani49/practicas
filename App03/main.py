import flet as ft


def main(page: ft.Page):
    page.title="App03"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="grey"
    
    lbl1=ft.Text("",
                style=ft.TextStyle(size=40,weight="bold"))
    
    def calcular_suma(txt_num1,txt_num2,txt_resultado):
        try:
            num1=float(txt_num1.value.strip())
            num2=float(txt_num2.value.strip())
            resultado= num1 + num2
            txt_resultado.value= f"Resultado{resultado}"
        except ValueError:
            txt_resultado.value="Error: ingresa valores correctos"
            
    Img1=ft.Image(src="shinobu.png", width=300,height=300)
    
    
    btnSi=ft.ElevatedButton("Sumar",
                            color="green",
                            width=110,
                            height=50)
    
    btnNo=ft.ElevatedButton("Limpiar",
                            color="red",
                            width=110,
                            height=50)
    
        
    def limpiar(e):
        txt_num1.value = ""
        txt_num2.value = ""
        txt_resultado.value = "Resultado: "
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