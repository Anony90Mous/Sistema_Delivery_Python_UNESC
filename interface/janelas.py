import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from funcoes.pedidos import (
    carregar_pedidos,
    salvar_pedidos,
    validar_horario,
    ordenar_pedidos_por_data,
    formatar_pedido
)

# Constantes
ITENS_CARDAPIO = {
    "Pizza Margherita": 45.90,
    "Pizza Pepperoni": 49.90,
    "Pizza 4 Queijos": 52.90,
    "Hambúrguer Clássico": 32.90,
    "Hambúrguer Bacon": 36.90,
    "Batata Frita": 12.90,
    "Água Mineral": 5.00,
    "Refrigerante": 7.50,
}


class Aplicacao:
    def __init__(self):
        self.pedidos = carregar_pedidos()
        self.selecionados = []
        self.janela_principal = None
        self.variaveis_itens = []

    def iniciar(self):
        self._configurar_janela_principal()
        self._criar_widgets_clientes()
        self._criar_widgets_cardapio()
        self._criar_widgets_resumo()
        self._criar_botoes()
        self.janela_principal.mainloop()

    def _configurar_janela_principal(self):
        self.janela_principal = ctk.CTk()
        self.janela_principal.title("Sistema Delivery")
        self.janela_principal.geometry("700x600")
        self.janela_principal.resizable(False, False)

    def _criar_widgets_clientes(self):
        titulo = ctk.CTkLabel(
            self.janela_principal,
            text="Informações do Cliente",
            font=("Arial", 16, "bold")
        )
        titulo.place(x=350, y=20, anchor="center")

        frame_cliente = ctk.CTkFrame(
            self.janela_principal,
            width=620,
            height=130,
            border_width=5,
            corner_radius=20,
            fg_color="transparent"
        )
        frame_cliente.place(x=40, y=30)

        ctk.CTkLabel(frame_cliente, text="Cliente", font=("Arial", 16, "bold")).place(x=90, y=15)
        self.entry_nome = ctk.CTkEntry(frame_cliente, width=300, placeholder_text="Nome do Cliente")
        self.entry_nome.place(x=175, y=15)

        ctk.CTkLabel(frame_cliente, text="Endereço", font=("Arial", 16, "bold")).place(x=90, y=50)
        self.entry_endereco = ctk.CTkEntry(frame_cliente, width=300, placeholder_text="Endereço do Cliente")
        self.entry_endereco.place(x=175, y=50)

        ctk.CTkLabel(frame_cliente, text="Horário", font=("Arial", 16, "bold")).place(x=90, y=85)
        self.entry_horario = ctk.CTkEntry(frame_cliente, width=300)
        self.entry_horario.place(x=175, y=85)
        self.entry_horario.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M"))

    def _criar_widgets_cardapio(self):
        titulo_cardapio = ctk.CTkLabel(
            self.janela_principal,
            text="Cardápio",
            font=("Arial", 16, "bold")
        )
        titulo_cardapio.place(x=350, y=175, anchor="center")

        frame_cardapio = ctk.CTkFrame(
            self.janela_principal,
            width=620,
            height=150,
            border_width=5,
            corner_radius=20,
            fg_color="transparent"
        )
        frame_cardapio.place(x=40, y=185)

        self.variaveis_itens = []
        for i, (item, preco) in enumerate(ITENS_CARDAPIO.items()):
            coluna = i % 2
            linha = i // 2
            x = 30 if coluna == 0 else 380
            y = 20 + linha * 30

            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(
                frame_cardapio,
                text=f"{item} - R${preco:.2f}",
                variable=var,
                command=self._atualizar_resumo
            )
            checkbox.place(x=x, y=y)
            self.variaveis_itens.append((var, item, preco))

    def _criar_widgets_resumo(self):
        frame_resumo = ctk.CTkFrame(
            self.janela_principal,
            width=620,
            height=150,
            border_width=5,
            corner_radius=20,
            fg_color="white"
        )
        frame_resumo.place(x=40, y=360)

        self.caixa_texto_resumo = ctk.CTkTextbox(
            frame_resumo,
            width=600,
            height=140,
            corner_radius=20
        )
        self.caixa_texto_resumo.pack(padx=10, pady=10)
        self.caixa_texto_resumo.configure(state="disabled")

        self.texto_total = ctk.CTkLabel(
            self.janela_principal,
            text="Total: R$ 0.00",
            font=("Arial", 14, "bold")
        )
        self.texto_total.place(x=50, y=540)

    def _criar_botoes(self):
        btn_mostrar = ctk.CTkButton(
            self.janela_principal,
            text="Mostrar Pedidos",
            command=self._mostrar_pedidos
        )
        btn_mostrar.place(x=350, y=540)

        btn_finalizar = ctk.CTkButton(
            self.janela_principal,
            text="Finalizar Compra",
            fg_color="green",
            hover_color="dark green",
            command=self._finalizar_pedido
        )
        btn_finalizar.place(x=500, y=540)

    def _atualizar_resumo(self):
        self.selecionados = [
            (item, preco)
            for var, item, preco in self.variaveis_itens
            if var.get()
        ]

        texto = "\n".join([
            f"{item} - R$ {preco:.2f}"
            for item, preco in self.selecionados
        ])

        total = sum(preco for _, preco in self.selecionados)

        self.caixa_texto_resumo.configure(state="normal")
        self.caixa_texto_resumo.delete("1.0", "end")
        self.caixa_texto_resumo.insert("1.0", texto)
        self.caixa_texto_resumo.configure(state="disabled")

        self.texto_total.configure(text=f"Total: R$ {total:.2f}")

    def _finalizar_pedido(self):
        nome = self.entry_nome.get().strip()
        endereco = self.entry_endereco.get().strip()
        horario = self.entry_horario.get().strip()

        if not nome or not endereco:
            messagebox.showerror("Erro", "Nome e endereço são obrigatórios.")
            return

        if not validar_horario(horario):
            messagebox.showerror("Erro", "Formato de horário inválido. Use dd/mm/aaaa hh:mm")
            return

        if not self.selecionados:
            messagebox.showerror("Erro", "Selecione ao menos um item do cardápio.")
            return

        novo_pedido = {
            "nome": nome,
            "endereco": endereco,
            "hora_pedido": horario,
            "itens": [item for item, _ in self.selecionados],
            "total": sum(preco for _, preco in self.selecionados)
        }

        self.pedidos.append(novo_pedido)
        try:
            salvar_pedidos(self.pedidos)
            messagebox.showinfo("Sucesso", "Pedido finalizado com sucesso!")
            self._limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o pedido: {str(e)}")

    def _mostrar_pedidos(self):
        janela_pedidos = ctk.CTkToplevel(self.janela_principal)
        janela_pedidos.title("Pedidos Finalizados")
        janela_pedidos.geometry("600x550")
        janela_pedidos.lift()
        janela_pedidos.focus_force()

        texto = ctk.CTkTextbox(janela_pedidos, width=580, height=460)
        texto.pack(padx=10, pady=(10, 0))
        texto.configure(state="normal")
        texto.delete("1.0", "end")

        def limpar_todos():
            if messagebox.askyesno("Confirmação", "Tem certeza que deseja limpar TODOS os pedidos?"):
                self.pedidos.clear()
                salvar_pedidos(self.pedidos)
                texto.configure(state="normal")
                texto.delete("1.0", "end")
                texto.insert("end", "Nenhum pedido registrado.")
                texto.configure(state="disabled")

        pedidos_ordenados = ordenar_pedidos_por_data(self.pedidos)
        if not pedidos_ordenados:
            texto.insert("end", "Nenhum pedido registrado.")
        else:
            for i, pedido in enumerate(pedidos_ordenados, 1):
                texto.insert("end", formatar_pedido(pedido, i))

        texto.configure(state="disabled")

        # Botão para limpar pedidos
        btn_limpar = ctk.CTkButton(
            janela_pedidos,
            text="Limpar Pedidos",
            fg_color="red",
            hover_color="#cc0000",
            command=limpar_todos
        )
        btn_limpar.pack(pady=10)

    def _limpar_campos(self):
        self.entry_nome.delete(0, "end")
        self.entry_endereco.delete(0, "end")
        self.entry_horario.delete(0, "end")
        self.entry_horario.insert(0, datetime.now().strftime("%d/%m/%Y %H:%M"))

        for var, _, _ in self.variaveis_itens:
            var.set(False)

        self._atualizar_resumo()


def iniciar_aplicacao():
    app = Aplicacao()
    app.iniciar()
