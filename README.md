# z3rob

Authorization research on identity platforms. Most of the work is Okta.

I test how access is actually enforced: object access, function access, admin roles, and tenant boundaries. The bugs worth reporting are the ones the UI never offers and the token still allows.

In-scope assets only. Reports go to the program that owns the asset, with the smallest proof that shows impact. No customer tenants, no social engineering, no availability testing.

## Now

Okta Privileged Access and Access Governance. Role scope, access requests and entitlement grants, and isolation between sandboxes.

## Scope of research

| Area | What I am looking for |
| --- | --- |
| BOLA / IDOR | Cross-object access on users, groups, apps, entitlements, and requests |
| BFLA | API actions a role can call that policy says it cannot |
| Broken access control | UI checks that the API does not repeat |
| Tenant isolation | Data or admin actions that cross an org or sandbox boundary |
| Workflow trust | Approvals and grants that skip a control the product implies is mandatory |

## Disclosure

Nothing is listed until the vendor has fixed it and the program allows publication. There is no public ledger yet. Cleared write-ups will be added here, not before.

## Method

Manual first. Burp Suite for request tampering. Obsidian for research notes. Kali Linux on WSL2 as the lab.

`bugcrowd-mcp` is a read-only client for program scope and submission state. It does not generate exploit traffic.

## Certifications

eJPT and eWPT. INE Security.

## Contact

No public contact on this page yet. Do not put vulnerability details in a GitHub issue.

PGP, a Bugcrowd profile, and write-ups will be linked here once they exist.
