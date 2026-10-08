# Employee Feedback Agent - Quick Start Guide

Get up and running in under 5 minutes with **IBM Bob** — no deployment or API keys needed.

## Prerequisites

- [IBM Bob](https://www.ibm.com/products/watsonx-orchestrate) installed
- This repository cloned locally:
  ```bash
  git clone https://github.com/Tadanntlewis/employee-feedback-agent.git
  cd employee-feedback-agent
  ```

The PDF knowledge base files are already included in `knowledge-bases/`. No setup required.

## 3 Steps to Your First Review

### Step 1: Open the Project in Bob (30 seconds)

Open Bob and set this cloned folder as your workspace. The `.bob/` directory in the repo contains the mode and skill — Bob loads them automatically.

### Step 2: Switch to "Employee Feedback Agent" Mode (5 seconds)

Click the mode picker at the bottom of the Bob interface and select **Employee Feedback Agent**.

### Step 3: Start a New Conversation

Tell the agent who needs a review. It will guide you through the rest.

## Sample Conversation

```
You: I need to create a Q1 review for Sarah Johnson

Agent: I'll help you create a performance review for Sarah.
       Let me gather some information. What is Sarah's role? (BTS or CSM)

You: Client Success Manager

Agent: What is Sarah's current salary band? (6-10)

You: Band 8

Agent: What review period is this for, and is this a Quarterly, Mid-Year, or Year-End review?

You: Q1 2026, Quarterly

Agent: Do you have a previous review for Sarah to reference for progress tracking?

You: No, this is her first review with us

Agent: Do you have Sarah's employee self-feedback for this period?

You: Yes, I'll paste it here...

Agent: Great. Please share Sarah's key accomplishments during Q1 2026, any challenges faced,
       client feedback, and your key talking points for this review.

You: - Increased client retention from 85% to 92%
     - Onboarded 5 new enterprise clients ($500K ARR)
     - Generated $250K in expansion revenue
     - Led 12 strategic business reviews
     - Mentored 2 junior CSMs
     [Manager's talking points: very strong quarter, wants to address communication gaps...]

Agent: I have all the information needed. I'll now load the role goals and CSM Band 8
       expectations from the knowledge base, then generate the quarterly review.
       Would you like me to proceed?

You: Yes

Agent: [Generates structured two-section quarterly review with KB references woven throughout]
```

## What the Agent Produces

### Quarterly & Mid-Year Reviews
```
# Performance Review: Sarah Johnson
Role: CSM | Band: 8 | Period: Q1 2026 | Type: Quarterly

## 1. What Went Well?
[3-5 paragraphs with specific examples referencing CSM role goals and Band 8 expectations]

## 2. What Could Be Improved?
[2-4 paragraphs with actionable, constructive feedback]

## Manager Notes
[Optional space for additional comments]
```

### Year-End Reviews
```
# Annual Performance Review: Sarah Johnson
Role: CSM | Band: 8 | Period: Year-End 2026

## 1. Business Outcomes Summary
## 2. Skills Outcomes Summary
## 3. Behaviors Outcomes Summary
## 4. Manager Evaluation Summary
   Performance Segment: [1-5] + Manager Comments
```

## Sample Test Data

Use this data to try the agent before your first real review:

**Employee:** Sarah Johnson  
**Role:** CSM | **Band:** 8 | **Period:** Q1 2026 | **Type:** Quarterly

**Accomplishments:**
- Increased client retention from 85% to 92%
- Onboarded 5 new enterprise clients ($500K ARR)
- Generated $250K in expansion revenue
- Led 12 strategic business reviews
- Mentored 2 junior CSMs
- Resolved 3 at-risk accounts successfully

**Challenges:**
- Initial adjustment to new CRM system (resolved in 2 weeks)
- One client escalation (handled professionally, client retained)

**Client Feedback:**
- "Sarah is proactive and always thinking ahead"
- "Best CSM we've worked with"
- "Helped us achieve 30% efficiency gain"

## Common Issues

| Issue | Fix |
|-------|-----|
| Mode not visible in picker | Confirm this folder is set as your Bob workspace and restart Bob |
| PDFs not loading | Verify PDF files exist at `knowledge-bases/role-goals.pdf`, `knowledge-bases/BTS band-expectations.pdf`, `knowledge-bases/CSM band-expectations.pdf` |
| Agent gives generic feedback | Provide more specific performance details and examples |

## Getting Help

- **Full Documentation**: See `employee-feedback-agent-README.md`
- **Self-Assessment Templates**: `employee-self-feedback-quarterly.md` / `employee-self-feedback-yearly.md`
- **GitHub**: https://github.com/Tadanntlewis/employee-feedback-agent
