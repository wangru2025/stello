import unittest
import tempfile
import os
from pathlib import Path


class TestSiteBuilderClass(unittest.TestCase):
    """测试网站构建器类"""

    def test_site_builder_imports(self):
        """测试网站构建器可以导入"""
        from stello.build.build_site import SiteBuilder
        self.assertIsNotNone(SiteBuilder)

    def test_site_builder_has_build_method(self):
        """测试网站构建器有 build 方法"""
        from stello.build.build_site import SiteBuilder
        
        self.assertTrue(hasattr(SiteBuilder, 'build'))


class TestBlockSystemClass(unittest.TestCase):
    """测试块系统类"""

    def test_block_manager_imports(self):
        """测试块管理器可以导入"""
        from stello.build.block_system import BlockManager
        self.assertIsNotNone(BlockManager)

    def test_block_manager_has_methods(self):
        """测试块管理器有必需方法"""
        from stello.build.block_system import BlockManager
        
        self.assertTrue(hasattr(BlockManager, '__init__'))


class TestHtmlGenerationClass(unittest.TestCase):
    """测试 HTML 生成类"""

    def test_html_generator_imports(self):
        """测试 HTML 生成器可以导入"""
        from stello.build.generate_html import HTMLGenerator
        self.assertIsNotNone(HTMLGenerator)


class TestGeneratorsClass(unittest.TestCase):
    """测试生成器类"""

    def test_nav_generator_imports(self):
        """测试导航生成器可以导入"""
        from stello.build.generate_nav import NavigationGenerator
        self.assertIsNotNone(NavigationGenerator)

    def test_list_generator_imports(self):
        """测试列表生成器可以导入"""
        from stello.build.generate_list import ArticleListGenerator
        self.assertIsNotNone(ArticleListGenerator)


class TestValidators(unittest.TestCase):
    """测试验证器"""

    def test_missing_field_validator_imports(self):
        """测试缺失字段验证器可以导入"""
        from stello.validate.missing_field import MissingFieldValidator
        self.assertIsNotNone(MissingFieldValidator)

    def test_url_conflict_validator_imports(self):
        """测试 URL 冲突验证器可以导入"""
        from stello.validate.conflict_url import URLConflictValidator
        self.assertIsNotNone(URLConflictValidator)


class TestPageModules(unittest.TestCase):
    """测试页面模块"""

    def test_markdown_parser_imports(self):
        """测试 Markdown 解析器可以导入"""
        from stello.pages.parse_markdown import MarkdownParser
        self.assertIsNotNone(MarkdownParser)

    def test_page_loader_imports(self):
        """测试页面加载器可以导入"""
        from stello.pages.load_md import load_markdown_file
        self.assertIsNotNone(load_markdown_file)

    def test_dsl_extractor_imports(self):
        """测试 DSL 提取器可以导入"""
        from stello.pages.extract_dsl import extract_dsl_header
        self.assertIsNotNone(extract_dsl_header)


class TestTemplateSystem(unittest.TestCase):
    """测试模板系统"""

    def test_default_theme_exists(self):
        """测试默认主题存在"""
        theme_path = Path(__file__).parent.parent / 'stello' / 'themes' / 'default'
        self.assertTrue(theme_path.exists())

    def test_base_template_exists(self):
        """测试基础模板存在"""
        template_path = Path(__file__).parent.parent / 'stello' / 'themes' / 'default' / 'base.html'
        self.assertTrue(template_path.exists())

    def test_block_templates_exist(self):
        """测试块模板存在"""
        blocks_path = Path(__file__).parent.parent / 'stello' / 'themes' / 'default' / 'blocks'
        
        if blocks_path.exists():
            templates = list(blocks_path.glob('*.html'))
            self.assertGreater(len(templates), 0)


class TestOutputClass(unittest.TestCase):
    """测试输出类"""

    def test_output_writer_imports(self):
        """测试输出写入器可以导入"""
        from stello.build.output import OutputWriter
        self.assertIsNotNone(OutputWriter)


if __name__ == '__main__':
    unittest.main()
