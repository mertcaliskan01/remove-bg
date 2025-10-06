import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from PIL import Image
from rembg import remove
from bg_remover import BACKGROUND_COLORS, createGradient

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'input'
app.config['OUTPUT_FOLDER'] = 'output'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.secret_key = 'your-secret-key-here'  # For flash messages

# Create folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html', backgroundColors=BACKGROUND_COLORS)

@app.route('/upload', methods=['POST'])
def uploadFile():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    backgroundChoice = request.form.get('background', '1')
    outputType = request.form.get('output-type', 'png')
    
    if file.filename == '':
        return redirect(request.url)
    
    if file and allowedFile(file.filename):
        # Generate unique filename
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        inputPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        outputFilename = os.path.splitext(filename)[0] + f'.{outputType}'
        outputPath = os.path.join(app.config['OUTPUT_FOLDER'], outputFilename)
        
        # Save file
        file.save(inputPath)
        
        # Remove background
        try:
            inputImage = Image.open(inputPath)
            outputImage = remove(inputImage)
            
            # Handle custom color
            if backgroundChoice == 'custom' or (backgroundChoice and backgroundChoice.startswith('#')):
                # Get custom color from the color picker input or from backgroundChoice
                if backgroundChoice.startswith('#'):
                    customColor = backgroundChoice
                else:
                    customColor = request.form.get('custom-color', '#05339C')
                
                if customColor and customColor.startswith('#'):
                    # Convert hex to RGB
                    hex_color = customColor.lstrip('#')
                    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                    bg = Image.new('RGBA', outputImage.size, (*rgb, 255))
                    bg.paste(outputImage, mask=outputImage.split()[3])
                    
                    # Save based on output type
                    if outputType.lower() == 'jpg':
                        bg.convert('RGB').save(outputPath, 'JPEG', quality=95)
                    else:
                        bg.save(outputPath, 'PNG')
                else:
                    # Fallback to transparent
                    outputImage.save(outputPath, 'PNG')
            else:
                backgroundSelection = BACKGROUND_COLORS[backgroundChoice]
                
                if 'gradient' in backgroundSelection:
                    # Gradient background
                    gradientBg = createGradient(outputImage.size, backgroundSelection['gradient'])
                    if gradientBg:
                        # Convert gradient to RGBA
                        gradientRgba = gradientBg.convert('RGBA')
                        # Paste image onto gradient
                        gradientRgba.paste(outputImage, mask=outputImage.split()[3])
                        
                        # Save based on output type
                        if outputType.lower() == 'jpg':
                            gradientRgba.convert('RGB').save(outputPath, 'JPEG', quality=95)
                        else:
                            gradientRgba.save(outputPath, 'PNG')
                elif 'color' not in backgroundSelection or backgroundSelection['color'] is None:
                    # Transparent background - always save as PNG for transparency
                    outputImage.save(outputPath, 'PNG')
                else:
                    # Solid color background
                    bg = Image.new('RGBA', outputImage.size, (*backgroundSelection['color'], 255))
                    bg.paste(outputImage, mask=outputImage.split()[3])
                    
                    # Save based on output type
                    if outputType.lower() == 'jpg':
                        bg.convert('RGB').save(outputPath, 'JPEG', quality=95)
                    else:
                        bg.save(outputPath, 'PNG')
            
            # Redirect to result page after processing
            return redirect(url_for('result', filename=outputFilename))
            
        except Exception as e:
            flash(f'Bir hata oluştu: {str(e)}', 'error')
            return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

@app.route('/output/<filename>')
def outputFile(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)