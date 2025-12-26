"""
DSL AST 节点定义
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ASTNode:
    """AST 节点基类"""
    line: int = 0
    
    
@dataclass
class GlobalConfig(ASTNode):
    """全局配置节点"""
    author: Optional[str] = None
    site_name: Optional[str] = None
    default_template: Optional[str] = None
    article_dir: Optional[str] = None
    output_dir: Optional[str] = None
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PageConfig(ASTNode):
    """页面配置节点"""
    title: Optional[str] = None
    author: Optional[str] = None
    add_to_nav: Optional[bool] = None
    nav_title: Optional[str] = None
    date: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    summary: Optional[str] = None
    source: Optional[str] = None
    order: Optional[int] = None
    blocks: List[str] = field(default_factory=list)  # 块列表（必须显式声明）
    params: Dict[str, Any] = field(default_factory=dict)
    
    
@dataclass
class PageDefinition(ASTNode):
    """页面定义（含DSL头部）"""
    config: Optional[PageConfig] = None
    content: str = ""  # Markdown 内容


@dataclass
class Token:
    """词法单元"""
    type: str
    value: str
    line: int
    column: int
