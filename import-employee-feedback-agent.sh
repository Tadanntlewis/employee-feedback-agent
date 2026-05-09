#!/bin/bash

# Employee Feedback Agent Deployment Script
# This script imports knowledge bases and the employee feedback agent to watsonx Orchestrate

set -e  # Exit on any error

# Activate virtual environment
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
    echo "✓ Virtual environment activated"
    echo ""
fi

echo "=========================================="
echo "Employee Feedback Agent Deployment"
echo "=========================================="
echo ""

# Check if PDF files exist
echo "Checking for required PDF files..."
if [ ! -f "knowledge-bases/role-goals.pdf" ]; then
    echo "❌ ERROR: knowledge-bases/role-goals.pdf not found"
    echo "Please upload your role goals PDF to knowledge-bases/role-goals.pdf"
    exit 1
fi

if [ ! -f "knowledge-bases/BTS band-expectations.pdf" ]; then
    echo "❌ ERROR: knowledge-bases/BTS band-expectations.pdf not found"
    echo "Please upload your BTS band expectations PDF"
    exit 1
fi

if [ ! -f "knowledge-bases/CSM band-expectations.pdf" ]; then
    echo "❌ ERROR: knowledge-bases/CSM band-expectations.pdf not found"
    echo "Please upload your CSM band expectations PDF"
    exit 1
fi

echo "✓ All required PDF files found"
echo ""

# Import Role Goals Knowledge Base
echo "Step 1: Importing Role Goals Knowledge Base..."
orchestrate knowledge-bases import --file knowledge-bases/role-goals-kb.yaml
if [ $? -eq 0 ]; then
    echo "✓ Role Goals KB imported successfully"
else
    echo "❌ Failed to import Role Goals KB"
    exit 1
fi
echo ""

# Import Band Expectations Knowledge Base
echo "Step 2: Importing Band Expectations Knowledge Base..."
orchestrate knowledge-bases import --file knowledge-bases/band-expectations-kb.yaml
if [ $? -eq 0 ]; then
    echo "✓ Band Expectations KB imported successfully"
else
    echo "❌ Failed to import Band Expectations KB"
    exit 1
fi
echo ""

# Wait for knowledge bases to be indexed
echo "Step 3: Waiting for knowledge bases to be indexed..."
echo "This may take 5-10 minutes depending on document size..."
echo ""

# Check role-goals-kb status
echo "Checking role-goals-kb status..."
max_attempts=30
attempt=0
while [ $attempt -lt $max_attempts ]; do
    status=$(orchestrate knowledge-bases check-status --name role-goals-kb 2>&1 || echo "ERROR")
    if echo "$status" | grep -q "READY"; then
        echo "✓ role-goals-kb is READY"
        break
    elif echo "$status" | grep -q "ERROR"; then
        echo "❌ Error checking role-goals-kb status"
        exit 1
    else
        echo "  Indexing in progress... (attempt $((attempt+1))/$max_attempts)"
        sleep 20
        attempt=$((attempt+1))
    fi
done

if [ $attempt -eq $max_attempts ]; then
    echo "⚠️  Warning: role-goals-kb indexing timeout. Proceeding anyway..."
fi
echo ""

# Check band-expectations-kb status
echo "Checking band-expectations-kb status..."
attempt=0
while [ $attempt -lt $max_attempts ]; do
    status=$(orchestrate knowledge-bases check-status --name band-expectations-kb 2>&1 || echo "ERROR")
    if echo "$status" | grep -q "READY"; then
        echo "✓ band-expectations-kb is READY"
        break
    elif echo "$status" | grep -q "ERROR"; then
        echo "❌ Error checking band-expectations-kb status"
        exit 1
    else
        echo "  Indexing in progress... (attempt $((attempt+1))/$max_attempts)"
        sleep 20
        attempt=$((attempt+1))
    fi
done

if [ $attempt -eq $max_attempts ]; then
    echo "⚠️  Warning: band-expectations-kb indexing timeout. Proceeding anyway..."
fi
echo ""

# Import Employee Feedback Agent
echo "Step 4: Importing Employee Feedback Agent..."
orchestrate agents import --file agents/employee_feedback_agent.yaml
if [ $? -eq 0 ]; then
    echo "✓ Employee Feedback Agent imported successfully"
else
    echo "❌ Failed to import Employee Feedback Agent"
    exit 1
fi
echo ""

# List all knowledge bases to confirm
echo "Step 5: Verifying deployment..."
echo ""
echo "Knowledge Bases:"
orchestrate knowledge-bases list
echo ""

echo "Agents:"
orchestrate agents list --kind native | grep -A 5 "employee_feedback_agent" || echo "Agent list command format may vary"
echo ""

echo "=========================================="
echo "✓ Deployment Complete!"
echo "=========================================="
echo ""
echo "Next Steps:"
echo "1. Verify knowledge bases are READY:"
echo "   orchestrate knowledge-bases check-status --name role-goals-kb"
echo "   orchestrate knowledge-bases check-status --name band-expectations-kb"
echo ""
echo "2. Test the agent:"
echo "   orchestrate chat --agent employee_feedback_agent"
echo ""
echo "3. Try a sample conversation:"
echo "   - Provide employee details (name, role, band, review period)"
echo "   - Share performance information"
echo "   - Request feedback generation"
echo ""
echo "=========================================="

# Made with Bob
