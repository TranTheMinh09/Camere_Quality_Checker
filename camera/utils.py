import os

def get_next_image_index(folder="captured", prefix="image_", ext=".jpg"):
    if not os.path.exists(folder):
        return 1

    existing_files = os.listdir(folder)
    indices = []

    for filename in existing_files:
        if filename.startswith(prefix) and filename.endswith(ext):
            number_part = filename[len(prefix):-len(ext)]
            if number_part.isdigit():
                indices.append(int(number_part))

    return max(indices) + 1 if indices else 1
