import os
import json
import hashlib

BUF_SIZE = 65536

# https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
def calculate_sha256(file):
    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def try_sha256(elf_file_folder, source_file):
    try:
        return calculate_sha256(elf_file_folder + '/package' + source_file)
    except:
        try:
            return calculate_sha256(elf_file_folder + '/recipe-sysroot' + source_file)
        except:
            try:
                return calculate_sha256(elf_file_folder + '/recipe-sysroot-native' + source_file)
            except:
                try:
                    return calculate_sha256("/home/yocto/poky/build/tmp/work/core2-64-poky-linux/" + "/".join(source_file.split("/", 4)[4:]))
                except:
                    return "No SHA256 available"

hash_dictionary = {}

# Loop over all srclist files and extract the data.
for file in os.listdir(os.curdir):
    if file.endswith('.srclist'):
        with open(file) as srclist_file:
            hash_dictionary[file] = {}
            data = json.load(srclist_file)

            # Loop over all ELF files in srclist.
            for elf_file, source_files in data.items():
                hash_dictionary[file][elf_file] = {}
                elf_file_folder = "/".join(elf_file.split("/", 10)[:10])

                # Loop over all source files of the ELF file.
                for source_file in source_files:
                    hash_dictionary[file][elf_file][source_file] = try_sha256(elf_file_folder, source_file)

with open('hash_list.json', 'w') as outfile:
    json.dump(hash_dictionary, outfile, indent=4, sort_keys=True)

# DEBUG
# print(json.dumps(hash_dictionary, sort_keys=True, indent=4))