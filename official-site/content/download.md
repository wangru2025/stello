标题 "下载 Stello"
加入导航 是
导航标题 下载
排序 2
块列表 [title, content]

# 下载 Stello

## 最新版本：1.0.0 (2025-12-25)

### 📦 完整包（推荐）

> **[⬇️ 下载 stello.zip](./stello.zip)**

## 安装步骤

下载stello.zip。

```bash
cd stello
pip install -e .
```

之后可以直接使用：
```bash
stello config.dsl
```

## 系统要求

- **Python**: 3.8 或更高版本
- **OS**: Windows、macOS、Linux
- **磁盘空间**: 约 50MB（含依赖）

## 获取帮助

### 遇到问题？

1. **查看示例** - `examples/` 目录有完整示例
2. **阅读文档** - `README.md` 有详细说明
3. **报告 Bug** - [GitHub Issues](https://github.com/wangru2025/stello/issues)

### 常见问题

**Q: 如何创建新主题？**  
A: 在 `stello/themes/` 中创建新目录，复制 `default` 主题的结构，修改 `style.css` 和块模板。在 `config.dsl` 中指定 `默认模板 mytheme;` 即可。

**Q: 如何自定义块？**  
A: 在主题的 `blocks/` 目录中修改对应的 HTML 文件。支持 Jinja2 模板语法。

**Q: 如何生成 RSS 或 Sitemap？**  
A: 当前版本不支持，但在 Roadmap 中。可以提出 Issue 或 PR。

**Q: 支持静态文件（图片、PDF 等）吗？**  
A: 支持。将文件放在 `content/` 目录中，会被自动复制到输出目录。

## 许可证

Stello 采用 **MIT 开源许可证**，允许自由使用、修改和分发。

---

## 其他资源

- 📖 [README - 项目介绍](https://github.com/wangru2025/stello)
- 💻 [GitHub 仓库](https://github.com/wangru2025/stello)

---

**有任何问题？** [联系我们](mailto:admin@wangru.net)
