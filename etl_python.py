from csv import reader
from collections import defaultdict
import time
from pathlib import Path

TXT_PATH = r"data\measurements.txt"

def processar_temperaturas(txt_path: Path):
    print('Iniciando processamento...')

    start_time = time.time()

    temperatura_por_estacao = defaultdict(list)
    with open(txt_path, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_estacao, temperatura = row[0], float(row[1])
            temperatura_por_estacao[nome_da_estacao].append(temperatura)

    print('Dados carregados. Calculando estatísticas...')

    results = {}

    for station, temperatures in temperatura_por_estacao.items():
        min_temp = min(temperatures)
        max_temp = max(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Calculo estatistico finalizado. Ordenando informações...")
    sorted_results = dict(sorted(results.items()))

    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()
    print(f'Processamento concluído em {end_time - start_time:.2f} segundos.')

    return formatted_results

if __name__ == "__main__":
    txt_path: Path = Path("data\measurements.txt")
    resultados = processar_temperaturas(txt_path)
    #print(resultados)