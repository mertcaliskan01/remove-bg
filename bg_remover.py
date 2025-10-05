import os
from PIL import Image
from rembg import remove

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

# Background color options
BACKGROUND_COLORS = {
    '1': {'name': 'White', 'color': (255, 255, 255)},
    '2': {'name': 'Black', 'color': (0, 0, 0)},
    '3': {'name': 'Transparent', 'color': None},
    '4': {'name': 'Light Gray', 'color': (240, 240, 240)},
    '5': {'name': 'Dark Gray', 'color': (64, 64, 64)},
    '6': {'name': 'Cream', 'color': (255, 253, 240)},
    '7': {'name': 'Light Cream', 'color': (255, 250, 230)},
    '8': {'name': 'Warm Cream', 'color': (255, 248, 220)},
    '9': {'name': 'Beige', 'color': (245, 245, 220)},
    '10': {'name': 'Ivory', 'color': (255, 255, 240)},
    '11': {'name': 'Antique White', 'color': (250, 235, 215)},
    '12': {'name': 'Mint Green', 'color': (152, 251, 152)},
    '13': {'name': 'Lavender', 'color': (230, 230, 250)},
    '14': {'name': 'Peach', 'color': (255, 218, 185)},
    '15': {'name': 'Light Blue', 'color': (173, 216, 230)},
    '16': {'name': 'Light Pink', 'color': (255, 182, 193)},
    '17': {'name': 'Salmon', 'color': (250, 128, 114)},
    '18': {'name': 'Light Yellow', 'color': (255, 255, 224)},
    '19': {'name': 'Light Orange', 'color': (255, 218, 185)},
    '20': {'name': 'Light Purple', 'color': (221, 160, 221)},
    '21': {'name': 'Light Green', 'color': (144, 238, 144)},
    '22': {'name': 'Light Brown', 'color': (210, 180, 140)},
    '23': {'name': 'Gradient: Cream-White', 'gradient': 'cream_white'},
    '24': {'name': 'Gradient: White-Cream', 'gradient': 'white_cream'},
    '25': {'name': 'Gradient: Lavender-Mint', 'gradient': 'lavender_mint'},
    '26': {'name': 'Gradient: Mint-Lavender', 'gradient': 'mint_lavender'},
    '27': {'name': 'Gradient: Peach-Cream', 'gradient': 'peach_cream'},
    '28': {'name': 'Gradient: Cream-Peach', 'gradient': 'cream_peach'},
    '29': {'name': 'Gradient: Light Blue-White', 'gradient': 'lightblue_white'},
    '30': {'name': 'Gradient: White-Light Blue', 'gradient': 'white_lightblue'},
    '31': {'name': 'Gradient: Mint-Light Green', 'gradient': 'mint_lightgreen'},
    '32': {'name': 'Gradient: Light Green-Mint', 'gradient': 'lightgreen_mint'},
    '33': {'name': 'Gradient: Light Pink-Cream', 'gradient': 'lightpink_cream'},
    '34': {'name': 'Gradient: Cream-Light Pink', 'gradient': 'cream_lightpink'},
    '35': {'name': 'Gradient: Salmon-Cream', 'gradient': 'salmon_cream'},
    '36': {'name': 'Gradient: Cream-Salmon', 'gradient': 'cream_salmon'},
    '37': {'name': 'Gradient: Lavender-White', 'gradient': 'lavender_white'},
    '38': {'name': 'Gradient: White-Lavender', 'gradient': 'white_lavender'},
    '39': {'name': 'Gradient: Light Yellow-Cream', 'gradient': 'lightyellow_cream'},
    '40': {'name': 'Gradient: Cream-Light Yellow', 'gradient': 'cream_lightyellow'}
}

