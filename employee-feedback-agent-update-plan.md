# Employee Feedback Agent Update Implementation Plan

## Overview
This document outlines the detailed implementation plan for updating the Employee Feedback Agent with new self-feedback templates, updated knowledge base structure, and enhanced agent instructions.

---

## Phase 1: Templates ✅ COMPLETED

### 1.1 Quarterly Self-Feedback Template ✅
- **File**: `employee-self-feedback-quarterly.md`
- **Status**: Created
- **Content**: 6-question format covering deliverables, strengths, challenges, improvements, support needed, and additional comments

### 1.2 Yearly Self-Feedback Template ✅
- **File**: `employee-self-feedback-yearly.md`
- **Status**: Created
- **Content**: 3 main sections (Business/Skills/Behaviors Outcomes) plus 6 additional reflection questions

---

## Phase 2: Knowledge Base Updates 🔄 IN PROGRESS

### 2.1 Update Knowledge Base Configuration
**File**: `knowledge-bases/employee-performance-kb.yaml`

**Current Structure**:
```yaml
spec_version: v1
kind: knowledge_base
name: employee-performance-kb
description: Comprehensive knowledge base containing role-specific goals, KPIs, success criteria for BTS and CSM roles, plus salary band expectations, competencies, and progression criteria for bands 6-10
documents:
  - path: ./role-goals.pdf
  - path: ./band-expectations.pdf
```

**Required Changes**:
```yaml
spec_version: v1
kind: knowledge_base
name: employee-performance-kb
description: Comprehensive knowledge base containing role-specific goals, KPIs, success criteria for BTS and CSM roles, plus role-specific salary band expectations, competencies, and progression criteria for bands 6-10
documents:
  - path: ./role-goals.pdf
  - path: ./BTS band-expectations.pdf
  - path: ./CSM band-expectations.pdf
```

**Notes**:
- Keep `role-goals.pdf` (contains team goals for both BTS and CSM)
- Remove `band-expectations.pdf` (generic band expectations)
- Add `BTS band-expectations.pdf` (BTS-specific band expectations) - ✅ Already uploaded
- Add `CSM band-expectations.pdf` (CSM-specific band expectations) - ✅ Already uploaded

### 2.2 Knowledge Base Files Status
- ✅ `role-goals.pdf` - Exists in knowledge-bases/
- ✅ `BTS band-expectations.pdf` - Exists in knowledge-bases/
- ✅ `CSM band-expectations.pdf` - Exists in knowledge-bases/
- ❌ `band-expectations.pdf` - To be removed from KB config (but can keep file for reference)

---

## Phase 3: Agent Configuration Updates 🔄 IN PROGRESS

### 3.1 Update Agent Instructions
**File**: `agents/employee_feedback_agent.yaml`

#### 3.1.1 Add "Key Points of Feedback" Collection
**Location**: Step 3 - Performance Information section

**Add after existing performance information questions**:
```yaml
- Manager's key points of feedback for the employee
  * What are the main talking points you want to discuss?
  * What specific feedback do you want to ensure is communicated?
```

#### 3.1.2 Update Employee Self-Feedback Request
**Location**: Step 2 - Previous Review Check section

**Add new step after Step 2**:
```yaml
### Step 2.5: Employee Self-Feedback
Ask: "Do you have the employee's self-feedback for this review period?"
- If YES: Request the employee's completed self-feedback
  * For Quarterly/Mid-Year: Use employee-self-feedback-quarterly.md template
  * For Year-End: Use employee-self-feedback-yearly.md template
- If NO: Proceed with manager's input only, but note this in the review
```

#### 3.1.3 Update Knowledge Base Query Instructions
**Location**: Knowledge Base Queries section

