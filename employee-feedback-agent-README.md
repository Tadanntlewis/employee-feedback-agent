# Employee Feedback Agent

An AI-powered performance review assistant built with IBM watsonx Orchestrate that generates structured, objective feedback for Brand Technical Specialists (BTS) and Client Success Managers (CSM) in salary bands 6-10.

## Overview

The Employee Feedback Agent helps managers create comprehensive performance reviews by:
- Gathering employee information through structured conversation
- Querying knowledge bases for role-specific goals and band expectations
- Analyzing performance against established criteria
- Generating structured feedback with ratings, summaries, and recommendations
- Tracking progress between quarterly and annual reviews

## Features

✅ **Structured Conversation Flow** - Guides managers through information gathering  
✅ **Knowledge Base Integration** - References role goals and band expectations via RAG  
✅ **Multi-Role Support** - Handles both BTS and CSM roles  
✅ **Band-Specific Evaluation** - Assesses against band 6-10 criteria  
✅ **Progress Tracking** - Compares performance across review periods  
✅ **Comprehensive Output** - Generates detailed feedback with ratings, summaries, and action items  
✅ **Chain of Thought** - Shows reasoning process for transparency

## Architecture

### Components

1. **Employee Feedback Agent** (`agents/employee_feedback_agent.yaml`)
   - Native watsonx Orchestrate agent
   - LLM: `groq/openai/gpt-oss-120b`
   - Integrates with 2 knowledge bases
   - Structured instructions for feedback generation

2. **Role Goals Knowledge Base** (`knowledge-bases/role-goals-kb.yaml`)
   - Contains BTS and CSM role goals, KPIs, and success criteria
   - Source: `role-goals.pdf` (user-provided)
   - Semantic chunking for context preservation

3. **Band Expectations Knowledge Base** (`knowledge-bases/band-expectations-kb.yaml`)
   - Contains band 6-10 competencies and progression criteria
   - Source: `band-expectations.pdf` (user-provided)
   - Semantic chunking for context preservation

### Data Flow

```
Manager Input → Agent Conversation → Information Gathering
                                    ↓
                            KB Query (Role Goals)
                                    ↓
                            KB Query (Band Expectations)
                                    ↓
                            Performance Analysis
                                    ↓
                            Structured Feedback Generation
                                    ↓
                            Review Output (Markdown)
```

## Project Structure

```
wxo-agentic-workflow/
├── agents/
│   └── employee_feedback_agent.yaml          # Agent configuration
├── knowledge-bases/
│   ├── role-goals-kb.yaml                    # Role goals KB config
│   ├── band-expectations-kb.yaml             # Band expectations KB config
│   ├── role-goals.pdf                        # Your role goals document
│   ├── band-expectations.pdf                 # Your band expectations document
│   └── upload-guide.md                       # KB upload instructions
├── import-employee-feedback-agent.sh         # Deployment script
├── employee-feedback-agent-plan.md           # Implementation plan
└── employee-feedback-agent-README.md         # This file
```

## Prerequisites

1. **IBM watsonx Orchestrate Account**
   - Access to watsonx Orchestrate platform
   - API key for authentication

2. **watsonx Orchestrate CLI**
   ```bash
   pip install ibm-watsonx-orchestrate
   ```

3. **Knowledge Base Documents**
   - `role-goals.pdf` - Your organization's role goals and KPIs
   - `band-expectations.pdf` - Your organization's band expectations

4. **Environment Configuration**
   - Set `IBM_CLOUD_API_KEY` environment variable
   - Configure `~/.config/orchestrate/config.yaml`
   - Configure `~/.cache/orchestrate/credentials.yaml`

## Setup Instructions

### Step 1: Prepare Knowledge Base Documents

1. Create or gather your organization's documents:
   - **Role Goals Document**: BTS and CSM goals, KPIs, success criteria
   - **Band Expectations Document**: Band 6-10 competencies and progression criteria

2. Convert to PDF format if needed

3. Place in the `knowledge-bases/` directory:
   ```bash
   knowledge-bases/role-goals.pdf
   knowledge-bases/band-expectations.pdf
   ```

See [`knowledge-bases/upload-guide.md`](knowledge-bases/upload-guide.md) for detailed content guidelines.

### Step 2: Configure Environment

Ensure your watsonx Orchestrate environment is configured:

```bash
# Set IBM Cloud API key
export IBM_CLOUD_API_KEY="your-api-key-here"

# Verify configuration
orchestrate env list
```

### Step 3: Deploy the Agent

Run the deployment script:

```bash
./import-employee-feedback-agent.sh
```

This script will:
1. ✓ Check for required PDF files
2. ✓ Import role goals knowledge base
3. ✓ Import band expectations knowledge base
4. ✓ Wait for knowledge bases to be indexed (5-10 minutes)
5. ✓ Import employee feedback agent
6. ✓ Verify deployment

