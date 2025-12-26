"""
DSL 头部提取模块
"""

from typing import Tuple


def extract_dsl_header(content: str) -> Tuple[str, str]:
    """
    从 Markdown 内容中提取 DSL 头部和正文
    
    DSL 头部在文件开头，以第一个空行结尾
    规则：DSL 头部不允许空行
    
    Args:
        content: Markdown 文件完整内容
        
    Returns:
        (dsl_text, body_text) 元组
    """
    lines = content.split('\n')
    
    dsl_lines = []
    body_start = 0
    
    for i, line in enumerate(lines):
        if line.strip() == '':
            # 找到第一个空行，DSL 到此结束
            body_start = i + 1
            break
        dsl_lines.append(line)
    else:
        # 没有空行，检查是否包含 DSL 关键字
        if dsl_lines and _is_dsl_line(dsl_lines[0]):
            # 包含 DSL 关键字但没有空行分隔
            body_start = len(lines)
        else:
            # 纯内容，无 DSL
            return '', content
    
    dsl_text = '\n'.join(dsl_lines)
    body_text = '\n'.join(lines[body_start:])
    
    return dsl_text, body_text


def _is_dsl_line(line: str) -> bool:
    """判断是否为 DSL 行"""
    dsl_keywords = [
        '标题', '作者', '加入导航', '导航标题', 'URL',
        '日期', '标签', '摘要', '来源', '排序', '类型'
    ]
    
    line = line.strip()
    for keyword in dsl_keywords:
        if line.startswith(keyword):
            return True
    return False
