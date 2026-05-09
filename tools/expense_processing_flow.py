from pydantic import BaseModel, Field
from ibm_watsonx_orchestrate.flow_builder.flows import Flow, flow, START, END
from ibm_watsonx_orchestrate.flow_builder.types import (
    DocProcInput,
    DocProcKVPSchema,
    DocProcField,
    DocProcOutputFormat,
)

# Define comprehensive KVP schema inline
EXPENSE_KVP_SCHEMA = DocProcKVPSchema(
    document_type="Expense Document",
    document_description="An expense document including airline tickets, hotel invoices, or general receipts",
    additional_prompt_instructions="Extract all values exactly as they appear in the document. For optional fields that are not present, leave them empty.",
    fields={
        # Invoice Information
        "invoice_date": DocProcField(
            description="The date of the invoice or receipt",
            default="",
            example="2024-01-15",
        ),
        "transaction_mode": DocProcField(
            description="The payment method used (e.g., Credit Card, Bank Transfer, Cash)",
            default="",
            example="Credit Card",
        ),
        
        # Airline Information (Optional)
        "airline_name": DocProcField(
            description="Name of the airline (if airline ticket)",
            default="",
            example="United Airlines",
        ),
        "passenger_name": DocProcField(
            description="Name of the passenger (if airline ticket)",
            default="",
            example="John Smith",
        ),
        "ticket_number": DocProcField(
            description="Airline ticket number (if airline ticket)",
            default="",
            example="0162345678901",
        ),
        "ticket_date": DocProcField(
            description="Date of ticket issuance (if airline ticket)",
            default="",
            example="2024-01-10",
        ),
        "flight_details": DocProcField(
            description="Flight information including flight number, route, departure and arrival times (if airline ticket)",
            default="",
            example="UA123, SFO to JFK, Dep: 08:00, Arr: 16:30",
        ),
        
        # Hotel Information (Optional)
        "hotel_name": DocProcField(
            description="Name of the hotel (if hotel invoice)",
            default="",
            example="Marriott Downtown",
        ),
        "customer_name": DocProcField(
            description="Name of the guest (if hotel invoice)",
            default="",
            example="Jane Doe",
        ),
        "city": DocProcField(
            description="City where the hotel is located (if hotel invoice)",
            default="",
            example="New York",
        ),
        
        # Fee Information
        "base_fare": DocProcField(
            description="Base fare or charges amount before taxes",
            default="",
            example="$450.00",
        ),
        "taxes": DocProcField(
            description="Tax amount with breakdown if available",
            default="",
            example="$67.50 (Sales Tax: $45.00, Service Tax: $22.50)",
        ),
        "total_amount": DocProcField(
            description="Total amount due including all charges and taxes",
            default="",
            example="$517.50",
        ),
        "currency": DocProcField(
            description="Currency code",
            default="",
            example="USD",
        ),
    }
)

# Output schema
class ExpenseReportOutput(BaseModel):
    summary: str = Field(description="Human-readable summary of the expense report")
    invoice_date: str = Field(default="", description="Date of invoice/receipt")
    transaction_mode: str = Field(default="", description="Payment method")
    airline_name: str = Field(default="", description="Airline name")
    passenger_name: str = Field(default="", description="Passenger name")
    ticket_number: str = Field(default="", description="Ticket number")
    ticket_date: str = Field(default="", description="Ticket date")
    flight_details: str = Field(default="", description="Flight information")
    hotel_name: str = Field(default="", description="Hotel name")
    customer_name: str = Field(default="", description="Customer name")
    city: str = Field(default="", description="City")
    base_fare: str = Field(default="", description="Base fare/charges")
    taxes: str = Field(default="", description="Tax amount")
    total_amount: str = Field(default="", description="Total amount")
    currency: str = Field(default="", description="Currency code")

@flow(
    name="expense_processing_flow",
    display_name="Expense Processing Flow",
    description="Extracts expense information from documents (airline tickets, hotel invoices, receipts)",
    input_schema=DocProcInput,
    output_schema=ExpenseReportOutput
)
def build_expense_processing_flow(aflow: Flow) -> Flow:
    """
    Document processing flow that extracts expense data using KVP extraction.
    """
    # DocProc node with inline KVP schema
    doc_node = aflow.docproc(
        name="extract_expense_data",
        display_name="Extract Expense Data",
        description="Extract expense fields from the uploaded document",
        task="text_extraction",
        document_structure=True,
        enable_hw=True,
        output_format=DocProcOutputFormat.object,
        kvp_schemas=[EXPENSE_KVP_SCHEMA],
        kvp_force_schema_name="Expense Document",
    )
    
    # Map inputs
    doc_node.map_input(
        input_variable="document_ref",
        expression="flow.input.document_ref"
    )
    
    # Prompt node to format the KVPs into structured output
    format_node = aflow.prompt(
        name="format_expense_report",
        display_name="Format Expense Report",
        system_prompt="You are a helpful assistant that formats expense data into structured reports.",
        user_prompt=[
            "Format the following expense data into a clear summary and structured fields. ",
            "Extract values from the KVP array where each KVP has key.semantic_label and value.raw_text. ",
            "KVP data: {kvps}"
        ],
        output_schema=ExpenseReportOutput
    )
    
    # Map KVPs to prompt node
    format_node.map_input(
        input_variable="kvps",
        expression="flow['extract_expense_data'].output.kvps"
    )
    
    # Sequence the nodes
    aflow.sequence(START, doc_node, format_node, END)
    
    # Map final output
    aflow.map_output(
        output_variable="summary",
        expression="flow['format_expense_report'].output.summary"
    )
    aflow.map_output(
        output_variable="invoice_date",
        expression="flow['format_expense_report'].output.invoice_date"
    )
    aflow.map_output(
        output_variable="transaction_mode",
        expression="flow['format_expense_report'].output.transaction_mode"
    )
    aflow.map_output(
        output_variable="airline_name",
        expression="flow['format_expense_report'].output.airline_name"
    )
    aflow.map_output(
        output_variable="passenger_name",
        expression="flow['format_expense_report'].output.passenger_name"
    )
    aflow.map_output(
        output_variable="ticket_number",
        expression="flow['format_expense_report'].output.ticket_number"
    )
    aflow.map_output(
        output_variable="ticket_date",
        expression="flow['format_expense_report'].output.ticket_date"
    )
    aflow.map_output(
        output_variable="flight_details",
        expression="flow['format_expense_report'].output.flight_details"
    )
    aflow.map_output(
        output_variable="hotel_name",
        expression="flow['format_expense_report'].output.hotel_name"
    )
    aflow.map_output(
        output_variable="customer_name",
        expression="flow['format_expense_report'].output.customer_name"
    )
    aflow.map_output(
        output_variable="city",
        expression="flow['format_expense_report'].output.city"
    )
    aflow.map_output(
        output_variable="base_fare",
        expression="flow['format_expense_report'].output.base_fare"
    )
    aflow.map_output(
        output_variable="taxes",
        expression="flow['format_expense_report'].output.taxes"
    )
    aflow.map_output(
        output_variable="total_amount",
        expression="flow['format_expense_report'].output.total_amount"
    )
    aflow.map_output(
        output_variable="currency",
        expression="flow['format_expense_report'].output.currency"
    )
    
    return aflow

# Made with Bob
