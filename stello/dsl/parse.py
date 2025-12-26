"""
DSL 解析器 - 将词法单元解析为 AST
"""

from typing import List, Optional, Dict, Any
from .ast_nodes import Token, GlobalConfig, PageConfig, PageDefinition


class Parser:
    """DSL 解析器"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None
        
    def parse_global_config(self) -> GlobalConfig:
        """解析全局配置"""
        config = GlobalConfig()
        
        while self.pos < len(self.tokens):
            if self._check_identifier('全局'):
                self._advance()
            elif self._check_identifier('作者'):
                self._advance()
                config.author = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('站点名'):
                self._advance()
                config.site_name = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('默认模板'):
                self._advance()
                config.default_template = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('文章集合'):
                self._advance()
                config.article_dir = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('输出目录'):
                self._advance()
                config.output_dir = self._expect_string_or_identifier()
                self._expect_semicolon()
            else:
                break
                
        return config
    
    def parse_page_config(self) -> PageConfig:
        """解析页面配置（Markdown 头部）"""
        config = PageConfig()
        
        while self.pos < len(self.tokens) and not self._is_at_end():
            if self._check_identifier('标题'):
                self._advance()
                config.title = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('作者'):
                self._advance()
                config.author = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('加入导航'):
                self._advance()
                value = self._expect_string_or_identifier()
                config.add_to_nav = value == '是'
                self._expect_semicolon()
            elif self._check_identifier('导航标题'):
                self._advance()
                config.nav_title = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('日期'):
                self._advance()
                config.date = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('标签'):
                self._advance()
                tags_str = self._expect_string_or_identifier()
                config.tags = [tag.strip() for tag in tags_str.split(',')]
                self._expect_semicolon()
            elif self._check_identifier('摘要'):
                self._advance()
                config.summary = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('来源'):
                self._advance()
                config.source = self._expect_string_or_identifier()
                self._expect_semicolon()
            elif self._check_identifier('排序'):
                self._advance()
                config.order = self._expect_number()
                self._expect_semicolon()
            elif self._check_identifier('块列表'):
                self._advance()
                config.blocks = self._expect_block_list()
                self._expect_semicolon()
            else:
                break
                
        return config
    
    def _advance(self):
        """前进到下一个词法单元"""
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
            self.current_token = self.tokens[self.pos]
    
    def _check_identifier(self, value: str) -> bool:
        """检查当前是否为特定标识符"""
        return (self.current_token and 
                self.current_token.type == 'IDENTIFIER' and 
                self.current_token.value == value)
    
    def _check_type(self, token_type: str) -> bool:
        """检查当前词法单元类型"""
        return self.current_token and self.current_token.type == token_type
    
    def _is_at_end(self) -> bool:
        """是否已到末尾"""
        return self.pos >= len(self.tokens)
    
    def _expect_string_or_identifier(self) -> str:
        """期望字符串或标识符"""
        if self._check_type('STRING'):
            value = self.current_token.value
            self._advance()
            return value
        elif self._check_type('IDENTIFIER'):
            value = self.current_token.value
            self._advance()
            return value
        else:
            raise SyntaxError(
                f"期望字符串或标识符，但得到 '{self.current_token}' "
                f"在第 {self.current_token.line if self.current_token else 'EOF'} 行"
            )
    
    def _expect_number(self) -> int:
        """期望数字"""
        if self._check_type('NUMBER'):
            value = int(self.current_token.value)
            self._advance()
            return value
        else:
            raise SyntaxError(
                f"期望数字，但得到 '{self.current_token}' "
                f"在第 {self.current_token.line if self.current_token else 'EOF'} 行"
            )
    
    def _expect_semicolon(self):
        """期望分号"""
        if not self._check_type('SEMICOLON'):
            raise SyntaxError(
                f"期望 ';'，但得到 '{self.current_token}' "
                f"在第 {self.current_token.line if self.current_token else 'EOF'} 行"
            )
        self._advance()
    
    def _expect_block_list(self) -> list:
        """期望块列表，格式: [块1, 块2, ...]"""
        if not self._check_type('LBRACKET'):
            raise SyntaxError(
                f"期望 '['，但得到 '{self.current_token}' "
                f"在第 {self.current_token.line if self.current_token else 'EOF'} 行"
            )
        self._advance()
        
        blocks = []
        while not self._check_type('RBRACKET') and not self._is_at_end():
            block_name = self._expect_string_or_identifier()
            blocks.append(block_name)
            
            if self._check_type('COMMA'):
                self._advance()
            elif not self._check_type('RBRACKET'):
                raise SyntaxError(
                    f"期望 ',' 或 ']'，但得到 '{self.current_token}' "
                    f"在第 {self.current_token.line if self.current_token else 'EOF'} 行"
                )
        
        if not self._check_type('RBRACKET'):
            raise SyntaxError(f"期望 ']'，但得到 EOF")
        self._advance()
        
        return blocks
