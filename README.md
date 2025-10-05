# Background Remover

This project is a web application that automatically removes the background from images.

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

### Running via Command Line

1. Place the images you want to remove the background from into the `input/` folder.

2. Run the script:

```bash
python3 bg_remover.py
```

3. Processed images will be found in the `output/` folder.

## Requirements

- Python 3.7+
- Pillow (PIL)
- rembg
- onnxruntime

## Notes

- The `rembg` model will be downloaded on the first run (requires internet connection).
- Processing time depends on image size and system performance.
