import os.path
import os

def dir_string(dirname, files):
    depth = dirname.count(os.sep)
    fs = [fname for fname in files if os.path.isfile(os.path.join(dirname, fname))]
    ds = [os.path.join(dirname, dname) for dname in files if os.path.isdir(os.path.join(dirname, dname))]
    return os.path.basename(dirname) + '\n' + \
        '\n'.join(['\t' + filename for filename in fs]) + \
        '\n\t'.join([dir_string(d, os.listdir(d)).replace('\n', '\n\t') for 
            d in ds])

if __name__ == "__main__":
    with open('filetree.txt', 'w') as f:
        f.write(dir_string(os.getcwd(), os.listdir(os.getcwd())))
