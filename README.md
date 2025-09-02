# 🖼️ Multithread Image Downloader

A simple project that demonstrates **image downloading** in two different ways:
1. **Sequential (Main branch)** – Downloads images one by one.
2. **Multithreaded (implemented_thread branch)** – Downloads multiple images concurrently using threads for better performance.

---

## 📂 Branches

- **`main`**  
  Contains the **sequential implementation** of the image downloader.  
  - Images are downloaded one at a time.  
  - Easier to understand but slower for large sets of images.  

- **`implemented_thread`**  
  Contains the **multithreaded implementation**.  
  - Uses Python threads to download multiple images concurrently.  
  - Improves download speed significantly compared to sequential processing.  

---

## 🚀 Features
- Download images from a list of URLs.  
- Compare performance between sequential and multithreaded approaches.  
- Beginner-friendly demonstration of Python threading.  

---

## ⚙️ Requirements
- Python 3.7+  
- `requests` library  

Install dependencies:
```bash
pip install -r requirements.txt
