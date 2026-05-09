# Employee Feedback Agent - Deployment Checklist

Use this checklist to track your deployment progress step by step.

---

## Pre-Deployment Checklist

### Environment Setup
- [ ] IBM watsonx Orchestrate account is active
- [ ] IBM Cloud API key is available
- [ ] watsonx Orchestrate CLI is installed
  ```bash
  pip install ibm-watsonx-orchestrate
  ```
- [ ] Environment variable is set
  ```bash
  export IBM_CLOUD_API_KEY="your-api-key-here"
  ```
- [ ] Configuration files are in place
  - [ ] `~/.config/orchestrate/config.yaml`
  - [ ] `~/.cache/orchestrate/credentials.yaml`

### Document Preparation
- [ ] Role goals document is ready (PDF format)
  - [ ] Contains BTS role goals and KPIs
  - [ ] Contains CSM role goals and KPIs
  - [ ] Contains cross-role competencies
  - [ ] Contains rating scales and measurement guidelines
  - [ ] File size is under 50MB
  - [ ] PDF is searchable (not scanned images)

- [ ] Band expectations document is ready (PDF format)
  - [ ] Contains Band 6 expectations
  - [ ] Contains Band 7 expectations
  - [ ] Contains Band 8 expectations
  - [ ] Contains Band 9 expectations
  - [ ] Contains Band 10 expectations
  - [ ] Contains progression criteria
  - [ ] File size is under 50MB
  - [ ] PDF is searchable (not scanned images)

### File Verification
- [ ] All implementation files are present:
  - [ ] `agents/employee_feedback_agent.yaml`
  - [ ] `knowledge-bases/role-goals-kb.yaml`
  - [ ] `knowledge-bases/band-expectations-kb.yaml`
  - [ ] `import-employee-feedback-agent.sh`
  - [ ] `employee-feedback-agent-README.md`
  - [ ] `QUICKSTART-employee-feedback-agent.md`

---

## Deployment Steps

### Step 1: Upload PDF Documents
- [ ] Copy role goals PDF to project
  ```bash
  cp /path/to/your/role-goals.pdf knowledge-bases/role-goals.pdf
  ```
- [ ] Copy band expectations PDF to project
  ```bash
  cp /path/to/your/band-expectations.pdf knowledge-bases/band-expectations.pdf
  ```
- [ ] Verify files are in place
  ```bash
  ls -lh knowledge-bases/*.pdf
  ```
- [ ] Confirm file sizes are reasonable (< 50MB each)

**Expected Result:**
```
-rw-r--r--  1 user  staff   2.5M May  4 15:30 knowledge-bases/band-expectations.pdf
-rw-r--r--  1 user  staff   1.8M May  4 15:30 knowledge-bases/role-goals.pdf
```

### Step 2: Run Deployment Script
- [ ] Make script executable (if not already)
  ```bash
  chmod +x import-employee-feedback-agent.sh
  ```
- [ ] Run deployment script
  ```bash
  ./import-employee-feedback-agent.sh
  ```
- [ ] Monitor output for errors
- [ ] Wait for completion (10-15 minutes)

**Expected Output Checkpoints:**
- [ ] ✓ All required PDF files found
- [ ] ✓ Role Goals KB imported successfully
- [ ] ✓ Band Expectations KB imported successfully
- [ ] ✓ role-goals-kb is READY
- [ ] ✓ band-expectations-kb is READY
- [ ] ✓ Employee Feedback Agent imported successfully
- [ ] ✓ Deployment Complete!

### Step 3: Verify Deployment
- [ ] Check knowledge base status
  ```bash
  orchestrate knowledge-bases check-status --name role-goals-kb
  orchestrate knowledge-bases check-status --name band-expectations-kb
  ```
- [ ] Both KBs show status: **READY**

- [ ] List all knowledge bases
  ```bash
  orchestrate knowledge-bases list
  ```
