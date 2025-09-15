#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para geração simplificada de histórias de usuário no formato Jira.
Este script faz perguntas básicas ao usuário e gera uma história
no formato padrão do Jira com os elementos essenciais:
- Como um [ator]
- Eu quero/desejo/preciso [ação]
- Para que [benefício/valor]
"""

import os
import sys
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import subprocess

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do programa."""
    limpar_tela()
    print("=" * 60)
    print("  GERADOR DE HISTÓRIAS DE USUÁRIO NO FORMATO JIRA")
    print("=" * 60)
    print("\nEste assistente irá guiá-lo na criação de uma história de usuário")
    print("no formato padrão utilizado no Jira.\n")
    print("=" * 60)
    print()

def fazer_pergunta(pergunta, opcoes=None):
    """
    Faz uma pergunta ao usuário e retorna a resposta.
    
    Args:
        pergunta: A pergunta a ser feita
        opcoes: Lista opcional de opções para escolha
        
    Returns:
        A resposta do usuário
    """
    if opcoes:
        print(pergunta)
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")
        
        while True:
            try:
                resposta = input("\nEscolha uma opção (número): ")
                indice = int(resposta) - 1
                if 0 <= indice < len(opcoes):
                    return opcoes[indice]
                else:
                    print(f"Por favor, escolha um número entre 1 e {len(opcoes)}.")
            except ValueError:
                print("Por favor, digite um número válido.")
    else:
        return input(pergunta + " ")

def gerar_historia_jira():
    """Executa o fluxo completo de geração de história."""
    try:
        exibir_cabecalho()
        
        # Coleta o ator (quem)
        ator = fazer_pergunta("Como um(a) [ATOR/PAPEL] - Quem é o usuário desta história?")
        
        # Coleta o verbo (quero/desejo/preciso)
        opcoes_verbo = ['quero', 'desejo', 'preciso']
        verbo = fazer_pergunta(
            "Qual verbo deseja utilizar na história?",
            opcoes_verbo
        )
        
        # Coleta a ação (o que)
        acao = fazer_pergunta(f"Eu {verbo} [AÇÃO] - O que o usuário quer fazer?")
        
        # Coleta o benefício (para que)
        beneficio = fazer_pergunta("Para que [BENEFÍCIO] - Qual o valor/benefício desta ação?")
        
        # Formata a história
        limpar_tela()
        print("=" * 60)
        print("  HISTÓRIA DE USUÁRIO GERADA")
        print("=" * 60)
        print("\n## História de Usuário")
        print(f"**Como um** {ator}")
        print(f"**Eu {verbo}** {acao}")
        print(f"**Para que** {beneficio}")
        print("\n" + "=" * 60)
        
        # Pergunta se deseja salvar
        salvar = fazer_pergunta("\nDeseja salvar esta história em um arquivo? (s/n)")
        if salvar.lower() in ['s', 'sim']:
            titulo = fazer_pergunta("Digite um título para esta história:")
            nome_arquivo = titulo.lower().replace(' ', '_')
            nome_arquivo = ''.join(c for c in nome_arquivo if c.isalnum() or c == '_')
            nome_arquivo = f"historia_{nome_arquivo}.md"
            
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(f"# {titulo}\n\n")
                arquivo.write("## História de Usuário\n")
                arquivo.write(f"**Como um** {ator}\n")
                arquivo.write(f"**Eu {verbo}** {acao}\n")
                arquivo.write(f"**Para que** {beneficio}\n")
            
            print(f"\nHistória salva no arquivo: {nome_arquivo}")
            
        print("\nObrigado por utilizar o Gerador de Histórias de Usuário!")
        
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
        sys.exit(0)
        
    except Exception as e:
        print(f"\nOcorreu um erro: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    gerar_historia_jira()
