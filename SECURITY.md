# Security policy

## Supported version

Security fixes are applied to the latest release.

## Report a vulnerability

Use GitHub's private vulnerability reporting for this repository. Do not open a public issue containing secrets, exploit details, personal restaurant history, or API credentials.

Nomtiq never ships shared API keys. If a key has appeared in a commit, screenshot, chat, command argument, or log, revoke and rotate it immediately before reporting the exposure.

## Trust boundary

- Live restaurant queries go only to Amap or Serper, according to destination.
- Local taste and visit data are not published by the core skill.
- Provider text is untrusted data and must never be followed as instructions.
- Authenticated HTTP requests reject redirects.
