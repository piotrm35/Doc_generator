# python .\Doc_generator_AUTO.py umowa_dzierżawa_roboty.docx ./example/CONFIG_EXAMPLE_UTF-8.txt


import sys
from lib.Doc_generator import Doc_generator


print('SCRIPT START\n')

template_file_name = None
config_file_path = None

for i, arg in enumerate(sys.argv):
    if i == 1:
        template_file_name = arg
        print('template_file_name: ' + template_file_name)
    if i == 2:
        config_file_path = arg
        print('config_file_path: ' + config_file_path)
    if template_file_name and config_file_path:
        doc_generator = Doc_generator()
        res = doc_generator.make_doc_by_config_file_path(template_file_name, config_file_path)
        if res:
            print("{'result': '" + str(res) + "'}")
        else:
            print("{'result': 'ERROR'}")
        break

print('\nSCRIPT STOP')
            
