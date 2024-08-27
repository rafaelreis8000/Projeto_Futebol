import flet as ft

class FutebolVarzeaApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "FuteVale"
        self.page.window_width = 800
        self.page.bgcolor = '#214E34'
        
        # Lista de times e jogos
        self.times = []
        self.jogos = []
        
        # Interface para adicionar times
        self.label_time = ft.Text("Adicionar Time:")
        self.entry_time = ft.TextField()
        self.botao_adicionar_time = ft.ElevatedButton(
            text="Adicionar Time", on_click=self.adicionar_time)
        
        self.page.add(
            ft.Row(controls=[
                self.label_time,
                self.entry_time,
                self.botao_adicionar_time
            ])
        )
        
        # Interface para marcar jogos
        self.label_time1 = ft.Text("Time 1:")
        self.combo_time1 = ft.Dropdown(options=[], width=200)
        
        self.label_time2 = ft.Text("Time 2:")
        self.combo_time2 = ft.Dropdown(options=[], width=200)
        
        self.label_data = ft.Text("Data do Jogo:")
        self.entry_data = ft.TextField()
        
        self.botao_marcar_jogo = ft.ElevatedButton(
            text="Marcar Jogo", on_click=self.marcar_jogo)
        
        self.page.add(
            ft.Row(controls=[
                self.label_time1,
                self.combo_time1
            ]),
            ft.Row(controls=[
                self.label_time2,
                self.combo_time2
            ]),
            ft.Row(controls=[
                self.label_data,
                self.entry_data
            ]),
            self.botao_marcar_jogo
        )
        
        # Tabela de jogos
        self.label_jogos = ft.Text("Jogos Marcados:")
        self.tabela_jogos = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Time 1")),
                ft.DataColumn(ft.Text("Time 2")),
                ft.DataColumn(ft.Text("Data")),
            ],
            rows=[]
        )
        
        self.page.add(self.label_jogos, self.tabela_jogos)
    
    def adicionar_time(self, e):
        time = self.entry_time.value
        if time:
            self.times.append(time)
            self.combo_time1.options.append(ft.dropdown.Option(time))
            self.combo_time2.options.append(ft.dropdown.Option(time))
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Time '{time}' adicionado com sucesso!")))
            self.entry_time.value = ""
            self.page.update()
        else:
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Erro"),
                    content=ft.Text("O nome do time não pode ser vazio!")
                )
            )
    
    def marcar_jogo(self, e):
        time1 = self.combo_time1.value
        time2 = self.combo_time2.value
        data = self.entry_data.value
        
        if time1 and time2 and data and time1 != time2:
            self.jogos.append((time1, time2, data))
            self.tabela_jogos.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(time1)),
                    ft.DataCell(ft.Text(time2)),
                    ft.DataCell(ft.Text(data))
                ])
            )
            self.page.show_snack_bar(ft.SnackBar(content=ft.Text("Jogo marcado com sucesso!")))
            self.combo_time1.value = None
            self.combo_time2.value = None
            self.entry_data.value = ""
            self.page.update()
        else:
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Erro"),
                    content=ft.Text("Verifique os dados inseridos. Os times devem ser diferentes e todos os campos devem estar preenchidos.")
                )
            )

# Criando a interface
def main(page: ft.Page):
    app = FutebolVarzeaApp(page)

ft.app(target=main)