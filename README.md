# 🖼️ Steganography Web Project

This is a **Flask-based web application** that allows users to **hide and extract secret messages** inside images using **LSB (Least Significant Bit) Steganography**.

---

## ✨ Features
- 🔒 **Hide Secret Messages** inside images.
- 🔍 **Extract Hidden Messages** from steganographic images.
- 📷 **Supports PNG and JPG images**.
- 🖥️ **User-friendly Web Interface** using Flask.
- 🛠️ **Built with Python, Flask, and Stegano Library**.

---

## 🚀 Installation & Setup

```sh
# 1️⃣ Clone the Repository
git clone https://github.com/bedapudi-harika6/steganography-web.git
cd steganography-web

# 2️⃣ Create & Activate Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run the Application
python app.py

# Open in Browser: http://127.0.0.1:5000/

# 📷 Usage
# 1. Upload an image and enter a secret message.
# 2. Click "Encode" to hide the message inside the image.
# 3. Download the steganographic image.
# 4. To extract the message, upload the steganographic image and click "Decode".

# 🛠️ Technology Stack
# - Backend: Python, Flask
# - Steganography: stegano library
# - Frontend: HTML, CSS, JavaScript
# - Hosting: (Future deployment options: GitHub Pages, Heroku, or AWS)

# 📜 License
# This project is open-source and available under the MIT License.

# 👤 Author
# - Harika Bedapudi
# - GitHub: https://github.com/bedapudi-harika6

# ⭐ Contribute
# Feel free to contribute! Fork the repo, create a pull request, or open an issue.

# 🎉 Happy Coding!
