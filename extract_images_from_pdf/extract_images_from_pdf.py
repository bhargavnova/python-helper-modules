import os
import fitz
import io
from PIL import Image

def extract_images_from_pdf(pdf_path):
    main_out_path = 'IMAGES_FROM_PDF/'
    os.makedirs(main_out_path, exist_ok=True)

    slug = pdf_path.split('/')[-1].split('.pdf')[0]
    images_path = main_out_path + slug
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    pdf_file = fitz.open(pdf_path)

    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        # get image list
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(image_list, start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open( images_path + '/'+ slug +'_'+ str(page_index+1).zfill(3) + '.' + image_ext, "wb"))

if __name__ == "__main__":
    input_file = 'sample-pdf-with-images.pdf'
    extract_images_from_pdf(input_file)
