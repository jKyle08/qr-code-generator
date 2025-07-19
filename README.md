# QR Code Generator API

A minimal Flask-based REST API to generate QR codes from different content types such as text, URLs, emails, phone numbers, WiFi configs, vCards, and more.

## 🔧 Features

- Supports multiple QR code content types
- Returns image as base64 string or PNG
- Supports Accept headers for JSON, XML, or image output
- Lightweight and fast

## 📦 Requirements

- Python 3.6+
- pip

## 📥 Installation

```bash
git clone <repo-url>
cd qr-api
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate    # Mac/Linux

pip install -r requirements.txt
python app.py
```

## 🧪 API Usage

### Endpoint

```
POST /api/qrcode
Content-Type: application/json
Accept: application/json | application/xml | image/png
```

### Request Body

```json
{
  "type": "url",
  "value": "https://example.com"
}
```

### Response (JSON)

```json
{
  "type": "url",
  "content": "https://example.com",
  "base64": "data:image/png;base64,..."
}
```

## ✍️ Supported Types

- `text`
- `url`
- `email`
- `phone`
- `sms`
- `wifi` (format: `SSID;PASSWORD;WPA`)
- `vcard` (vCard format string)
- `json`
- `xml`

---

## 🧑‍💻 Author

Created by John Kyle Lastimosa