# Policy Engine

The purpose of the policy engine component is to issue warnings, errors and/or tasks based on comparing the license analysis of a codebase to pre-defined sets of rules and exceptions (**policy elements**).

In the context of the PoC, policy elements can be both **repository-based** and **universal** (i.e. applied to any repositor).

## Universal policy elements

### Contexts

An organization may freely create and name different contexts, which enables it to apply different rulesets and exceptions to different use contexts. For example, an organization may want to differentiate rules based on contexts such as `distribution of code on device` and `provision of service over network` etc.

Contexts are specified, i.e. named and listed, in a universal policy document. To associate an individual codebase/deliverable with its relevant context, the relevant context is given in a repository-level document.

### License whitelists

License whitelists are lists of SPDX license expressions for licenses that upon discovery in license analysis, will not create a _rule violation_ and an ensuing error, warning or similar. License whitelists can but do not have to be context-specific, i.e. there can be whitelists applicable only to one or more contexts.

Whitelists can be overridden on the repository level on a licence-by-license basis.

### License blacklists

License blaclists are lists of SPDX license expressions for licenses that upon discovery in license analysis, _will_ create an error, warning or similar. While the use of _whitelists_ should be encouraged as the basis of any policy element setup, blacklists may have their place when, for example, certain rule violations need to be emphasized or otherwise treated differently. For example, where a license whitelist violation may be defined to create a mere warning, a blacklist violation can be defined to create an error that immediately fails the build in a continuous integration context.

Blacklists can be overridden on the repository level on a licence-by-license basis.

### Rule violation triggers

Violations of license whitelists and blacklists can be individually set to either merely output warnings or exit with an error code. This behavior can be overridden on the repository level on a whitelist and/or blacklist basis (i.e. applying the override to all whitelists and/or blacklists).

## Repository-level policy elements

### Context choice

The context relevant for the repository can be specified in the repository level config document.

### Excluded files and paths

Files and file paths can be excluded from policy violation analysis by specifying them with globs and also supplying a reason for doing so (e.g. "Files only used for testing and not included in released artifacts in the context of this project.").

### Supplementary license information

The concluded license information can be overridden for specified files or filepaths (specified as globs). A reason for this must also be supplied.

### Whitelist / blacklist override

Universally set whitelists and blacklists can be overridden on the repository level on a licence-by-license basis.

### Rule violation trigger override

In universal config, violations of license whitelists and blacklists can be individually set to either merely output warnings or exit with an error code. This behavior can be overridden on the repository level on a whitelist and/or blacklist basis (i.e. applying the override to all whitelists and/or blacklists).

## Examples

### Universal policy config

```yaml
contexts:
  - "service provision"
  - "distributed software"
  - "consumer device"
whitelists:
  - whitelisted:
      - "Apache-2.0"
      - "BSD-3-Clause"
      - "GPL-2.0-only"
      - "..."
    trigger: "warning"
blacklists:
  - context: "consumer device"
    blacklisted:
      - "GPL-3.0-only"
      - "GPL-3.0-or-later"
      - "LGPL-3.0-only"
      - "LGPL-3.0-or-later"
      - "AGPL-3.0-only"
      - "AGPL-3.0-or-later"
      - "..."
    trigger: "error"
```

### Repository policy config

```yaml
context: "consumer device"
trigger_override:
  scope: "whitelists"
  trigger: "error"
excludes:
  - path: "test-utils/**"
    reason: "Only used for testing. Not included in released artifacts in the context of this project."
```
