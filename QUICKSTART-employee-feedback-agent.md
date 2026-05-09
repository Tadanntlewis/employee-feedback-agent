# Employee Feedback Agent - Quick Start Guide

Get your Employee Feedback Agent up and running in 15 minutes!

## Prerequisites Checklist

- [ ] IBM watsonx Orchestrate account with API access
- [ ] watsonx Orchestrate CLI installed (`pip install ibm-watsonx-orchestrate`)
- [ ] IBM Cloud API key set as environment variable
- [ ] Two PDF documents ready:
  - `role-goals.pdf` (BTS and CSM role goals, KPIs, success criteria)
  - `band-expectations.pdf` (Band 6-10 competencies and progression criteria)

## Quick Setup (3 Steps)

### Step 1: Upload Your PDF Documents (2 minutes)

Place your PDF files in the `knowledge-bases/` directory:

```bash
# Copy your PDFs to the knowledge-bases directory
cp /path/to/your/role-goals.pdf knowledge-bases/role-goals.pdf
cp /path/to/your/band-expectations.pdf knowledge-bases/band-expectations.pdf

# Verify files are in place
ls -lh knowledge-bases/*.pdf
```

**Expected output:**
```
-rw-r--r--  1 user  staff   2.5M May  4 15:30 knowledge-bases/band-expectations.pdf
-rw-r--r--  1 user  staff   1.8M May  4 15:30 knowledge-bases/role-goals.pdf
```

### Step 2: Deploy the Agent (10 minutes)

Run the deployment script:

```bash
./import-employee-feedback-agent.sh
```

**What happens:**
1. ✓ Checks for required PDF files
2. ✓ Imports role goals knowledge base
3. ✓ Imports band expectations knowledge base
4. ✓ Waits for indexing (5-10 minutes)
5. ✓ Imports employee feedback agent
6. ✓ Verifies deployment

**Expected output:**
```
==========================================
Employee Feedback Agent Deployment
==========================================

✓ All required PDF files found

Step 1: Importing Role Goals Knowledge Base...
✓ Role Goals KB imported successfully

Step 2: Importing Band Expectations Knowledge Base...
✓ Band Expectations KB imported successfully

Step 3: Waiting for knowledge bases to be indexed...
✓ role-goals-kb is READY
✓ band-expectations-kb is READY

Step 4: Importing Employee Feedback Agent...
✓ Employee Feedback Agent imported successfully

==========================================
✓ Deployment Complete!
==========================================
```

### Step 3: Test the Agent (3 minutes)

Start a chat session:

```bash
orchestrate chat --agent employee_feedback_agent
```

Try this sample conversation:

```
You: I need to create a performance review for Sarah Johnson

Agent: Hello! I'll help you create a performance review. Let's start with the employee basics.
       What is Sarah's role?

You: Client Success Manager

Agent: What is Sarah's current salary band?

You: Band 8

Agent: What review period is this for?

You: Q1 2026

Agent: Is this a quarterly or annual review?

You: Quarterly

Agent: Do you have a previous review for Sarah that I should reference for progress tracking?

You: No, this is her first review with us

Agent: Thank you. Please share Sarah's key accomplishments during Q1 2026.

You: - Increased client retention rate from 85% to 92%
     - Successfully onboarded 5 new enterprise clients
     - Generated $250K in expansion revenue
     - Led strategic business reviews with 12 key accounts
     - Mentored 2 junior CSMs

[Continue providing performance details...]

Agent: I have all the information needed. Would you like me to generate the performance review now?

You: Yes

Agent: [Generates comprehensive structured feedback with ratings, summary, and recommendations]
```

## Verification Checklist

After deployment, verify everything is working:

- [ ] Knowledge bases show status "READY"
  ```bash
  orchestrate knowledge-bases check-status --name role-goals-kb
  orchestrate knowledge-bases check-status --name band-expectations-kb
  ```

- [ ] Agent appears in agent list
  ```bash
  orchestrate agents list --kind native | grep employee_feedback_agent
  ```

- [ ] Agent responds to chat
  ```bash
  orchestrate chat --agent employee_feedback_agent
  ```

- [ ] Agent can query knowledge bases (test by asking about role goals)

## Common Issues & Quick Fixes

### Issue: "PDF file not found"
**Fix:** Ensure PDFs are in `knowledge-bases/` directory with exact names:
```bash
ls knowledge-bases/role-goals.pdf
ls knowledge-bases/band-expectations.pdf
```

### Issue: "Knowledge base indexing timeout"
**Fix:** Large PDFs may take longer. Wait 15 minutes and check status:
```bash
orchestrate knowledge-bases check-status --name role-goals-kb
```

### Issue: "Agent import failed"
**Fix:** Ensure knowledge bases are imported and READY first:
```bash
orchestrate knowledge-bases list
```

### Issue: "Authentication error"
**Fix:** Set your IBM Cloud API key:
```bash
export IBM_CLOUD_API_KEY="your-api-key-here"
```

## Next Steps

Once your agent is running:

1. **Create Your First Review**
   - Start with a simple test case
   - Provide detailed performance information
   - Review the generated feedback

2. **Refine Knowledge Bases**
   - Update PDFs based on feedback quality
   - Add more specific criteria and examples
   - Re-import updated knowledge bases

3. **Train Your Team**
   - Share the README with managers
   - Provide sample conversations
   - Establish best practices for your organization

4. **Monitor and Improve**
   - Collect feedback from managers
   - Track review quality and consistency
   - Iterate on knowledge base content

## Getting Help

- **Full Documentation**: See `employee-feedback-agent-README.md`
- **Upload Guide**: See `knowledge-bases/upload-guide.md`
- **Implementation Plan**: See `employee-feedback-agent-plan.md`
- **watsonx Orchestrate Docs**: https://developer.watson-orchestrate.ibm.com

## Sample Performance Data

Need test data? Use this sample for Sarah Johnson (CSM, Band 8, Q1 2026):

**Accomplishments:**
- Increased client retention from 85% to 92%
- Onboarded 5 new enterprise clients ($500K ARR)
- Generated $250K in expansion revenue
- Led 12 strategic business reviews
- Mentored 2 junior CSMs
- Resolved 3 at-risk accounts successfully

**Challenges:**
- Initial difficulty with new CRM system (resolved in 2 weeks)
- One client escalation (handled professionally, client retained)

**Client Feedback:**
- "Sarah is proactive and always thinking ahead" - Client A
- "Best CSM we've worked with" - Client B
- "Helped us achieve 30% efficiency gain" - Client C

**Goals for Next Quarter:**
- Achieve 95% retention rate
- Generate $300K expansion revenue
- Complete advanced negotiation training
- Lead cross-functional project

---

**Ready to start?** Run `./import-employee-feedback-agent.sh` now!