import unittest
from stello.dsl.ast_nodes import Token, GlobalConfig
from stello.dsl.parse import Parser
from stello.dsl.validate import DSLValidator


class TestParserInitialization(unittest.TestCase):
    """测试解析器初始化"""

    def test_parser_creation(self):
        """测试解析器创建"""
        token = Token('IDENTIFIER', 'test', 1, 1)
        tokens = [token]
        parser = Parser(tokens)
        
        self.assertIsNotNone(parser)
        self.assertEqual(parser.pos, 0)

    def test_parser_with_empty_tokens(self):
        """测试空 token 列表"""
        parser = Parser([])
        
        self.assertIsNotNone(parser)
        self.assertEqual(parser.pos, 0)

    def test_parser_attributes(self):
        """测试解析器属性"""
        tokens = [Token('IDENTIFIER', 'test', 1, 1)]
        parser = Parser(tokens)
        
        self.assertTrue(hasattr(parser, 'tokens'))
        self.assertTrue(hasattr(parser, 'pos'))
        self.assertTrue(hasattr(parser, 'parse_global_config'))


class TestGlobalConfigClass(unittest.TestCase):
    """测试 GlobalConfig 类"""

    def test_config_creation(self):
        """测试配置创建"""
        config = GlobalConfig()
        self.assertIsNotNone(config)

    def test_config_attributes(self):
        """测试配置属性"""
        config = GlobalConfig()
        
        # 应该有基本属性
        self.assertTrue(hasattr(config, '__dict__'))


class TestDSLValidator(unittest.TestCase):
    """测试 DSL 验证器"""

    def test_validator_creation(self):
        """测试验证器创建"""
        validator = DSLValidator()
        self.assertIsNotNone(validator)

    def test_validator_has_validate_method(self):
        """测试验证器有验证方法"""
        validator = DSLValidator()
        
        self.assertTrue(hasattr(validator, 'validate_global_config'))
        self.assertTrue(callable(getattr(validator, 'validate_global_config')))

    def test_validate_global_config(self):
        """测试全局配置验证"""
        config = GlobalConfig()
        validator = DSLValidator()
        
        result = validator.validate_global_config(config)
        
        # 应该返回列表
        self.assertIsInstance(result, list)


class TestPageConfiguration(unittest.TestCase):
    """测试页面配置"""

    def test_parse_page_config_exists(self):
        """测试解析页面配置方法存在"""
        tokens = []
        parser = Parser(tokens)
        
        self.assertTrue(hasattr(parser, 'parse_page_config'))


class TestMarkdownIntegration(unittest.TestCase):
    """测试 Markdown 集成"""

    def test_markdown_basic_conversion(self):
        """测试基本 Markdown 转换"""
        import markdown
        
        text = "# 标题\n\n这是段落。"
        html = markdown.markdown(text)
        
        self.assertIn('<h1>', html)
        self.assertIn('标题', html)

    def test_markdown_list_conversion(self):
        """测试列表转换"""
        import markdown
        
        text = "- 项目 1\n- 项目 2"
        html = markdown.markdown(text)
        
        self.assertIn('<li>', html)


if __name__ == '__main__':
    unittest.main()