- [ ] Confirm both KBs appear in list

- [ ] List agents
  ```bash
  orchestrate agents list --kind native
  ```
- [ ] Confirm `employee_feedback_agent` appears in list

**Verification Checklist:**
- [ ] role-goals-kb status is READY
- [ ] band-expectations-kb status is READY
- [ ] employee_feedback_agent is listed
- [ ] No error messages in deployment output

---

## Testing Phase

### Step 4: Initial Test
- [ ] Start chat session
  ```bash
  orchestrate chat --agent employee_feedback_agent
  ```
- [ ] Agent responds to initial message
- [ ] Agent asks for employee information

### Step 5: Sample Review Test
Use the sample data provided in QUICKSTART guide:

- [ ] Provide employee basics
  - Name: Sarah Johnson
  - Role: Client Success Manager
  - Band: 8
  - Review Period: Q1 2026
  - Review Type: Quarterly

- [ ] Provide performance information
  - Accomplishments (5+ items)
  - Challenges faced
  - Client feedback
  - Goals achieved

- [ ] Agent queries knowledge bases successfully
- [ ] Agent generates structured feedback
- [ ] Output includes all required sections:
  - [ ] Overall rating
  - [ ] Category ratings (6 areas)
  - [ ] Performance summary
  - [ ] Strengths (3-5 items)
  - [ ] Areas for improvement (2-4 items)
  - [ ] Development recommendations
  - [ ] Band progression assessment
  - [ ] Action items

### Step 6: Quality Check
- [ ] Review generated feedback for:
  - [ ] Accuracy (aligns with input data)
  - [ ] Completeness (all sections present)
  - [ ] Relevance (references role goals and band expectations)
  - [ ] Clarity (easy to understand)
  - [ ] Actionability (specific recommendations)

- [ ] Test knowledge base retrieval
  - [ ] Ask agent about BTS role goals
  - [ ] Ask agent about Band 7 expectations
  - [ ] Verify agent retrieves relevant information

---

## Post-Deployment Tasks

### Step 7: Documentation Review
- [ ] Review `employee-feedback-agent-README.md`
- [ ] Review `QUICKSTART-employee-feedback-agent.md`
- [ ] Understand troubleshooting procedures
- [ ] Familiarize with best practices

### Step 8: Team Preparation
- [ ] Identify managers who will use the agent
- [ ] Schedule training sessions
- [ ] Prepare training materials
- [ ] Create internal usage guidelines

### Step 9: Pilot Program
- [ ] Select 2-3 managers for pilot
- [ ] Generate 3-5 test reviews
- [ ] Collect feedback from managers
- [ ] Collect feedback from employees (if appropriate)
- [ ] Document issues and improvements needed

### Step 10: Refinement
- [ ] Review pilot feedback
- [ ] Update knowledge base documents if needed
  - [ ] Refine role goals content
  - [ ] Refine band expectations content
  - [ ] Re-import updated KBs
- [ ] Adjust agent instructions if needed
  - [ ] Modify `agents/employee_feedback_agent.yaml`
  - [ ] Re-import agent
- [ ] Test improvements

---

## Production Rollout

### Step 11: Full Deployment
- [ ] Announce agent availability to all managers
- [ ] Provide access to documentation
- [ ] Set up support channel for questions
- [ ] Monitor initial usage

### Step 12: Monitoring & Support
- [ ] Track agent usage metrics
  - [ ] Number of reviews generated
  - [ ] Manager adoption rate
  - [ ] Time saved per review
- [ ] Collect ongoing feedback
  - [ ] Manager satisfaction
  - [ ] Employee satisfaction
  - [ ] Review quality
- [ ] Address issues promptly
- [ ] Document common questions and solutions

### Step 13: Maintenance Schedule
- [ ] Set up monthly review of agent performance
- [ ] Schedule quarterly KB updates
- [ ] Plan annual comprehensive review
- [ ] Establish process for continuous improvement

