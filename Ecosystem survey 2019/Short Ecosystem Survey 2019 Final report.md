# Double Open Short Ecosystem Survey 2019 Final Report <!-- omit in toc -->
**UNDER DEVELOPMENT** <!-- omit in toc -->
---

- [Introduction](#introduction)
- [Participation and use of open compliance initiatives](#participation-and-use-of-open-compliance-initiatives)
- [Open tools in open source compliance](#open-tools-in-open-source-compliance)
- [Commercial tools in open source compliance](#commercial-tools-in-open-source-compliance)
- [Request and incident management tools](#request-and-incident-management-tools)
- [IDEs, Integrated Development Environments](#ides-integrated-development-environments)
- [Build tools, frameworks and dependency management](#build-tools-frameworks-and-dependency-management)
- [Package indexes and repositories](#package-indexes-and-repositories)
- [Document management](#document-management)
- [Testing frameworks](#testing-frameworks)
- [Container technologies](#container-technologies)
- [What is the size of your organization?](#what-is-the-size-of-your-organization)

## Introduction

Double Open launched the Double Open Short Ecosystem Survey 2019 to accumulate real life factual information from members of the open source ecosystem to investigate the existing landscape, and popularity of open source compliance tools and development tools/technologies as well as open source initiatives.

All of the results of the Double Open Short Ecosystem Survey 2019 are copyrighted to HH Partners, Attorneys-at-law Ltd and published under license CC-BY-4.0.

In this report we are giving anonymised raw data for the public with analysis of the process and the results. From the raw data, you can see the relation of tools used to size of companies. The total amount of answers given was 28 from various different groups of people and from a diverse sample of companies. We feel confident that even though the sample could have been larger, in some respects, this does show how the field works in various levels.

We must remind that some of the data here is affected by the groups we have sent the link to. E.g. the reason why some tools have gotten certain amounts of hits is affected by the fact that the survey has been sent to their respective mailing lists. This does not falsify the data in any way but should be taken into account and this is what we are also going to be doing. 

In addition our list of initiatives and tools has grown with due time and research. However, the survey is in its original form as it was when launched, so that abnormalities to the current answers would be minimized. Therefore tools and initiatives found after the launch of the survey have not been taken in this survey. Some are however noted in the analysis. 

In this report we are going to analyse the results section by section. Afterwards there will be a conclusion and some forward words from the Double Open project. 

---

## Participation and use of open compliance initiatives

### Results <!-- omit in toc -->

| Initiative                       | Number of users |
| :------------------------------- | :-------------: |
| ClearlyDefined                   |       10        |
| Eclipse Oscano                   |        1        |
| Automated Compliance Tooling ACT |        3        |
| Sharing-creates-value            |        5        |
| AboutCode.org                    |        1        |

### Analysis <!-- omit in toc -->

Some fluctuation in the results, due to where this survey has been sent to, might come to the Sharing-creates-value initiative. However, this does not affect the end result, that the ClearlyDefined initiative is clearly leading the board here. None of the other initiatives are at the same point as ClearlyDefined in the sense of readiness to give anything usable and renewable information. At this point ClearlyDefined is the only initiative on the board, that can already function in the manner it has been intended to. Others are still pending and require plenty of contributing to, before they can function. However, after this has been said, the other initiatives do give valuable information to the public and have potential of becoming viable options for the field of open source compliance. 

Notes:  
Our list didn't contain the REUSE initiative. We have seen that the REUSE software is getting air under their wing. REUSE initiative is an initiative to provide a set of recommendations
to make licensing your free software projects easier. Please see Reuse Software section in the publications for more information. 

---

## Open tools in open source compliance

### Results <!-- omit in toc -->

| Tool                                                        | Number of users |
| :---------------------------------------------------------- | :-------------: |
| Fossology                                                   |       15        |
| ScanCode toolkit                                            |       14        |
| AboutCode toolkit                                           |        3        |
| Deltacode                                                   |        2        |
| AboutCode Manager                                           |        2        |
| TraceCode toolkit                                           |        2        |
| OSS Discovery by OpenLogic                                  |        0        |
| Licensee.js                                                 |        1        |
| Ninka                                                       |        2        |
| Eclipse SW360                                               |        3        |
| OSS Review Toolkit ORT                                      |        7        |
| license-compatibility-checker                               |        0        |
| The Quartermaster Project QMSTR                             |        2        |
| Open Source License Checklists by OSADL                     |        2        |
| Apache Rat                                                  |        0        |
| Apache Tentacles                                            |        0        |
| Apache Whisker                                              |        0        |
| Cregit                                                      |        1        |
| OSS Attribution Builder                                     |        1        |
| OSSSanitizer and OSSPolice                                  |        0        |
| CLIPol                                                      |        0        |
| Tern                                                        |        3        |
| SPDX Tools                                                  |       11        |
| SPDX Maven plugin                                           |        1        |
| Licensee from GitHub (that powers the license checks there) |        1        |
| LicenseFinder                                               |        1        |

### Analysis <!-- omit in toc -->

As is clear, Fossology and ScanCode are the most used FOSS tools in open source compliance. Notable third is the SPDX Tools, which are meant to manage e.g. the results given by Fossology and ScandCode. Notice that in addition to plenty other output options, both Fossology and ScanCode give SPDX documentation as an output, which then can be managed through SPDX tools to convert into wanted format. We have been using Fossology as our main tool to achieve open source compliance. It has a great Web UI to use and provides different capabilities to tackle the challenge of compliance work.   

Many of the tools are rather tools that are not primarily used solitarily, so this might affect the end result. For example ACT initiative has Fossology, Tern, SPDX and Quartermaster integrated in it and ClearlyDefined has at least Fossology and ScanCode scanners. When asking such question as this was, users might have disregarded the tools they are actually using as they are just integrated in a bigger set of tools.  

Either way, this shows in such clarity the 3 main FOSS tools used in open source compliance, that it doesn't leave our project a doubt, what is needed. First, license scanning will always have to be done to a certain extent, manually. For these purposes both Fossology and ScanCode are both great and have a varied set of different tools to achieve the goals of a compliance officer. The SPDX implementation in Fossology and ScanCode is valuable to many, who want to do an easy access, easily readable Bill of Materials to the distribution of their software. 

---

## Commercial tools in open source compliance

### Results <!-- omit in toc -->

| Tool                       | Number of users |
| :------------------------- | :-------------: |
| Flexera                    |        1        |
| BlackDuck                  |        6        |
| Fossa                      |        2        |
| FOSSID                     |        7        |
| TripleCheck                |        0        |
| WhiteSource                |        6        |
| NexB                       |        2        |
| Insigniary                 |        0        |
| Sonatype                   |        1        |
| Anchore                    |        0        |
| CAST Software Intelligence |        0        |
| Rogue Wave Software        |        0        |
| Snyk.io                    |        1        |


### Analysis <!-- omit in toc -->

Regarding the commercial tool question, commercial tools are not in the center of attention for the Double Open project. However, it is interesting to see what tools people working in open source compliance want to work with. These might direct us to find features, which are lacking in the FOSS tools. Either way, many use commercial tools not just for the tools, but for the service they include with such tools. This can be seen from the top three of these tools. The service relation is something that a FOSS tool rarely can provide as they are only tools and usually there is no helpdesk or other service for them. Initially must be asked though, are FOSS tools too complicated or scattered so that one would wonder to commercial providers. The answer here is probably yes and this issue should be acknowledged by the community. 

---

## Request and incident management tools

### Results <!-- omit in toc -->

| Tool                                                                | Number of users |
| :------------------------------------------------------------------ | :-------------: |
| Polarion                                                            |        2        |
| Team Foundation Server                                              |        6        |
| JIRA                                                                |       21        |
| Github/Gitlab/other Git service                                     |       23        |
| Visual Studio DevOps (former TFS)                                   |        1        |
| Perforce                                                            |        1        |
| RT                                                                  |        1        |
| Azure DevOps (the new name for VSTS which was the new name for TFS) |        1        |


### Analysis <!-- omit in toc -->

TBD

--- 

## IDEs, Integrated Development Environments

### Results <!-- omit in toc -->

| Tool                   | Number of users |
| :--------------------- | :-------------: |
| Jenkins                |       23        |
| Team Foundation Server |        7        |
| Bamboo                 |        2        |
| TeamCity               |        5        |
| CircleCI               |        6        |
| Azure DevOps           |        6        |
| Travis CI              |       10        |
| GitLab CI              |        5        |
| Concourse              |        1        |
| AWS CodeBuild          |        1        |
| Codeship               |        2        |
| Appveyor               |        4        |
| Puppet                 |        3        |
| Ansible                |        7        |
| Octopus                |        2        |
| GitHub Actions         |        1        |
 
### Analysis <!-- omit in toc -->

TBD

---

## Build tools, frameworks and dependency management

### Results <!-- omit in toc -->

| Tool                 | Number of users |
| :------------------- | :-------------: |
| Cmake                |       10        |
| Yocto / OpenEmbedded |       12        |
| BitBake              |        4        |
| Visual Studio        |       14        |
| Apache Maven         |       19        |
| Gradle               |       16        |
| npm                  |       19        |
| yarn                 |        9        |
| pip / pipenv         |       15        |
| Conda                |        3        |
| Composer             |        6        |
| sbt                  |        5        |
| Make                 |       13        |
| Apache Ant           |        8        |
| Webpack              |        7        |
| Godep, Bundler       |        1        |


### Analysis <!-- omit in toc -->

TBD

---

## Package indexes and repositories

### Results <!-- omit in toc -->

| Tool                                            | Number of users |
| :---------------------------------------------- | :-------------: |
| Go Search                                       |        7        |
| npm registry                                    |       19        |
| Packagist (the PHP package repository)          |        6        |
| Maven repositories                              |       17        |
| RubyGems.org                                    |        8        |
| NuGet                                           |       13        |
| Bower                                           |       11        |
| CPAN                                            |        4        |
| Cargo (crates.io)                               |        3        |
| PEAR (PHP extension and application repository) |        3        |
| PlatformIO registry                             |        0        |
| Nexus Repository                                |        8        |
| JFrog Artifactory                               |        9        |
| CocoaPods                                       |        4        |
| RPM and Debian/Ubuntu repos                     |        1        |

### Analysis <!-- omit in toc -->

TBD

---

## Document management

### Results <!-- omit in toc -->

| Tool         | Number of users |
| :----------- | :-------------: |
| Flowdock     |        0        |
| Confluence   |       18        |
| Polarion     |        1        |
| GitHub       |        1        |
| Liferay Sync |        1        |

### Analysis <!-- omit in toc -->

TBD

---

## Testing frameworks

### Results <!-- omit in toc -->

| Tool             | Number of users |
| :--------------- | :-------------: |
| Robot Framework  |        7        |
| Cypress          |        0        |
| RedwoodHQ        |        0        |
| Selenium         |       10        |
| Serenity         |        0        |
| Citrus Framework |        0        |
| TestRail         |        1        |
| qTest            |        4        |
| JUnit            |        7        |
| AndroidTest      |        5        |
| Roboelectric     |        1        |
| mochito          |        3        |
| py.test          |        1        |
| Nunit googletest |        1        |
| Cunit            |        1        |
| Robolectric      |        1        |
| Unity            |        1        |

### Analysis <!-- omit in toc -->

TBD

---

## Container technologies

### Results <!-- omit in toc -->

| Tool          | Number of users |
| :------------ | :-------------: |
| Docker        |       23        |
| Cloud Foundry |        4        |
| Atomic        |        0        |
| OpenShift     |        5        |
| Kubernetes    |       14        |
| VirtualBox    |        1        |

### Analysis <!-- omit in toc -->

TBD

---

## What is the size of your organization?

### Results <!-- omit in toc -->

| Tool                    | Number of users |
| :---------------------- | :-------------: |
| 10000 employees or more |       10        |
| 1000 - 9999 employees   |        7        |
| 100 - 999 employees     |        5        |
| 10 - 99 employees       |        3        |
| Less than 10 employees  |        3        |

### Analysis <!-- omit in toc -->

TBD

---