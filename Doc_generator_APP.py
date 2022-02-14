
import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from lib.Doc_generator import Doc_generator

#====================================================================================================================


class Doc_generator_APP(QtWidgets.QWidget):


    def __init__(self):
        super(Doc_generator_APP, self).__init__()
        print('SCRIPT START\n')
        
        doc_generator = Doc_generator()
        print(doc_generator.get_name() + '\n')
        TEMPLATES_keys_list = list(doc_generator.TEMPLATES.keys())
        for i in range(len(TEMPLATES_keys_list)):
            print(str(i+1) + ') ' + TEMPLATES_keys_list[i].replace('.docx', ''))
        temptate_idx = input("wybierz szablon: ")
        template_file_name = TEMPLATES_keys_list[int(temptate_idx) - 1]
        
        config_file_path = QFileDialog.getOpenFileName(self, 'select config file', 'example', 'Text files (*.txt)')
        if config_file_path and os.path.exists(config_file_path[0]):
            doc_generator.make_doc_by_config_file_path(template_file_name, config_file_path[0])
        else:
            print('config_file_path is None or file not exsists')
            
        print('\nSCRIPT STOP')


#====================================================================================================================


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    doc_generator_app = Doc_generator_APP()
    sys.exit(app.exec_())

