import unittest
from barcode_print.engine import ThermalBarcodePrintEngine, ProductBarcodeLabelSpec

class TestBarcodeThermalPrinter(unittest.TestCase):
    def test_zpl_generation(self):
        engine = ThermalBarcodePrintEngine()
        spec = ProductBarcodeLabelSpec(
            item_code="SKU-JEANS-32",
            item_name="Denim Jeans Regular 32",
            barcode_value="8901030991124",
            barcode_symbology="CODE128",
            mrp_inr=2499.0,
            sale_price_inr=1999.0,
            batch_number="B-2026",
            expiry_date="12/2028"
        )

        label = engine.generate_zpl_label(spec)
        self.assertEqual(label.printer_language, "ZPL")
        self.assertTrue(label.raw_command_stream.startswith("^XA"))
        self.assertTrue(label.raw_command_stream.endswith("^XZ"))
        self.assertIn("8901030991124", label.raw_command_stream)
        self.assertIn("Rs.1999.00", label.raw_command_stream)

if __name__ == "__main__":
    unittest.main()
