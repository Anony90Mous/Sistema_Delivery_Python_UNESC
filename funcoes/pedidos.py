import json
import os
import re
from datetime import datetime
from typing import List, Dict, Any


PASTA_DATA = "data"
ARQUIVO_PEDIDOS = os.path.join(PASTA_DATA, "pedidos.json")


def carregar_pedidos() -> List[Dict[str, Any]]:
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)

    if os.path.exists(ARQUIVO_PEDIDOS):
        try:
            with open(ARQUIVO_PEDIDOS, "r", encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def salvar_pedidos(pedidos: List[Dict[str, Any]]) -> None:
    """Salva a lista de pedidos no arquivo JSON."""
    try:
        with open(ARQUIVO_PEDIDOS, "w", encoding='utf-8') as f:
            json.dump(pedidos, f, indent=2, ensure_ascii=False)
    except IOError as e:
        raise ValueError(f"Erro ao salvar pedidos: {str(e)}")


def validar_horario(horario: str) -> bool:
    padrao = r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$'
    if not re.match(padrao, horario):
        return False
    try:
        datetime.strptime(horario, "%d/%m/%Y %H:%M")
        return True
    except ValueError:
        return False


def ordenar_pedidos_por_data(pedidos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    def merge_sort(lista: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if len(lista) <= 1:
            return lista

        meio = len(lista) // 2
        esquerda = merge_sort(lista[:meio])
        direita = merge_sort(lista[meio:])
        return merge(esquerda, direita)

    def merge(esq: List[Dict[str, Any]], dir: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        resultado = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            dt1 = datetime.strptime(esq[i]['hora_pedido'], "%d/%m/%Y %H:%M")
            dt2 = datetime.strptime(dir[j]['hora_pedido'], "%d/%m/%Y %H:%M")
            if dt1 <= dt2:
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir[j])
                j += 1

        resultado.extend(esq[i:])
        resultado.extend(dir[j:])
        return resultado

    return merge_sort(pedidos.copy())


def formatar_pedido(pedido: Dict[str, Any], indice: int) -> str:
    return (
            f"Pedido #{indice}\n"
            f"Cliente: {pedido['nome']}\n"
            f"Endereço: {pedido['endereco']}\n"
            f"Horário: {pedido['hora_pedido']}\n"
            "Itens:\n" + "\n".join([f"- {item}" for item in pedido['itens']]) + "\n"
                                                                                f"Total: R${pedido['total']:.2f}\n"
                                                                                "-------------------------\n"
    )
