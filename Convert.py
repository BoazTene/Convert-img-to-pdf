import  os
from PIL import Image
import sys


class ConvertToPdf:
    def __init__(self, images_path, output_full_path):
        self.images_path = images_path
        self.output_path = output_full_path
        self.images = []
        
    def load_images(self):
        for i in range(len(self.images_path)):
            try:
                print(i)
                self.images.append(Image.open(self.images_path[i]))
                self.images[-1].convert('RGB')
            except MemoryError:
                print("MemoryError")
                break
     
    def save(self):
        img = self.images[0]
        self.images.pop(0)
        img.save(self.output_path, save_all=True, append_images=self.images)
    

if __name__ == "__main__":
    output_path = input("Enter the full output path:")
    images = []
    print("To exit stop adding images press enter with nothing")
    
    while True:
        user_input = input("Enter path to your image: ")
        if user_input == "":
            break
          
        images.append(user_input)
        
    input("Press Enter to save the pdf...")
    
    convert_to_pdf = ConvertToPdf(images, output_path)
    
    convert_to_pdf.load_images()
    
    convert_to_pdf.save()