# Employee Feedback Agent - Project Structure

## Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    EMPLOYEE FEEDBACK AGENT                       │
│                  Performance Review Assistant                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         AGENT CONFIGURATION             │
        │  agents/employee_feedback_agent.yaml    │
        │                                         │
        │  • Native Agent (groq/gpt-oss-120b)    │
        │  • Structured Instructions (301 lines)  │
        │  • Chain of Thought Enabled            │
        │  • Knowledge Base Integration          │
        └─────────────────────────────────────────┘
                    │                │
        ┌───────────┘                └───────────┐
        ▼                                        ▼
┌──────────────────────┐              ┌──────────────────────┐
│  ROLE GOALS KB       │              │  BAND EXPECTATIONS KB│
│  role-goals-kb.yaml  │              │  band-expectations-  │
│                      │              │  kb.yaml             │
│  Source:             │              │                      │
│  role-goals.pdf      │              │  Source:             │
│                      │              │  band-expectations.  │
│  Content:            │              │  pdf                 │
│  • BTS goals & KPIs  │              │                      │
│  • CSM goals & KPIs  │              │  Content:            │
│  • Success criteria  │              │  • Band 6-10 criteria│
│  • Rating scales     │              │  • Competencies      │
│                      │              │  • Progression rules │
└──────────────────────┘              └──────────────────────┘
```

## Directory Structure

```
wxo-agentic-workflow/
│
├── 📁 agents/
│   ├── employee_feedback_agent.yaml      ⭐ Main agent configuration
│   ├── expense_report_agent.yaml         (Previous project)
│   └── AskOrchestrate.yaml              (System agent)
│
├── 📁 knowledge-bases/
│   ├── role-goals-kb.yaml               ⭐ Role goals KB config
│   ├── band-expectations-kb.yaml        ⭐ Band expectations KB config
│   ├── role-goals.pdf                   ⚠️  USER MUST UPLOAD
│   ├── band-expectations.pdf            ⚠️  USER MUST UPLOAD
│   ├── upload-guide.md                  📖 KB upload instructions
│   └── role-goals-template.md           (Optional template)
│
├── 📁 tools/
│   └── expense_processing_flow.py       (Previous project)
│
├── 📁 connections/
│   └── (Connection configurations)
│
├── 📁 models/
│   └── (Model configurations)
│
├── 📁 toolkits/
│   └── (Toolkit configurations)
│
├── 🚀 import-employee-feedback-agent.sh  ⭐ Deployment script
├── 📖 employee-feedback-agent-README.md  ⭐ Full documentation
├── 📖 QUICKSTART-employee-feedback-agent.md ⭐ Quick start guide
├── 📖 IMPLEMENTATION-SUMMARY.md          ⭐ This summary
├── 📖 PROJECT-STRUCTURE.md              ⭐ Project structure
├── 📖 employee-feedback-agent-plan.md   📋 Implementation plan
│
├── import-all.sh                        (Previous project)
├── workspace_config.yaml                (Workspace config)
├── .env                                 (Environment variables)
└── README.md                            (Main project README)

⭐ = New files for Employee Feedback Agent
⚠️  = Required user action
📖 = Documentation
📋 = Planning document
🚀 = Executable script
```

## File Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT FLOW                           │
└─────────────────────────────────────────────────────────────┘

1. USER UPLOADS PDFs
   └─> knowledge-bases/role-goals.pdf
   └─> knowledge-bases/band-expectations.pdf

2. RUN DEPLOYMENT SCRIPT
   └─> ./import-employee-feedback-agent.sh
       │
       ├─> Import role-goals-kb.yaml
       │   └─> References role-goals.pdf
       │   └─> Creates searchable KB
       │
       ├─> Import band-expectations-kb.yaml
       │   └─> References band-expectations.pdf
       │   └─> Creates searchable KB
       │
       ├─> Wait for indexing (5-10 min)
       │
       └─> Import employee_feedback_agent.yaml
           └─> Links to both KBs
           └─> Agent ready to use

3. TEST AGENT
   └─> orchestrate chat --agent employee_feedback_agent
```

## Component Dependencies

```
employee_feedback_agent.yaml
    │
    ├─── Requires: role-goals-kb (knowledge base)
    │    └─── Requires: role-goals.pdf
    │
    └─── Requires: band-expectations-kb (knowledge base)
         └─── Requires: band-expectations.pdf
```

## Documentation Hierarchy

