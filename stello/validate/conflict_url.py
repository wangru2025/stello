"""
验证模块 - URL 冲突检查
"""

from typing import List, Dict, Set
from pathlib import Path


class URLConflictValidator:
    """URL 冲突检查"""
    
    def __init__(self):
        self.url_map: Dict[str, Path] = {}  # URL -> 文件路径映射
        self.conflicts: List[tuple] = []
    
    def register_url(self, url: str, file_path: Path) -> List[str]:
        """
        注册 URL
        
        Args:
            url: 页面 URL
            file_path: 页面文件路径
            
        Returns:
            冲突错误列表
        """
        errors = []
        
        if url in self.url_map:
            # 发现冲突
            existing_file = self.url_map[url]
            error = (
                f"错误: URL 冲突\n"
                f"  URL: {url}\n"
                f"  文件1: {existing_file}\n"
                f"  文件2: {file_path}"
            )
            errors.append(error)
            self.conflicts.append((url, existing_file, file_path))
        else:
            # 注册新 URL
            self.url_map[url] = file_path
        
        return errors
    
    def has_conflicts(self) -> bool:
        """是否有冲突"""
        return len(self.conflicts) > 0
    
    def get_conflicts(self) -> List[tuple]:
        """获取所有冲突"""
        return self.conflicts
