# ERPNext Thermal Barcode Label & ZPL Print Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hardware](https://img.shields.io/badge/Thermal%20Printer-Zebra%20ZPL%20%2F%20TSPL-black.svg)](https://frappe.io)

Generates direct thermal printer commands (Zebra ZPL II, TSPL, ESC/POS) for industrial barcode and shelf-edge pricing labels without requiring print drivers or browser dialogs.

## Features
- **Direct Socket/Raw Printing:** Bypasses browser print dialogues to stream raw ZPL bytes directly to USB/Network thermal printers.
- **Code-128 & EAN-13 Support:** Native printer hardware barcode rendering for laser/CCD scanner readability.
- **Retail Shelf & MRP Tagging:** Encodes MRP, discount offer pricing, batch numbers, and expiry dates.

## Tests
```bash
python3 -m unittest discover tests
```
