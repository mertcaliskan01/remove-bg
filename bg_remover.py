import os
from PIL import Image
from rembg import remove

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

# Arka plan renk seçenekleri
BACKGROUND_COLORS = {
    '1': {'name': 'Beyaz', 'color': (255, 255, 255)},
    '2': {'name': 'Siyah', 'color': (0, 0, 0)},
    '3': {'name': 'Şeffaf', 'color': None},
    '4': {'name': 'Açık Gri', 'color': (240, 240, 240)},
    '5': {'name': 'Koyu Gri', 'color': (64, 64, 64)},
    '6': {'name': 'Krem', 'color': (255, 253, 240)},
    '7': {'name': 'Açık Krem', 'color': (255, 250, 230)},
    '8': {'name': 'Sıcak Krem', 'color': (255, 248, 220)},
    '9': {'name': 'Bej', 'color': (245, 245, 220)},
    '10': {'name': 'Fildişi', 'color': (255, 255, 240)},
    '11': {'name': 'Antik Beyaz', 'color': (250, 235, 215)},
    '12': {'name': 'Mint Yeşili', 'color': (152, 251, 152)},
    '13': {'name': 'Lavanta', 'color': (230, 230, 250)},
    '14': {'name': 'Şeftali', 'color': (255, 218, 185)},
    '15': {'name': 'Açık Mavi', 'color': (173, 216, 230)},
    '16': {'name': 'Açık Pembe', 'color': (255, 182, 193)},
    '17': {'name': 'Somon', 'color': (250, 128, 114)},
    '18': {'name': 'Açık Sarı', 'color': (255, 255, 224)},
    '19': {'name': 'Açık Turuncu', 'color': (255, 218, 185)},
    '20': {'name': 'Açık Mor', 'color': (221, 160, 221)},
    '21': {'name': 'Açık Yeşil', 'color': (144, 238, 144)},
    '22': {'name': 'Açık Kahverengi', 'color': (210, 180, 140)},
    '23': {'name': 'Gradient: Krem-Beyaz', 'gradient': 'cream_white'},
    '24': {'name': 'Gradient: Beyaz-Krem', 'gradient': 'white_cream'},
    '25': {'name': 'Gradient: Lavanta-Mint', 'gradient': 'lavender_mint'},
    '26': {'name': 'Gradient: Mint-Lavanta', 'gradient': 'mint_lavender'},
    '27': {'name': 'Gradient: Şeftali-Krem', 'gradient': 'peach_cream'},
    '28': {'name': 'Gradient: Krem-Şeftali', 'gradient': 'cream_peach'},
    '29': {'name': 'Gradient: Açık Mavi-Beyaz', 'gradient': 'lightblue_white'},
    '30': {'name': 'Gradient: Beyaz-Açık Mavi', 'gradient': 'white_lightblue'},
    '31': {'name': 'Gradient: Mint-Açık Yeşil', 'gradient': 'mint_lightgreen'},
    '32': {'name': 'Gradient: Açık Yeşil-Mint', 'gradient': 'lightgreen_mint'},
    '33': {'name': 'Gradient: Açık Pembe-Krem', 'gradient': 'lightpink_cream'},
    '34': {'name': 'Gradient: Krem-Açık Pembe', 'gradient': 'cream_lightpink'},
    '35': {'name': 'Gradient: Somon-Krem', 'gradient': 'salmon_cream'},
    '36': {'name': 'Gradient: Krem-Somon', 'gradient': 'cream_salmon'},
    '37': {'name': 'Gradient: Lavanta-Beyaz', 'gradient': 'lavender_white'},
    '38': {'name': 'Gradient: Beyaz-Lavanta', 'gradient': 'white_lavender'},
    '39': {'name': 'Gradient: Açık Sarı-Krem', 'gradient': 'lightyellow_cream'},
    '40': {'name': 'Gradient: Krem-Açık Sarı', 'gradient': 'cream_lightyellow'}
}

def create_gradient(size, gradient_type):
    """Gradient arka plan oluşturur"""
    width, height = size
    
    # Gradient renk tanımları - Daha belirgin geçişler
    gradients = {
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
    
    if gradient_type not in gradients:
        return None
    
    color1, color2 = gradients[gradient_type]
    
    # Gradient oluştur
    gradient_img = Image.new('RGB', (width, height))
    pixels = gradient_img.load()
    
    for y in range(height):
        # Y pozisyonuna göre renk karışımı
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    return gradient_img

def get_background_color():
    """Kullanıcıdan arka plan rengi seçmesini ister"""
    print("\n=== Arka Plan Rengi Seçimi ===")
    print("Lütfen arka plan rengini seçin:")
    
    for key, value in BACKGROUND_COLORS.items():
        print(f"{key}. {value['name']}")
    
    while True:
        choice = input("\nSeçiminizi yapın (1-40): ").strip()
        if choice in BACKGROUND_COLORS:
            selected = BACKGROUND_COLORS[choice]
            print(f"\nSeçilen arka plan rengi: {selected['name']}")
            return selected
        else:
            print("Geçersiz seçim! Lütfen 1-40 arasında bir sayı girin.")

# Klasörleri oluştur
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Desteklenen resim uzantıları
image_extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.PNG']

def main():
    """Ana fonksiyon - komut satırından çalıştırıldığında çağrılır"""
    try:
        # Input klasöründeki resimleri bul
        image_files = [f for f in os.listdir(INPUT_DIR) if os.path.splitext(f)[1] in image_extensions]

        if not image_files:
            print("Input klasöründe resim bulunamadı!")
            return

        print(f'Input klasöründe bulunan resimler: {image_files}')

        # Kullanıcıdan arka plan rengi seçmesini iste
        background_selection = get_background_color()

        for img_file in image_files:
            input_path = os.path.join(INPUT_DIR, img_file)
            output_path = os.path.join(OUTPUT_DIR, os.path.splitext(img_file)[0] + '.png')
            try:
                input_image = Image.open(input_path)
                output_image = remove(input_image)
                
                if 'gradient' in background_selection:
                    # Gradient arka plan
                    gradient_bg = create_gradient(output_image.size, background_selection['gradient'])
                    if gradient_bg:
                        # Gradient'i RGBA'ya çevir
                        gradient_rgba = gradient_bg.convert('RGBA')
                        # Resmi gradient üzerine yapıştır
                        gradient_rgba.paste(output_image, mask=output_image.split()[3])
                        gradient_rgba.convert('RGB').save(output_path)
                        print(f'{img_file} -> {output_path} (gradient arka plan: {background_selection["name"]})')
                elif 'color' not in background_selection or background_selection['color'] is None:
                    # Şeffaf arka plan - PNG olarak kaydet
                    output_image.save(output_path, 'PNG')
                    print(f'{img_file} -> {output_path} (arka plan şeffaf)')
                else:
                    # Düz renkli arka plan
                    bg = Image.new('RGBA', output_image.size, (*background_selection['color'], 255))
                    bg.paste(output_image, mask=output_image.split()[3])
                    bg.convert('RGB').save(output_path)
                    print(f'{img_file} -> {output_path} (arka plan {background_selection["name"].lower()}landı)')
                    
            except Exception as e:
                print(f'Hata oluştu ({img_file}): {e}')
        
        print("\nİşlem tamamlandı! Çıktı dosyaları 'output' klasöründe bulunabilir.")
        
    except KeyboardInterrupt:
        print("\nİşlem kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")

if __name__ == "__main__":
    main() 