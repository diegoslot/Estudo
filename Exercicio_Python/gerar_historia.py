class GeradorHistoriaJira:
    """Classe para gerar histórias de usuário no formato Jira."""

    def __init__(self, respostas=None):
        """Inicializa o gerador de histórias com dados fornecidos."""
        self.respostas = respostas or {
            'ator': 'Diego',
            'verbo': '',
            'acao': '',
            'beneficio': '',
            'criterios_aceitacao': [],
            'prioridade': '',
            'complexidade': '',
            'titulo': ''
        }
        self.opcoes_verbo = ['quero', 'desejo', 'preciso']

    def exibir_historia(self):
        """Mostra a história de usuário formatada no estilo Jira."""
        print("\n=== História Jira Gerada ===")
        print(f"Título: {self.respostas['titulo']}")
        print(f"Como {self.respostas['ator']}, {self.respostas['verbo']} {self.respostas['acao']} "
              f"para {self.respostas['beneficio']}.")
        print(f"Prioridade: {self.respostas['prioridade']}")
        print(f"Complexidade: {self.respostas['complexidade']}")
        print("\nCritérios de Aceitação:")
        for i, c in enumerate(self.respostas['criterios_aceitacao'], start=1):
            print(f"- {i}. {c}")
