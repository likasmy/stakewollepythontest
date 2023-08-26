import requests
import base64

# # # Написать функцию, которая на вход принимает номер блока и выводит данные о транзакциях из очередного блока, учитываем, что в блоке их может не быть
# # # в сети Акаш есть вот такой блок https://www.mintscan.io/akash/blocks/11260637
# # # доступные rest можно посмотреть тут https://chains.cosmos.directory/akash
# # # в текущем задании нужно из response выдернуть данные по пути data.txs , данные лежат в base64, то есть понадобится метод base64.b64decode()

def get_block_transactions(block_number):
    api_url = f"https://api.mintscan.io/akash/blocks/{block_number}"

    response = requests.get(api_url)
    if response.status_code == 200:
        txs_base64 = response.json().get("result", {}).get("block", {}).get("data", {}).get("txs", [])
        
        transactions = [base64.b64decode(tx).decode() for tx in txs_base64]
        
        return transactions
    else:
        print(f"Ошибка получения данных блока {block_number}")
        return []

# Пример вызова функции для блока 11260637
block_number = 11260637
transactions = get_block_transactions(block_number)

for transaction in transactions:
    print(transaction)
