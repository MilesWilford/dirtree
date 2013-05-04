import os.path
import os

if os.name == 'nt':
    import win32api, win32con


def folder_is_hidden(p):
    if os.name== 'nt':
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux

def dir_string(dirname, files):
    depth = dirname.count(os.sep)
    files = [f for f in files if not f.startswith('.')]
    fs = sorted([fname for fname in files if os.path.isfile(os.path.join(dirname, fname))])
    ds = sorted([os.path.join(dirname, dname) for dname in files if os.path.isdir(os.path.join(dirname, dname))])
    return os.path.basename(dirname) + os.linesep + \
        (os.linesep).join(['\t' + filename for filename in fs]) + os.linesep + \
        (os.linesep).join(['\t' + dir_string(d, os.listdir(d)).replace(os.linesep, os.linesep + '\t') for d in ds])

if __name__ == "__main__":
    with open('filetree.txt', 'w') as f:
        f.write(dir_string(os.getcwd(), os.listdir(os.getcwd())))
