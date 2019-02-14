# Double Open Landscape Survey
Version 1.dev 2019-02-14

___

## Table of Contents
[Introduction](#introduction)

[Open Initiatives](#open-initiatives-for-open-source-compliance)
* [ClearlyDefined](#clearlydefined)
* [Eclipse Oscano](#eclipse-oscano)
* [Automated Compliance Tooling (ACT)](#automated-compliance-tooling-act-)
* [OpenChain](#openchain)
* [Sharing-creates-value](#sharing-creates-value)

[FOSS tools](#foss-tools-for-open-source-compliance)
* [Fossology](#fossology)
* [ScanCode toolkit](#scancode-toolkit)
* [AboutCode toolkit](#aboutcode-toolkit)
* [Deltacode](#deltacode)
* [AboutCode Manager](#aboutcode-manager-scancode-workbench)
* [TraceCode toolkit](#tracecode-toolkit)
* [OSS Discovery (OpenLogic)](#oss-discovery-openlogic-)
* [Licensee.js](#licensee-js)
* [Ninka](#ninka)
* [Eclipse SW360](#eclipse-sw360)
* [OSS Review Toolkit (ORT)](#oss-review-toolkit-ort-)
* [license-compatibility-checker](#license-compatibility-checker)
* [The Quartermaster (QMSTR) Project](#the-quartermaster-qmstr-project)
* [Open Source License Checklists (by OSADL)](#open-source-license-checklists-by-osadl-)
* [Apache Rat](#apache-rat)
* [Apache Tentacles](#apache-tentacles)
* [Apache Whisker](#apache-whisker)
* [Cregit](#cregit)
* [OSS Attribution Builder](#oss-attribution-builder)
* [OSSSanitizer / OSSPolice](#osssanitizer-osspolice)
* [CLIPol](#cippic-licensing-information-project-for-open-licences-clipol-)
* [Tern](#tern)
* [SPDX Tools](#spdx-tools)
* [SPDX Maven Plugin](#spdx-maven-plugin)

[Commercial Tools](#commercial-tools-for-open-source-compliance)
* [Flexera](#flexera)
* [BlackDuck ](#blackduck-by-synopsys)
* [Fossa](#fossa)
* [FOSSID](#fossid)
* [TripleCheck](#triplecheck)
* [WhiteSource](#whitesource)
* [NexB/DejaCode](#nexb-dejacode)
* [Insigniary](#insigniary)
* [Sonatype](#sonatype)
* [Anchore](#anchore)
* [CAST Software Intelligence](#cast-software-intelligence)
* [Rogue Wave Software](#rogue-wave-software)
* [Verifa](#verifa)

[Development Environments](#development-environments)

---

## Introduction

Open source software has eaten the world, but organizations are still struggling with effective compliance. Open source software is heterogenous and re-used, which, while positive for software development, create a challenge for compliance. Compliance requires multiple tools and these should be ideally combined into a work-flow that supports a number of (business and developer) requirements. One of the requirements is ease of use in a modern development environment where code development cycles are getting ever shorter and new development results are pushed to operations ever faster. For this to work, open source compliance tools likely need to integrate with development toolings.

In the following report some of these tools are listed with information of their main license, website and a summary of their features (based on accounts by the projects). The report has been crafted to map out the wide range of open source tools that one might use to help keep their open source software compliant. However, this report, ever so comprehensive, is not exhaustive. The report includes FOSS tools as well as a few commercial tools. It also has a section for Open Source Initiatives and Development Environments, as these are  also important on a way towards automated open compliance with open tooling and open data. 

This report will be complemented on basis of an ecosystem survey; and based on practical testing of the most popular (based on the survey) open source tools.

This report is part of the fist work package in the Double Open project. See doubleopen.org for more details.

---

## Open Initiatives for open source compliance

### ClearlyDefined
#### Website

[ClearlyDefined.io](https://clearlydefined.io/)

ClearlyDefined on [GitHub](https://github.com/clearlydefined/clearlydefined)

#### Summary

ClearlyDefined is a community / contributor powered project in which the goals are: 
1. Raise awareness about this challenge within FOSS project teams
2. Automatically harvest data from projects
3. Make it easy for anyone to contribute missing information
4. Crowd-source the curation of these contributions
5. Feed curated contributions back to the original projects

ClearlyDefined provides a mechanism for harvesting available data using tools such as ScanCode and FOSSology, and facilitates crowd-sourcing the curation of that information when ambiguities or gaps arise. The ultimate goal of harvesting and curation is to contribute any new-found clarity (e.g., new licenses found) to the upstream projects so they can include the updates in their next release. The project focuses now on clarifying individual project's license, source code location and copyright holders, but do see security, accessibility, and internationalization being important parts of the ClearlyDefined ecosystem.

### Eclipse Oscano
#### Website
[Eclipse Oscano](https://projects.eclipse.org/proposals/eclipse-oscano)

#### Summary
The mission of the Oscano project is to solve the problem of scaling SCA to modern needs with Open Source approach. The Eclipse Oscano project provides a complete software composition analysis solution, focused on compliance and security, that can be installed on cloud, local server, or workstation environment. To achieve this, existing OSS components will be reviewed by the project team for possible integration into the Oscano stack and capabilities not existing will be built and integrated. Main use cases of Oscano include Open Source license compliance management, open source inventory management, vulnerability remediation automation and software analysis reporting. 

The solution is designed to meet the challenge of massively increasing scale and continuous nature of build and releasing of modern software systems. It addresses the scaling problem through four principal means: 

1. Continuous and fully automated operation cycle from new code commit to analysis, scan and action 
2. Maximum engagement of developers in the software analysis and management use cases for direct and early troubleshooting 
3. Risk-based smart analysis of compliance and vulnerability issues 
4. Maximum re-use of pre-scanned open source software data.

### Automated Compliance Tooling (ACT)
#### Website
[ACT](https://www.linuxfoundation.org/press-release/2018/12/the-linux-foundation-to-launch-new-tooling-project-to-improve-open-source-compliance/)

#### Summary
ACT is a Linux Foundation project. The goal is to consolidate investment in, and increase interoperability and usability of, open source compliance tooling, which helps organizations manage compliance obligations.ACT also welcomes two new projects to be hosted at The Linux Foundation as part of the initiative, in addition to two existing Linux Foundation projects that will become part of the new project. The new projects are complementary to existing Linux Foundation compliance projects such as OpenChain, which identifies key recommended processes to make open source license compliance simpler and more consistent, and the Open Compliance Program, which educates and helps developers and companies understand their license requirements and how to build efficient, frictionless and often automated processes to support compliance.

The four projects that will be part of ACT are:
* FOSSology
* QMSTR
* SPDX Tools
* Tern

### OpenChain
#### Website
[OpenChain](https://www.openchainproject.org/)

#### Summary
OpenChain is a project hosted by the Linux Foundation. It answers a question: "How do I trust my open source supply chain"? It provides a framework for shared, compliant use of FOSS. Conforming companies create an environment that supports use of FOSS internally and sharing of FOSS with partners. The [OpenChain Specification](https://www.openchainproject.org/spec) defines a core set of requirements every quality compliance program must satisfy. [OpenChain Conformance](https://www.openchainproject.org/conformance) allows organizations to display their adherence to these requirements. The [OpenChain Curriculum](https://www.openchainproject.org/curriculum) supports this process by providing extensive reference material for effective open source training and management. The result is that open source license compliance becomes more predictable, understandable and efficient for all participants in the software supply chain.

### Sharing-creates-value
#### Website
[Sharing-creates-value](https://github.com/Open-Source-Compliance/Sharing-creates-value)

#### Summary
This is GitHub repository hosted by Siemens. Sharing creates value strives for the goal to lower the required effort in license compliance work for all who want to make use of OSS in a license compliant way. To achieve this Sharing creates value will develop, share and improve the artifacts needed to fulfill the requirements of the different Free and Open Source Software licenses by applying the Open Source Software development principles.

Another objective of Sharing creates value is a very close collaboration with the OSS community in order to fix detected "bugs" in licensing as well as introducing the information needed for license compliance activities in the Open Source projects, i.e. provide our analysis work to the OSS projects.

Last but not least Sharing creates value support tools which will help automate and reduce effort in component management, license identification, OSS license compliance activities.

Sharing creates value wants to be the platform, which provides all information and artifacts for OSS license compliance.

---

## FOSS tools for open source compliance

### Fossology
#### Website
[Fossology](https://www.fossology.org/ )
#### Main License
[GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
#### Summary
Fossology is a scanning tool for license, copyright and export control scans. In one click you can generate an SPDX file, or a ReadMe with all the copyrights notices from your software. It provides a Web UI and a database for a compliance workflow. To scan, a package must be uploaded to the server. Scanners provided are Monk, Nomos and Ninka. It has version control on packages scanned, so when scanning a newer version of a previous package, only changed files are rescanned.

### ScanCode toolkit
#### Website
[ScanCode](https://www.aboutcode.org/ )
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
ScanCode is a suite of command line utilities to reliably scan a codebase for license, copyright, package manifests and direct dependencies and other interesting origin and licensing information discovered in source and binary code files. ScanCode provides comprehensive scan results that you can save as JSON, HTML, CSV or SPDX. As a command line application returning JSON, ScanCode is easy to integrate in a code analysis pipeline and CI/CD.

### AboutCode toolkit
#### Website
[AboutCode](https://www.aboutcode.org/ )
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
The AboutCode Toolkit and ABOUT files provide a simple way to document the origin, license, usage and other important or interesting information about third-party software components that you use in your project. In addition, this tool is able to generate attribution notices and identify redistributable source code used in your project.

### Deltacode
#### Website
[AboutCode](https://www.aboutcode.org/ )
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
DeltaCode allows you to easily compare ScanCode scans for two versions of a package, component, codebase or product in order to quickly identify possible changes with a focus on identifying license changes. DeltaCode reports matching files with a score and a list of factors that contribute to that score. 

You can use DeltaCode with ScanCode to identify and track license and related changes in open source or third party software packages or components from release to release. 

### AboutCode Manager / ScanCode Workbench
#### Website
[AboutCode](https://www.aboutcode.org/ )
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
AboutCode Manager provides an advanced visual UI to help you quickly evaluate license and other notices identified by ScanCode and record your conclusion about the effective license(s) for a component. 

AboutCode Manager is based on Electron and is the primary desktop/GUI tool for using nexB’s AboutCode tools.

### TraceCode toolkit
#### Website
[AboutCode](https://www.aboutcode.org/ )
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
TraceCode Toolkit helps you determine which components are actually distributed or deployed for your product. This is essential information for determining your open source license obligations because many are only triggered by distribution or deployment. 

TraceCode Toolkit is a tool to analyze the traced execution of a build, so you can learn which files are built into binaries and ultimately deployed in your distributed software.

### OSS Discovery (OpenLogic)
#### Website
[OSS Discovery](http://ossdiscovery.sourceforge.net/)
#### Main License
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)
#### Summary
OSS Discovery finds the open source software embedded in applications and installed on computers. It is a scanning tool, which gives human readable and machine readable results.

### Licensee.js
#### Website
[Licensee.js](https://github.com/jslicense/licensee.js)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
Licensee.js is a command line utility to check npm package dependency license metadata against rules. It uses SPDX license expression and whitelisted data to capture packages that are under different license than whitelisted.

### Ninka
#### Website
[Ninka](http://ninka.turingmachine.org/)
#### Main License
[GPL-2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
#### Summary
Ninka is a lightweight license identification tool for source code. It is sentence-based, and provides a simple way to identify open source licenses in a source code file. It is capable of identifying several dozen different licenses (and their variations).

### Eclipse SW360
#### Website
[Eclipse SW360](https://projects.eclipse.org/projects/technology.sw360)
#### Main License
[EPL-1.0](https://www.eclipse.org/org/documents/epl-v10.php)
#### Summary
A software catalogue application designed to provide a central place for sharing information about software components used by an organization. It is designed to neatly integrate into existing infrastructures related to the management of software artifacts and projects by providing separate backend services for distinct tasks and a set of portlets to access these services. It has connectors to interact with external systems such as code scan tools. Thus far the project has not provided download information.

### OSS Review Toolkit (ORT)
#### Website
[ORT](https://github.com/heremaps/oss-review-toolkit)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
Verifies free and open source software license compliance by checking source code and dependencies. it works by analyzing the source code for dependencies, downloading the source code of the dependencies, scanning all source code for license information, and summarizing the results. The different tools that make up ORT are designed as libraries (for programmatic use) with a minimal command line interface (for scripted use). Currently the report formats are Excel sheet, NOTICE file, static HTML and Web App. 

### license-compatibility-checker
#### Website
[license-compatibility-checker](https://github.com/HansHammel/license-compatibility-checker#readme)
#### Main License
[MIT](https://opensource.org/licenses/MIT)
#### Summary
Check npm dependencies' package.json for license compatibility based on SPDX standards. Claimed to be a work in progress, but gives a simple comparison of the licenses in the package with an explanation to how permissive the license is (Permissive > Weakly Protective > Strongly Protective > Network Protective). Shows potential incompatibilities with a colorful scheme.

### The Quartermaster (QMSTR) Project
#### Website
[QMSTR](https://qmstr.org/)
#### Main License
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)
#### Summary
Quartermaster is a suite of command line tools and build system extensions that instruments software builds to create FOSS compliance documentation and support compliance decisions. Quartermaster runs adjacent to a software build process. A master process collects information about the software that is build. Once the build is complete, the master executes a number of analysis tools, and finally a number of reporters. All modules are executed in the context of the master, not the build machine. The master ships all dependencies of the modules without affecting the build clients file system (it runs in a container).

### Open Source License Checklists (by OSADL)
#### Website
[Open Source License Checklists](https://www.osadl.org/Open-Source-License-Checklists.oss-compliance-lists.0.html)
#### Main License
Unidentified
#### Summary
A project to create and disseminate generally accepted rules to fulfill the obligations when distributing software that is licensed under commonly used Open Source licenses. The goal of this project is to create checklists for the most frequently used and the most important Open Source licenses and to provide assistance tools for the determination of differences between them. 

### Apache Rat
#### Website
http://creadur.apache.org/rat/
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
Apache Rat is a release audit tool, focused on licenses. Coded in Java, it runs from the command line with plugins for Maven and Ant. Rat is extensible. It is part of the Apache Creadur project.

### Apache Tentacles
#### Website
[Apache Tentacles](http://creadur.apache.org/tentacles/)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
Apache Tentacles helps the reviewer by automating interactions with the repository containing the artifacts comprising the release. Apache Tentacles simplifies the job of reviewing repository releases consisting of large numbers of artifacts. Coded in Java, it runs from the command line.

### Apache Whisker
#### Website
[Apache Whisker](http://creadur.apache.org/whisker/)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
Apache Whisker assists assembled applications maintain correct legal documentation.

Whisker can 
* verify - checking meta-data quality against a distribution
* generate - legal documents from meta-data

Particular useful for complex assembled applications.

### Cregit
#### Website
[Cregit](https://github.com/cregit/cregit)
#### Main License
[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html)
#### Summary
Cregit identifies the contributors of source code. The cregit version of a source file has two interactive features:
* Mouse-over: you will get a summary of the information of the commit that added this token. This information is:
    * Its commit id
    * Its git-author (the value of the Author field of the commit)
    * Its git-author-date (the value of the field Author Date of the commit)
    * Summary log of the commit
* Left-click on a token will open a new window with the details of the commit (in github). You can keep this window open and it will keep reloading the files.

### OSS Attribution Builder
#### Website
[OSS Attribution Builder](https://github.com/amzn/oss-attribution-builder)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
#### Summary
OSS Attribution Builder is a website that helps teams create attribution documents for software products. 

### OSSSanitizer / OSSPolice
#### Website
[OSSSanitizer](http://osspolice.com/)
#### Main License
#### Summary
OSSSanitizer is a suite of web services for automating open-source software risk management. It has three components:
1. OSSPolice
    * a risk assessment service for developers that can quickly identify potential free software license violations and known nday security vulnerabilties in their apps.
2. AppSanitizer
    * a service for developers to automatically mitigate reported n-day known security risks in their apps.
3. AppOptimizer
    * optimize apps for performance and reduce their memory footprint to minimize security risks.

### CIPPIC Licensing Information Project for Open Licences (CLIPol)
#### Website
[CLIPol](http://www.clipol.org/)
#### Main License
[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
#### Summary
CLIPol is a web platform, maintained by the Samuelson-Glushko Canadian Internet Policy and Public Interest Clinic, a public interest technology law clinic at the Faculty of Law, Common Law Section, University of Ottawa, designed to serve useful information about open data licences, open content licences, and open source software. It consists of:
* a database of machine-readable information on the rights, restrictions and obligations in different licences;
* an API for retrieving this information;
* a web-accessible site for viewing this information in a user-friendly way (avoiding legalese); and
* a set of web apps built on top of this information (currently consisting of a compatibility-checking tool and a text-comparison tool).

### Tern
#### Website
[Tern](https://github.com/vmware/tern)
#### Main License
[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
#### Summary
Tern is a software package inspection tool for containers written in Python. Tern is an inspection tool to find the metadata of the packages installed in a container image. It does this in two steps:
1. It uses overlayfs to mount the first filesystem layer in a container image
2. It then executes scripts from the "command library" in a chroot environment to collect information about packages installed in that layer
3. With that information as a base, it continues to iterate over step 1 and 2 for the rest of the layers in the container image
4. Once done, it generates a report in different formats. The default report is a verbose explanation of what layers brought in what software components. If a Dockerfile is provided then it will also provide what lines in the Dockerfile was used to create the layers.

### SPDX Tools
#### Website
[SPDX Tools](https://spdx.org/tools)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)
#### Summary
The consolidated SPDX workgroup tool provides translation, comparison, and verification functionality in a single download. The tool is a Java command line utility.

The following functions are available:

* TagToSpreadsheet - Convert a tag format input file to a spreadsheet output file
* TagToRDF - Convert a tag format input file to an RDF format output file
* RdfToTag - Convert an RDF format input file to a tag format output file
* RdfToHtml - Convert an RDF format input file to an HTML web page output file
* RdfToSpreadsheet - Convert an RDF format input file to a spreadsheeet format output file
* SpreadsheetToRDF - Convert a spreadsheet input file to an RDF format output file
* SpreadsheetToTag - Convert a spreadsheet input file to a tag format output file
* SPDXViewer - Display an SPDX document input file (in either tag/value or RDF format)
* CompareMultipleSpdxDocs - Compare multiple SPDX documents (in either tag/value or RDF formats) and output to a spreadsheet
* CompareSpdxDocs - Compare two SPDX documents (in either tag/value or RDF format)
* GenerateVerificationCode - Geneinkrate a Verification Code from a directory of files.

### SPDX Maven Plugin
#### Website
[SPDX Maven Plugin](https://github.com/spdx/spdx-maven-plugin)
#### Main License
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)
#### Summary
SPDX Maven Plugin is a plugin to Maven which produces Software Package Data Exchange (SPDX) documents for artifacts described in the POM file. 

------------------------------------------------------

## Commercial Tools for Open Source Compliance

### Flexera

#### Website
[Flexera](https://www.flexera.com/)

#### Products for Open Source Software
* FlexNet Code Insight
* FlexNet Code Aware

#### Summary
[FlexNet Code Insight](https://www.flexera.com/products/software-composition-analysis/flexnet-code-insight.html) is a single integrated solution for open source license compliance and security. Find vulnerabilities and remediate associated risk, while you build your products and during their lifecycle. Manage open source license compliance. And add automation to your processes and implement a formal OSS strategy and policy that balances business benefits and risk management.

[FlexNet Code Aware](https://www.flexera.com/products/software-composition-analysis/flexnet-code-aware.html) sees what you can’t in your open source code — from security threats to intellectual property (IP) compliance issues. It’s a simple scan that ensures you’re safe to ship…or stops you from spreading risk. All in a matter of minutes. It’s free for developers.

### BlackDuck by Synopsys

#### Website
[BlackDuck](https://www.blackducksoftware.com/black-duck-home)

#### Products for Open Source Software
* BlackDuck
* OpsSight
* Tools for Open Source Project Teams
    * Black Duck CoPilot
        Helps open source project teams verify that their public GitHub projects don’t pull in vulnerabilities through dependencies on other open source components, and helps them communicate the security status of their component to users via the Black Duck security badge.
    * OpenHub
        Community that helps open source project leads, developers, and users aggregate and analyze information for their projects.

#### Summary
Black Duck gives development, operations, and security teams the tools they need to get the benefits of open source, while minimizing the security, license compliance, and code quality risks that can come with it.

[Black Duck](https://www.blackducksoftware.com/products/hub) is a complete open source management solution with features such as: 
* Fully discover all open source in your code
* Map components to known vulnerabilities
* Identify license compliance and component quality risks
* Set and enforce open source policies
* [Integrate](https://www.blackducksoftware.com/technology/integrations) open source management into your DevOps environment
* Monitor and alert when new threats are reported

[OpsSight](https://www.blackducksoftware.com/products/opssight) helps you prevent known open source vulnerabilities from being deployed into production environments. With OpsSight, you can:
* Automatically scan and inventory all open source in container images as they are utilized
* Identify and highlight any images that contain disclosed open source vulnerabilities
* Flag container images that violate open source security policies 
* Receive automated alerts when any newly discovered vulnerabilities may affect container images in use within your cluster

### Fossa

#### Website
[Fossa](https://fossa.com/)

#### Products for Open Source Software
* The product is FOSSA, but the pricing goes according to plans chosen:

    *  **Personal** is for small teams and projects to replace manual auditing, scripts and lightweight commercial utilities for license / dependency tracking.

    * **For Business** adds full code scanning, compliance automation and more to help companies set up an enterprise-grade compliance program in minutes.

#### Summary
Compliance at every commit. You can add deep license scanning, dependency analysis & intelligent compliance into your realtime development workflow.

Features:
* Deep Code Scanning
* Real time Compliance
* Smart review workflow
* [Integrations](https://docs.fossa.com/docs) and real time alerts
* Automated attributions and reports
* Release Management/Flexibility

### FOSSID

#### Website
[FOSSID](https://fossid.com/)

#### Products for Open Source Software
* FOSSID

#### Summary
Features:
* Precise Results
    * Get the most accurate reports thanks to the biggest Knowledge Base in the industry, which identifies the true origin of your code, instead of leaving you with incomplete scan results or inaccurate lists of endless matches.
* Lightning Fast Scans
    * FOSSID’s extreme code search algorithm scans files in milliseconds. That’s up to 1000 times faster than the competition. Thus introducing no time penalty in your development cycle.
* Safe and Private
    * Your code is never uploaded or sent to the server. For maximum privacy and reliability, FOSSID can be deployed entirely within your work network so that performing scans does not involve any external dependencies or traffic outside your network premises.
* Seamless Integration
    * Whether as stand-alone tool or within a continuous integration environment, FOSSID’s lightweight Linux or Windows clients can be incorporated seamlessly into your development process.

### TripleCheck

#### Website
[TripleCheck](http://triplecheck.tech/)

#### Products for Open Source Software
* TripleCheck Xray

#### Summary
Features
* Find the licenses and plagiarized source code snippets that are inside your software. 
* Save yourself from copyright infringements and start cleaning the code snippets, icons or hidden software that should not be there.
* This tool runs offline from your laptop with verifiable privacy. No clouds, no installs, no complications. Clean your software.

### WhiteSource

#### Website
[WhiteSource](https://www.whitesourcesoftware.com/)

#### Products for Open Source Software
* WhiteSource offers one comprehensive solution that includes all the tools needed to ensure that you’re on top of your open source usage, including the full extent of our database with vulnerabilities from the CVE and dozens of other sources and all features (Web Advisor, unlimited number of plugins, unlimited number of users, unlimited number of policies, and more).

#### Summary
WhiteSource is with you in every step of the software development lifecycle, and keeps monitoring your open source components, even after you release, based on the last build inventory report. 

Features
* Detection
    Automatically identiﬁes all the open source components and dependencies in your build by constant and automatic cross-referencing of your open source components against WhiteSource’s deﬁnitive database of open source repositories.
* Selection
    While you search for open source components, our browser plugin reveals any reported bugs, security risks, undesirable licenses (as deﬁned by the company policy you set up) newer versions and more for each component, so you can make better decisions about which component to add to your build.
* Alerting
    The earlier you detect an issue the easier and less expensive it is to ﬁx. Find out about potential pitfalls in your open source components and their dependencies before they turn into problems with optional security, policy, bug, and newer version email alerts. Each indicates level of severity, from high to low.
* Reporting
    Because WhiteSource continually and automatically logs a detailed inventory of your open source components, dependencies, licenses and license references, 100% accurate, up-to-date reports are always just a click away, and can be downloaded to spreadsheets in seconds.

All [integrations](https://www.whitesourcesoftware.com/whitesource-integrations/). 

### NexB/DejaCode

#### Website
[NexB](https://www.nexb.com/index.html)

#### Products for Open Source Software
* DejaCode

#### Summary
DejaCode helps companies better manage open source code in their software development.
Features: 
* Component Identification
    Determine software component provenance (origin and license) using a combination of scanning tools and expert review. Different software component identification activities may be needed at multiple points in your software development lifecycle ranging from code check-in to product release.
* Governance
    Establish policies for licensing and use of open source software components, design processes to implement these policies and automate compliance with license obligations wherever possible. Good governance policies, processes and tools can significantly reduce the costs of compliance and the risks of non-compliance.
* Component Management
    Record your inventories of software development components and your bills of materials for products in nexB's DejaCode. DejaCode is designed to consolidate your software component data from internal and external sources and automate common compliance tasks like generating an Attribution Notice for a product release.
* Software Reuse
    Enable software developers to easily identify open source software components that are approved for reuse in your products and systems, and also those components that may not be acceptable for reuse. This can significantly accelerate software component selection.

### Insigniary

#### Website
[Insigniary](https://www.insignary.com/)

#### Products for Open Source Software
* Clarity

#### Summary
Clarity is a specialized software composition analysis solution that helps customers gain visibility into the binary code they use by identifying known, preventable security vulnerabilities, while also highlighting potential license compliance issues. It uses unique fingerprint-based technology, which works on the binary-level without the need for source code or reverse engineering. 

Features:
* Identify Open Source Security And Compliance in Binary Code
    Insignary is dedicated to making the connected world a safer place by providing insight into identifying security and compliance issues in Open Source code.
* License Compliance
    Prevents conflicts with license compliance issues and copyright trolls
* Export Options
    Able to export security and compliance BoM in Excel, CSV, and JSON formats
* Vulnerability Ranking
    Uses Clarity algorithm to rank and prioritize open source security vulnerabilities in binary code
* Update Notification
    Notifies users of new vulnerabilities in already scanned files
* Flexible Deployment
    Available as cloud-based or on-premise solution

### Sonatype

#### Website
[Sonatype](https://www.sonatype.com/)

#### Products for Open Source Software
Nexus:
* Nexus Platform
    Empower dev, security and ops with fully automated OSS governance
* Nexus Lifecycle
    Continuously remediate OSS risk across entire SDLC
* Nexus Firewall
    Stop risky OSS components from entering SDLC
* Nexus Auditor
    Monitor production apps for OSS risk
* Nexus Repository Pro
    Manage binaries, artifacts, and release candidates with support
* Nexus Repository OSS
    Manage binaries, artifacts, and release candidates for FREE 
* Nexus Intelligence
    Real time OSS intel service (the power behind the platform)
* Nexus Vulnerability Scanner
    Identify open source risk in apps for FREE

#### Summary
Our integrated open source governance platform (Nexus) helps more than 1,000 organizations and 10 million software developers simultaneously accelerate innovation and improve application security.

Universally Intelligent
* The Nexus platform is pure polyglot and knows more about the quality of open source than anyone else in the world.

Universally Integrated
* The Nexus platform infuses polyglot intelligence into your preferred tools early, everywhere, and at scale.

[View all integrations](https://www.sonatype.com/products-overview)

### Anchore

#### Website
[Anchore](https://anchore.com/)

#### Products for Open Source Software
* [Anchore Engine (i.e. Anchore Open Source)](https://anchore.com/opensource/)
    * The Anchore open source project allows developers to perform detailed analysis on their container images, run queries, produce reports and define policies that can be used in CI/CD pipelines. Developers can extend the tool to add new plugins that add new queries, new image analysis, and new policies.
* [Anchore Enterprise](https://anchore.com/enterprise/)
    * Anchore’s On-Premises solution provides end-to-end security and compliance for the enterprise built on the open source Anchore Engine. With Anchore Enterprise you can use the Anchore UI to perform deep image scans and create and apply policies for security and compliance, as well as take advantage of an air-gapped feed service.

#### Summary
The Most Complete Container Security Inspection Platform for the Enterprise. The only end-to-end container security and compliance platform built on open source. Anchore performs an in depth analysis of your container image allowing you to generate a detailed manifest and create and apply specific policy gates and checks for your entire container workload on premises and in the cloud.

### CAST Software Intelligence

#### Website
[CAST](https://www.castsoftware.com/)

#### Products for Open Source Software
* [CAST Highlight](https://www.castsoftware.com/products/highlight)
    * CAST Highlight is a leading SaaS Digital Readiness Platform that consolidates Software Intelligence to track hidden risks in your custom & open source software
        * Assess and Track Application Portfolio Health
        * Build your smart Cloud Migration Roadmap with Fact-Based Software Analytics
        * Identify Vulnerabilities (CVE’s), Third-Party and Open Source software across your Application Portfolio
        * Detect Data Privacy Issues Hiding In Your Software
* [CAST AIP](https://www.castsoftware.com/products/application-intelligence-platform)
    * Software Intelligence engine designed to measure software health, size, flaws and generate architectural blueprints of multi-tiered, multi-technology software.

#### Summary
CAST technology combines architectural and engineering assessments to examine how the application’s components interact and work across technology layers, data structures, and other software systems.  

* Analyzes the system architecture to identify invalid calls and references between technology layers.
* Emulates run-time behavior of system components.
* Scans for patterns and anti-patterns in application control flow.
* Aggregates and normalizes findings based on industry standards and consolidate across applications.
* Adjusts findings to match application behaviors
* Track data flow along static and dynamic call stacks
* Verifies cross-layer and cross-technology links between components
* Understands programming language syntaxes and grammar using source code parsing
* Validates engineering practices against a rules engine to identify non-compliant objects or situations
* Identifies cross-layer and technology transactions from user interface to data entities

CAST Software Intelligence provides a holistic understanding of a system enabling the identification of dangerous software flaws while ensuring safe, resilient, agile, and high-performing systems.

### Rogue Wave Software

#### Website
[Rogue Wave](https://www.roguewave.com/)

#### Products for Open Source Software
* OpenLogic
    * OpenLogic CentOS support
        Bring expertise and around-the-clock support, offering guidance, training, and solutions to troubleshoot issues and optimize deployments along with competitive pricing.
    * OpenLogic open source support
        You get around-the-clock access to Tier 3/4 open source architects ready to support, consult, and educate your team to solve issues across your entire software stack and development lifecycle.
    * OpenLogic stacks
        OpenLogic is an expert-curated and orchestrated open source infrastructure, offering six different stacks designed for enterprise scale and performance, and allowing you to rapidly create and deploy applications, APIs, and more.

#### Summary
OpenLogic provides everything you need to build and manage your open source solutions (OSS):
* Out-of-the-box solutions
* Enhanced support
* Strategic consulting and training
* Multi-technology support
* No vendor lock-in
* Free assessment workshop

### Verifa

#### Website
[Verifa](https://verifa.io/)

#### Products for Open Source Software
* Verifa DevOps Platform is a Pipeline as a Service
    A Continuous Delivery Pipeline is made up of a collection of processes and tools that Verifa interacts with.

#### Summary
Verifa helps, advises, implements and maintains Continuous Delivery pipelines for their customers.The Verifa DevOps Platform can be deployed using existing infrastructure within your premises, or on scalable and self-managed cloud solutions, such as Google Cloud, AWS, Azure, or a provider of your choice. The platform is encapsulated within orchestration technology and can therefore be easily transferred and scaled across your organization.

---

## Development Environments

---