```
📚 DOCUMENTATION SUITE
│
├── 🚀 QUICKSTART-employee-feedback-agent.md
│   └─> For: First-time users
│   └─> Time: 15 minutes
│   └─> Content: Quick setup, sample data, common issues
│
├── 📖 employee-feedback-agent-README.md
│   └─> For: All users and administrators
│   └─> Time: Full reference
│   └─> Content: Complete documentation, all features
│
├── 📋 employee-feedback-agent-plan.md
│   └─> For: Developers and architects
│   └─> Time: Deep dive
│   └─> Content: Design decisions, architecture, rationale
│
├── 📖 knowledge-bases/upload-guide.md
│   └─> For: Content creators
│   └─> Time: KB preparation
│   └─> Content: PDF guidelines, content structure
│
├── 📊 IMPLEMENTATION-SUMMARY.md
│   └─> For: Project stakeholders
│   └─> Time: Executive overview
│   └─> Content: What was built, status, next steps
│
└── 🗺️  PROJECT-STRUCTURE.md (this file)
    └─> For: New team members
    └─> Time: Project orientation
    └─> Content: File organization, relationships
```

## Data Flow Diagram

```
┌──────────────┐
│   Manager    │
│   (User)     │
└──────┬───────┘
       │
       │ 1. Start chat session
       ▼
┌─────────────────────────────────────┐
│  Employee Feedback Agent            │
│  (Native Agent)                     │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Conversation Manager          │ │
│  │ • Gather employee info        │ │
│  │ • Collect performance data    │ │
│  │ • Check for previous review   │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Knowledge Base Queries        │ │
│  │ • Query role-goals-kb         │◄─┼─── role-goals.pdf
│  │ • Query band-expectations-kb  │◄─┼─── band-expectations.pdf
│  │ • Retrieve relevant context   │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Analysis Engine               │ │
│  │ • Compare vs role goals       │ │
│  │ • Compare vs band criteria    │ │
│  │ • Calculate ratings           │ │
│  │ • Track progress              │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Feedback Generator            │ │
│  │ • Structure output            │ │
│  │ • Generate ratings            │ │
│  │ • Write summaries             │ │
│  │ • Create recommendations      │ │
│  └───────────────────────────────┘ │
└─────────────┬───────────────────────┘
              │
              │ 2. Return structured review
              ▼
┌─────────────────────────────────────┐
│  Performance Review Output          │
│  (Markdown Format)                  │
│                                     │
│  • Overall Rating (1-5)             │
│  • Category Ratings (6 areas)       │
│  • Performance Summary              │
│  • Strengths (3-5 items)            │
│  • Areas for Improvement (2-4)      │
│  • Progress Notes (if applicable)   │
│  • Development Recommendations      │
│  • Band Progression Assessment      │
│  • Action Items (3-5 items)         │
└─────────────────────────────────────┘
```

## Knowledge Base Architecture

```
┌─────────────────────────────────────────────────────────┐
│              KNOWLEDGE BASE SYSTEM                       │
└─────────────────────────────────────────────────────────┘

PDF Documents
    │
    ├─> role-goals.pdf
    │   └─> Processed by watsonx Orchestrate
    │       ├─> Text extraction
    │       ├─> Semantic chunking (1000 chars, 200 overlap)
    │       ├─> Embedding generation (text-embedding-ada-002)
    │       └─> Vector storage
    │
    └─> band-expectations.pdf
        └─> Processed by watsonx Orchestrate
            ├─> Text extraction
            ├─> Semantic chunking (1000 chars, 200 overlap)
            ├─> Embedding generation (text-embedding-ada-002)
            └─> Vector storage

Agent Query
    │
    ├─> "What are the goals for a BTS at Band 7?"
    │   └─> Query embedding generated
    │       └─> Vector similarity search
    │           └─> Top 5-10 relevant chunks retrieved
    │               └─> Context provided to LLM
    │
    └─> "What competencies are expected at Band 8?"
        └─> Query embedding generated
            └─> Vector similarity search
                └─> Top 5-10 relevant chunks retrieved
                    └─> Context provided to LLM
```

## Deployment States

