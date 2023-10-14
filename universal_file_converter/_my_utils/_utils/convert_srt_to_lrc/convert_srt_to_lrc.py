class ConvertSRTtoLRC(object):

    def __init__(self, file_path, out_path):
        self.file_path = file_path
        self.out_path = out_path

    def remove_certain_character(self, list_data, character):
        return [l_d for l_d in list_data if l_d != character]

    def split_index_to_tuple(self,list_index):
        list_tuple_index = []
        for l_i,l_data in enumerate(list_index):
            try:
                list_tuple_index.append((l_data,list_index[l_i+1]))
            except IndexError:
                list_tuple_index.append((l_data,'end'))
        return list_tuple_index

    def get_dict(self):
        with open(self.file_path,'r') as srt_file:
            srt_data = srt_file.readlines()

        #Reomve '\n' for srt_data
        data_without_n = [d.strip() for d in self.remove_certain_character(srt_data,'\n')]
        data_index_list = []
        data_dict = {}

        #Find index of integer from srt data , ex : 1, 2, 3
        for d_index,d in enumerate(data_without_n):
            try:
                int(d)
                data_index_list.append(d_index)
            except ValueError:
                pass

        #Get data index tuple like : [(1,3),(3,6),.....]
        data_index_tuple = self.split_index_to_tuple(data_index_list)

        for index_tuple in data_index_tuple:
            if index_tuple[1] != 'end':
                data = data_without_n[index_tuple[0]:index_tuple[1]]
                try:
                    data_dict[str(data[0])] = {data[1]:' '.join(data[2:]).replace('[','').replace(']','')}
                except IndexError:
                    print(data)
            else:
                data = data_without_n[index_tuple[0]:]
                try:
                    data_dict[str(data[0])] = {data[1]:' '.join(data[2:]).replace('[','').replace(']','')}
                except IndexError:
                    print(data)
        return data_dict

    def convert_dict_to_lrc(self,data_dict):
        out_lrc_data_string = ''
        for d_i,d_d in data_dict.items():
            for l_i,l_d in d_d.items():
                first_t_stamp=l_i.split('-->')[0].strip()
                t_stamp_list=first_t_stamp.split(':')
                if t_stamp_list[0] == '00':
                    t_stamp_list.pop(0)
                    first_t = t_stamp_list[0]
                    second_t = t_stamp_list[1].split(',')[0]
                    third_t = t_stamp_list[1].split(',')[1]
                    main_t_stamp = "[" + first_t + ":" + second_t + "." + third_t + "]"
                else:
                    first_t = t_stamp_list[0]
                    second_t = t_stamp_list[1]
                    third_t = t_stamp_list[1].split(',')[0]
                    forth_t = t_stamp_list[1].split(',')[1]
                    main_t_stamp = "[" + first_t + ":" + second_t + ":" + third_t + "." + forth_t + "]"
                str_string = main_t_stamp+l_d+'\n'
                out_lrc_data_string += str_string
        return out_lrc_data_string

    def convert_srt_to_lrc(self):
        data_dict= self.get_dict()
        lrc_data = self.convert_dict_to_lrc(data_dict)
        print('[+] Making lrc file from srt .....')
        with open(self.out_path, 'w') as lrc_f:
            lrc_f.write(lrc_data)

if __name__ == "__main__":
    file_name = 'zen_of_python.srt'
    out_path = 'zen_of_python.lrc'
    srt_object = ConvertSRTtoLRC(file_name, out_path)
    srt_object.convert_srt_to_lrc()
