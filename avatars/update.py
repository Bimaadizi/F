import os
from PIL import Image

def convert_bmp_to_jpg(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.bmp'):
                bmp_path = os.path.join(subdir, file)
                jpg_path = os.path.splitext(bmp_path)[0] + '.jpg'
                
                try:
                    with Image.open(bmp_path) as img:
                        rgb_img = img.convert('RGB')  # Ensure no alpha channel
                        rgb_img.save(jpg_path, 'JPEG', quality=95, optimize=True)
                    print(f"Converted: {bmp_path} -> {jpg_path}")
                except Exception as e:
                    print(f"Failed to convert {bmp_path}: {e}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    convert_bmp_to_jpg(current_dir)
