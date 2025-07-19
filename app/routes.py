from flask import Blueprint, request, jsonify, make_response, render_template
from .qr_utils import build_qr_content, generate_qr_image
import base64
from dicttoxml import dicttoxml

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/qrcode', methods=['POST'])
def generate_qrcode():
    data = request.get_json()
    qr_type = data.get('type', 'text')
    value = data.get('value', '')

    if not value:
        return jsonify({"error": "Value is required"}), 400

    content = build_qr_content(qr_type, value)
    img_bytes = generate_qr_image(content)

    accept = request.headers.get('Accept', 'application/json')

    if 'image/png' in accept:
        response = make_response(img_bytes)
        response.headers.set('Content-Type', 'image/png')
        return response

    elif 'application/xml' in accept:
        xml = dicttoxml({
            "type": qr_type,
            "content": content,
            "base64": base64.b64encode(img_bytes).decode()
        }, custom_root='response')
        response = make_response(xml)
        response.headers.set('Content-Type', 'application/xml')
        return response

    else:
        return jsonify({
            "type": qr_type,
            "content": content,
            "base64": f"data:image/png;base64,{base64.b64encode(img_bytes).decode()}"
        })
