import errno
import os

def write_file(path, file, text):
    output = open(path+file, 'w')
    output.write(str(text))
    output.close()
    return output

def append_file(path, file, text):
    output = open(path+file, 'a')
    text = str(text)
    output.write(text)
    output.close()
    return output

def create_directory(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

def write_file_xml(path, file, text):
    output = open(path+file, 'w')
    output.write(text.decode("utf8"))
    output.closed
    return output

def read_file(path, file):
    output = open(path+file, 'r')
    return output.read()
