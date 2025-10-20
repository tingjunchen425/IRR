from pathlib import Path
from pdfminer.high_level import extract_text


def convert_pdf_to_markdown(pdf_path: Path) -> str:
    text = extract_text(str(pdf_path)) or ""
    return text.replace("\x00", "")


def main() -> None:
    project_root = Path(__file__).resolve().parent
    source_root = project_root / "testtopic"
    output_root = project_root / "testfile_md"
    output_root.mkdir(exist_ok=True)

    for topic_dir in source_root.glob("*"):
        if not topic_dir.is_dir():
            continue
        for pdf_path in topic_dir.glob("*.pdf"):
            md_path = output_root / f"{pdf_path.stem}.md"
            md_content = convert_pdf_to_markdown(pdf_path)
            md_path.write_text(md_content, encoding="utf-8")


if __name__ == "__main__":
    main()