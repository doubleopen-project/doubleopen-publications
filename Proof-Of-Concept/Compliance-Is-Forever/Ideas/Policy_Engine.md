# Policy Engine

The purpose of the policy engine component is to issue warnings, errors and/or tasks based on comparing the license analysis of a codebase to pre-defined sets of rules and exceptions (**policy elements**).

In the context of the PoC, policy elements can be both **repository-based** and **universal** (i.e. applied to any repositor).

## Universal policy elements

### Contexts

An organization may freely create and name different contexts, which enables it to apply different rulesets and exceptions to different use contexts. For example, an organization may want to differentiate rules based on contexts such as `distribution of code on device` and `provision of service over network` etc.

Contexts are specified, i.e. named and listed, in a universal policy document in YAML. To associate an individual codebase/deliverable with its relevant context, the relevant context is specified in a repository-level document for each defined application.

### License allowlists

License allowlists are lists of SPDX license expressions for licenses that upon discovery in license analysis, will not create a _rule violation_ and an ensuing error or warning. License allowlists can but do not have to be context-specific, i.e. there can be allowlists applicable only to one or more contexts.

Allowlists can be amended on the repository level on a licence-by-license basis per application.

### License denylists

License denylists are lists of SPDX license expressions for licenses that upon discovery in license analysis, _will_ create an error or warning. While the use of _allowlists_ should be encouraged as the basis of any policy element setup, denylists may have their place when, for example, certain rule violations need to be emphasized or otherwise treated differently. For example, where a license allowlist violation may be defined to create a mere warning, a denylist violation can be defined to create an error that immediately fails the build in a continuous integration context.

Denylists can be amended on the repository level on a licence-by-license basis per application.

### Rule violation triggers

Violations of license allowlists and denylists can be individually set to either merely output warnings or exit with an error code. This behavior can be overridden on the repository level on a allowlist and/or denylist basis (i.e. applying the override to all allowlists and/or denylists) per application.

## Repository-level policy elements

### Context choice

The context relevant for each defined application can be specified in the repository level config document.

### Excluded files and paths

Files and file paths can be excluded from policy violation analysis by specifying them with globs and also supplying a reason for doing so (e.g. "Files only used for testing and not included in released applications in the context of this project.").

### Supplementary license information

The concluded license information can be overridden for specified files or filepaths (specified as globs). A reason for this must also be supplied.

### Rule violation emission override

In universal config, violations of license allowlists and denylists can be individually set to either merely output warnings or exit with an error code. This behavior can be overridden on the repository level on an allowlist and/or denylist basis (i.e. applying the override to all allowlists and/or denylists) per application.

## Examples

Below you can see examples for global and repository-level configurations. On the repository level, you can see that two non-consumer applications are built from the code in the repository, one for software-only distribution and one for distribution on device.

### Universal policy config

```yaml
# Definition of contexts available for repo-level conf
contexts:
  - "saas"
  - "consumer software"
  - "non-consumer software"
  - "consumer device"
  - "non-consumer device"
# More expressions can be added to allow/denylists on repo-level
allowlists:
  - allowlisted: # List of allowed SPDX expressions (global context by default)
      - "0BSD"
      - "Apache-1.1"
      - "Apache-2.0"
      - "BSD-1-Clause"
      - "BSD-2-Clause"
      - "BSD-3-Clause"
      - "BSD-3-Clause-Clear"
      - "BSD-4-Clause-UC"
      - "BSD-Source-Code"
      - "BSL-1.0"
      - "FSFAP"
      - "FSFUL"
      - "FSFULLR"
      - "GPL-2.0-only"
      - "GPL-2.0-or-later"
      - "GPL-3.0-only"
      - "GPL-3.0-or-later"
      - "ISC"
      - "LGPL-2.0-only"
      - "LGPL-2.0-or-later"
      - "LGPL-2.1-only"
      - "LGPL-2.1-or-later"
      - "LGPL-3.0-only"
      - "LGPL-3.0-or-later"
      - "MIT"
      - "..."
    emit: "warning" # Warning or error
denylists: # List of rejected SPDX expressions
  - context: # Applied only in defined contexts
      -"consumer device"
      -"consumer software"
    denylisted:
      - "GPL-3.0-only"
      - "GPL-3.0-or-later"
      - "LGPL-3.0-only"
      - "LGPL-3.0-or-later"
      - "AGPL-3.0-only"
      - "AGPL-3.0-or-later"
      - "..."
    emit: "error"
global_exclude: # Files excluded from review globally
  - path: "LICENSE*"
```

### Repository policy config

```yaml
global: # Applied for any application
  exclude:
    - path: "test-utils/**"
      reason: "Only used for testing. Not included in released applications."
applications: # Application-level conf
  - name: "Alpha"
    context: "non-consumer software" # Selected context
    allowlisted: # Expressions *added* to global allowlist
      - "GPL-2.0-only"
      - "GPL-2.0-or-later"
      - "GPL-2.0-with-bison-exception"
      - "GPL-2.0-with-autoconf-exception"
    emit_override: # Override global emit option
      - scope: "allowlisted" # allowlisted or denylisted
        emit: "error"
    exclude:
      - path: ["plugins/**", "!plugins/alpha/**"] # Exclude folder except for one subfolder
        reason: "Not included in released application"
      - path: "LICENSES/*"
        reason: "License files"
  - name: "Beta"
    context: "non-consumer device"
    allowlisted:
      - "GPL-2.0-only"
      - "GPL-2.0-or-later"
      - "GPL-2.0-with-bison-exception"
      - "GPL-2.0-with-autoconf-exception"
    include_only: # Review only specified files/folders
      - path: "beta/**"
      - path: "beta_plugins/**"
    exclude:
      - path: "beta/tests"
        reason: "Only used for testing. Not included in released application"
```
