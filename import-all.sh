#!/bin/bash

# Import script for Expense Report Agent
# This script imports the flow and agent to watsonx Orchestrate

set -e  # Exit on error

echo "=========================================="
echo "Expense Report Agent - Import Script"
echo "=========================================="
echo ""

# Check if orchestrate CLI is available
if ! command -v orchestrate &> /dev/null; then
    echo "Error: 'orchestrate' CLI not found. Please install the watsonx Orchestrate CLI."
    exit 1
fi

echo "Step 1: Importing expense processing flow..."
orchestrate tools import --kind flow --file tools/expense_processing_flow.py
if [ $? -eq 0 ]; then
    echo "✓ Flow imported successfully"
else
    echo "✗ Flow import failed"
    exit 1
fi

echo ""
echo "Step 2: Importing expense report agent..."
orchestrate agents import --file agents/expense_report_agent.yaml
if [ $? -eq 0 ]; then
    echo "✓ Agent imported successfully"
else
    echo "✗ Agent import failed"
    exit 1
fi

echo ""
echo "=========================================="
echo "Import completed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Open watsonx Orchestrate chat UI"
echo "2. Select 'Expense Report Agent'"
echo "3. Ask to process an expense document"
echo "4. Upload your document when prompted"
echo "5. Review the extracted expense data"
echo ""

# Made with Bob
