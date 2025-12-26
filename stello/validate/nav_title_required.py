"""
验证模块 - 导航标题检查
"""

from typing import List
from pathlib import Path
from ..dsl.ast_nodes import PageConfig


class NavTitleValidator:
    """导航标题检查"""
    
    @staticmethod
    def validate(config: PageConfig, file_path: Path) -> List[str]:
        """
        检查导航标题
        
        如果页面要加入导航，必须填写导航标题
        
        Args:
            config: 页面配置对象
            file_path: 页面文件路径
            
        Returns:
            错误列表
        """
        errors = []
        
        if config.add_to_nav:
            if not config.nav_title or not config.nav_title.strip():
                errors.append(
                    f"错误: 页面 '{file_path}' 加入导航但缺少必填字段 '导航标题'"
                )
        
        return errors
