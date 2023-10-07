class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def exibirInformacoes(self):
        print('--- DADOS DO FUNCIONÁRIO ---')
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Salário: {self.salario}')

class Professor(Funcionario):
    def __init__(self, matricula, nome, salario, turma):
        # chamando o construtor de Funcionario
        super().__init__(matricula, nome, salario)
        self.turma = turma
    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Turma: {self.turma}")

class Monitor(Funcionario):
    def __init__(self, matricula, nome, salario, carga_horaria):
        # chamando o construtor de Funcionario
        super().__init__(matricula, nome, salario)
        self.carga_horaria = carga_horaria

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Carga horária: {self.carga_horaria}")
class Coordenador(Funcionario):
    def __init__(self, matricula, nome, salario, area):
        # chamando o construtor de Funcionario
        super().__init__(matricula, nome, salario)
        self.area = area

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Área: {self.area}")

p1 = Professor(1, "Luana", 3500, "DFS619")
p1.exibirInformacoes()

m1 = Monitor(1, "Luana", 3500, 25)
m1.exibirInformacoes()

c1 = Coordenador(1, "Luana", 3500, "Engenharia civil")
c1.exibirInformacoes()