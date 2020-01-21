# Double Open Feasibility Study

Version 0.1

The Double Open proof of concept is approaching the compliance issues of Embedded Linux and Yocto with two different approaches. A feasibility study is made to evaluate which of these two is more viable option. Neither will be totally ruled out, as the Double Open proof of concept is ultimately a modular approach.

## Basic statistics of the used build environment

* Yocto Project version x.x
* BitBake version x.x
* Linux distribution version x.x

## File level approach

The file level approach is designed to get the license information for only those files within open source packages that are redistributed. This will rule out many potentially incompliant files due to the fact that many compliance issues are located in areas of the package that are not usually distributed with the end product. The idea is to focus the compliance check on files that come out of the build. This might enable the use of some open source packages, which with a preliminary compliance check would have otherwise been ruled out as incompliant to the organizations open source policy.

### Extracting file data from build

#### dwarfsrcfiles

First encountered issue is, how do we manage to extract file data from the Yocto build. We encountered a recipe called dwarfsrcfiles. This has the ability to extract file information from build and form a list of said files.

Dwarfsrcfiles can be included in the build process by patching package.bbclass recipe with two patches made by Richard Purdie, [patch 1](http://git.yoctoproject.org/cgit.cgi/poky-contrib/commit/?h=rpurdie/license-experiments-osls&id=51f58f4caa9d70a7621009d9ea59bbbf5e3928b2) and [patch 2](http://git.yoctoproject.org/cgit.cgi/poky-contrib/commit/?h=rpurdie/license-experiments-osls&id=bf9305ad33791536c3db4fc3e11b5d698d928cd9). These patches generate *.srclist and *. filelics files during the do_package step of the build, and they are generated for each package included in the build. These files can be found in /build/tmp/pkgdata/\<MACHINE>. Examples of both file types can be found in the Example-files directory.

Srclist file includes a list of all [ELF files](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) of the package in question and all source files for each ELF file, as determined by dwarfsrcfiles.

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

The next step is to convert the list of files into a list of unique hash values (SHA-256). This should be implemented to the previously mentioned patches to calculate the hash values during the build. For the Proof of Concept, we've decided to utilize standalone Python scripting.



### Extracting file level data from Fossology via REST query