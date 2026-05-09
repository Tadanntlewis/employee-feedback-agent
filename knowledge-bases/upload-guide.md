# Knowledge Base Upload Guide for Employee Feedback Agent

## Overview

This guide explains how to upload your role goals and band expectations documents to watsonx Orchestrate and configure them as knowledge bases for the Employee Feedback Agent.

---

## Required Documents

You'll need to prepare **2 PDF documents**:

### 1. Role Goals Document
**Filename suggestion:** `role-goals.pdf`

**Should contain:**
- Brand Technical Specialist (BTS) role goals, KPIs, and success criteria
- Client Success Manager (CSM) role goals, KPIs, and success criteria
- Cross-role competencies and expectations
- Performance measurement guidelines
- Rating scales and evaluation criteria

**Format tips:**
- Use clear headings and sections
- Include specific metrics and targets
- Provide concrete examples where possible
- Keep language clear and professional

### 2. Band Expectations Document
**Filename suggestion:** `band-expectations.pdf`

**Should contain:**
- Band 6 expectations, competencies, and progression criteria
- Band 7 expectations, competencies, and progression criteria
- Band 8 expectations, competencies, and progression criteria
- Band 9 expectations, competencies, and progression criteria
- Band 10 expectations, competencies, and progression criteria
- Progression guidelines between bands
- Skill development requirements

**Format tips:**
- Organize by band level (6-10)
- Include technical and soft skill requirements
- Specify experience expectations
- Define leadership and autonomy levels
- Include progression indicators

---

## Upload Methods

### Method 1: Using the CLI (Recommended)

Once you have your PDF files ready, we'll use the watsonx Orchestrate CLI to upload them:

```bash
# Import role goals knowledge base
orchestrate knowledge-bases import \
  --file knowledge-bases/role-goals-kb.yaml

# Import band expectations knowledge base
orchestrate knowledge-bases import \
  --file knowledge-bases/band-expectations-kb.yaml
```

The YAML configuration files will be created during implementation and will reference your PDF files.

### Method 2: Using the Web UI

1. Log into watsonx Orchestrate web interface
2. Navigate to **Knowledge Bases** section
3. Click **Create Knowledge Base**
4. Upload your PDF document
5. Configure the knowledge base settings
6. Save and wait for indexing to complete

---

## Knowledge Base Configuration

### Role Goals Knowledge Base

**Configuration details:**
```yaml
kind: knowledge_base
name: role-goals-kb
description: Role-specific goals, KPIs, and success criteria for BTS and CSM roles
spec:
  type: document
  source:
    type: local
    path: ./role-goals.pdf
  chunking:
    strategy: semantic
    chunk_size: 1000
    overlap: 200
  embedding:
    model: text-embedding-ada-002
```

**What this does:**
- Creates a searchable knowledge base from your role goals PDF
- Uses semantic chunking to preserve context
- Enables the agent to retrieve relevant role expectations during feedback generation

### Band Expectations Knowledge Base

**Configuration details:**
```yaml
kind: knowledge_base
name: band-expectations-kb
description: Salary band expectations, competencies, and progression criteria for bands 6-10
spec:
  type: document
  source:
    type: local
    path: ./band-expectations.pdf
  chunking:
    strategy: semantic
    chunk_size: 1000
    overlap: 200
  embedding:
    model: text-embedding-ada-002
```

**What this does:**
- Creates a searchable knowledge base from your band expectations PDF
- Enables the agent to compare employee performance against band-specific criteria
- Supports progression readiness assessments

---

## Upload Process Steps

### Step 1: Prepare Your Documents
- [ ] Create or gather your role goals document
- [ ] Create or gather your band expectations document
- [ ] Convert to PDF format if not already
- [ ] Review for completeness and accuracy
- [ ] Save in the `knowledge-bases/` directory

### Step 2: Place Files in Project
```bash
# Place your PDF files here:
knowledge-bases/role-goals.pdf
knowledge-bases/band-expectations.pdf
```

### Step 3: Create Knowledge Base Configurations
We'll create YAML configuration files that reference your PDFs:
- `knowledge-bases/role-goals-kb.yaml`
- `knowledge-bases/band-expectations-kb.yaml`

### Step 4: Upload to watsonx Orchestrate
```bash
# Import both knowledge bases
orchestrate knowledge-bases import --file knowledge-bases/role-goals-kb.yaml
orchestrate knowledge-bases import --file knowledge-bases/band-expectations-kb.yaml
```

### Step 5: Verify Upload
```bash
# List all knowledge bases to confirm
orchestrate knowledge-bases list
```

### Step 6: Check Indexing Status
```bash
# Check if knowledge bases are ready
orchestrate knowledge-bases check-status --name role-goals-kb
orchestrate knowledge-bases check-status --name band-expectations-kb
```

**Wait for status:** `READY` before proceeding with agent testing.

---

## Document Content Guidelines

### For Role Goals Document

**Essential sections:**
1. **Role Overview** - Purpose and key responsibilities
2. **Core Goals** - 4-6 main goal areas per role
3. **Success Criteria** - Specific, measurable criteria for each goal
4. **KPIs** - Quantifiable metrics with targets
5. **Measurement Methods** - How performance is assessed
6. **Cross-Role Competencies** - Skills expected of all employees
7. **Rating Scale** - How to interpret performance levels (1-5)

**Example structure:**
```
Role: Brand Technical Specialist (BTS)

Goal 1: Technical Excellence
- Success Criteria:
  * Maintain 95%+ accuracy in technical implementations
  * Complete 2+ technical certifications per year
  * Resolve 90% of issues without escalation
- KPIs:
  * Technical Accuracy Rate: 95%
  * Certification Completion: 2/year
  * Issue Resolution Rate: 90%
```

### For Band Expectations Document

**Essential sections:**
1. **Band Overview** - General expectations for each band
2. **Technical Skills** - Required technical competencies
3. **Leadership & Autonomy** - Expected independence level
4. **Experience Requirements** - Years of experience or equivalent
5. **Soft Skills** - Communication, collaboration, etc.
6. **Progression Criteria** - What's needed to move to next band
7. **Examples** - Concrete examples of band-level work

**Example structure:**
```
Band 7: Senior Level

Technical Skills:
- Expert in core technologies
- Can architect solutions independently
- Mentors junior team members

Leadership & Autonomy:
- Works independently on complex projects
- Leads small project teams
- Makes technical decisions with minimal oversight

Experience:
- 5-7 years relevant experience
- Demonstrated expertise in domain

Progression to Band 8:
- Consistently delivers complex projects
- Demonstrates strategic thinking
- Shows leadership across teams
```

---

## Troubleshooting

### Issue: Knowledge base upload fails
**Solution:** Check file size (max 50MB per file) and format (must be PDF)

### Issue: Indexing takes too long
**Solution:** Large documents may take 5-10 minutes to index. Check status periodically.

### Issue: Agent can't find relevant information
**Solution:** 
- Ensure documents use clear headings and structure
- Check that content is searchable (not scanned images)
- Verify knowledge base status is READY

### Issue: Retrieval returns irrelevant content
**Solution:**
- Adjust chunking strategy in configuration
- Improve document structure and headings
- Add more specific keywords in documents

---

## Next Steps

Once your documents are uploaded and indexed:

1. **Switch to Code/Advanced mode** to implement the agent
2. **Configure the agent** to use both knowledge bases
3. **Test the agent** with sample employee data
4. **Refine** based on feedback quality
5. **Deploy** to production environment

---

## Questions?

If you encounter any issues during upload or have questions about document format, let me know and I can help troubleshoot or adjust the configuration.
