---
name: employee-feedback-kb
description: Use when the Employee Feedback Agent needs to load role goals or band expectations into context. Reads the local PDF knowledge base files (role-goals.pdf, BTS band-expectations.pdf, CSM band-expectations.pdf) so the agent can reference them without a WXO deployment.
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
  - BTS employee: `knowledge-bases/BTS band-expectations.pdf`
  - CSM employee: `knowledge-bases/CSM band-expectations.pdf`
  - ATL employee: `knowledge-bases/ATL IBM Performance Expectations By Band 2026.pdf`

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
