from random import choice, sample, randint
from string import ascii_letters, digits, ascii_lowercase
import csv
import json

class FileWriter:
    def __init__(self, filename_with_path, file_data=None):
        self.filename_with_path = filename_with_path
        self.filedata = file_data
#########################################################################
    def _txt(self):
        my_string = ''.join(choice(ascii_letters + digits + chr(32) + chr(44) + chr(45) + chr(58) + chr(59)) for i in range(randint(100, 1000)))
        indexes = [i for i in range(len(my_string))]
        sam = sample(indexes, 9)
        my_list = list(my_string)
        for i in sam:
            my_list[i] = chr(10)
        return ''.join(my_list)

    def _write_txt(self):
        f = open(self.filename_with_path, 'w')
        if not self.filedata:
            f.write(self._txt())
        else:
            f.write(self.filedata)

##################################################
    def _get_randvalue(self):
        my_list = [randint(-100, 100), randint(0, 100) / 100, bool(randint(0, 1))]
        return choice(my_list)

    def _get_dict(self):
        my_list = [''.join(choice(ascii_lowercase) for i in range(5)) for i in range(randint(5, 20))]
        my_dict = {key: self._get_randvalue() for key in my_list}
        return my_dict

    def _write_json(self):
        if not self.filedata:
            my_json = json.dumps(self._get_dict())
        else:
            my_json = json.dumps(self.filedata)

        with open(self.filename_with_path, 'w') as json_file:
            json.dump(my_json, json_file, indent=2)

        with open(self.filename_with_path, 'r') as json_file:
            json.load(json_file)
##########################################
    def _get_value(self):
        return randint(0, 1)

    def _get_randints(self):
        return randint(3, 10)

    def _get_list(self):
        my_list = [self._get_value() for _ in range(self._get_randints())]
        return my_list

    def _get_data(self):
        data = [self._get_list() for _ in range(self._get_randints())]
        return data

    def _write_csv(self):
        with open(self.filename_with_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=";")
            if not self.filedata:
                csvwriter.writerows(self._get_data())
            else:
                csvwriter.writerows(self.filedata)
################################################
    def _file_writer(self):
        mode = self.filename_with_path.rsplit(".")[-1]
        if mode == "txt":
            self._write_txt()
        elif mode == "json":
            self._write_json()
        elif mode == "csv":
            self._write_csv()
        else:
            raise Exception("Unsupported file format!")

    def write(self):
        return self._file_writer()

my_class = FileWriter('test.csv', [['dsgdhfdfhsssssssssssss'],['swvwe']])
my_class.write()



