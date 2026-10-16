# 🖼️ Background Remover Using Python

A simple Python application that automatically removes the background from images using the `rembg` library. It takes an input image, processes it using AI-powered background removal, and saves the result as a PNG file with a transparent background.

## ✨ Features

- 🪄 **Automatic Background Removal:** Removes image backgrounds with minimal effort.
- 🤖 **AI-Powered Processing:** Uses the `rembg` library for foreground detection.
- 🖼️ **Transparent Background:** Exports the processed image in PNG format.
- 📁 **Simple File Handling:** Reads an input image and saves the output automatically.
- ⚡ **Easy to Use:** Requires only a few lines of Python code.

## 🛠️ Technologies Used

- Python
- rembg
- PNG and JPG image formats

## 🚀 Getting Started

### 1. Install the Required Library

```bash
pip install rembg
```

### 2. Add Your Image

Place your image in the project directory and name it `input.jpg`, or update the input path in the Python script.

### 3. Run the Script

```bash
python main.py
```

### 4. Get the Result

The processed image will be saved as `output.png` in the same directory, with the background removed and transparency preserved where supported.

## 📂 How It Works

1. Reads the input image as binary data.
2. Passes the image bytes to `rembg.remove()`.
3. Removes the detected background.
4. Writes the processed image to a PNG file.

## 🎯 Use Cases

- Product photography
- Profile pictures and portraits
- E-commerce product images
- Graphic design and marketing materials
- Image editing and creative projects

## 👨‍💻 Author

**Hussain Kola**

GitHub: [@hussain205](https://github.com/hussain205)

---

⭐ If you find this project useful, consider giving the repository a star!
