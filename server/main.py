import random
import time
import sys
from flask import Flask, jsonify
import structs.structs as structs

def create_app(port):
    app = Flask(__name__)

    @app.route("/")
    def port_handler():
        delay = structs.random_int(0, structs.RESPONSE_DELAY_MAX)
        time.sleep(delay)

        response_rows = structs.random_int(structs.RESPONSE_ROWS_PER_SERVER_MIN, structs.RESPONSE_ROWS_PER_SERVER_MAX)
        rows = [
            {
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "price": structs.random_int(1, 100),
                "supply": structs.random_int(1000, 100000000),
                "address": f"0x{i}"
            }
            for i in range(response_rows)
        ]
        return jsonify({"dex": f"DEX {port}", "responses": rows})

    return app

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        app = create_app(port)
        app.run(host='localhost', port=port, use_reloader=False, threaded=True)
    else:
        ports = structs.Ports.get_ports()
        for port in range(ports.min, ports.max + 1):
            if port not in ports.failed:
                app = create_app(port)
                app.run(host='localhost', port=port, use_reloader=False, threaded=True)