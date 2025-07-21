# Background Remover

Bu proje, resimlerin arka planını otomatik olarak kaldıran bir Python uygulamasıdır.

## Özellikler

- `input/` klasöründeki resimlerin arka planını kaldırır
- Desteklenen formatlar: JPG, JPEG, PNG
- Çıktı resimleri `output/` klasörüne kaydedilir
- 40 farklı arka plan seçeneği:
  - **Düz Renkler:** Beyaz, Siyah, Şeffaf, Açık Gri, Koyu Gri
  - **Krem Tonları:** Krem, Açık Krem, Sıcak Krem, Bej, Fildişi, Antik Beyaz
  - **Soft Renkler:** Mint Yeşili, Lavanta, Şeftali, Açık Mavi, Açık Pembe, Somon, Açık Sarı, Açık Turuncu, Açık Mor, Açık Yeşil, Açık Kahverengi
  - **Gradient Arka Planlar:** 18 farklı yumuşak gradient seçeneği (her gradient'in ters versiyonu da mevcut)

## Kurulum

1. Virtual environment oluşturun:
```bash
python3 -m venv venv
```

2. Virtual environment'ı aktif edin:
```bash
source venv/bin/activate
```

3. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

1. Arka planını kaldırmak istediğiniz resimleri `input/` klasörüne koyun
2. Scripti çalıştırın:
```bash
python3 bg_remover.py
```
3. Açılan menüden arka plan rengini seçin (1-40)
4. İşlenmiş resimler `output/` klasöründe bulunacaktır

## Renk Seçenekleri

### Düz Renkler
| No | Renk Adı | RGB Kodu | Hex Kodu |
|----|----------|----------|----------|
| 1 | Beyaz | (255, 255, 255) | #FFFFFF |
| 2 | Siyah | (0, 0, 0) | #000000 |
| 3 | Şeffaf | - | - |
| 4 | Açık Gri | (240, 240, 240) | #F0F0F0 |
| 5 | Koyu Gri | (64, 64, 64) | #404040 |

### Krem Tonları
| No | Renk Adı | RGB Kodu | Hex Kodu |
|----|----------|----------|----------|
| 6 | Krem | (255, 253, 240) | #FFFDF0 |
| 7 | Açık Krem | (255, 250, 230) | #FFFAE6 |
| 8 | Sıcak Krem | (255, 248, 220) | #FFF8DC |
| 9 | Bej | (245, 245, 220) | #F5F5DC |
| 10 | Fildişi | (255, 255, 240) | #FFFFF0 |
| 11 | Antik Beyaz | (250, 235, 215) | #FAEBD7 |

### Soft Renkler
| No | Renk Adı | RGB Kodu | Hex Kodu |
|----|----------|----------|----------|
| 12 | Mint Yeşili | (152, 251, 152) | #98FB98 |
| 13 | Lavanta | (230, 230, 250) | #E6E6FA |
| 14 | Şeftali | (255, 218, 185) | #FFDAB9 |
| 15 | Açık Mavi | (173, 216, 230) | #ADD8E6 |
| 16 | Açık Pembe | (255, 182, 193) | #FFB6C1 |
| 17 | Somon | (250, 128, 114) | #FA8072 |
| 18 | Açık Sarı | (255, 255, 224) | #FFFFE0 |
| 19 | Açık Turuncu | (255, 218, 185) | #FFDAB9 |
| 20 | Açık Mor | (221, 160, 221) | #DDA0DD |
| 21 | Açık Yeşil | (144, 238, 144) | #90EE90 |
| 22 | Açık Kahverengi | (210, 180, 140) | #D2B48C |

### Gradient Arka Planlar (Belirgin Geçişler)
| No | Gradient Adı | Renkler | Açıklama |
|----|--------------|---------|----------|
| 23 | Krem-Beyaz | #FFFDF0 → #FFFFFF | Yumuşak geçiş |
| 24 | Beyaz-Krem | #FFFFFF → #FFFDF0 | Yumuşak geçiş |
| 25 | Lavanta-Mint | #9370DB → #98FB98 | Mor-Yeşil geçiş |
| 26 | Mint-Lavanta | #98FB98 → #9370DB | Yeşil-Mor geçiş |
| 27 | Şeftali-Krem | #FFA07A → #FFFDF0 | Turuncu-Krem geçiş |
| 28 | Krem-Şeftali | #FFFDF0 → #FFA07A | Krem-Turuncu geçiş |
| 29 | Açık Mavi-Beyaz | #6495ED → #FFFFFF | Mavi-Beyaz geçiş |
| 30 | Beyaz-Açık Mavi | #FFFFFF → #6495ED | Beyaz-Mavi geçiş |
| 31 | Mint-Açık Yeşil | #98FB98 → #228B22 | Açık-Koyu Yeşil geçiş |
| 32 | Açık Yeşil-Mint | #228B22 → #98FB98 | Koyu-Açık Yeşil geçiş |
| 33 | Açık Pembe-Krem | #FF69B4 → #FFFDF0 | Pembe-Krem geçiş |
| 34 | Krem-Açık Pembe | #FFFDF0 → #FF69B4 | Krem-Pembe geçiş |
| 35 | Somon-Krem | #DC143C → #FFFDF0 | Kırmızı-Krem geçiş |
| 36 | Krem-Somon | #FFFDF0 → #DC143C | Krem-Kırmızı geçiş |
| 37 | Lavanta-Beyaz | #8A2BE2 → #FFFFFF | Mor-Beyaz geçiş |
| 38 | Beyaz-Lavanta | #FFFFFF → #8A2BE2 | Beyaz-Mor geçiş |
| 39 | Açık Sarı-Krem | #FFD700 → #FFFDF0 | Altın-Krem geçiş |
| 40 | Krem-Açık Sarı | #FFFDF0 → #FFD700 | Krem-Altın geçiş |

## Gereksinimler

- Python 3.7+
- Pillow (PIL)
- rembg
- onnxruntime

## Notlar

- İlk çalıştırmada rembg modeli indirilecektir (internet bağlantısı gerekir)
- İşlem süresi resim boyutuna ve sistem performansına bağlıdır

## Lisans

Bu proje MIT License altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## İletişim

- GitHub: [@mertcaliskan](https://github.com/mertcaliskan01)
- Proje Linki: [https://github.com/mertcaliskan01/remove-bg](https://github.com/mertcaliskan01/remove-bg) 