**Update to**:
```yaml
## Knowledge Base Queries

After gathering information, query the knowledge base to retrieve:

### From Role Goals:
- Role-specific goals and KPIs for the employee's role (BTS or CSM)
- Success criteria for each goal area
- Cross-role competencies expected
- Performance measurement guidelines

### From Role-Specific Band Expectations:
**IMPORTANT**: Query the appropriate band expectations document based on employee role:
- For BTS employees: Query BTS band-expectations.pdf
- For CSM employees: Query CSM band-expectations.pdf

Retrieve:
- Competency expectations for the employee's current band
- Technical and soft skill requirements specific to their role
- Leadership and autonomy expectations
- Progression criteria to the next band
- Role-specific behavioral expectations
```

#### 3.1.4 Update Feedback Generation Instructions
**Location**: Feedback Generation section

**Add integrated analysis guidance**:
```yaml
## Integrated Analysis Approach

When generating feedback, naturally integrate references to knowledge base expectations throughout:

1. **Compare Against Role Goals**: 
   - Reference specific goals from role-goals.pdf
   - Note alignment or gaps with team objectives
   - Cite specific KPIs or success criteria

2. **Compare Against Band Expectations**:
   - Reference role-specific band expectations (BTS or CSM)
   - Note how performance aligns with band-level competencies
   - Identify areas where employee exceeds or needs development relative to band standards

3. **Synthesize Employee and Manager Input**:
   - Compare employee self-feedback with manager observations
   - Note areas of alignment and divergence
   - Use both perspectives to create balanced assessment

4. **Natural Integration**:
   - Weave KB references throughout feedback sections
   - Avoid creating separate "comparison" sections
   - Use phrases like:
     * "This aligns with the Band [X] expectation for..."
     * "According to [Role] goals, this demonstrates..."
     * "This exceeds the band-level requirement of..."
     * "Development needed to meet Band [X] standard for..."
```

#### 3.1.5 Update Confirmation Checklist
**Location**: Before Generating Feedback section

**Update to**:
```yaml
## Before Generating Feedback

Always confirm you have:
- ✓ Employee name, role, and band
- ✓ Review period and type (Quarterly/Mid-Year/Year-End)
- ✓ Performance information and examples from manager
- ✓ Manager's key points of feedback for employee
- ✓ Employee self-feedback (if available)
- ✓ Previous review (if applicable)
- ✓ Retrieved relevant information from role-goals.pdf
- ✓ Retrieved role-specific band expectations (BTS or CSM)
- ✓ Confirmed which output format to use based on review type

Then ask: "I have all the information needed. Based on this being a [Quarterly/Mid-Year/Year-End] review, I will generate feedback using the appropriate format and integrate insights from the knowledge base. Would you like me to proceed?"
```

### 3.2 Update Agent YAML Metadata
**File**: `agents/employee_feedback_agent.yaml`

**Update description**:
```yaml
description: Generates structured performance reviews for Brand Technical Specialists (BTS) and Client Success Managers (CSM) in salary bands 6-10, with role-specific band expectations, integrated knowledge base analysis, and progress tracking between reviews
```

**Update knowledge_base section**:
```yaml
knowledge_base:
  - employee-performance-kb
```

---

## Phase 4: Documentation Updates 📝 PENDING

### 4.1 Update README
**File**: `employee-feedback-agent-README.md`

**Changes needed**:
1. Update "Knowledge Base Structure" section to reflect new 3-document structure
2. Add section on new self-feedback templates
3. Update "How It Works" to mention integrated KB analysis
4. Add "Key Points of Feedback" to manager input requirements

### 4.2 Update Quickstart Guide
**File**: `QUICKSTART-employee-feedback-agent.md`

**Changes needed**:
1. Update prerequisites to mention new self-feedback templates
2. Update knowledge base upload instructions for 3 documents
3. Add step for providing employee self-feedback
4. Update example conversation flow

### 4.3 Update Implementation Summary
**File**: `IMPLEMENTATION-SUMMARY.md`

**Changes needed**:
1. Document the KB consolidation and role-specific split
2. Add new self-feedback templates to file structure
3. Update agent capabilities section
4. Document integrated analysis approach

### 4.4 Update Upload Guide
**File**: `knowledge-bases/upload-guide.md`

