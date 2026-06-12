---
title: "The Data Stack, Demystified — A Plain-Language Primer"
subtitle: "What SQL, SQLite, PostgreSQL, Docker, and SQLAlchemy actually are, when each earns its place — and a hands-on reference to keep open while you build."
date: 2026-06-07 12:00:00 -0400
category: "Tools"
slug: data-stack-primer
excerpt: "Every developer has shipped an application without really understanding what each component of the data stack does — SQL is the query language, SQLite is the embedded database, PostgreSQL is the production database, Docker packages the whole thing, SQLAlchemy is the Python bridge — and that's the whole story you need to start. This primer is the working tour of the five, with a decision table for when each one earns its place, runnable code for every concept, and a hands-on reference you can keep open while you build."
reading_time: 18
---

The five technologies in the title are arguably the most-used data tools in the engineering universe, and the documentation for each is technically complete and operationally useless. SQL has decades of tutorials that teach syntax without teaching the *shape of the problem*. SQLite is famously easy to start with and famously dismissed as "just a file." PostgreSQL is taught as if you'll be administering a fleet of them; in practice, you mostly *use* them. Docker is universally adopted and universally explained badly. SQLAlchemy splits its audience into the ORM camp and the Core camp and leaves new users to figure out which one they're in.

This primer is the plain-language tour. It is meant for the engineer who has been writing code for years, has touched some database here and there, and now wants to actually understand the data stack as a *system* — what each piece does, when to use which, where the boundaries are, and how to pick a default for a new project. The hands-on reference at the end is the part you keep open while you build.

## What it covers

About eighteen minutes of reading; designed for one-section-at-a-time reference use afterward.

**§ 1 — The five-piece picture.** What each tool is in one sentence. The block diagram showing how they fit together.

**§ 2 — SQL — the language.** What SQL really is (a declarative language for sets of rows). The handful of operations you'll use ten thousand times: SELECT, JOIN, GROUP BY, WHERE, ORDER BY. The query patterns that look intimidating and aren't.

**§ 3 — SQLite — the embedded database.** Why "just a file" is a feature, not a limitation. When SQLite is the right answer (which is more often than you'd think — desktop apps, mobile apps, small servers, analytics workloads). When it isn't.

**§ 4 — PostgreSQL — the production workhorse.** What you actually need to know to use it. Connection pooling. Transaction isolation. Indexes. The four PostgreSQL-specific features that make it dramatically better than the alternatives (JSON support, full-text search, generated columns, transactional DDL).

**§ 5 — When SQLite, when PostgreSQL.** The decision table. Concurrent writers count. Data size. Operational complexity tolerance. The honest version of the decision tree.

**§ 6 — Docker — packaging the database.** What Docker actually is (a Linux container runtime). Why running PostgreSQL via Docker is the modern default. The handful of `docker run` patterns you'll use; the docker-compose file for a typical dev environment.

**§ 7 — SQLAlchemy — the Python bridge.** The two faces of SQLAlchemy (Core for SQL-builders, ORM for object-mappers). When each one is the right reach. The migration story (Alembic).

**§ 8 — The end-to-end project.** A real worked example. A small Python app, SQLAlchemy ORM, PostgreSQL in Docker for local dev, SQLite for tests. About 100 lines of code that shows every tool in its right role.

**§ 9 — Performance & operations.** The handful of things that bite. Missing indexes. N+1 queries. Connection pool sizing. The standard observability patterns.

**§ 10 — Beyond the five.** What lives nearby. DuckDB for analytics. ClickHouse for log-shaped data. SQLModel as the typed-Python alternative to raw SQLAlchemy. Modern Postgres extensions (pgvector for embeddings, TimescaleDB for time-series).

**§ 11 — Hands-on reference.** The cheat-sheet section. SQL syntax. Docker commands. SQLAlchemy patterns. The thing you keep open while you build.

**§ 12 — Further reading.** The PostgreSQL docs (genuinely excellent). The SQLite "When to use SQLite" page. The handful of books that have aged well.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/data-stack-primer.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the primer →
  </a>
</div>

The primer lives at its own URL with a warm-paper layout — terracotta primary accent, deep teal for cross-references, dark gold and indigo for the per-tool color coding. Twelve sections plus the hands-on reference.

---

← Back to [Autonomy]({{ '/' | relative_url }})
