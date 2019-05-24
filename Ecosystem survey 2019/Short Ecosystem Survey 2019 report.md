# Double Open Short Ecosystem Survey 2019 Report <!-- omit in toc -->

**UNDER DEVELOPMENT** <!-- omit in toc -->
---

- [Introduction](#introduction)
- [Participation and use of open compliance initiatives](#participation-and-use-of-open-compliance-initiatives)
- [Open tools in open source compliance](#open-tools-in-open-source-compliance)
- [Commercial tools in open source compliance](#commercial-tools-in-open-source-compliance)
- [Request and incident management tools](#request-and-incident-management-tools)
- [IDEs, Integrated Development Environments](#ides-integrated-development-environments)
- [Source code management (SCM) tools and services](#source-code-management-scm-tools-and-services)
- [Continuous integration (CI) and continuous deployment (CD) tools](#continuous-integration-ci-and-continuous-deployment-cd-tools)
- [Build tools, frameworks and dependency management](#build-tools-frameworks-and-dependency-management)
- [Package indexes and repositories](#package-indexes-and-repositories)
- [Document management](#document-management)
- [Testing frameworks](#testing-frameworks)
- [Container technologies](#container-technologies)
- [What is the size of your organization?](#what-is-the-size-of-your-organization)
- [Conclusion](#conclusion)

## Introduction

Double Open launched the Double Open Short Ecosystem Survey 2019 to accumulate real life factual information from members of the open source ecosystem to investigate the existing landscape, and popularity of open source compliance tools and development tools/technologies as well as open source initiatives.

This report is copyrighted to HH Partners, Attorneys-at-law Ltd. and published under CC-BY-4.0 license. 

A total of 28 responses were given from a diverse sample of different sized companies. This report includes anonymised data from the survey with analysis of the process and the results. We feel confident that the data shows the general behavious of the field. 

Some of the data has been affected by who the survey has been shared with. The survey has been publicly available on our website. In addition, we have sent a link to our survey to specific mailing lists. This may have some impact on the results of the survey, but these have been taken into consideration in the analysis.

Also new compliance tools have come to our knowledge after the launch of the survey. Therefore, these "new" tools are not visible in the results of the survey and their evaluation is not possible through survey data. 

In this report we are going to analyse the results section by section. Afterwards there will be a conclusion and some forward words from the Double Open project. 

---

## Participation and use of open compliance initiatives

### Results <!-- omit in toc -->

| Initiative                       | Number of users |
| :------------------------------- | :-------------: |
| OpenChain                        |       15        |
| ClearlyDefined                   |       10        |
| Sharing-creates-value            |        5        |
| Automated Compliance Tooling ACT |        3        |
| Eclipse Oscano                   |        1        |
| AboutCode.org                    |        1        |

### Analysis <!-- omit in toc -->

- Link was sent to sharing-creates-value initiative mailing list (and ClearlyDefined and OpenChain mailing lists?)
  - Fluctuation due to this? The end result is so clear that we can conclude that the effect of possible external influences are insignificant.
- It should be noted that some of the initiatives were launched just prior to the survey. Therefore, e.g. the ACT initiative maintained by the Linux Foundation may become a valid tool in the future. ClearlyDefined and OpenChain are already working and ongoing initiatives.

---

## Open tools in open source compliance

### Results <!-- omit in toc -->

| Tool                                                        | Number of users |
| ----------------------------------------------------------- | :-------------: |
| Fossology                                                   |       15        |
| ScanCode toolkit                                            |       14        |
| SPDX Tools                                                  |       11        |
| OSS Review Toolkit ORT                                      |        7        |
| AboutCode toolkit                                           |        3        |
| Eclipse SW360                                               |        3        |
| Tern                                                        |        3        |
| Deltacode                                                   |        2        |
| AboutCode Manager                                           |        2        |
| TraceCode toolkit                                           |        2        |
| Ninka                                                       |        2        |
| The Quartermaster Project QMSTR                             |        2        |
| Open Source License Checklists by OSADL                     |        2        |
| Licensee.js                                                 |        1        |
| Cregit                                                      |        1        |
| OSS Attribution Builder                                     |        1        |
| SPDX Maven plugin                                           |        1        |
| Licensee from GitHub (that powers the license checks there) |        1        |
| LicenseFinder                                               |        1        |
| OSS Discovery by OpenLogic                                  |        0        |
| license-compatibility-checker                               |        0        |
| Apache Rat                                                  |        0        |
| Apache Tentacles                                            |        0        |
| Apache Whisker                                              |        0        |
| OSSSanitizer and OSSPolice                                  |        0        |
| CLIPol                                                      |        0        |

### Analysis <!-- omit in toc -->

- Fossology, ScanCode and SPDX Tools are clear leaders. 
- Both Fossology and ScanCode produce SPDX. 
- ScanCode is already integrated into e.g. OSS Review Toolkit and ClearlyDefined. 
- Fossology is already integrated to e.g. ACT initiative and ClearlyDefined 
- However, when responses given by companies with less than 1,000 employees are removed, we find that the 3 biggest tools are Fossology, ScanCode, and ORT. 

---

## Commercial tools in open source compliance

### Results <!-- omit in toc -->

| Tool                       | Number of users |
| :------------------------- | :-------------: |
| FOSSID                     |        7        |
| BlackDuck                  |        6        |
| WhiteSource                |        6        |
| Fossa                      |        2        |
| NexB                       |        2        |
| Flexera                    |        1        |
| Sonatype                   |        1        |
| Snyk.io                    |        1        |
| TripleCheck                |        0        |
| Insigniary                 |        0        |
| Anchore                    |        0        |
| CAST Software Intelligence |        0        |
| Rogue Wave Software        |        0        |


### Analysis <!-- omit in toc -->

Regarding the commercial tool question, commercial tools are not in the center of attention for the Double Open project. However, it is interesting to see what tools people working in open source compliance want to work with. These might direct us to find features, which are lacking in the FOSS tools. Either way, many use commercial tools not just for the tools, but for the service they include with such tools. This can be seen from the top three of these tools. The service relation is something that a FOSS tool rarely can provide as they are only tools and usually there is no helpdesk or other service for them. Initially must be asked though, are FOSS tools too complicated or scattered so that one would wonder to commercial providers. The answer here is probably yes and this issue should be acknowledged by the community. 

---

## Request and incident management tools

### Results <!-- omit in toc -->

| Tool                                                                | Number of users |
| :------------------------------------------------------------------ | :-------------: |
| Github/Gitlab/other Git service                                     |       23        |
| JIRA                                                                |       21        |
| Team Foundation Server                                              |        6        |
| Polarion                                                            |        2        |
| Visual Studio DevOps (former TFS)                                   |        1        |
| Perforce                                                            |        1        |
| RT                                                                  |        1        |
| Azure DevOps (the new name for VSTS which was the new name for TFS) |        1        |

### Analysis <!-- omit in toc -->

TBD

--- 

## IDEs, Integrated Development Environments

### Results <!-- omit in toc -->

| Tool                    | Number of users |
| ----------------------- | --------------- |
| Visual Studio           | 20              |
| Eclipse                 | 19              |
| JetBrains IntelliJ IDEA | 10              |
| Android Studio          | 9               |
| JetBrains PyCharm       | 7               |
| Visual Studio Code      | 3               |
| Qt Creator              | 3               |
| Netbeans IDE            | 3               |
| JetBrains WebStorm      | 2               |
| JetBrains PhpStorm      | 2               |
| JetBrains GoLand        | 2               |
| JetBrains CLion         | 2               |
| vim                     | 1               |
| JetBrains RubyMine      | 1               |
| JetBrains Rider         | 1               |
 
### Analysis <!-- omit in toc -->

TBD

---

## Source code management (SCM) tools and services

### Results <!-- omit in toc -->

| Tool       | Number of users |
| ---------- | --------------- |
| Git        | 19              |
| GitHub     | 18              |
| GitLab     | 13              |
| Bitbucket  | 8               |
| SVN        | 5               |
| gerrit     | 2               |
| Mercurial  | 1               |
| Perforce   | 1               |
| Clear Case | 1               |

### Analysis <!-- omit in toc -->

TBD

---

## Continuous integration (CI) and continuous deployment (CD) tools

### Results <!-- omit in toc -->

| Tool                   | Number of users |
| ---------------------- | --------------- |
| Jenkins                | 23              |
| Travis CI              | 10              |
| Team Foundation Server | 7               |
| Ansible                | 7               |
| CircleCI               | 6               |
| Azure DevOps           | 6               |
| TeamCity               | 5               |
| GitLab CI              | 5               |
| Appveyor               | 4               |
| Puppet                 | 3               |
| Octopus                | 2               |
| Codeship               | 2               |
| Bamboo                 | 2               |
| GitHub Actions         | 1               |
| Concourse              | 1               |
| AWS CodeBuild          | 1               |
| wercker                | 0               |
| Semaphore              | 0               |
| Go.CD                  | 0               |
| Drone.io               | 0               |
| Buildkite              | 0               |

### Analysis <!-- omit in toc -->

TBD

---

## Build tools, frameworks and dependency management

### Results <!-- omit in toc -->

| Tool                 | Number of users |
| -------------------- | --------------- |
| Apache Maven         | 19              |
| npm                  | 19              |
| Gradle               | 16              |
| pip / pipenv         | 15              |
| Visual Studio        | 14              |
| Make                 | 13              |
| Yocto / OpenEmbedded | 12              |
| Cmake                | 10              |
| yarn                 | 9               |
| Apache Ant           | 8               |
| Webpack              | 7               |
| Composer             | 6               |
| sbt                  | 5               |
| BitBake              | 4               |
| Conda                | 3               |
| Godep, Bundler       | 1               |

### Analysis <!-- omit in toc -->

TBD

---

## Package indexes and repositories

### Results <!-- omit in toc -->

| Tool                                            | Number of users |
| ----------------------------------------------- | --------------- |
| npm registry                                    | 19              |
| Maven repositories                              | 17              |
| NuGet                                           | 13              |
| Bower                                           | 11              |
| JFrog Artifactory                               | 9               |
| RubyGems.org                                    | 8               |
| Nexus Repository                                | 8               |
| Go Search                                       | 7               |
| Packagist (the PHP package repository)          | 6               |
| CPAN                                            | 4               |
| CocoaPods                                       | 4               |
| Cargo (crates.io)                               | 3               |
| PEAR (PHP extension and application repository) | 3               |
| RPM and Debian/Ubuntu repos                     | 1               |
| PlatformIO registry                             | 0               |

### Analysis <!-- omit in toc -->

TBD

---

## Document management

### Results <!-- omit in toc -->

| Tool         | Number of users |
| ------------ | --------------- |
| Confluence   | 18              |
| Polarion     | 1               |
| GitHub       | 1               |
| Liferay Sync | 1               |
| Flowdock     | 0               |

### Analysis <!-- omit in toc -->

TBD

---

## Testing frameworks

### Results <!-- omit in toc -->

| Tool             | Number of users |
| ---------------- | --------------- |
| Selenium         | 10              |
| Robot Framework  | 7               |
| JUnit            | 7               |
| AndroidTest      | 5               |
| qTest            | 4               |
| mochito          | 3               |
| TestRail         | 1               |
| Roboelectric     | 1               |
| py.test          | 1               |
| Nunit googletest | 1               |
| Cunit            | 1               |
| Robolectric      | 1               |
| Unity            | 1               |
| Cypress          | 0               |
| RedwoodHQ        | 0               |
| Serenity         | 0               |
| Citrus Framework | 0               |

### Analysis <!-- omit in toc -->

TBD

---

## Container technologies

### Results <!-- omit in toc -->

| Tool          | Number of users |
| ------------- | --------------- |
| Docker        | 23              |
| Kubernetes    | 14              |
| OpenShift     | 5               |
| Cloud Foundry | 4               |
| VirtualBox    | 1               |
| Atomic        | 0               |

### Analysis <!-- omit in toc -->

TBD

---

## What is the size of your organization?

### Results <!-- omit in toc -->

| Number of employees | Responses |
| ------------------- | --------- |
| 10000 <             | 10        |
| 1000 - 9999         | 7         |
| 100 - 999           | 5         |
| 10 - 99             | 3         |
| < 10                | 3         |

### Analysis <!-- omit in toc -->

TBD

---

## Conclusion



---