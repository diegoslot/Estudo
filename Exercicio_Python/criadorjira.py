import os

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
        """Limpa a tela do terminal (funciona no Windows, Linux e Mac)."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def criar_historia(self):
        """Coleta informações e monta a história Jira."""
        print("=== Gerador de Histórias Jira ===\n")
        self.respostas['ator'] = input("Quem é o ator (ex: Usuário, Cliente, Admin)? ")
        self.respostas['verbo'] = input(f"Qual verbo deseja usar {self.opcoes_verbo}? ")
        self.respostas['acao'] = input("O que deseja fazer (ação)? ")
        self.respostas['beneficio'] = input("Qual o benefício esperado? ")
        self.respostas['titulo'] = input("Defina um título para a história: ")
        self.respostas['prioridade'] = input("Qual a prioridade (Alta, Média, Baixa)? ")
        self.respostas['complexidade'] = input("Qual a complexidade (Baixa, Média, Alta)? ")

        print("\nDigite os critérios de aceitação (digite 'fim' para encerrar):")
        while True:
            criterio = input("- ")
            if criterio.lower() == 'fim':
                break
            self.respostas['criterios_aceitacao'].append(criterio)

    def exibir_historia(self):
        """Mostra a história de usuário formatada no estilo Jira."""
        print("\n=== História Jira Gerada ===")
        print(f"Título: {self.respostas['titulo']}")
        print(f"Como {self.respostas['ator']}, {self.respostas['verbo']} {self.respostas['acao']} "
              f"para {self.respostas['beneficio']}.")
        print(f"Prioridade: {self.respostas['prioridade']}")
        print(f"Complexidade: {self.respostas['complexidade']}")
        print
