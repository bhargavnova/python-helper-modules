import json
import os

def divide(json_file, chunk_size=1, output_folder='output_folder', custom_names=[]):

  data = json.load(open(json_file))

  fileIndex=1
  for i in range(0,len(data), chunk_size):
    jsonSplit = data[i:i+chunk_size]

    filename =  'part'+ str(fileIndex)+ '.json'

    if fileIndex-1 < len(custom_names):
      filename=custom_names[fileIndex-1]

    fileIndex = fileIndex + 1
    
    path = output_folder + '/' + filename

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as outfile:
      outfile.write(json.dumps(jsonSplit))