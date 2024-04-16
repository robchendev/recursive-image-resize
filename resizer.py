import os
import argparse
from PIL import Image

def resize_image(file_path, max_dimension):
  with Image.open(file_path) as img:
    width, height = img.size
    if height > max_dimension or width > max_dimension:
      if width > height: # Resize by width if width is greater
        new_width = min(width, max_dimension)
        new_height = int((new_width / width) * height)
      else: # Resize by height otherwise
        new_height = min(height, max_dimension)
        new_width = int((new_height / height) * width)
      resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
      resized_img.save(file_path)
      print(f"Resized {file_path} to {new_width}x{new_height} pixels.")

def delete_file(file_path):
  os.remove(file_path)
  print(f"Deleted file: {file_path}")

def walk_directory(directory, max_dimension, delete_non_images):
  image_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'}
  for root, directories, files in os.walk(directory):
    for file in files:
      file_path = os.path.join(root, file)
      extension = os.path.splitext(file)[1].lower()
      if extension in image_extensions:
        resize_image(file_path, max_dimension)
      elif delete_non_images:
        delete_file(file_path)

def main():
  parser = argparse.ArgumentParser(description="Resize images to a specified maximum dimension, and optionally delete non-image files in a directory.")
  parser.add_argument('max_dimension', type=int, help='Maximum dimension for both width and height of the images')
  parser.add_argument('directory', type=str, help='Directory to operate on')
  parser.add_argument('--delete', action='store_true', help='Delete all non-image files', default=False)
  args = parser.parse_args()
  walk_directory(args.directory, args.max_dimension, args.delete)

if __name__ == "__main__":
  main()
