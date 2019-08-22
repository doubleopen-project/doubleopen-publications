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
- [Links to Results](#links-to-results)

## Introduction

Double Open launched the Double Open Short Ecosystem Survey 2019 to accumulate real life factual information from members of the open source ecosystem to investigate the existing landscape, and popularity of open source compliance tools and development tools/technologies as well as open source initiatives.

This report is copyrighted to HH Partners, Attorneys-at-law Ltd. and published under CC-BY-4.0 license.

A total of 28 responses were given from a diverse sample of different sized companies. The survey was open during February, March and early April of 2019. This report includes anonymised data from the survey with analysis of the process and the results. The anonymised data is also available as raw data for further analysis. [LINK] 

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

 A request to fill the survey was introduced to the sharing-creates-value initiatives mailing list, as well as to ClearlyDefined's Slack and OpenChain's mailing lists. Therefore the top three results represent the activity of those lists quite well. Also, please note that the sharing-creates-value initiative has been used under the OSS Based Compliance Tooling group which is now (since early August 2019) working under OpenChain.
 Also, worthy of note is that OpenChain is likely the oldest initiative of these (at the time issuing the survey) and Automated Compliance Tooling ACT is the youngest.
 With the merging of OpenChain and Sharing-creates-value, it seems that the currently strongest initiative/working group is the OSS Based Compliance Tooling group, although their respective areas of work (quality based process improvement in OpenChain and tooling work under the OSS Based Compliance Tooling group) are distinct but complementary. That observation is also supported by our own experience in participating in the work of the three topmost initiatives. 
 ClearlyDefined has a significant amount of mentions too and its approach is different; an API based actual service. The approach has clear value in the sense of ease of integration. 

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

- Fossology, ScanCode and SPDX Tools are clear leaders. All of these have existed quite some time already.
- Both Fossology and ScanCode produce SPDX. 
- ScanCode is already integrated into e.g. OSS Review Toolkit and ClearlyDefined. 
- Fossology is already integrated to e.g. ACT initiative and ClearlyDefined
- OSS Review Toolkit ORT has not been officially publicised and is very young; and had regardless gathered several replies. 
- Also, when responses given by companies with less than 1,000 employees are removed, we find that the 3 tools with most answers are Fossology, ScanCode, and ORT. 

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

Commercial tools are not in the center of attention for the Double Open project, hence the above result is not analysed more.

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

Based on the results it seems clear that an open toolchain should likely produce reports into Git services and JIRA. A proof of concept should choose either of these.

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

Based on the results it seems clear that any possible integration into IDEs should consider Visual Studio and Eclipse.

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

Based on the results it seems clear that integration into SCMs should first focus on GIT based services/tools. 

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

Based on the results the natural first choice for CI/CD integartion in a proof of concept would be Jenkins. 

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

Java based technologies are clearly on top of the build tools list. Python technologies follow. Gradle as a framework is less dependent on development language.  Also an important number of Linux embedded technologies are mentioned, e.g. Make, Yocto and Cmake each getting at least 10 mentions. A proof of concept for automated compliance should likely integrate into one or several of these. 

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

Package indexes are popularly used in Java & Javascript, which can be seen in the answers for this question. Any proof of concept in these technologies should likely use the information available from the topmost registries here.

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

Document management integration should be Confluence, based on these replies.

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

The testing framework answers are more divided with no clear top result, considering 28 answers in general.

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

Container related integration should likely start with Docker and followed with Kubernetes.

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

The above gives a view on the type of responents to this questionnaire. At the same time it reflects the type of organizations who are interested in open source compliance, i.e. large enterprises.

---

## Conclusion

The response quantity to the survey was small to medium. However, the purpose of the survey was to explore the potential direction and development of the open source software industry and practices. 61 per cent of the sample group was companies with over 1000 employees. Large companies are de facto influential in the OSS industry. Therefore we deem the Survey to be an overall success and it does give valid information of e.g. integrations to all who wish to develop and contribute in open source. A more substantial survey will be held to support in the conceptualising endeavours of Double Open project concerning the creation of an automated open source toolchain.

---

## Links to Results

* The final results of the Double Open Short Ecosystem Survey 2019 can be found (here)[/Ecosystem-Survey-2019/Final-Results-Double-Open-Short-Ecosystem-Survey-2019.pdf]
* The final results of only companies with over 1000 employees can be found (here)[/Ecosystem-Survey-2019/Results-Companies-With-Over-1000-Employees.pdf]
* The raw data of the final results can be found (here)[/Ecosystem-Survey-2019/Raw-Data-Double-Open-Short-Ecosystem-Survey-2019.xlsx]

---

---END OF DOCUMENT---