import os
import sys
from typing import List, Optional


class GeradorHistoriaJira:
    """Classe para gerar histórias de usuário no formato Jira."""

    def __init__(self):
        """Inicializa o gerador de histórias."""
        self.respostas = {
            'ator': '',
            'verbo': '',
            'acao': '',
            'beneficio': '',
            'criterios_aceitacao': [],
            'prioridade': '',
            'complexidade': '',
            'titulo': ''
        }
        self.opcoes_verbo = ['quero', 'desejo', 'preciso']

    def limpar_tela(self):
        """Limpa a tela do terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_cabecalho(self):
        """Exibe o cabeçalho do programa."""
        self.limpar_tela()
        print("=" * 60)
        print("  GERADOR DE HISTÓRIAS DE USUÁRIO NO FORMATO JIRA")
        print("=" * 60)
        print("\nEste assistente irá guiá-lo na criação de uma história de usuário")
        print("no formato padrão utilizado no Jira.\n")
        print("=" * 60)
        print()

    def fazer_pergunta(self, pergunta: str, opcoes: Optional[List[str]] = None) -> str:
        """Faz uma pergunta ao usuário e retorna a resposta."""
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
                    print(f"Por favor, escolha um número entre 1 e {len(opcoes)}.")
                except ValueError:
                    print("Por favor, digite um número válido.")
        else:
            return input(pergunta + " ")

    def coletar_informacoes(self):
        """Coleta todas as informações necessárias para a história."""
        self.exibir_cabecalho()

        self.respostas['ator'] = self.fazer_pergunta("Como um(a) [ATOR/PAPEL] - Quem é o usuário desta história?")

        self.respostas['verbo'] = self.fazer_pergunta(
            "Qual verbo deseja utilizar na história?", self.opcoes_verbo
        )

        self.respostas['acao'] = self.fazer_pergunta(f"Eu {self.respostas['verbo']} [AÇÃO] - O que o usuário quer fazer?")

        self.respostas['beneficio'] = self.fazer_pergunta("Para que [BENEFÍCIO] - Qual o valor/benefício desta ação?")

        print("\nCritérios de Aceitação (digite 'fim' quando terminar):")
        contador = 1
        while True:
            criterio = self.fazer_pergunta(f"Critério {contador} (ou 'fim' para encerrar):")
            if criterio.lower() == 'fim':
                break
            self.respostas['criterios_aceitacao'].append(criterio)
            contador += 1

        self.respostas['prioridade'] = self.fazer_pergunta(
            "\nQual a prioridade desta história?", ["Alta", "Média", "Baixa"]
        )

        self.respostas['complexidade'] = self.fazer_pergunta(
            "Qual a complexidade desta história?", ["Simples", "Média", "Complexa"]
        )

        self.respostas['titulo'] = self.fazer_pergunta("\nDigite um título curto para esta história:")

    def formatar_historia(self) -> str:
        """Formata a história de usuário com base nas informações coletadas."""
        historia = (
            f"Título: {self.respostas['titulo']}\n\n"
            f"Como um {self.respostas['ator']}, "
            f"eu {self.respostas['verbo']} {self.respostas['acao']} "
            f"para {self.respostas['beneficio']}.\n\n"
            f"Prioridade: {self.respostas['prioridade']}\n"
            f"Complexidade: {self.respostas['complexidade']}\n\n"
        )

        if self.respostas['criterios_aceitacao']:
            historia += "Critérios de Aceitação:\n"
            for i, criterio in enumerate(self.respostas['criterios_aceitacao'], 1):
                historia += f"- {i}. {criterio}\n"

        return historia

    def salvar_historia(self, historia: str) -> str:
        """Salva a história em um arquivo de texto."""
        pasta = "historias"
        os.makedirs(pasta, exist_ok=True)

        nome_arquivo = self.respostas['titulo'].lower().replace(' ', '_')
        nome_arquivo = ''.join(c for c in nome_arquivo if c.isalnum() or c == '_')
        caminho_arquivo = os.path.join(pasta, f"historia_{nome_arquivo}.txt")

        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(historia)
            print(f"\n✅ História salva em: {caminho_arquivo}")
        except Exception as e:
            print(f"\n❌ Erro ao salvar a história: {e}")

        return caminho_arquivo

    def executar(self):
        """Executa o fluxo completo de geração de história."""
        try:
            self.coletar_informacoes()
            historia = self.formatar_historia()

            self.limpar_tela()
            print("=" * 60)
            print("  HISTÓRIA DE USUÁRIO GERADA")
            print("=" * 60)
            print(historia)

            salvar = self.fazer_pergunta("\nDeseja salvar esta história em um arquivo? (s/n)")
            if salvar.lower() in ['s', 'sim']:
                self.salvar_historia(historia)

            print("\nObrigado por utilizar o Gerador de Histórias de Usuário!")

        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            sys.exit(0)

        except Exception as e:
            print(f"\nOcorreu um erro: {str(e)}")
            sys.exit(1)


if __name__ == "__main__":
    gerador = GeradorHistoriaJira()
    gerador.executar()
