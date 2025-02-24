async function hideMessage() {
    let image = document.getElementById('imageInput').files[0];
    let message = document.getElementById('messageInput').value;
    
    if (!image || !message) {
        alert("⚠️ Please select an image and enter a message.");
        return;
    }
    
    let formData = new FormData();
    formData.append("image", image);
    formData.append("message", message);
    
    let response = await fetch("/hide", { method: "POST", body: formData });
    let data = await response.blob();
    let url = window.URL.createObjectURL(data);
    
    let a = document.createElement("a");
    a.href = url;
    a.download = "stego_image.png";
    a.click();
}

async function revealMessage() {
    let image = document.getElementById('stegoImageInput').files[0];
    
    if (!image) {
        alert("⚠️ Please select a stego image.");
        return;
    }
    
    let formData = new FormData();
    formData.append("image", image);
    
    let response = await fetch("/reveal", { method: "POST", body: formData });
    let data = await response.text();
    
    alert("🔍 Hidden Message: " + data);
}
