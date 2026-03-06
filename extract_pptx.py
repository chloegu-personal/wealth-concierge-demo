import sys
from pptx import Presentation

def extract_text(pptx_path, output_path):
    try:
        prs = Presentation(pptx_path)
        with open(output_path, "w", encoding="utf-8") as f:
            for i, slide in enumerate(prs.slides):
                f.write(f"--- Slide {i+1} ---\n")
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        f.write(shape.text + "\n")
                f.write("\n")
        print(f"Success: Extracted text to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text("SC4025 Digital Product Management - 13Weeks - Rapid MVP-1.pptx", "extracted_text_utf8.txt")
