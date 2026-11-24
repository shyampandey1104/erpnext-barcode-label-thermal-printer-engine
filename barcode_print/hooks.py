# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "barcode_print"
app_title = "Erpnext Barcode Label Thermal Printer Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Barcode Label Thermal Printer Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/barcode_print/css/barcode_print.bundle.css"
app_include_js = "/assets/barcode_print/js/barcode_print.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Barcode Label Thermal Printer Engine Entry": {
        "validate": "barcode_print.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "barcode_print.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "barcode_print.tasks.hourly_sync"
    ],
    "daily": [
        "barcode_print.tasks.daily_reconciliation"
    ],
    "weekly": [
        "barcode_print.tasks.weekly_digest"
    ]
}
