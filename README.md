# 📦 QR Code Generator

## Requirements

- Python 3.10+

## Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py --url <my_site.com>
```

## (Optional) Configuration

```bash
cp .env.sample .env
vi .env
```

Hex codes are supported ie.
FILL_COLOR="#f02973"

## (Optional) Docker Setup 🐳

```bash
docker build -t qr_code_app .
docker run -it --rm qr_code_app
```
