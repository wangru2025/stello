"""
Markdown 文件加载与处理
"""

from pathlib import Path
from typing import Tuple
from .extract_dsl import extract_dsl_header
from ..dsl.tokenize import Tokenizer
from ..dsl.parse import Parser
from ..dsl.ast_nodes import PageConfig


def extract_dsl_header(content: str) -> Tuple[str, str]:
    """
    从 Markdown 内容中提取 DSL 头部和正文
    
    DSL 头部在文件开头，以第一个空行结尾
    
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
        # 没有空行，整个文件都是 DSL（不可能）或纯内容
        if dsl_lines and dsl_lines[0].startswith('标题') or \
           dsl_lines and dsl_lines[0].startswith('作者'):
            # 包含 DSL 关键字
            body_start = len(lines)
        else:
            # 纯内容，无 DSL
            return '', content
    
    dsl_text = '\n'.join(dsl_lines)
    body_text = '\n'.join(lines[body_start:])
    
    return dsl_text, body_text


def parse_page_config_from_markdown(dsl_text: str) -> PageConfig:
    """
    从 Markdown 头部 DSL 解析页面配置
    
    Args:
        dsl_text: DSL 文本
        
    Returns:
        PageConfig 对象
    """
    if not dsl_text.strip():
        # 空 DSL，返回空配置
        return PageConfig()
    
    # 处理 DSL 格式：每行是一条语句
    # 将每行转换为以分号结尾的格式
    lines = dsl_text.strip().split('\n')
    dsl_lines = []
    
    for line in lines:
        line = line.strip()
        if line:  # 非空行
            # 如果不以分号结尾，添加分号
            if not line.endswith(';'):
                line += ';'
            dsl_lines.append(line)
    
    dsl_text = ' '.join(dsl_lines)
    
    tokenizer = Tokenizer(dsl_text)
    tokens = tokenizer.tokenize()
    
    parser = Parser(tokens)
    config = parser.parse_page_config()
    
    return config


def load_markdown_file(file_path: Path) -> Tuple[PageConfig, str]:
    """
    加载 Markdown 文件并提取配置与内容
    
    Args:
        file_path: Markdown 文件路径
        
    Returns:
        (PageConfig, markdown_content) 元组
    """
    if not file_path.exists():
        raise FileNotFoundError(f"文件不存在: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    dsl_text, body_text = extract_dsl_header(content)
    config = parse_page_config_from_markdown(dsl_text)
    
    return config, body_text


def _generate_url_from_path(file_path: Path) -> str:
    """
    从文件路径生成 URL
    
    例如：
    - about.md → /about
    - posts/hello.md → /posts/hello
    - index.md → /（或 /）
    """
    # 获取相对路径（去掉扩展名）
    rel_path = str(file_path.with_suffix(''))
    
    # 标准化路径分隔符
    rel_path = rel_path.replace('\\', '/')
    
    # index.md 特殊处理
    if rel_path.endswith('/index') or rel_path == 'index':
        return '/'
    
    # 其他情况前面加 /
    return '/' + rel_path if not rel_path.startswith('/') else rel_path
