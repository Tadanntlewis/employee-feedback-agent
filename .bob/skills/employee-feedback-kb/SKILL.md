---
name: employee-feedback-kb
description: Use when the Employee Feedback Agent needs to load role goals or band expectations into context. Reads the local knowledge base files (role-goals.pdf, ATL-role-goals.md, and the BTS, CSM, and ATL band-expectations-by-band files) so the agent can reference them without a WXO deployment.
---

# Employee Feedback Knowledge Base Loader

This skill replaces the watsonx Orchestrate knowledge base queries with local PDF reads.
Follow these steps to load the relevant content into context.

## Step 1 — Determine Which Documents to Load

Ask (or infer from context) which documents are needed:

- **Role goals**:
  - BTS or CSM employee: `knowledge-bases/role-goals.pdf`
  - ATL employee: `knowledge-bases/ATL-role-goals.md`
- **Band expectations**:
  - BTS employee: `knowledge-bases/BTS-band-expectations-by-band.md`
  - CSM employee: `knowledge-bases/CSM-band-expectations-by-band.md`
  - ATL employee: `knowledge-bases/ATL-band-expectations-by-band.md`

The three `*-band-expectations-by-band.md` files restate the source PDFs' Factor x Band tables
with every cell tied to its band column. **Use them instead of the PDFs**: read as text, the
PDFs lose their table layout, so it is unclear which band a block of text belongs to. The PDFs
stay in the folder as the authoritative source.

Band coverage notes:
- ATL: expectations are defined for Bands 8-10 only (Bands 6 and 7 are empty in the source).
- BTS: Band 10 has no defined expectations. Bands 7-9 are cumulative
  ("B06, plus: ...").
- CSM: all Bands 6-10 are defined.
- If the employee's band has no defined expectations, tell the manager rather than inventing any.

If the employee role has not been established yet, load all role goals files and all band
expectations files so the content is available.

## Step 2 — Read the Files

Use `read_file` to load each needed document. Issue these calls sequentially (one at a time):

1. Read the appropriate role goals file based on the employee's role
2. Read the appropriate band expectations file based on the employee's role

## Step 3 — Confirm Content Is in Context

After reading, briefly summarise what was loaded so the manager can confirm the right
documents were retrieved, for example:

> "I have loaded the role goals and BTS Band 8 expectations into context. I'll reference
> these when generating the performance review."

## Step 4 — Continue With the Review

Return control to the Employee Feedback Agent workflow. The agent should now naturally
weave references to the loaded KB content throughout the generated feedback sections.
