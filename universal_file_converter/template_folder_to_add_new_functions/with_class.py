class YourFunctionName(object):

    def __init__(self, file_path, out_path):
        self.file_path = file_path
        self.out_path = out_path

    #change ext1 and ext2 according to your function 
    #(only this one should be done carefully, you can do anything you want for rest.)
    def convert_ext1_to_ext2(self):
        pass

if __name__ == "__main__":
    file_name = 'file_path.ext1'
    out_path = 'file_path.ext2'
    srt_object = YourFunctionName(file_name, out_path)
    srt_object.convert_ext1_to_ext2()