```
┌─────────────────────────────────────────────────────────┐
│                  DEPLOYMENT STATES                       │
└─────────────────────────────────────────────────────────┘

State 1: INITIAL (Current)
├─ ✅ Agent YAML created
├─ ✅ KB configs created
├─ ✅ Deployment script ready
├─ ✅ Documentation complete
├─ ⚠️  PDFs not uploaded
└─ ⚠️  Not deployed to watsonx Orchestrate

State 2: READY TO DEPLOY (After PDF upload)
├─ ✅ Agent YAML created
├─ ✅ KB configs created
├─ ✅ Deployment script ready
├─ ✅ Documentation complete
├─ ✅ PDFs uploaded
└─ ⚠️  Not deployed to watsonx Orchestrate

State 3: DEPLOYING (During script execution)
├─ ✅ Agent YAML created
├─ ✅ KB configs created
├─ ✅ Deployment script running
├─ ✅ Documentation complete
├─ ✅ PDFs uploaded
├─ 🔄 KBs importing
├─ 🔄 KBs indexing
└─ ⚠️  Agent not yet imported

State 4: DEPLOYED (After successful deployment)
├─ ✅ Agent YAML created
├─ ✅ KB configs created
├─ ✅ Deployment script completed
├─ ✅ Documentation complete
├─ ✅ PDFs uploaded
├─ ✅ KBs imported and READY
├─ ✅ Agent imported
└─ ✅ Ready for testing

State 5: PRODUCTION (After testing and validation)
├─ ✅ All deployment steps complete
├─ ✅ Testing completed
├─ ✅ Validation successful
├─ ✅ Managers trained
└─ ✅ In active use
```

## File Size Summary

```
Configuration Files:
├─ employee_feedback_agent.yaml      ~15 KB (301 lines)
├─ role-goals-kb.yaml               ~1 KB (23 lines)
└─ band-expectations-kb.yaml        ~1 KB (26 lines)
                                    ─────────
                                    ~17 KB total

Scripts:
└─ import-employee-feedback-agent.sh ~6 KB (143 lines)

Documentation:
├─ employee-feedback-agent-README.md        ~45 KB (571 lines)
├─ QUICKSTART-employee-feedback-agent.md    ~18 KB (244 lines)
├─ IMPLEMENTATION-SUMMARY.md                ~35 KB (485 lines)
├─ PROJECT-STRUCTURE.md                     ~15 KB (this file)
├─ employee-feedback-agent-plan.md          ~80 KB (1000+ lines)
└─ knowledge-bases/upload-guide.md          ~22 KB (285 lines)
                                            ─────────
                                            ~215 KB total

User-Provided Files (to be uploaded):
├─ role-goals.pdf                   Variable (user content)
└─ band-expectations.pdf            Variable (user content)

Total Project Size: ~240 KB + user PDFs
```

## Integration Points

```
┌─────────────────────────────────────────────────────────┐
│           EXTERNAL INTEGRATIONS                          │
└─────────────────────────────────────────────────────────┘

IBM watsonx Orchestrate Platform
    │
    ├─> Authentication
    │   └─> IBM Cloud IAM
    │       └─> API Key authentication
    │
    ├─> Agent Runtime
    │   └─> Native agent execution
    │       └─> LLM: groq/openai/gpt-oss-120b
    │
    ├─> Knowledge Base Service
    │   ├─> Document processing
    │   ├─> Vector storage
    │   ├─> Semantic search
    │   └─> Embedding model: text-embedding-ada-002
    │
    └─> CLI Interface
        ├─> orchestrate agents import
        ├─> orchestrate knowledge-bases import
        ├─> orchestrate chat
        └─> orchestrate knowledge-bases check-status
```

## Quick Reference

### Key Files to Know

| File | Purpose | When to Use |
|------|---------|-------------|
| `agents/employee_feedback_agent.yaml` | Agent configuration | Modify agent behavior |
| `knowledge-bases/role-goals-kb.yaml` | Role goals KB config | Update KB settings |
| `knowledge-bases/band-expectations-kb.yaml` | Band expectations KB config | Update KB settings |
| `import-employee-feedback-agent.sh` | Deployment script | Deploy or redeploy |
| `QUICKSTART-employee-feedback-agent.md` | Quick start guide | First-time setup |
| `employee-feedback-agent-README.md` | Full documentation | Reference and troubleshooting |

### Key Commands

```bash
# Deploy the agent
./import-employee-feedback-agent.sh

# Check KB status
orchestrate knowledge-bases check-status --name role-goals-kb

# List agents
orchestrate agents list --kind native

# Start chat
orchestrate chat --agent employee_feedback_agent

# Update KB
orchestrate knowledge-bases import --file knowledge-bases/role-goals-kb.yaml
```

### Key Directories

```
agents/          → Agent configurations
knowledge-bases/ → KB configs and PDFs
tools/           → Custom tools (not used in this project)
connections/     → Connection configs (not used in this project)
```

---

**Last Updated:** 2026-05-04  
**Version:** 1.0  
**Status:** Implementation Complete, Ready for Deployment