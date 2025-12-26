"""
DSL 分词器
"""

import re
from typing import List
from .ast_nodes import Token


class Tokenizer:
    """DSL 分词器"""
    
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        
    def tokenize(self) -> List[Token]:
        """分词"""
        while self.pos < len(self.text):
            self._skip_whitespace_and_comments()
            
            if self.pos >= len(self.text):
                break
                
            char = self.text[self.pos]
            
            # 分号作为语句结束符
            if char == ';':
                self.tokens.append(Token('SEMICOLON', ';', self.line, self.column))
                self._advance()
            # 左方括号
            elif char == '[':
                self.tokens.append(Token('LBRACKET', '[', self.line, self.column))
                self._advance()
            # 右方括号
            elif char == ']':
                self.tokens.append(Token('RBRACKET', ']', self.line, self.column))
                self._advance()
            # 逗号
            elif char == ',':
                self.tokens.append(Token('COMMA', ',', self.line, self.column))
                self._advance()
            # 中文和ASCII标识符（包括路径）
            elif self._is_identifier_start(char) or char == '.':
                self._read_identifier_or_path()
            # 数字
            elif char.isdigit():
                self._read_number()
            # 字符串（用引号）
            elif char in ('"', "'"):
                self._read_string()
            # 其他非空白字符作为错误
            else:
                raise SyntaxError(f"未预期的字符 '{char}' 在第 {self.line} 行第 {self.column} 列")
                
        return self.tokens
    
    def _skip_whitespace_and_comments(self):
        """跳过空白和注释"""
        while self.pos < len(self.text):
            char = self.text[self.pos]
            
            # 空白
            if char in ' \t\n\r':
                if char == '\n':
                    self.line += 1
                    self.column = 1
                else:
                    self.column += 1
                self.pos += 1
            # 注释（#开头）
            elif char == '#':
                while self.pos < len(self.text) and self.text[self.pos] != '\n':
                    self.pos += 1
            else:
                break
    
    def _is_identifier_start(self, char: str) -> bool:
        """判断是否为标识符起始字符"""
        return char.isalpha() or '\u4e00' <= char <= '\u9fff' or char == '_'
    
    def _is_identifier_char(self, char: str) -> bool:
        """判断是否为标识符字符"""
        return char.isalnum() or '\u4e00' <= char <= '\u9fff' or char == '_'
    
    def _advance(self):
        """前进一个字符"""
        if self.pos < len(self.text) and self.text[self.pos] == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1
    
    def _read_identifier(self):
        """读取标识符"""
        start_line = self.line
        start_col = self.column
        start_pos = self.pos
        
        while self.pos < len(self.text) and self._is_identifier_char(self.text[self.pos]):
            self._advance()
        
        value = self.text[start_pos:self.pos]
        self.tokens.append(Token('IDENTIFIER', value, start_line, start_col))
    
    def _read_identifier_or_path(self):
        r"""读取标识符或路径（支持 : \ / . 等文件系统字符）"""
        start_line = self.line
        start_col = self.column
        start_pos = self.pos
        
        # 读取标识符或路径
        while self.pos < len(self.text):
            char = self.text[self.pos]
            # 标识符字符、路径字符、或数字
            if (self._is_identifier_char(char) or 
                char in (':', '\\', '/', '.', '-') or 
                char.isdigit()):
                self._advance()
            else:
                break
        
        value = self.text[start_pos:self.pos]
        self.tokens.append(Token('IDENTIFIER', value, start_line, start_col))
    
    def _read_number(self):
        """读取数字"""
        start_line = self.line
        start_col = self.column
        start_pos = self.pos
        
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            self._advance()
        
        value = self.text[start_pos:self.pos]
        self.tokens.append(Token('NUMBER', value, start_line, start_col))
    
    def _read_string(self):
        """读取字符串"""
        start_line = self.line
        start_col = self.column
        quote = self.text[self.pos]
        self._advance()  # 跳过开引号
        
        value = ""
        while self.pos < len(self.text) and self.text[self.pos] != quote:
            if self.text[self.pos] == '\\' and self.pos + 1 < len(self.text):
                self._advance()
                if self.text[self.pos] == 'n':
                    value += '\n'
                elif self.text[self.pos] == 't':
                    value += '\t'
                elif self.text[self.pos] == '\\':
                    value += '\\'
                elif self.text[self.pos] == quote:
                    value += quote
                else:
                    value += self.text[self.pos]
                self._advance()
            else:
                value += self.text[self.pos]
                self._advance()
        
        if self.pos >= len(self.text):
            raise SyntaxError(f"未闭合的字符串，起始于第 {start_line} 行第 {start_col} 列")
        
        self._advance()  # 跳过结尾引号
        self.tokens.append(Token('STRING', value, start_line, start_col))
