import os


def convert():
    name = ["grab.py"]
    os.system("pyinstaller --clean --onefile --noconsole -n{} webhook.py".format(name[0]))

convert()