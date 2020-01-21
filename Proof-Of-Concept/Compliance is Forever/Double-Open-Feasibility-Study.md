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

#### SHA-256

The next step is to convert the list of files into a list of unique hash values (SHA-256). This was done by...

### Extracting file level data from Fossology via REST query