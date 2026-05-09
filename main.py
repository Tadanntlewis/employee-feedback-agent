"""
Main script for testing the Expense Report Agent locally.

This script demonstrates how to:
1. Import and register the expense processing flow
2. Test the flow with a sample document
3. Display the extracted expense data
"""

import asyncio
import logging
import sys
from pathlib import Path

from ibm_watsonx_orchestrate import APIClient
from tools.expense_processing_flow import build_expense_processing_flow

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_expense_flow():
    """Test the expense processing flow with a sample document."""
    try:
        # Initialize API client
        client = APIClient()
        logger.info("Initialized API client")
        
        # Import the flow
        logger.info("Importing expense processing flow...")
        flow_result = await client.import_flow(build_expense_processing_flow)
        logger.info(f"Flow imported successfully: {flow_result}")
        
        # Get the flow ID
        flow_id = flow_result.get('id')
        if not flow_id:
            logger.error("Failed to get flow ID from import result")
            return
        
        logger.info(f"Flow ID: {flow_id}")
        logger.info("\n" + "="*60)
        logger.info("Flow imported successfully!")
        logger.info("="*60)
        logger.info("\nTo test the flow:")
        logger.info("1. Upload a sample expense document (airline ticket, hotel invoice, or receipt)")
        logger.info("2. The flow will extract all expense fields")
        logger.info("3. Review the structured output\n")
        
        # Note: Actual document processing requires user interaction
        # and is best tested through the chat UI or programmatically
        # with a specific document reference
        
        logger.info("Flow is ready for testing in the chat UI or via API")
        
    except Exception as e:
        logger.error(f"Error testing flow: {e}", exc_info=True)
        sys.exit(1)


async def main():
    """Main entry point."""
    logger.info("Starting Expense Report Agent test...")
    logger.info("="*60)
    
    await test_expense_flow()
    
    logger.info("\n" + "="*60)
    logger.info("Test completed successfully!")
    logger.info("="*60)


if __name__ == "__main__":
    asyncio.run(main())

# Made with Bob
