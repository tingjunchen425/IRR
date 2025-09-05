import arxiv
import os
from google.adk import tools

def search_arxiv(query):
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=1,
        sort_by=arxiv.SortCriterion.Relevance,
    )
    results = list(client.results(search))
    return results

import fitz

def extract_text_from_pdf(pdf_path):
    if not pdf_path:
        return None
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()

        # --- 在這裡加入檢查 ---
        print("--- PDF 文字提取成功 ---")

        return full_text
    except Exception as e:
        print(f"提取PDF文字時發生錯誤: {e}")
        return None


def arxiv_tool(query: str) -> str:
    """
    Search for a paper on arXiv and extract its PDF content.
    The result will be the most relevant paper found.
    The extracted text will be returned as a string.
    Args:
        query (str): The search query for the paper.
    Returns:
        str: Extracted text from the most relevant paper.
    """
    os.makedirs("arxiv_papers", exist_ok=True)
    paper = search_arxiv(query)[0]
    arxiv_id = paper.entry_id.split('/')[-1]
    pdf_path = f"./arxiv_papers/{arxiv_id}.pdf"
    paper.download_pdf(dirpath="./arxiv_papers", filename=f"{arxiv_id}.pdf")
    extracted_text = extract_text_from_pdf(pdf_path)
    return extracted_text

if __name__ == "__main__":
    query = "machine learning"
    extracted_text = arxiv_tool(query)
    print(extracted_text)