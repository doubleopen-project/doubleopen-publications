#!/usr/bin/env python3
# Copyright (c) 2020 HH Partners, Attorneys-at-law Ltd
# SPDX-License-Identifier: MIT
# Author: Mikko Murto

import os
import json
import hashlib
import argparse
import glob

# Buffer size for hash calculation.
BUF_SIZE = 65536

# Build pkgdata folder.
pkgdata_folder = "/home/yocto/poky/build/tmp/pkgdata/qemux86-64/"

# Parse for '--debug' argument.
parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
debug = parser.parse_args().debug
if debug:
    print("DEBUG MODE ON!")

# Calculate SHA256 hash for a file.
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

# Try to calculate hash for all possible source file locations.
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
                    path = "/".join(elf_file_folder.split("/", 8)[:8])
                    return calculate_sha256(path + "/" + "/".join(source_file.split("/", 4)[4:]))
                    # "/home/yocto/poky/build/tmp/work/core2-64-poky-linux/"
                except:
                    return None

# Debug function, return hash for each location, None if not found at the location.
def debug_sha256(elf_file_folder, source_file):
    debug_dictionary = {}
    try:
        debug_dictionary['package'] = calculate_sha256(elf_file_folder + '/package' + source_file)
    except:
        debug_dictionary['package'] = None
    try:
        debug_dictionary['recipe-sysroot'] = calculate_sha256(elf_file_folder + '/recipe-sysroot' + source_file)
    except:
        debug_dictionary['recipe-sysroot'] = None
    try:
        debug_dictionary['recipe-sysroot-native'] = calculate_sha256(elf_file_folder + '/recipe-sysroot-native' + source_file)
    except:
        debug_dictionary['recipe-sysroot-native'] = None
    try:
        debug_dictionary['root'] = calculate_sha256(path + "/" + "/".join(source_file.split("/", 4)[4:]))
    except:
        debug_dictionary['root'] = None
    return debug_dictionary


hash_dictionary = {}

srclist_amount = len(glob.glob1(pkgdata_folder, '*.srclist'))
srclist_current_counter = 1

# Loop over all srclist files and extract the data.
for file in os.listdir(pkgdata_folder):
    if file.endswith('.srclist'):

        # Progress 
        print(f"Currently processing srclist {srclist_current_counter} of {srclist_amount} total.", end='\r')
        srclist_current_counter += 1

        with open(pkgdata_folder + file) as srclist_file:
            hash_dictionary[file] = {}
            data = json.load(srclist_file)

            # Loop over all ELF files in srclist.
            for elf_file, source_files in data.items():
                hash_dictionary[file][elf_file] = {}
                elf_file_folder = "/".join(elf_file.split("/", 10)[:10])

                # Loop over all source files of the ELF file.
                for source_file in source_files:
                    hash_dictionary[file][elf_file][source_file] = try_sha256(elf_file_folder, source_file)
                   
                    if debug:
                        hash_dictionary[file][elf_file][source_file] = debug_sha256(elf_file_folder, source_file)

print()

# Write the data to a file.
print('Writing data to hash_list.json.')
with open('hash_list.json', 'w') as outfile:
    json.dump(hash_dictionary, outfile, indent=4, sort_keys=True)
