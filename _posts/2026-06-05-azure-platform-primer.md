---
title: "The Azure Platform — A Plain-Language Primer"
subtitle: "What Microsoft's cloud actually is, what lives inside it, and how the pieces fit together — explained from first principles, with diagrams."
date: 2026-06-05 09:00:00 -0400
category: "Tools"
slug: azure-platform-primer
excerpt: "Azure documentation is comprehensive in the same way that an unabridged dictionary is comprehensive — every term is defined, nothing is summarized, and you can spend a month reading it without ever learning what the cloud actually does. This primer is the plain-language alternative. Eleven sections covering what the cloud means, what Azure is, the three service models (IaaS/PaaS/SaaS), the three core service families, how resources are organized, global infrastructure, a worked example, and the rules of thumb that let an engineer make sensible decisions in their first month."
reading_time: 14
---

There is a particular kind of difficulty that mature cloud platforms create for new engineers: the documentation is *complete* in the sense that every term is defined, every service is listed, and every parameter is described — and *operationally useless* in the sense that none of it tells you what the cloud actually is, or how the pieces fit together, or which of the eight hundred services you'll actually reach for in your first year. Azure is the canonical example.

This primer is the plain-language fix. It is meant for the engineer who has been writing software for years, has used some cloud here and there, and now wants to understand Azure specifically — what it is, what's inside it, how it's organized, and what the mental model looks like — without first reading a thousand-page reference. The diagrams are the point. Every concept gets at least one figure. Every section ends with "the takeaway in one sentence."

## What it covers

Eleven sections, about fourteen minutes of reading.

**§ 01 — What "the cloud" actually means.** Before Azure specifically, the cloud generally. The five characteristics (on-demand, network-accessible, pooled, elastic, measured). Why renting compute beats owning it for most workloads, and the few cases where it doesn't.

**§ 02 — What Azure is.** Microsoft's slice of the cloud. The competitive position vs AWS and Google Cloud. The historical arc (started as "Windows Azure" in 2010, rebranded in 2014, now one of three serious hyperscalers).

**§ 03 — The three service models: IaaS, PaaS, SaaS.** The taxonomy that explains everything else. Infrastructure as a Service — you get a VM, you manage everything above the OS. Platform as a Service — you get a managed runtime, Microsoft manages everything below your code. Software as a Service — you get a finished application. The pizza-as-a-service analogy that finally makes the distinction land.

**§ 04 — The three core service families.** *Compute* — VMs, App Service, Functions, Containers, Kubernetes. *Storage* — Blob, File, Queue, Table, Disk. *Networking* — Virtual Network, Load Balancer, DNS, Front Door. The dozen services every Azure engineer touches in the first month.

**§ 05 — Beyond the basics.** The next layer out. Databases (SQL, Cosmos, MySQL, Postgres). AI services (OpenAI, Cognitive Services, Machine Learning). Identity (Entra ID, formerly Azure AD). DevOps (Azure DevOps, GitHub Actions integration). The handful you'll meet in the second month.

**§ 06 — How resources are organized.** The hierarchy. Tenant → Management Group → Subscription → Resource Group → Resource. Why each level exists and what you use it for. The naming conventions and tagging discipline that separate a maintainable Azure estate from a hopeless one.

**§ 07 — Global infrastructure: regions & zones.** The physical layer. Sixty-plus regions worldwide, organized into geographies, with availability zones for high availability within a region. How to pick a region. The latency and data-sovereignty trade-offs.

**§ 08 — A worked example: a web app on Azure.** The architectural walkthrough. A simple three-tier web app — frontend, API, database — deployed three different ways: IaaS (VMs), PaaS (App Service + SQL Database), and serverless (Static Web Apps + Functions + Cosmos). The cost, ops, and scaling implications of each.

**§ 09 — Pricing — how Azure charges you.** The mental model. Pay-per-second compute, pay-per-GB storage, pay-per-request networking. Reserved capacity for predictable workloads. Spot instances for interruptible ones. The four ways the bill surprises you in production.

**§ 10 — Security & identity.** The trust model. Managed identities. Role-based access control (RBAC). Key Vault for secrets. The "deny by default, allow on purpose" discipline that every production environment converges on.

**§ 11 — The handful of rules of thumb.** The shortlist. Start with PaaS, drop to IaaS only when you must. Tag everything. Use managed identities, never connection strings. Watch egress costs. Set budget alerts on day one. The dozen habits that compound into operational maturity.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/azure-platform-primer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The primer lives at its own URL with a warm-paper editorial layout — Azure-blue accent, five diagrams, eleven sections. Designed to be the document you keep open in a tab during your first month of Azure work.

---

← Back to [Autonomy]({{ '/' | relative_url }})