### Step 4: Verify Deployment

Check knowledge base status:

```bash
# Check role goals KB
orchestrate knowledge-bases check-status --name role-goals-kb

# Check band expectations KB
orchestrate knowledge-bases check-status --name band-expectations-kb
```

Both should show status: **READY**

List agents to confirm:

```bash
orchestrate agents list --kind native
```

You should see `employee_feedback_agent` in the list.

## Usage

### Starting a Review Session

```bash
orchestrate chat --agent employee_feedback_agent
```

### Sample Conversation Flow

**Step 1: Provide Employee Information**
```
Agent: Hello! I'll help you create a performance review. Let's start with the employee basics.
       What is the employee's name?

You: John Smith

Agent: Thank you. What is John's role?

You: Brand Technical Specialist

Agent: What is John's current salary band?

You: Band 7

Agent: What review period is this for?

You: Q1 2026

Agent: Is this a quarterly or annual review?

You: Quarterly
```

**Step 2: Previous Review Check**
```
Agent: Do you have a previous review for John that I should reference for progress tracking?

You: Yes, I have his Q4 2025 review. His overall rating was 3/5.

Agent: Thank you. I'll track progress from that baseline.
```

**Step 3: Performance Information**
```
Agent: Please share John's key accomplishments during Q1 2026.

You: - Led the implementation of the new client portal, completed 2 weeks ahead of schedule
     - Resolved 45 technical issues with 98% accuracy
     - Mentored 2 junior BTS team members
     - Received excellent feedback from 3 major clients

Agent: Were there any challenges John faced during this period?

You: He struggled initially with the new authentication system but quickly adapted
     and created documentation to help the team.

[Continue providing performance details...]
```

**Step 4: Generate Feedback**
```
Agent: I have all the information needed. I'll now query the knowledge bases for:
       - BTS role goals and KPIs
       - Band 7 expectations and competencies
       
       Would you like me to generate the performance review now?

You: Yes, please generate the review.

Agent: [Generates comprehensive structured feedback...]
```

### Review Output Format

The agent generates a structured review including:

1. **Overall Rating** (1-5 scale)
2. **Category Ratings** (6 categories for BTS, 6 for CSM)
3. **Performance Summary** (2-3 paragraphs)
4. **Strengths** (3-5 bullet points with examples)
5. **Areas for Improvement** (2-4 bullet points)
6. **Progress Notes** (if previous review exists)
7. **Development Recommendations** (3-5 items)
8. **Band Progression Assessment**
9. **Action Items** (3-5 items with deadlines)

## Supported Roles

### Brand Technical Specialist (BTS)

**Evaluation Categories:**
- Technical Excellence
- Brand Knowledge and Advocacy
- Client Relationship Management
- Innovation and Problem-Solving
- Collaboration and Knowledge Sharing
- Band-Level Competencies

### Client Success Manager (CSM)

**Evaluation Categories:**
- Client Relationship Excellence
- Revenue Growth and Account Expansion
- Client Advocacy and Success
- Proactive Account Management
- Strategic Planning and Execution
- Band-Level Competencies

## Supported Salary Bands

**Band 6-10** with specific competency expectations:
- **Band 6**: Entry-level professional
- **Band 7**: Experienced professional
- **Band 8**: Senior professional
- **Band 9**: Lead/Principal level
- **Band 10**: Expert/Distinguished level

## Knowledge Base Management

### Updating Knowledge Bases

To update role goals or band expectations:

1. Update your PDF document
2. Re-import the knowledge base:
   ```bash
   orchestrate knowledge-bases import --file knowledge-bases/role-goals-kb.yaml
   ```
3. Wait for re-indexing to complete
4. Verify status:
   ```bash
   orchestrate knowledge-bases check-status --name role-goals-kb
   ```

### Viewing Knowledge Base Content

```bash
# List all knowledge bases
orchestrate knowledge-bases list

# Get details of a specific KB
orchestrate knowledge-bases get --name role-goals-kb
```

### Removing Knowledge Bases

```bash
# Remove a knowledge base
orchestrate knowledge-bases remove --name role-goals-kb
```

## Troubleshooting

### Issue: Knowledge base import fails

**Symptoms:** Error during `orchestrate knowledge-bases import`

**Solutions:**
- Check PDF file exists in correct location
- Verify PDF is not corrupted (try opening it)
- Check file size (max 50MB per file)
- Ensure PDF is searchable (not scanned images)

### Issue: Knowledge base indexing timeout

**Symptoms:** Status check shows "INDEXING" for >10 minutes

**Solutions:**
- Large documents may take longer - wait up to 15 minutes
- Check document size and complexity
- Try re-importing with smaller chunk size
- Contact support if issue persists