---

## Troubleshooting Checklist

If you encounter issues, work through this checklist:

### Knowledge Base Issues
- [ ] Verify PDF files exist in correct location
- [ ] Check PDF file sizes (< 50MB)
- [ ] Confirm PDFs are searchable (not scanned images)
- [ ] Check KB import logs for errors
- [ ] Verify indexing completed (status: READY)
- [ ] Try re-importing KB if needed

### Agent Issues
- [ ] Verify agent YAML syntax is correct
- [ ] Confirm KB names match exactly in agent config
- [ ] Check that KBs are imported before agent
- [ ] Verify LLM model name is correct
- [ ] Review agent import logs for errors
- [ ] Try re-importing agent if needed

### Authentication Issues
- [ ] Verify IBM_CLOUD_API_KEY is set
- [ ] Check API key is valid and not expired
- [ ] Confirm config files are properly formatted
- [ ] Test authentication with simple command
  ```bash
  orchestrate agents list
  ```

### Quality Issues
- [ ] Review KB content for completeness
- [ ] Check if agent is retrieving relevant information
- [ ] Verify input data is specific and detailed
- [ ] Consider adjusting chunking strategy
- [ ] Review and refine agent instructions

---

## Success Criteria

Your deployment is successful when:

- [x] All deployment steps completed without errors
- [x] Both knowledge bases show status: READY
- [x] Agent appears in agent list
- [x] Agent responds to chat commands
- [x] Agent generates complete, structured reviews
- [x] Reviews reference role goals and band expectations
- [x] Managers can use agent independently
- [x] Review quality meets organizational standards
- [x] Time savings are measurable
- [x] Feedback from users is positive

---

## Next Steps After Successful Deployment

1. **Scale Usage**
   - [ ] Expand to more managers
   - [ ] Track adoption metrics
   - [ ] Share success stories

2. **Continuous Improvement**
   - [ ] Collect feedback regularly
   - [ ] Update KBs quarterly
   - [ ] Refine agent behavior based on usage
   - [ ] Add new features as needed

3. **Integration**
   - [ ] Consider HRIS integration
   - [ ] Explore automation opportunities
   - [ ] Link to goal tracking systems
   - [ ] Build analytics dashboard

4. **Documentation**
   - [ ] Keep documentation updated
   - [ ] Document lessons learned
   - [ ] Create FAQ based on common questions
   - [ ] Share best practices

---

## Emergency Rollback Procedure

If you need to rollback the deployment:

1. **Remove Agent**
   ```bash
   orchestrate agents remove --name employee_feedback_agent --kind native
   ```

2. **Remove Knowledge Bases**
   ```bash
   orchestrate knowledge-bases remove --name role-goals-kb
   orchestrate knowledge-bases remove --name band-expectations-kb
   ```

3. **Verify Removal**
   ```bash
   orchestrate agents list --kind native
   orchestrate knowledge-bases list
   ```

4. **Document Issues**
   - Record what went wrong
   - Note any error messages
   - Document steps taken
   - Plan corrective actions

5. **Fix and Redeploy**
   - Address identified issues
   - Test fixes locally if possible
   - Re-run deployment script
   - Verify success

---

## Support Resources

- **Documentation**: `employee-feedback-agent-README.md`
- **Quick Start**: `QUICKSTART-employee-feedback-agent.md`
- **Upload Guide**: `knowledge-bases/upload-guide.md`
- **Project Structure**: `PROJECT-STRUCTURE.md`
- **Implementation Summary**: `IMPLEMENTATION-SUMMARY.md`
- **watsonx Orchestrate Docs**: https://developer.watson-orchestrate.ibm.com

---

## Completion Sign-Off

Deployment completed by: ___________________________

Date: ___________________________

Verified by: ___________________________

Date: ___________________________

Notes:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

**Version:** 1.0  
**Last Updated:** 2026-05-04  
**Status:** Ready for Use