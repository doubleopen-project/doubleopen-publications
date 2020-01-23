# Double Open Feasibility Study

Version 0.1

The Double Open proof of concept is approaching the compliance issues of Embedded Linux and Yocto with two different approaches. A feasibility study is made to evaluate which of these two is more viable option. Neither will be totally ruled out, as the Double Open proof of concept is ultimately a modular approach.

## Basic statistics of the used build environment

* Yocto Project version 3.0
* BitBake Build Tool Core version 1.44.0
* Ubuntu 18.04.3 LTS

## File level approach

The file level approach is designed to get the license information for only those files within open source packages that are redistributed. This will rule out many potentially incompliant files due to the fact that many compliance issues are located in areas of the package that are not usually distributed with the end product. The idea is to focus the compliance check on files that come out of the build. This might enable the use of some open source packages, which with a preliminary compliance check would have otherwise been ruled out as incompliant to the organizations open source policy.

### Extracting file data from build

#### dwarfsrcfiles

First encountered issue is, how do we manage to extract file data from the Yocto build. We encountered a recipe called dwarfsrcfiles. This has the ability to extract file information from build and form a list of said files.

Dwarfsrcfiles can be included in the build process by patching package.bbclass recipe with two patches made by Richard Purdie, [patch 1](http://git.yoctoproject.org/cgit.cgi/poky-contrib/commit/?h=rpurdie/license-experiments-osls&id=51f58f4caa9d70a7621009d9ea59bbbf5e3928b2) and [patch 2](http://git.yoctoproject.org/cgit.cgi/poky-contrib/commit/?h=rpurdie/license-experiments-osls&id=bf9305ad33791536c3db4fc3e11b5d698d928cd9). These patches generate *.srclist and *. filelics files during the do_package step of the build, and they are generated for each package included in the build. These files can be found in /build/tmp/pkgdata/\<MACHINE>. Examples of both file types can be found in the Example-files directory.

Srclist file includes a list of all [ELF files](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) of the package in question and all source files for each ELF file, as determined by dwarfsrcfiles.

##### acl.srclist
```json
{
    "/home/yocto/poky/build/tmp/work/core2-64-poky-linux/acl/2.2.52-r0/package/lib/libacl.so.1.1.0": [
        "/usr/src/debug/glibc/2.30-r0/git/sysdeps/x86_64/crti.S",
        "/usr/src/debug/acl/2.2.52-r0/acl-2.2.52/libacl/acl_add_perm.c",
        "/usr/include/errno.h",
        "/usr/src/debug/acl/2.2.52-r0/acl-2.2.52/include/sys/acl.h"
    ],
    "/home/yocto/poky/build/tmp/work/core2-64-poky-linux/acl/2.2.52-r0/package/usr/bin/chacl": [
        "/usr/src/debug/glibc/2.30-r0/git/sysdeps/x86_64/start.S",
        "/usr/src/debug/glibc/2.30-r0/git/csu/init.c",
        "/usr/src/debug/glibc/2.30-r0/git/sysdeps/x86_64/crti.S",
        "/usr/src/debug/acl/2.2.52-r0/acl-2.2.52/chacl/chacl.c"
    ]
}
```

Our method for getting all of the source files in the build is to loop over all srclist files in the build and extract the source file names.

This step of the process can be included in the build process by modifying the patches previously mentioned. For the Proof of Concept, we've decided to utilize standalone Python scripting for the benefit of development time.

The end result of this step is a list of all source files in all packages of the build output.

#### SHA-256

The next step is to convert the list of files into a list of unique hash values (SHA-256). This should be implemented to the previously mentioned patches to calculate the hash values during the build. For the Proof of Concept, we've decided to utilize standalone Python scripting. Current version of our script `hash_list.py` can be found in the Code folder.

The script iterates over all of the srclist files in the build and calculates the hash (currenlty SHA256) for all source files of all ELF files in each list. The result is then printed to a json file, preserving names of the srclist files, paths of the ELF files and paths of the source files, as provided by dwarfsrcfiles. Finding the correct source file with the provided path proved to be a complicated matter. The script is currently configured to look for the files in four possible locations.

An example of the output format can be found below.

##### hash_list.json

```json
{
    "acl.srclist": {
        "/home/yocto/poky/build/tmp/work/core2-64-poky-linux/acl/2.2.52-r0/package/lib/libacl.so.1.1.0": {
            "/usr/include/attr/error_context.h": "73aed837d2440b941266c854844a1d834dd2ee9bd8545de24d5aa322f48a319e",
            "/usr/include/attr/xattr.h": "0da8f0b3bedb511e3a3fb0cfd5562c22abde9f12f81c42e6b4d1e0d21ecdb501",
            "/usr/include/bits/dirent.h": "e73c3c2488d14685339bbc68d3d39660423ffd4aa6468157cbdabf2b0de822b6",
        },
        "/home/yocto/poky/build/tmp/work/core2-64-poky-linux/acl/2.2.52-r0/package/usr/bin/chacl": {
            "/usr/include/bits/dirent.h": "e73c3c2488d14685339bbc68d3d39660423ffd4aa6468157cbdabf2b0de822b6",
            "/usr/include/bits/getopt_core.h": "1923be731ac79fb7449c431ddf45f2ca3b2f7ad82eeacc9e8101e8fe7c2ffd6e",
            "/usr/include/bits/stdio2.h": "da7ee4876646a5f056ebe3f4cfbd62f2feaf6c01acc9346772c749df03d7dcd7",
        }
    },
    "alsa-lib.srclist": {
        "/home/yocto/poky/build/tmp/work/core2-64-poky-linux/alsa-lib/1.1.9-r0/package/usr/bin/aserver": {
            "/usr/include/asm-generic/int-ll64.h": "eb8b891e775ebb50af0353fdcbc625854fd98780399b3a57a404d36af6c29749",
            "/usr/include/asm-generic/posix_types.h": "0b94eebdf4488407d32fa199136f302653ab51a2843bd68dee24c38c9f0ce82e",
            "/usr/include/assert.h": "10d935dbd217e52c0bcddd5a8301b4d4d7536296c8e4c7162a01c1e9c4329807",
        }
    }
}
```

### Extracting file level data from Fossology via REST query

Extracting file level licencing data from Fossology is not currently possible by hash values.