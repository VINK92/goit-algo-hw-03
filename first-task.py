import os
import shutil
import argparse

def copy_and_move_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isdir(source_path):
            copy_and_move_files(source_path, dest_path)
        else:
            _, extension = os.path.splitext(item)
            extension_dir = os.path.join(dest_dir, extension[1:])
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            try:
                shutil.copy2(source_path, extension_dir)
                print(f"Копіювання {item} завершено")
                shutil.move(source_path, dest_dir)
                print(f"Переміщення {item} завершено")
            except Exception as e:
                print(f"Помилка копіювання або переміщення {item}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Копіювання файлів та переміщення їх у нову директорію')
    parser.add_argument('source_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення')
    args = parser.parse_args()
    copy_and_move_files(args.source_dir, args.dest_dir)
