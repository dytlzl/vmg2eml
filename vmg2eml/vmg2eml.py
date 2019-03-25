import sys
from .functions import create_dir


class Convert:
    DIR_NAME = './EMLs/'

    def __init__(self):
        try:
            self.in_filename = sys.argv[1]
        except IndexError:
            print('A command-line argument(path to VMG file) required.')
            sys.exit()
        self.count = 0
        self.out_data = ''
        create_dir(self.DIR_NAME)

    def convert(self):
        with open(self.in_filename, mode='r', encoding='shift-jis') as file:
            for line in file.readlines():
                if 'END:VBODY' in line:
                    count_str = str(self.count)
                    f_name = self.DIR_NAME + count_str.zfill(10) + '.eml'
                    with open(f_name, mode='w') as f:
                        f.write(self.out_data)
                self.out_data += line
                if 'BEGIN:VBODY' in line:
                    print('\rConvert # %s' % self.count, end='')
                    self.out_data = ''
                    self.count += 1
        print('\nDone.')