### Issue: Agent can't find relevant information

**Symptoms:** Agent says "I couldn't find information about..."

**Solutions:**
- Verify knowledge base status is READY
- Check document structure (use clear headings)
- Ensure content is searchable (not images)
- Try rephrasing the query
- Review KB content for completeness

### Issue: Agent import fails

**Symptoms:** Error during `orchestrate agents import`

**Solutions:**
- Verify YAML syntax is correct
- Check knowledge base names match exactly
- Ensure knowledge bases are imported first
- Verify LLM model name is correct
- Check for special characters in agent name

### Issue: Generated feedback is generic

**Symptoms:** Feedback lacks specific details

**Solutions:**
- Provide more specific performance examples
- Include concrete metrics and outcomes
- Reference specific projects or achievements
- Ensure knowledge bases contain detailed criteria
- Try providing more context about the employee's work

## Best Practices

### For Managers

1. **Prepare Before the Session**
   - Gather performance data and examples
   - Review previous feedback if available
   - Note specific accomplishments and challenges

2. **Be Specific**
   - Provide concrete examples
   - Include metrics and outcomes
   - Reference specific projects or clients

3. **Be Balanced**
   - Share both strengths and areas for improvement
   - Provide context for challenges
   - Note progress and growth

4. **Review and Refine**
   - Review generated feedback carefully
   - Ask agent to adjust if needed
   - Add personal observations
   - Ensure alignment with organizational standards

### For Knowledge Base Content

1. **Structure Clearly**
   - Use consistent headings and formatting
   - Organize by role and band
   - Include specific, measurable criteria

2. **Be Comprehensive**
   - Cover all evaluation categories
   - Include examples and benchmarks
   - Define rating scales clearly

3. **Keep Updated**
   - Review and update quarterly
   - Align with organizational changes
   - Incorporate feedback from managers

4. **Make Searchable**
   - Use clear, descriptive language
   - Include relevant keywords
   - Avoid jargon or acronyms without explanation

## Advanced Configuration

### Customizing Chunking Strategy

Edit the knowledge base YAML files to adjust chunking:

```yaml
chunking:
  strategy: semantic  # or 'fixed', 'paragraph'
  chunk_size: 1000    # characters per chunk
  overlap: 200        # overlap between chunks
```

### Changing the LLM Model

Edit `agents/employee_feedback_agent.yaml`:

```yaml
llm: groq/openai/gpt-oss-120b  # Change to your preferred model
```

Available models can be listed with:
```bash
orchestrate models list
```

### Adjusting Agent Behavior

Modify the `instructions` section in `agents/employee_feedback_agent.yaml` to:
- Change conversation flow
- Adjust output format
- Add custom evaluation criteria
- Modify rating scales

## Security and Privacy

### Data Handling

- Employee performance data is processed in real-time
- No data is stored permanently by the agent
- Knowledge bases contain only organizational standards, not personal data
- Follow your organization's data privacy policies

### Access Control

- Restrict agent access to authorized managers only
- Use appropriate authentication mechanisms
- Audit agent usage regularly
- Ensure compliance with HR policies

### Sensitive Information

- Avoid including sensitive personal information in knowledge bases
- Don't share confidential salary information
- Follow data protection regulations (GDPR, etc.)
- Use secure channels for review distribution

## Support and Maintenance

### Regular Maintenance Tasks

- **Monthly**: Review agent performance and feedback quality
- **Quarterly**: Update knowledge base documents
- **Annually**: Comprehensive review of evaluation criteria

### Getting Help

1. **Documentation**: Review this README and the implementation plan
2. **Upload Guide**: See `knowledge-bases/upload-guide.md`
3. **watsonx Orchestrate Docs**: https://developer.watson-orchestrate.ibm.com
4. **Support**: Contact your watsonx Orchestrate administrator

## Future Enhancements

Potential improvements for future versions:

1. **Multi-Language Support** - Generate reviews in multiple languages
2. **Custom Templates** - Organization-specific review templates
3. **Integration with HRIS** - Pull employee data automatically
4. **Peer Feedback Integration** - Incorporate 360-degree feedback
5. **Goal Tracking** - Link to OKR/goal management systems
6. **Analytics Dashboard** - Aggregate review insights
7. **Email Integration** - Send reviews directly to employees
8. **Version History** - Track review changes over time

## License

[Your License Here]

## Contributors

[Your Team/Organization]

## Changelog

### Version 1.0.0 (2026-05-04)
- Initial release
- Support for BTS and CSM roles
- Support for bands 6-10
- Knowledge base integration
- Progress tracking between reviews
- Comprehensive structured output

---

**Questions or Issues?**  
Contact: [Your Contact Information]

**Last Updated:** 2026-05-04