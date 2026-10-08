# Employee Feedback Agent - Setup Checklist

Use this checklist to confirm the agent is set up and working correctly in IBM Bob.

---

## Prerequisites

- [ ] IBM Bob is installed
- [ ] Repository is cloned locally:
  ```bash
  git clone https://github.com/Tadanntlewis/employee-feedback-agent.git
  ```
- [ ] Knowledge base PDFs are present:
  - [ ] `knowledge-bases/role-goals.pdf`
  - [ ] `knowledge-bases/BTS band-expectations.pdf`
  - [ ] `knowledge-bases/CSM band-expectations.pdf`
- [ ] Bob configuration files are present:
  - [ ] `.bob/custom_modes.yaml`
  - [ ] `.bob/skills/employee-feedback-kb/SKILL.md`

---

## Setup Steps

### Step 1: Open the Project in Bob
- [ ] Open Bob
- [ ] Set the cloned `employee-feedback-agent` folder as your workspace
- [ ] Confirm the mode picker shows **Employee Feedback Agent**

> If the mode does not appear: verify `.bob/custom_modes.yaml` exists and restart Bob.

### Step 2: Verify the Knowledge Base Skill
- [ ] In a conversation (in Employee Feedback Agent mode), type: `/employee-feedback-kb`
- [ ] Confirm the skill activates and reads the PDFs without error

---

## First Review Test

Use the sample data below to confirm everything works end to end.

### Sample Employee: Sarah Johnson (CSM, Band 8, Q1 2026 Quarterly)

- [ ] Start a new conversation in Employee Feedback Agent mode
- [ ] Provide employee basics:
  - Name: Sarah Johnson
  - Role: Client Success Manager
  - Band: 8
  - Review Period: Q1 2026
  - Review Type: Quarterly
- [ ] Answer "No" to previous review
- [ ] Provide performance information:
  - Increased client retention from 85% to 92%
  - Onboarded 5 new enterprise clients ($500K ARR)
  - Generated $250K in expansion revenue
  - Led 12 strategic business reviews
  - Mentored 2 junior CSMs
- [ ] Confirm agent loads KB (role-goals.pdf + CSM band-expectations.pdf)
- [ ] Agent generates review with two sections (What Went Well / What Could Be Improved)
- [ ] Review references Band 8 CSM expectations and role goals

### Quality Check
- [ ] Feedback is specific to the performance data provided (not generic)
- [ ] Band expectations are referenced naturally throughout the narrative
- [ ] Review format matches the Quarterly template (two sections, no rating score)
- [ ] Tone is professional and constructive

---

## Optional: Deploy to watsonx Orchestrate

If you also want to run this agent in watsonx Orchestrate:

### Prerequisites
- [ ] IBM watsonx Orchestrate account is active
- [ ] IBM Cloud API key is available
- [ ] watsonx Orchestrate CLI is installed:
  ```bash
  pip install ibm-watsonx-orchestrate
  ```
- [ ] Environment variable is set:
  ```bash
  export IBM_CLOUD_API_KEY="your-api-key-here"
  ```

### WXO Deployment Steps
- [ ] Import knowledge bases:
  ```bash
  orchestrate kb import knowledge-bases/role-goals-kb.yaml
  orchestrate kb import knowledge-bases/band-expectations-kb.yaml
  ```
- [ ] Wait for KB indexing (5-10 minutes), confirm both show status READY:
  ```bash
  orchestrate knowledge-bases list
  ```
- [ ] Import the agent:
  ```bash
  orchestrate agent import agents/employee_feedback_agent.yaml
  ```
- [ ] Confirm agent appears in agent list:
  ```bash
  orchestrate agents list --kind native
  ```
- [ ] Test via chat:
  ```bash
  orchestrate chat --agent employee_feedback_agent
  ```

---

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| "Employee Feedback Agent" not in mode picker | Confirm `.bob/custom_modes.yaml` exists in the workspace root and restart Bob |
| KB skill fails to load PDFs | Verify the three PDF files are present in `knowledge-bases/` with exact filenames |
| Generic feedback not tied to role/band | Provide more specific performance details; confirm KB was loaded before generation |
| Mode picker shows mode but behavior seems wrong | Start a new conversation to reset context |

---

## Resources

- **Quick Start**: `QUICKSTART-employee-feedback-agent.md`
- **Full Documentation**: `employee-feedback-agent-README.md`
- **Implementation Summary**: `IMPLEMENTATION-SUMMARY.md`
- **Self-Assessment Templates**: `employee-self-feedback-quarterly.md` / `employee-self-feedback-yearly.md`
- **GitHub**: https://github.com/Tadanntlewis/employee-feedback-agent

---

**Version:** 2.0  
**Last Updated:** 2026  
**Runtime:** IBM Bob (local) — no WXO deployment required
