import unittest
from stello.dsl.ast_nodes import Token


class TestTokenClass(unittest.TestCase):
    """测试 Token 类"""

    def test_token_creation(self):
        """测试 Token 创建"""
        token = Token('IDENTIFIER', 'test', 1, 1)
        self.assertEqual(token.type, 'IDENTIFIER')
        self.assertEqual(token.value, 'test')

    def test_token_with_different_types(self):
        """测试不同类型的 Token"""
        token1 = Token('STRING', 'hello', 1, 5)
        token2 = Token('NUMBER', '42', 2, 1)
        token3 = Token('OPERATOR', '+', 2, 3)
        
        self.assertEqual(token1.type, 'STRING')
        self.assertEqual(token2.value, '42')
        self.assertEqual(token3.type, 'OPERATOR')

    def test_token_attributes(self):
        """测试 Token 属性"""
        token = Token('IDENTIFIER', 'myvar', 5, 10)
        
        self.assertTrue(hasattr(token, 'type'))
        self.assertTrue(hasattr(token, 'value'))
        self.assertTrue(hasattr(token, 'line'))
        self.assertTrue(hasattr(token, 'column'))


class TestTokenization(unittest.TestCase):
    """测试分词功能"""

    def test_tokenizer_initialization(self):
        """测试分词器初始化"""
        from stello.dsl.tokenize import Tokenizer
        
        code = ""
        tokenizer = Tokenizer(code)
        
        self.assertEqual(tokenizer.pos, 0)
        self.assertEqual(tokenizer.line, 1)

    def test_tokenizer_properties(self):
        """测试分词器属性"""
        from stello.dsl.tokenize import Tokenizer
        
        code = "test code"
        tokenizer = Tokenizer(code)
        
        self.assertTrue(hasattr(tokenizer, 'text'))
        self.assertTrue(hasattr(tokenizer, 'pos'))
        self.assertTrue(hasattr(tokenizer, 'tokens'))
        self.assertTrue(hasattr(tokenizer, 'tokenize'))


if __name__ == '__main__':
    unittest.main()
