import unittest
from stello.dsl.ast_nodes import Token, GlobalConfig


class TestASTNodes(unittest.TestCase):
    """测试 AST 节点"""

    def test_token_creation(self):
        """测试 Token 创建"""
        token = Token('IDENTIFIER', 'test', 1, 1)
        self.assertEqual(token.type, 'IDENTIFIER')
        self.assertEqual(token.value, 'test')
        self.assertEqual(token.line, 1)
        self.assertEqual(token.column, 1)

    def test_global_config_attributes(self):
        """测试 GlobalConfig 属性"""
        config = GlobalConfig()
        
        # 检查标准属性
        self.assertTrue(hasattr(config, '__dict__'))


class TestModuleImports(unittest.TestCase):
    """测试核心模块可以导入"""

    def test_import_tokenizer(self):
        """测试分词器导入"""
        from stello.dsl.tokenize import Tokenizer
        self.assertIsNotNone(Tokenizer)

    def test_import_parser(self):
        """测试解析器导入"""
        from stello.dsl.parse import Parser
        self.assertIsNotNone(Parser)

    def test_import_validator(self):
        """测试验证器导入"""
        from stello.dsl.validate import DSLValidator
        self.assertIsNotNone(DSLValidator)

    def test_import_build_site(self):
        """测试网站构建器导入"""
        from stello.build.build_site import SiteBuilder
        self.assertIsNotNone(SiteBuilder)

    def test_import_block_manager(self):
        """测试块管理器导入"""
        from stello.build.block_system import BlockManager
        self.assertIsNotNone(BlockManager)


class TestStelloPackage(unittest.TestCase):
    """测试 Stello 包结构"""

    def test_main_module_exists(self):
        """测试主模块存在"""
        import stello
        self.assertTrue(hasattr(stello, '__file__'))

    def test_dsl_module_exists(self):
        """测试 DSL 模块存在"""
        import stello.dsl
        self.assertTrue(hasattr(stello.dsl, '__file__'))

    def test_build_module_exists(self):
        """测试构建模块存在"""
        import stello.build
        self.assertTrue(hasattr(stello.build, '__file__'))

    def test_pages_module_exists(self):
        """测试页面模块存在"""
        import stello.pages
        self.assertTrue(hasattr(stello.pages, '__file__'))

    def test_validate_module_exists(self):
        """测试验证模块存在"""
        import stello.validate
        self.assertTrue(hasattr(stello.validate, '__file__'))


class TestLibraryDependencies(unittest.TestCase):
    """测试依赖库可用"""

    def test_jinja2_available(self):
        """测试 Jinja2 可用"""
        import jinja2
        self.assertIsNotNone(jinja2.Template)

    def test_markdown_available(self):
        """测试 Markdown 可用"""
        import markdown
        md = markdown.Markdown()
        self.assertIsNotNone(md)

    def test_markdown_basic_conversion(self):
        """测试 Markdown 基本转换"""
        import markdown
        html = markdown.markdown("# 标题")
        self.assertIn('<h1>', html)


if __name__ == '__main__':
    unittest.main()
