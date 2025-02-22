from xrpl.clients import JsonRpcClient
from xrpl.models.requests import Ledger
import time 


# Connect to the XRPL
client = JsonRpcClient("https://s1.ripple.com:51234")

def get_latest_validated_ledger():

    request = Ledger(ledger_index="validated")
    response = client.request(request)
    return response.result["ledger_index"]

def ledger_get_data(ledger_index):
# Fetch the latest validated closed ledger index from the XRPL network
    try:
        # Fetch the data of the latest ledger index
        request = Ledger(
            ledger_index=ledger_index,
            transactions=True,
            expand=True,
            binary=False
        )

        response = client.request(request)
        return response.result.get('ledger', None)

    except Exception as e:
        print(f"Failed to fetch ledger data: {e}")
        return None

def fetch_last_500_ledgers():
    latest_index = get_latest_validated_ledger()
    start_index = max(0, latest_index - 500)
    counter = 0
    XRPL = []

    start = time.time()
    for ledger_index in range(latest_index, start_index, - 1):
        ledger_data = ledger_get_data(ledger_index)

        if ledger_data is not None and 'transactions' in ledger_data:
            counter += 1
            for transaction in ledger_data['transactions']:
                XRPL.append(transaction)

    end = time.time()

    time_taken = end - start
    avg_time_taken = time_taken / counter 
    print(f"Total time spent fetching all ledgers: {time_taken:.4f} seconds")
    print(f"Number of ledgers fetched: {counter} ledgers")
    print(f"Average time taken to fetch each ledger: {avg_time_taken:.4f} seconds")

fetch_last_500_ledgers()


