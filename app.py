from flask import Flask, request, send_file, render_template
from stegano import lsb
from PIL import Image
import io
import logging

app = Flask(__name__)

# Setup Logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hide", methods=["POST"])
def hide():
    try:
        image = request.files["image"]
        message = request.form["message"]

        if not image or not message:
            return "⚠️ Image and message are required!", 400

        img = Image.open(image)
        secret = lsb.hide(img, message)

        img_io = io.BytesIO()
        secret.save(img_io, format="PNG")
        img_io.seek(0)
        
        return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="stego_image.png")
    
    except Exception as e:
        logging.error(f"Error in hiding message: {str(e)}")
        return "❌ Error processing the image.", 500

@app.route("/reveal", methods=["POST"])
def reveal():
    try:
        image = request.files["image"]
        img = Image.open(image)
        message = lsb.reveal(img)
        return message if message else "⚠️ No hidden message found."
    
    except Exception as e:
        logging.error(f"Error in revealing message: {str(e)}")
        return "❌ Error processing the image.", 500

if __name__ == "__main__":
    app.run(debug=True)
