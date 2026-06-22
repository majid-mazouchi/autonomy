---
title: "The Data Plumbing Behind Fleet Diagnosis"
subtitle: "Every fleet method assumes a clean, joined, trustworthy table. Here is how that table is actually built — joining records by VIN, aligning clocks, and surviving missing data."
date: 2026-04-11 23:55:00 -0400
category: "Control Systems"
slug: data-plumbing-fleet-diagnosis
excerpt: "The unglamorous foundation under the fleet posts. Those posts assumed a clean 'one row per car' table — build attributes, telemetry summary, warranty outcome — and went straight to de-mixing and surveillance. But that table does not arrive by post; it is assembled from messy raw sources that disagree about identity, time, and meaning. This piece builds it from the raw for the 6,000-car EV fleet with the P0AE0 charging code: join build records, telemetry, warranty claims, service notes, and DTC logs by VIN; survive the record-linkage pitfalls that corrupt the join — typos, duplicate claims, many-to-one rows, remanufactured parts — with fuzzy matching in the Fellegi–Sunter sense; align events that live on four different clocks to a common time-in-service reference so onset curves and survival models are valid; map and respect biased missingness instead of imputing over it; harmonize units and drifting DTC dictionaries into one shared canonical model; and wire it into an ingestion → canonical store → per-vehicle summary → analysis pipeline with lineage so any diagnosis can be re-run. Plain words, worked numbers, figures, algorithms, practical notes, and references."
reading_time: 21
---

This is the foundation beneath [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }}) and the posts that follow it. Those posts built the *method* of diagnosing a population — de-mix the mixture, draw the cohort boundary, fit the hazard, run the surveillance. Every one of them opens with the same silent assumption: that you already hold a clean, joined, trustworthy table, one row per car. You almost never do. That table is the output of a long, dull pipeline nobody writes about, and when the pipeline is wrong the analysis on top is *confidently* wrong — a plumbing artifact wearing the costume of a finding.

This post is how the table actually gets built from the raw. It takes the same 6,000-car EV fleet throwing the `P0AE0` charging code — firmware regression and bad connector lot — and assembles its one-row-per-car table from five messy, disagreeing sources. The theme throughout: garbage in, confident-garbage out.

## What it covers

Ten sections, about twenty-one minutes, in plain language with the arithmetic and decisions shown.

**Part A · Joining the sources**

**§ 2 — The entities and the spine.** VIN as the join key; the five sources — build records, telemetry, warranty claims, service notes, DTC logs — reduced to one row per car, with the `build_vehicle_summary` algorithm.

**§ 3 — Record-linkage pitfalls.** VIN typos and OCR errors, duplicate claims, many-to-one rows, remanufactured parts, and fuzzy matching in the Fellegi–Sunter sense when the key is dirty.

**Part B · Making it analyzable**

**§ 4 — Time alignment.** Build, in-service, event, and report dates disagree; align everything to time-in-service so onset curves and survival models are valid.

**§ 5 — Missingness & data quality.** Why the gaps are not random, how missingness ties to selection and survivorship, validation rules, and provenance per field.

**§ 6 — Schema & semantics.** Harmonizing units, drifting DTC dictionaries, and supplier-lot encodings into one canonical data model.

**Part C · The platform**

**§ 7 — Architecture.** Ingestion → canonical store → per-vehicle summary → analysis; batch vs streaming; lineage and reproducibility.

**§ 8 — Worked example.** Assembling the 6,000-car table: join by VIN, dedupe claims, align to in-service date, flag the 4% missing connector-temperature, and emit the table the fleet de-mix consumes.

**§ 9 — Practical notes.** Field rules for the data plumbing.

**§ 10 — References & further reading.** Databases, warehousing, record linkage, and data quality, with pointers.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/data-plumbing-fleet-diagnosis.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL in the warm-paper layout of the series, with an entity/spine diagram, a record-linkage pitfalls panel, a multi-clock alignment timeline, a cars-by-fields missingness map, a canonical-semantics table, a pipeline architecture diagram, two algorithms, a worked assembly of the 6,000-car table, practical notes, and references.

## Where it sits

The diagnosis series, in order:

**I · The core method**

1. [Root-Cause Analysis Under Uncertain, Heterogeneous Evidence]({{ '/posts/rca-under-uncertain-heterogeneous-evidence/' | relative_url }})
2. [When Is the Evidence Enough?]({{ '/posts/evidence-sufficiency-and-conflict/' | relative_url }})
3. [Harder Cases in Diagnosis]({{ '/posts/harder-cases-in-diagnosis/' | relative_url }})

**II · At fleet scale**

4. [Fleet-Scale Root-Cause Analysis]({{ '/posts/fleet-scale-root-cause-analysis/' | relative_url }})
5. [Fleet RCA, Made Rigorous]({{ '/posts/fleet-rca-made-rigorous/' | relative_url }})

**III · Proof, foundations & prevention**

6. [Proving Cause with Experiments]({{ '/posts/proving-cause-with-experiments/' | relative_url }})
7. [Diagnosis on the Vehicle]({{ '/posts/diagnosis-on-the-vehicle/' | relative_url }})
8. **The Data Plumbing Behind Fleet Diagnosis** — *(this post)*
9. [From Root Cause to No Cause]({{ '/posts/prevention-and-corrective-action/' | relative_url }})

Full map: [The Diagnosis Series index]({{ '/posts/diagnosis-series/' | relative_url }}).

---

← Back to [Autonomy]({{ '/' | relative_url }})
