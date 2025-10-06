# Background Remover

Background Changer is a web application that uses advanced artificial intelligence to remove and replace image backgrounds.

## 🛠️ Built With

- **Flask** - Lightweight Python web framework
- **Rembg** - Advanced AI background removal using U²-Net model
- **Pillow** - Professional image processing
- **ONNX Runtime** - Optimized AI inference engine

  <p align="center">
  <img src="https://github.com/user-attachments/assets/4081a5ab-37e0-4eec-a111-06b048d5d691" 
       alt="App Main Screen" 
       width="500"
       style="border-radius: 12px; box-shadow: 0 4px 14px rgba(0,0,0,0.15);" />
</p>

## Setup and Running

### Installation Steps

1. Create a virtual environment:

```bash
python3 -m venv venv
```

2. Activate the virtual environment:

```bash
source venv/bin/activate
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

### Running the Web Application

1. Start the web application:

```bash
source venv/bin/activate && python app.py
```

2. Go to http://127.0.0.1:5000/ in your browser.


## Requirements

- Python 3.7+
- Flask
- Pillow (PIL)

