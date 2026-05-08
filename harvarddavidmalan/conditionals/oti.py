import numpy as np

class IrrigationOptimizer:
    def __init__(self, num_areas=10, agua_total=200):
        self.num_areas = num_areas
        self.agua_total = agua_total
        self.areas = np.arange(1, num_areas + 1)
        self.umidade = np.random.randint(20, 70, size=num_areas)

    def calcular_necessidade(self):
        return 70 - self.umidade

    def otimizar_distribuicao(self):
        necessidade = self.calcular_necessidade()
        ordem = np.argsort(necessidade)[::-1]

        distribuicao = np.zeros(self.num_areas)
        agua_restante = self.agua_total

        for i in ordem:
            if agua_restante <= 0:
                break
            qtd = min(necessidade[i], agua_restante)
            distribuicao[i] = qtd
            agua_restante -= qtd

        return distribuicao

    def gerar_relatorio(self, distribuicao):
        eficiencia = np.sum(distribuicao) / self.agua_total * 100

        print("=== Jorginho | Irrigation Optimization Report ===\n")
        print("Área | Umidade(%) | Água Recebida")
        print("-" * 40)

        for i in range(self.num_areas):
            print(f"{self.areas[i]:>4} | {self.umidade[i]:>10}% | {distribuicao[i]:>14}")

        print("\nEficiência do uso de água: {:.2f}%".format(eficiencia))


if __name__ == "__main__":
    optimizer = IrrigationOptimizer()
    distribuicao = optimizer.otimizar_distribuicao()
    optimizer.gerar_relatorio(distribuicao)