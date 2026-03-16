import os

def split_file(file, size):

    parts = []

    with open(file,"rb") as f:

        i = 1

        while True:

            chunk = f.read(size)

            if not chunk:
                break

            part_name = f"{file}.part{i}"

            with open(part_name,"wb") as p:
                p.write(chunk)

            parts.append(part_name)
            i+=1

    return parts
