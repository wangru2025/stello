# Stello - 中文 DSL 的静态网站生成器

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/wangru2025/stello)](https://github.com/wangru2025/stello)
[![GitHub Issues](https://img.shields.io/github/issues/wangru2025/stello)](https://github.com/wangru2025/stello/issues)

> 为中文用户设计的**简洁、易学、高效**的静态网站生成器

Stello 是一个使用 **中文 DSL + Markdown** 的静态网站生成器。

它通过明确的规则，将 Markdown 文件编译为结构清晰、可预测的静态 HTML 网站。

---

## 特点概览

- 使用中文 DSL 描述页面结构和元数据
- 页面结构由「块列表」显式声明
- URL 由文件路径唯一决定
- 无隐式默认值，配置缺失直接报错
- 适合多页面、文章站点、文档站点

---

## 安装

### 从源代码安装（推荐用于开发）

```bash
git clone https://github.com/wangru2025/stello.git
cd stello
pip install -r requirements.txt
```

### 从本地源安装

```bash
pip install -e .
```

之后可以直接使用：
```bash
stello config.dsl
```

### 运行环境

* **Python**: 3.8 或更高版本
* **依赖**: 见 `requirements.txt`（仅需 Jinja2 和 Markdown）
* **操作系统**: Windows、macOS、Linux

---

## 快速开始

### 1. 创建项目结构

```bash
mkdir my-site
cd my-site
mkdir content
```

### 2. 创建全局配置 `config.dsl`

```dsl
全局
站点名 我的网站;
作者 张三;
默认模板 default;
文章集合 ./content;
输出目录 ./dist;
```

**必填字段**：

* `站点名`
* `文章集合`
* `输出目录`

---

### 3. 创建页面（Markdown + DSL 头）

#### 首页 `content/index.md`

```markdown
标题 "首页"
加入导航 是
导航标题 首页
排序 1
块列表 [title, content]

# 欢迎来到我的网站

这是首页内容。
```

#### 关于页 `content/about.md`

```markdown
标题 "关于"
加入导航 是
导航标题 关于
排序 2
块列表 [title, content]

# 关于我

这是关于页面。
```

---

### 4. 构建网站

```bash
stello config.dsl
```

生成结果在 `dist/` 目录。

本地预览：

```bash
python -m http.server 8000 --directory dist
```

---

## DSL 规范

### 全局配置（config.dsl）

| 字段   | 必填 | 说明                 |
| ---- | -- | ------------------ |
| 站点名  | ✅  | 网站名称               |
| 作者   | ❌  | 全局默认作者             |
| 默认模板 | ❌  | 主题目录名，默认 `default` |
| 文章集合 | ✅  | Markdown 文件目录      |
| 输出目录 | ✅  | 构建输出目录             |

---

### 页面配置（Markdown 头部）

Markdown 文件**开头到第一个空行**为 DSL 区域。

| 字段   | 必填 | 说明         |
| ---- | -- | ---------- |
| 块列表  | ✅  | 页面结构定义     |
| 标题   | ❌  | 页面标题       |
| 作者   | ❌  | 覆盖全局作者     |
| 加入导航 | ❌  | 是 / 否      |
| 导航标题 | 条件 | 加入导航时必须    |
| 日期   | ❌  | YYYY-MM-DD |
| 标签   | ❌  | 逗号分隔       |
| 摘要   | ❌  | 页面摘要       |
| 来源   | ❌  | 内容来源       |
| 排序   | ❌  | 导航排序权重     |

---

### 块列表说明

`块列表` 决定页面的**结构和顺序**。

可用块：

* `title`：标题、作者、日期
* `content`：Markdown 正文
* `nav`：导航菜单
* `author`：作者信息、标签、来源
* `article_list`：页面列表

示例：

```markdown
块列表 [title, content, author]
```

块的顺序即渲染顺序。

---

## URL 规则

URL **只由文件路径决定**：

| 文件路径                       | 生成 URL           |
| -------------------------- | ---------------- |
| content/index.md           | /                |
| content/about.md           | /about           |
| content/posts/hello.md     | /posts/hello     |
| content/blog/2025/first.md | /blog/2025/first |

修改 URL 的唯一方式是 **修改文件路径或文件名**。

---

## 常见错误

### 缺少块列表

```markdown
# ❌ 会失败
标题 "页面"
```

修复：

```markdown
块列表 [title, content]
```

---

### 加入导航但缺少导航标题

```markdown
加入导航 是
# ❌ 缺少 导航标题
```

修复：

```markdown
加入导航 是
导航标题 页面名称
```

---

### URL 冲突

```
content/posts/hello.md
content/posts/hello/index.md
```

两个文件生成相同 URL，会导致构建失败。

---

## 项目结构示例

```
my-site/
├── config.dsl
├── content/
│   ├── index.md
│   ├── about.md
│   └── posts/
│       └── hello.md
└── dist/
    ├── index.html
    ├── about/
    │   └── index.html
    └── posts/
        └── hello/
            └── index.html
```

---

## 主题与样式

默认主题位于：

```
themes/default/
```

可通过修改 CSS 或创建新主题来自定义样式：

```dsl
默认模板 mytheme;
```

---

## 部署

`dist/` 目录是完整的静态网站，可直接部署到：

* **GitHub Pages** - 免费托管
* **Netlify** - 自动构建和部署
* **任意静态文件服务器** - Apache、Nginx 等
* **CDN** - Cloudflare、AWS S3 + CloudFront 等

---

## 文档和资源

| 资源 | 描述 |
|------|------|
| [API.md](API.md) | 完整的编程接口文档 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献指南 |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 行为准则 |
| [CHANGELOG.md](CHANGELOG.md) | 更新日志 |
| [官方网站](official-site/) | 示例网站源代码 |
| [示例项目](examples/) | 完整的示例项目 |

---

## 社区和支持

- 🐛 **报告 Bug**: [GitHub Issues](https://github.com/wangru2025/stello/issues)
- 💬 **讨论功能**: [GitHub Discussions](https://github.com/wangru2025/stello/discussions)
- 📧 **联系我们**: admin@wangru.net
- 🤝 **贡献代码**: 见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 许可证

MIT License - 自由开源使用

---

## 致谢

感谢所有使用和支持 Stello 的用户！

---

**项目状态**: ✅ **Stable (1.0.0)**

**最后更新**: 2025-12-25
