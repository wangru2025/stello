"""
验证模块 - 缺失字段检查
"""

from typing import List
from pathlib import Path
from ..dsl.ast_nodes import PageConfig


class MissingFieldValidator:
    """缺失必填字段检查"""
    
    @staticmethod
    def validate_page_config(config: PageConfig, file_path: Path) -> List[str]:
        """
        检查页面配置的必填字段
        
        Args:
            config: 页面配置对象
            file_path: 页面文件路径（用于错误信息）
            
        Returns:
            错误列表，如果没有错误则返回空列表
        """
        errors = []
        
        # 如果加入导航，必须填写导航标题
        if config.add_to_nav and not config.nav_title:
            errors.append(
                f"错误: 页面 '{file_path}' 设置加入导航但缺少必填字段 '导航标题'"
            )
        
        return errors
    
    @staticmethod
    def validate_global_config(config) -> List[str]:
        """验证全局配置的必填字段"""
        from ..dsl.ast_nodes import GlobalConfig
        
        errors = []
        
        if not config.site_name:
            errors.append("错误: 全局配置缺少必填字段 '站点名'")
        
        if not config.output_dir:
            errors.append("错误: 全局配置缺少必填字段 '输出目录'")
        
        return errors
