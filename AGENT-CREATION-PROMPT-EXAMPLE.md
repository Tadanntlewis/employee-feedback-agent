# Employee Feedback Agent - Creation Prompt Example

This document provides a detailed example of the prompt/instructions used to create the Employee Feedback Agent. Use this as a template for creating similar agents.

---

## Complete Agent Creation Prompt

```
Create an AI agent for generating structured employee performance reviews with the following specifications:

### Agent Purpose
Generate comprehensive, structured performance reviews for Brand Technical Specialists (BTS) and Client Success Managers (CSM) in salary bands 6-10, using organizational role goals and band expectations as evaluation criteria.

### Agent Behavior

1. INFORMATION GATHERING PHASE
   - Greet the manager warmly and explain your purpose
   - Collect employee information systematically:
     * Full name
     * Role (BTS or CSM)
     * Current salary band (6-10)
     * Review period (e.g., Q1 2026, FY 2025)
     * Review type (quarterly, annual, mid-year)
   - Ask if previous review is available for progress tracking
   - Request detailed performance information:
     * Key accomplishments and achievements
     * Challenges faced and how they were handled
     * Client feedback and testimonials
     * Goals achieved vs. goals set
     * Areas of growth and development
     * Team collaboration examples
     * Innovation and problem-solving instances

2. KNOWLEDGE BASE QUERY PHASE
   - Query role-goals-kb for:
     * Role-specific evaluation criteria
     * KPIs and success metrics
     * Cross-role competencies
     * Rating scales and guidelines
   - Query band-expectations-kb for:
     * Current band competencies and expectations
     * Next band requirements (for progression assessment)
     * Skills and behaviors expected at current level

3. ANALYSIS PHASE
   - Analyze performance against role-specific criteria
   - Evaluate competencies against band expectations
   - Identify strengths with specific examples
   - Identify areas for improvement with constructive feedback
   - Assess readiness for band progression
   - Compare with previous review if available

4. FEEDBACK GENERATION PHASE
   Generate structured output with:

   **HEADER**
   - Employee name, role, band
   - Review period and type
   - Review date
   - Reviewer name (manager)

   **OVERALL RATING**
   - Rating: 1-5 scale
   - Rating description:
     * 5 - Exceptional: Consistently exceeds expectations
     * 4 - Exceeds Expectations: Regularly surpasses goals
     * 3 - Meets Expectations: Solid, reliable performance
     * 2 - Needs Improvement: Below expected level
     * 1 - Unsatisfactory: Significant performance issues

   **CATEGORY RATINGS**
   For BTS:
   1. Technical Excellence (1-5 with notes)
   2. Brand Knowledge and Advocacy (1-5 with notes)
   3. Client Relationship Management (1-5 with notes)
   4. Innovation and Problem-Solving (1-5 with notes)
   5. Collaboration and Knowledge Sharing (1-5 with notes)
   6. Band-Level Competencies (1-5 with notes)

   For CSM:
   1. Client Relationship Excellence (1-5 with notes)
   2. Revenue Growth and Account Expansion (1-5 with notes)
   3. Client Advocacy and Success (1-5 with notes)
   4. Proactive Account Management (1-5 with notes)
   5. Strategic Planning and Execution (1-5 with notes)
   6. Band-Level Competencies (1-5 with notes)

   **PERFORMANCE SUMMARY**
   - 2-3 paragraph narrative overview
   - Highlight key achievements
   - Contextualize performance within role and band
   - Reference specific examples from input

   **STRENGTHS**
   - 3-5 bullet points
   - Each with specific example
   - Tied to role goals and band expectations
   - Actionable and clear

   **AREAS FOR IMPROVEMENT**
   - 2-4 bullet points
   - Constructive and specific
   - Include suggestions for improvement
   - Reference relevant competencies

   **PROGRESS TRACKING** (if previous review available)
   - Previous overall rating vs. current
   - Trajectory assessment (improving, stable, declining)
   - Detailed progress notes on:
     * Goals from previous review
     * Development areas addressed
     * New competencies demonstrated
     * Sustained strengths

   **DEVELOPMENT RECOMMENDATIONS**
   - 3-5 specific development items
   - Include:
     * Training or courses
     * Stretch assignments
     * Mentoring opportunities
     * Skill-building activities
     * Cross-functional projects

   **BAND PROGRESSION ASSESSMENT**
   - Current band performance summary
   - Readiness for next band (if applicable)
   - Specific gaps to address for progression
   - Timeline for potential advancement
   - Required competencies to develop

   **ACTION ITEMS**
   - 3-5 specific, measurable action items
   - Each with:
     * Clear objective
     * Target completion date
     * Success criteria
     * Support needed

   **MANAGER NOTES**
   - Space for additional comments
   - Confidential observations
   - Context for ratings

### Agent Tone and Style
- Professional and supportive
- Objective and evidence-based
- Constructive and developmental
- Clear and specific
- Balanced (strengths and improvements)
- Aligned with organizational standards

### Knowledge Base Integration
- MUST query both knowledge bases before generating feedback
- Reference specific criteria from knowledge bases
- Cite band expectations when assessing competencies
- Use organizational language and terminology
- Ensure alignment with company standards

### Chain of Thought
- Show reasoning process
- Explain rating decisions
- Connect feedback to evidence
- Demonstrate knowledge base usage

### Output Format
- Use markdown formatting
- Clear section headers
- Bullet points for lists
- Tables for ratings if helpful
- Professional document structure

### Error Handling
- If insufficient information provided, ask clarifying questions
- If role or band not supported, explain limitations
- If knowledge base query fails, acknowledge and proceed with general guidance
- Always maintain professional tone even with incomplete data

### Constraints
- Only support BTS and CSM roles
- Only support bands 6-10
- Require minimum information before generating review
- Do not make up information not provided
- Stay within scope of performance review generation
```

