# FoShodan

FoShodan is a tool that can be used to facilitate searches on Shodan using its API. This helps bypass the search restrictions imposed on free accounts over their Web UI.

## Setup

1. Create a virtual environment (`python -m venv venv`)
2. Activate your virtual environment
3. Install requirements (`pip install -r requirements.txt`)

## Usage

```bash
usage: foshodan.py [-h] api_key

Use FOSHOdan to look up crap in Shodan.

positional arguments:
  api_key     Your Shodan API key

optional arguments:
  -h, --help  show this help message and exit
```
