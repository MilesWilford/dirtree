import os.path
import os

def dir_string(dirname, files):
    depth = dirname.count(os.sep)
    fs = [fname for fname in files if os.path.isfile(os.path.join(dirname, fname))]
    ds = [os.path.join(dirname, dname) for dname in files if os.path.isdir(os.path.join(dirname, dname))]
    return os.path.basename(dirname) + os.linesep + \
        (os.linesep).join(['\t' + filename for filename in fs]) + \
        (os.linesep + '\t').join([dir_string(d, os.listdir(d)).replace(os.linesep, os.linesep + '\t') for 
            d in ds])

if __name__ == "__main__":
    with open('filetree.txt', 'w') as f:
        f.write(dir_string(os.getcwd(), os.listdir(os.getcwd())))