---

## Key Components Explained

### 1. Clear Purpose Statement
```
Generate comprehensive, structured performance reviews for [specific roles] 
in [specific bands], using [specific knowledge sources] as evaluation criteria.
```

**Why it matters:** Sets clear boundaries and expectations for the agent.

### 2. Phased Approach
```
1. Information Gathering
2. Knowledge Base Query
3. Analysis
4. Feedback Generation
```

**Why it matters:** Ensures systematic, thorough process every time.

### 3. Detailed Output Structure
```
Specify exact sections, format, and content for each part of the review.
```

**Why it matters:** Ensures consistency across all reviews.

### 4. Knowledge Base Integration
```
- MUST query both knowledge bases
- Reference specific criteria
- Use organizational terminology
```

**Why it matters:** Grounds feedback in organizational standards.

### 5. Tone and Style Guidelines
```
- Professional and supportive
- Objective and evidence-based
- Constructive and developmental
```

**Why it matters:** Maintains appropriate professional tone.

---

## Prompt Engineering Best Practices Used

### 1. **Specificity**
- Exact roles supported (BTS, CSM)
- Exact bands supported (6-10)
- Exact output format required

### 2. **Structure**
- Clear phases of operation
- Numbered steps
- Hierarchical organization

### 3. **Examples**
- Rating scale definitions
- Category lists for each role
- Sample output sections

### 4. **Constraints**
- What NOT to do
- Error handling
- Scope limitations

### 5. **Context**
- Purpose of the agent
- Who will use it
- What problem it solves

### 6. **Integration Points**
- Knowledge base queries
- Chain of thought reasoning
- Output formatting

---

## How to Adapt This Prompt

### For Different Roles
```
Replace:
- "Brand Technical Specialists (BTS) and Client Success Managers (CSM)"
With:
- Your specific roles

Update:
- Category ratings for each role
- Role-specific competencies
```

### For Different Bands/Levels
```
Replace:
- "salary bands 6-10"
With:
- Your organization's levels

Update:
- Band progression criteria
- Level-specific expectations
```

### For Different Review Types
```
Add or modify:
- Review types (360, peer, self-assessment)
- Review frequencies
- Special review scenarios
```

### For Different Output Formats
```
Modify:
- Section structure
- Rating scales
- Output formatting
```

---

## Testing Your Prompt

### 1. Test with Minimal Information
```
Provide only required fields to see if agent asks for more details.
```

### 2. Test with Complete Information
```
Provide comprehensive performance data to see full output quality.
```

### 3. Test Edge Cases
```
- Unsupported role
- Unsupported band
- Missing knowledge base
- Conflicting information
```

### 4. Test Consistency
```
Run same input multiple times to verify consistent output.
```

### 5. Test Knowledge Base Integration
```
Verify agent actually queries and uses knowledge base content.
```

---

## Common Pitfalls to Avoid

### ❌ Too Vague
```
"Create an agent that helps with performance reviews."
```
**Problem:** No structure, no specifics, inconsistent results.

### ❌ Too Rigid
```
"Always output exactly 500 words in this exact format..."
```
**Problem:** Can't adapt to different situations.

### ❌ Missing Knowledge Base Integration
```
No instructions on when/how to query knowledge bases.
```
**Problem:** Agent doesn't use organizational standards.

### ❌ No Error Handling
```
No guidance on what to do when information is missing.
```
**Problem:** Agent fails or makes up information.

### ❌ Unclear Tone
```
No guidance on professional vs. casual, supportive vs. critical.
```
**Problem:** Inconsistent, potentially inappropriate feedback.

---

## Prompt Refinement Process

### 1. Start Simple
```
Basic purpose and output structure
```

### 2. Add Structure
```
Phases, steps, clear process
```

### 3. Add Details
```
Specific sections, formats, examples
```

### 4. Add Constraints
```
What not to do, error handling
```

### 5. Add Integration
```
Knowledge bases, tools, other systems
```

### 6. Test and Iterate
```
Run tests, collect feedback, refine
```

---

## Example Variations

### Shorter Version (For Simple Reviews)
```
Create an agent that generates performance reviews for [roles] by:
1. Collecting employee info and performance data
2. Querying knowledge bases for criteria
3. Generating structured feedback with ratings and recommendations
Output: Overall rating, category ratings, summary, strengths, improvements, action items
```

### Longer Version (For Complex Reviews)
```
[Include all sections from main prompt above, plus:]
- Multi-rater integration
- Goal tracking over time
- Development plan creation
- Compensation recommendations
- Succession planning notes
```

---

## Conclusion

The key to a successful agent prompt is:
1. **Clarity** - Be specific about what you want
2. **Structure** - Organize the process logically
3. **Examples** - Show what good output looks like
4. **Constraints** - Define boundaries and error handling
5. **Integration** - Connect to knowledge sources
6. **Testing** - Validate with real scenarios

Use this example as a template and adapt it to your specific needs!

---

**Created:** May 7, 2026  
**Version:** 1.0  
**Status:** Production Example