def createGradient(size, gradientType):
    """Creates a gradient background"""
    width, height = size
    
    # Gradient color definitions - More distinct transitions
    GRADIENTS = {
        'cream_white': [(255, 253, 240), (255, 255, 255)],
        'white_cream': [(255, 255, 255), (255, 253, 240)],
        'lavender_mint': [(147, 112, 219), (152, 251, 152)],
        'mint_lavender': [(152, 251, 152), (147, 112, 219)],
        'peach_cream': [(255, 160, 122), (255, 253, 240)],
        'cream_peach': [(255, 253, 240), (255, 160, 122)],
        'lightblue_white': [(100, 149, 237), (255, 255, 255)],
        'white_lightblue': [(255, 255, 255), (100, 149, 237)],
        'mint_lightgreen': [(152, 251, 152), (34, 139, 34)],
        'lightgreen_mint': [(34, 139, 34), (152, 251, 152)],
        'lightpink_cream': [(255, 105, 180), (255, 253, 240)],
        'cream_lightpink': [(255, 253, 240), (255, 105, 180)],
        'salmon_cream': [(220, 20, 60), (255, 253, 240)],
        'cream_salmon': [(255, 253, 240), (220, 20, 60)],
        'lavender_white': [(138, 43, 226), (255, 255, 255)],
        'white_lavender': [(255, 255, 255), (138, 43, 226)],
        'lightyellow_cream': [(255, 215, 0), (255, 253, 240)],
        'cream_lightyellow': [(255, 253, 240), (255, 215, 0)]
    }
    
    if gradientType not in GRADIENTS:
        return None
    
    color1, color2 = GRADIENTS[gradientType]
    
    # Create gradient
    gradientImg = Image.new('RGB', (width, height))
    pixels = gradientImg.load()
    
    for y in range(height):
        # Color mix based on Y position
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    return gradientImg

def getBackgroundColor():
    """Asks the user to choose a background color"""
    print("\n=== Background Color Selection ===")
    print("Please select a background color:")
    
    for key, value in BACKGROUND_COLORS.items():
        print(f"{key}. {value['name']}")
    
    while True:
        choice = input("\nMake your selection (1-40): ").strip()
        if choice in BACKGROUND_COLORS:
            selected = BACKGROUND_COLORS[choice]
            print(f"\nSelected background color: {selected['name']}")
            return selected
        else:
            print("Invalid selection! Please enter a number between 1-40.")

# Create folders
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Supported image extensions
imageExtensions = ['.jpg', '.jpeg', '.png', '.JPG', '.PNG']

def main():
    """Main function - called when run from the command line"""
    try:
        # Find images in the input folder
        imageFiles = [f for f in os.listdir(INPUT_DIR) if os.path.splitext(f)[1] in imageExtensions]

        if not imageFiles:
            print("No images found in the input folder!")
            return

        print(f'Images found in the input folder: {imageFiles}')

        # Ask user to select background color
        backgroundSelection = getBackgroundColor()

        for imgFile in imageFiles:
            inputPath = os.path.join(INPUT_DIR, imgFile)
            outputPath = os.path.join(OUTPUT_DIR, os.path.splitext(imgFile)[0] + '.png')
            try:
                inputImage = Image.open(inputPath)
                outputImage = remove(inputImage)
                
                if 'gradient' in backgroundSelection:
                    # Gradient background
                    gradientBg = createGradient(outputImage.size, backgroundSelection['gradient'])
                    if gradientBg:
                        # Convert gradient to RGBA
                        gradientRgba = gradientBg.convert('RGBA')
                        # Paste image onto gradient
                        gradientRgba.paste(outputImage, mask=outputImage.split()[3])
                        gradientRgba.convert('RGB').save(outputPath)
                        print(f'{imgFile} -> {outputPath} (gradient background: {backgroundSelection["name"]})')
                elif 'color' not in backgroundSelection or backgroundSelection['color'] is None:
                    # Transparent background - save as PNG
                    outputImage.save(outputPath, 'PNG')
                    print(f'{imgFile} -> {outputPath} (transparent background)')
                else:
                    # Solid color background
                    bg = Image.new('RGBA', outputImage.size, (*backgroundSelection['color'], 255))
                    bg.paste(outputImage, mask=outputImage.split()[3])
                    bg.convert('RGB').save(outputPath)
                    print(f'{imgFile} -> {outputPath} (background {backgroundSelection["name"].lower()}d)')
                    
            except Exception as e:
                print(f'An error occurred ({imgFile}): {e}')
        
        print("\nOperation completed! Output files can be found in the 'output' folder.")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 