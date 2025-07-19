import qrcode
import io

def build_qr_content(qr_type, value):
    qr_type = qr_type.lower()

    if qr_type == "url":
        return value
    elif qr_type == "email":
        return f"mailto:{value}"
    elif qr_type == "phone":
        return f"tel:{value}"
    elif qr_type == "sms":
        return f"sms:{value}"
    elif qr_type == "text":
        return value
    elif qr_type == "wifi":
        try:
            ssid, password, sec_type = value.split(";")
            return f"WIFI:S:{ssid};T:{sec_type};P:{password};;"
        except:
            return value
    elif qr_type == "vcard":
        return value
    elif qr_type in ["json", "xml"]:
        return value
    else:
        return value

def generate_qr_image(content):
    img = qrcode.make(content)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()