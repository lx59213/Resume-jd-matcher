import pdfplumber
import io
import re


def extract_text_from_pdf(pdf_file):
    """
    从PDF文件中提取文本内容，并进行智能清理

    Args:
        pdf_file: 文件对象或文件路径

    Returns:
        str: 提取的文本内容
    """
    try:
        if isinstance(pdf_file, (str, bytes, io.IOBase)):
            with pdfplumber.open(pdf_file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
        else:
            raise ValueError("不支持的文件类型")
        
        # 智能清理文本
        text = clean_text(text)

        return text
    except Exception as e:
        raise Exception(f"PDF解析错误: {str(e)}")


def clean_text(text):
    """
    智能清理提取的文本

    Args:
        text: 原始文本

    Returns:
        str: 清理后的文本
    """
    # 基础清理
    text = text.strip()

    # 移除多余的空白字符
    text = re.sub(r"\s+", " ", text)

    # 移除特殊字符，但保留中文标点
    text = "".join(
        char
        for char in text
        if char.isprintable() or char in '，。！？；：""' "（）《》【】"
    )

    # 合并多行
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:  # 忽略空行
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)
