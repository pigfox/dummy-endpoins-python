# Dummy Endpoints Python

This project is a Python translation of the Go project "dummy-endpoints-http". It simulates a client-server application for querying DEX endpoints and comparing token prices.

## Structure
- `client/main.py`: Client logic for querying endpoints and analyzing responses.
- `requester/requestWG.py`: HTTP requester for fetching data.
- `server/main.py`: Flask server simulating DEX endpoints.
- `structs/structs.py`: Shared constants and data structures.

## Requirements
- Python 3.8+
- Flask

## Usage
1. ./setup.sh
2. Start the server: `python3 -m server.start_servers`
3. Run the client: `python3 -m client.main`

