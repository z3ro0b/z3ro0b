<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.png">
  <img alt="z3rob — Abdelrahman Zourob. Authorization research on identity platforms." src="assets/banner-dark.png" width="100%">
</picture>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/strip-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/strip-light.png">
  <img alt="Now: Okta PAM and access governance. Class: authorization logic. Posture: coordinated disclosure. Credentials: eJPT and eWPT." src="assets/strip-dark.png" width="100%">
</picture>

<br>

Okta Privileged Access and Access Governance. Role scope, access requests, entitlement grants, and isolation between sandboxes.

### Research

| Class | The failure |
| --- | --- |
| BOLA / IDOR | An object identifier is doing the authorization |
| BFLA | A role can call a function the policy does not grant |
| Broken access control | The console hides an action the API still performs |
| Tenant isolation | State or admin control crosses an org or sandbox boundary |
| Workflow trust | An approval or a grant is assumed, and never checked |

### Rules

In-scope assets only. The proof is the smallest request that shows impact. A finding is published after it is fixed and the program allows it.

No customer tenants. No social engineering. No availability testing.

### Practice

| | |
| --- | --- |
| Burp Suite | Request tampering and replay |
| Kali Linux, WSL2 | Lab |
| Obsidian | Research notes |
| `bugcrowd-mcp` | Read-only scope and submission state. It does not send exploit traffic |

### Credentials

eJPT · eWPT — INE Security

<sub>Write-ups, a disclosure ledger, and a PGP key are added here only after a program clears them. Do not send vulnerability details in a GitHub issue.</sub>
