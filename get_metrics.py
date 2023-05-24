import argparse
import requests
import time

def save_response_content(response, filename):
    with open(filename, 'wb') as file:
        file.write(response.content)

def get_current_time():
    return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

# Args
parser = argparse.ArgumentParser(description='Script para acessar uma URL e salvar o conteúdo em um arquivo.')
parser.add_argument('ipv4', type=str, help='IPV4 que será acessada')
parser.add_argument('--interval', type=int, default=20, help='Intervalo em segundos entre as requisições (padrão: 20)')

args = parser.parse_args()

ipv4 = 'http://{}:9109/metrics'.format(args.ipv4)
interval = args.interval

proxies = {
    'http': '',
    'https': ''
}

duracao = 3600
inicio = time.time()

while True:
    # verificar 1 hora
    tempo_atual = time.time()
    if tempo_atual - inicio >= duracao:
        print('1 hour completed, Finish...')
        break

    response = requests.get(ipv4, proxies=proxies)
    current_time = get_current_time()
    filename = f"response_{current_time}.txt"

    save_response_content(response, filename)
    print(f"Saved in: {filename}")

    # esperar intervalo
    time.sleep(interval)

# python3 get_metrics.py 192.168.29.30 --interval 20
