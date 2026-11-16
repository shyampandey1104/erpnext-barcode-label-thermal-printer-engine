# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "barcode_print"
app_title = "Erpnext Barcode Label Thermal Printer Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Barcode Label Thermal Printer Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/barcode_print/css/barcode_print.bundle.css"
app_include_js = "/assets/barcode_print/js/barcode_print.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "barcode_print.engine.on_document_submit",
        "on_cancel": "barcode_print.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "barcode_print.engine.daily_scheduled_sync"
    ]
}
