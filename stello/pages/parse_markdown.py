"""
Markdown 解析模块
"""

import markdown
from typing import Dict, Any


class MarkdownParser:
    """Markdown 解析器"""
    
    def __init__(self):
        # 使用 markdown 库进行解析，支持扩展
        self.md = markdown.Markdown(
            extensions=['extra', 'codehilite', 'toc'],
            extension_configs={
                'codehilite': {'use_pygments': False},
            }
        )
    
    def parse(self, content: str) -> str:
        """
        将 Markdown 内容转换为 HTML
        
        Args:
            content: Markdown 文本
            
        Returns:
            HTML 字符串
        """
        # 重置解析器状态
        self.md.reset()
        
        html = self.md.convert(content)
        return html
    
    def parse_with_meta(self, content: str) -> tuple[str, Dict[str, Any]]:
        """
        解析 Markdown 并提取元数据
        
        Args:
            content: Markdown 文本
            
        Returns:
            (html, metadata) 元组
        """
        self.md.reset()
        html = self.md.convert(content)
        
        # 从 markdown 对象获取元数据（如果有的话）
        meta = getattr(self.md, 'Meta', {})
        
        return html, meta
