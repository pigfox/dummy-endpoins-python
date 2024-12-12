import threading
import time
import math
import requester.requester as requester
import structs.structs as structs

def main():
    ports = structs.Ports.get_ports()
    all_responses = []
    lock = threading.Lock()

    while True:
        start_time = time.time()
        threads = []

        for port in range(ports.min, ports.max + 1):
            if port in ports.failed:
                continue

            thread = threading.Thread(target=fetch_data, args=(port, all_responses, lock))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        grouped_by_address = {}

        for response in all_responses:
            for resp in response["responses"]:
                grouped_by_address.setdefault(resp["address"], []).append(response)

        price_difference_threshold = structs.PRICE_DIFFERENCE_PCT / 100.0

        for address, responses in grouped_by_address.items():
            if len(responses) < 2:
                continue

            responses.sort(key=lambda x: x["responses"][0]["price"])

            for i in range(len(responses)):
                for j in range(i + 1, len(responses)):
                    price1 = responses[i]["responses"][0]["price"]
                    price2 = responses[j]["responses"][0]["price"]
                    diff_pct = abs(price2 - price1) / price1

                    if diff_pct > price_difference_threshold:
                        from_dex = responses[i]["dex"]
                        to_dex = responses[j]["dex"]
                        print(f"Price difference found for Address: {address}")
                        print(f"Lowest Price: {from_dex} ---> Highest Price: {to_dex}")
                        print(f"Price1: {price1}, Price2: {price2}, Difference: {diff_pct * 100:.2f}%")

        print("Total time taken: ", time.time() - start_time)
        print("Total number of responses: ", len(all_responses))
        time.sleep(3)


def fetch_data(port, all_responses, lock):
    url = f"http://localhost:{port}"
    try:
        response = requester.make(url)
        with lock:
            all_responses.append(response)
    except Exception as e:
        print(f"Error fetching data from port {port}: {e}")


if __name__ == "__main__":
    main()
