"""Direct Thermal Barcode Label Generator (Zebra ZPL II / ESC-POS / TSPL) for Retail & Warehouses."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ProductBarcodeLabelSpec:
    item_code: str
    item_name: str
    barcode_value: str
    barcode_symbology: str  # CODE128, EAN13, QR
    mrp_inr: float
    sale_price_inr: float
    batch_number: Optional[str] = None
    expiry_date: Optional[str] = None


@dataclass
class GeneratedLabelPayload:
    item_code: str
    printer_language: str  # ZPL, TSPL, ESC_POS
    raw_command_stream: str
    label_width_mm: int
    label_height_mm: int


class ThermalBarcodePrintEngine:
    """Generates direct native command streams for Zebra, TSC, and TVS thermal label printers."""

    def generate_zpl_label(
        self,
        spec: ProductBarcodeLabelSpec,
        width_dots: int = 400,  # 50mm at 203 DPI = ~406 dots
        height_dots: int = 300  # 38mm at 203 DPI = ~304 dots
    ) -> GeneratedLabelPayload:
        # Zebra ZPL II raw command protocol
        zpl_lines = [
            "^XA",  # Start Format
            "^PW400",  # Print Width
            "^LL300",  # Label Length
            # Header Item Name
            f"^FO20,20^A0N,28,28^FD{spec.item_name[:24]}^FS",
            # Item Code
            f"^FO20,55^A0N,20,20^FDCode: {spec.item_code}^FS",
            # Barcode Code-128
            f"^FO30,85^BY2,2,70^BCN,70,Y,N,N^FD{spec.barcode_value}^FS",
            # Pricing details
            f"^FO20,185^A0N,22,22^FDM.R.P: Rs.{spec.mrp_inr:.2f}^FS",
            f"^FO20,215^A0N,32,32^FDOur Price: Rs.{spec.sale_price_inr:.2f}^FS",
        ]

        if spec.batch_number and spec.expiry_date:
            zpl_lines.append(f"^FO20,260^A0N,18,18^FDBatch: {spec.batch_number} Exp: {spec.expiry_date}^FS")

        zpl_lines.append("^XZ")  # End Format
        raw_zpl = "\n".join(zpl_lines)

        return GeneratedLabelPayload(
            item_code=spec.item_code,
            printer_language="ZPL",
            raw_command_stream=raw_zpl,
            label_width_mm=50,
            label_height_mm=38
        )