**Changes needed**:
1. Update to reflect 3-document structure
2. Add instructions for BTS and CSM band-expectations files
3. Update file naming conventions

---

## Phase 5: Testing Plan 🧪 PENDING

### 5.1 Test Scenarios

#### Test 1: Quarterly Review - BTS Employee
- Employee: Band 7 BTS
- With employee self-feedback
- Verify KB queries BTS band-expectations.pdf
- Verify integrated analysis in output

#### Test 2: Mid-Year Review - CSM Employee
- Employee: Band 8 CSM
- Without employee self-feedback
- Verify KB queries CSM band-expectations.pdf
- Verify "Key Points of Feedback" collected

#### Test 3: Year-End Review - BTS Employee
- Employee: Band 9 BTS
- With employee self-feedback (yearly template)
- With previous review for comparison
- Verify comprehensive 4-section output
- Verify integrated KB analysis

#### Test 4: Year-End Review - CSM Employee
- Employee: Band 6 CSM
- With employee self-feedback (yearly template)
- Verify role-specific band expectations referenced
- Verify Business/Skills/Behaviors outcomes

### 5.2 Validation Checklist
- [ ] Agent collects all required information including "Key Points of Feedback"
- [ ] Agent requests appropriate self-feedback template based on review type
- [ ] Agent queries correct band expectations file based on role (BTS vs CSM)
- [ ] Agent queries role-goals.pdf for both roles
- [ ] Output naturally integrates KB references throughout
- [ ] Output format matches review type (Quarterly/Mid-Year vs Year-End)
- [ ] Employee and manager perspectives are synthesized
- [ ] Band-level expectations are referenced appropriately

---

## Implementation Steps Summary

### Immediate Actions (Requires Code Mode)
1. ✅ Create quarterly self-feedback template
2. ✅ Create yearly self-feedback template
3. ⏳ Update `knowledge-bases/employee-performance-kb.yaml` to include 3 documents
4. ⏳ Update `agents/employee_feedback_agent.yaml` with new instructions
5. ⏳ Deploy updated KB configuration
6. ⏳ Deploy updated agent configuration

### Follow-up Actions
7. ⏳ Test agent with all review types and both roles
8. ⏳ Update all documentation files
9. ⏳ Update deployment scripts if needed
10. ⏳ Create user guide for new self-feedback templates

---

## Files Modified/Created

### Created ✅
- `employee-self-feedback-quarterly.md` - Quarterly/Mid-Year self-feedback template
- `employee-self-feedback-yearly.md` - Year-End self-feedback template
- `employee-feedback-agent-update-plan.md` - This implementation plan

### To Be Modified ⏳
- `knowledge-bases/employee-performance-kb.yaml` - Update documents list
- `agents/employee_feedback_agent.yaml` - Update instructions and KB queries
- `employee-feedback-agent-README.md` - Update documentation
- `QUICKSTART-employee-feedback-agent.md` - Update quickstart guide
- `IMPLEMENTATION-SUMMARY.md` - Update implementation details
- `knowledge-bases/upload-guide.md` - Update upload instructions

### Already Exists ✅
- `knowledge-bases/role-goals.pdf` - Team goals (keep)
- `knowledge-bases/BTS band-expectations.pdf` - BTS band expectations (use)
- `knowledge-bases/CSM band-expectations.pdf` - CSM band expectations (use)

---

## Next Steps

**To complete this implementation, switch to Code or Advanced mode to:**

1. Update `knowledge-bases/employee-performance-kb.yaml` with the new 3-document structure
2. Update `agents/employee_feedback_agent.yaml` with enhanced instructions
3. Redeploy the knowledge base and agent
4. Test the updated agent
5. Update all documentation files

**Command to switch modes:**
- For code changes: Switch to "Code" or "Advanced" mode
- For testing: Use Advanced mode (has MCP tools for deployment)

---

*This plan was created in Plan mode. Implementation requires Code or Advanced mode for YAML file modifications.*