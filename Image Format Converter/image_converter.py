#using aspose-words python module
import aspose.words

#file formats
choose_format=["png", "jpeg", "jpg", "gif", "webp", "tiff", "pdf"]

#printing list to show popular options to user
print(choose_format)

cf=input("Type the format you want to convert to: ")
inp=input("Type the file path which you want to convert: ")
out=input("Type the file path to which you want to convert: ")

#defning main function
def convert_image(i,o,cf):
    doc = aspose.words.Document()
    builder = aspose.words.DocumentBuilder(doc)
    shape = builder.insert_image(i)
    l=inp.split('.')
    l.pop()
    l.append(cf)
    s='.'
    k=s.join(l)
    shape.image_data.save(k)

#defining condition for unmatching image extension

v=out.split('.')
if cf==v[1]:
    convert_image(inp,out,cf)
else:
    print('ERROR: chosen file format and saving file path extension do not match.')
