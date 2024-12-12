import multiprocessing
from server.main import create_app
import structs.structs as structs

def run_server(port):
    app = create_app(port)
    app.run(host='localhost', port=port, use_reloader=False, threaded=True)

def start_servers():
    ports = structs.Ports.get_ports()
    processes = []

    for port in range(ports.min, ports.max + 1):
        if port not in ports.failed:
            process = multiprocessing.Process(target=run_server, args=(port,))
            process.start()
            processes.append(process)

    # Wait for all processes to complete (which they won't, as servers run continuously)
    for process in processes:
        process.join()

if __name__ == "__main__":
    start_servers()