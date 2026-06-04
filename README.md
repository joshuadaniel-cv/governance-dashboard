passcode is test
# <div align="center">[CV Data Governance Dashboard](https://joshuadaniel-cv.github.io/governance-dashboard/)</div>

# CV Data Governance Dashboard — Executive Summary

## What is it?

A single-page internal tool that gives CVGlobal's dataOPS team a real-time
operational view of how well the DW team's data assets are governed,
catalogued, and maintained .

---

## Purpose

Designed for a Data Stewards or Governance Analyst to open at the start of
the day and immediately know what needs attention across seven governance
dimensions in one place.

---

## What it shows

| Panel | Question it answers |
|---|---|
| **Connector Health** | Are our OvalEdge data connections crawling successfully? |
| **Data Quality & Anomalies** | How complete, accurate, and timely is our data? |
| **Lineage Coverage** | How far does our data flow traceability reach? |
| **Asset Descriptions** | Are business and technical descriptions filled in? |
| **Tags & Business Terms** | Is our taxonomy and glossary in order? |
| **Log of Changes** | What changed recently — schema, access, classifications? |
| **Monthly Report** | Are our governance metrics improving month on month? |

---

## Who it is for

- **Primary** — Data Steward, Governance Analyst (CVGlobal)
- **Secondary** — Ops Managers, DPO, or platform owner wanting a one-page health check

---

## What it is not

A replacement for OvalEdge. This is a **read-only observability layer** —
it does not allow editing, cataloguing, or data access. It sits on top of
existing governance operations and makes them visible at a glance.

---

## Technical notes

- Static site hosted on GitHub Pages
- Connector data fetched live from a Google Sheet (Overview tab)
- Falls back to placeholder data if the sheet is not yet published
- Password-protected via Staticrypt (AES-256, shared team password)- See 1password 
- No data is transmitted to any third party — all processing is client-side
- Aligned to ISO/IEC 27001:2022 and GDPR (EU) 2016/679

---

*CV Data Governance Dashboard · Draft · CVGlobal Data & Governance Operations*
