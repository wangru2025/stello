# 贡献指南

感谢你对 Stello 项目的兴趣！我们欢迎各种形式的贡献。

## 📋 行为准则

本项目采用 [Contributor Covenant](CODE_OF_CONDUCT.md) 行为准则。参与此项目的任何人都应遵守此准则。

## 🚀 如何贡献

### 报告 Bug

在报告 Bug 之前，请先搜索 [Issues](https://github.com/wangru2025/stello/issues)，确保 Bug 没有被报告过。

**提交 Bug 报告时，请包括以下信息：**

- 使用的 Stello 版本
- 操作系统和 Python 版本
- 详细的重现步骤
- 预期行为 vs 实际行为
- 错误消息（如果有）
- 代码示例或配置文件（如果相关）

### 建议功能

**功能建议提交时，请包括：**

- 清晰的功能描述
- 使用场景说明
- 可能的实现方式（可选）
- 与其他功能的关系

### 代码贡献

#### 开发环境设置

1. Fork 本仓库
2. Clone 到本地：
   ```bash
   git clone https://github.com/YOUR_USERNAME/stello.git
   cd stello
   ```

3. 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate     # Windows
   ```

4. 安装开发依赖：
   ```bash
   pip install -r requirements.txt
   ```

#### 开发流程

1. 创建特性分支：
   ```bash
   git checkout -b feature/my-feature
   ```

2. 编写代码
   - 遵循项目的代码风格
   - 添加必要的注释和文档字符串
   - 编写单元测试

3. 提交更改：
   ```bash
   git add .
   git commit -m "Add: 功能说明"
   ```

   提交消息建议格式：
   - `Add:` 新增功能
   - `Fix:` 修复 Bug
   - `Improve:` 改进现有功能
   - `Refactor:` 代码重构
   - `Docs:` 文档更新
   - `Test:` 测试相关
   - `Chore:` 构建过程、依赖等

4. Push 到 Fork 仓库：
   ```bash
   git push origin feature/my-feature
   ```

5. 创建 Pull Request
   - 描述你的改动
   - 链接相关的 Issue
   - 解释为什么需要这个改动

#### 代码风格

- Python 代码遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- 使用 4 空格缩进
- 最大行长度 100 字符
- 文件编码：UTF-8
- 使用有意义的变量名和函数名
- 添加类型提示（Python 3.8+）

#### 提交规范

```python
"""
函数/类的简短说明

详细说明（如果需要）

Args:
    param1: 参数1说明
    param2: 参数2说明

Returns:
    返回值说明

Raises:
    异常说明
"""
```

### 文档贡献

- 改进 README.md 的清晰度
- 修复文档中的拼写或语法错误
- 添加更多使用示例
- 翻译文档（如果有帮助）

### 翻译贡献

我们欢迎将 Stello 翻译为其他语言：

1. 在 Issue 中表明你的意图
2. 创建翻译分支
3. 翻译相关文档
4. 提交 Pull Request

## 📝 Pull Request 流程

1. **关联 Issue**：在 PR 描述中提到相关 Issue（使用 #issue_number）

2. **描述改动**：清楚地描述你的改动，包括：
   - 做了什么
   - 为什么这样做
   - 如何测试
   - 可能的副作用

3. **测试**：确保：
   - 新功能有测试
   - 所有现有测试通过
   - 代码覆盖率没有下降

4. **代码审查**：
   - 至少需要一个维护者的批准
   - 解决所有反馈意见
   - 及时更新 PR

## 🔍 审查标准

我们的维护者会根据以下标准审查 PR：

- ✅ **功能正确性** - 功能按预期工作
- ✅ **代码质量** - 代码清晰、可维护
- ✅ **向后兼容** - 不破坏现有 API
- ✅ **文档** - 更新相关文档
- ✅ **测试** - 包含适当的测试
- ✅ **性能** - 没有显著的性能退化

## 📚 开发工具推荐

- **代码编辑器**: VS Code、PyCharm
- **格式化**: black、autopep8
- **Linting**: pylint、flake8
- **类型检查**: mypy
- **文档**: Sphinx

## 🤝 社区

- **讨论**: [GitHub Discussions](https://github.com/wangru2025/stello/discussions)
- **问题**: [GitHub Issues](https://github.com/wangru2025/stello/issues)
- **邮件**: admin@wangru.net

## 📖 额外资源

- [Stello 文档](README.md)
- [API 文档](API.md)
- [项目总结](PROJECT_SUMMARY.md)

## 🎯 当前优先事项

以下是目前的优先开发方向：

- [ ] RSS 订阅支持
- [ ] Sitemap 生成
- [ ] 开发服务器 (watch 模式)
- [ ] 更多主题模板
- [ ] 插件系统设计

## 许可证

通过向该项目贡献，你同意你的贡献将遵循其 [MIT 许可证](LICENSE)。

---

感谢你的贡献！❤️
