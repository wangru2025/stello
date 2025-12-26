"""
DSL 验证模块 - 完整的 DSL 语法和语义验证
"""

from typing import List
from .ast_nodes import Token, GlobalConfig, PageConfig


class BlockValidator:
    """块类型验证器"""
    VALID_BLOCKS = {'title', 'content', 'nav', 'author', 'article_list'}


class DSLValidator:
    """DSL 验证器 - 验证 DSL 的语法正确性和语义有效性"""
    
    # 有效的全局配置字段
    VALID_GLOBAL_FIELDS = {
        '全局', '作者', '站点名', '默认模板', 
        '文章集合', '输出目录'
    }
    
    # 有效的页面配置字段
    VALID_PAGE_FIELDS = {
        '标题', '作者', '加入导航', '导航标题',
        '日期', '标签', '摘要', '来源', '排序', '块列表'
    }
    
    # 必填的全局字段
    REQUIRED_GLOBAL_FIELDS = {'站点名', '输出目录'}
    
    @staticmethod
    def validate_global_config(config: GlobalConfig) -> List[str]:
        """
        验证全局配置
        
        Args:
            config: 全局配置对象
            
        Returns:
            错误列表
        """
        errors = []
        
        # 检查必填字段
        if not config.site_name:
            errors.append("错误: 全局配置缺少必填字段 '站点名'")
        
        if not config.output_dir:
            errors.append("错误: 全局配置缺少必填字段 '输出目录'")
        
        return errors
    
    @staticmethod
    def validate_page_config(config: PageConfig, page_name: str) -> List[str]:
        """
        验证页面配置
        
        Args:
            config: 页面配置对象
            page_name: 页面名称（用于错误报告）
            
        Returns:
            错误列表
        """
        errors = []
        
        # 块列表必须显式声明且非空
        if not config.blocks:
            errors.append(
                f"错误: 页面 '{page_name}' 缺少必填字段 '块列表'，必须显式声明页面的块结构"
            )
        
        # 如果加入导航，则需要导航标题
        if config.add_to_nav and not config.nav_title:
            errors.append(
                f"错误: 页面 '{page_name}' 设置加入导航但缺少必填字段 '导航标题'"
            )
        
        # 验证日期格式（仅检查格式，不检查有效性）
        if config.date:
            if not _is_valid_date(config.date):
                errors.append(
                    f"警告: 页面 '{page_name}' 日期格式不符合 YYYY-MM-DD: {config.date}"
                )
        
        # 验证块列表中的块名称
        valid_blocks = set(BlockValidator.VALID_BLOCKS)
        for block_name in (config.blocks or []):
            if block_name not in valid_blocks:
                errors.append(
                    f"错误: 页面 '{page_name}' 使用无效的块类型 '{block_name}'，"
                    f"有效的块类型: {', '.join(sorted(valid_blocks))}"
                )
        
        return errors
    
    @staticmethod
    def validate_tokens(tokens: List[Token]) -> List[str]:
        """
        验证词法单元序列
        
        Args:
            tokens: 词法单元列表
            
        Returns:
            错误列表
        """
        errors = []
        
        # 检查每个语句都以分号结尾
        i = 0
        while i < len(tokens):
            # 找到下一个分号
            while i < len(tokens) and tokens[i].type != 'SEMICOLON':
                i += 1
            
            if i >= len(tokens):
                errors.append("错误: 存在未以分号结尾的语句")
                break
            
            i += 1
        
        return errors


def _is_valid_date(date_str: str) -> bool:
    """判断日期字符串格式是否有效"""
    # 简单的日期格式检查 YYYY-MM-DD
    import re
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_str))

