import zipfile
import os

def create_zip(files, output):

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as z:

        for file in files:
            z.write(file, os.path.basename(file))
