# Stello GitHub 发布快速指南

> ⚡ 5 分钟快速发布到 GitHub

---

## 📋 准备清单

所有以下项已完成：

```
✅ .gitignore           - Git 配置
✅ LICENSE              - MIT 许可证
✅ README.md            - 项目文档
✅ CONTRIBUTING.md      - 贡献指南
✅ CODE_OF_CONDUCT.md   - 行为准则
✅ CHANGELOG.md         - 更新日志
✅ .github/             - GitHub 配置
✅ .git/                - Git 仓库初始化
```

---

## 🚀 发布步骤

### 1️⃣ 创建 GitHub 仓库（2 分钟）

访问 https://github.com/new，填写：

- **Repository name**: `stello`
- **Description**: Stello - 中文 DSL 的静态网站生成器
- **Public**: ✓
- **其他选项**: 都跳过

点击 **Create repository** → 完成！

### 2️⃣ 关联仓库（1 分钟）

```bash
cd d:\stello

# 替换 YOUR_USERNAME 为你的 GitHub 用户名
git remote add origin https://github.com/YOUR_USERNAME/stello.git
git branch -M main
```

### 3️⃣ 上传代码（1 分钟）

```bash
git add .
git commit -m "Initial commit: Stello v1.0.0 - Chinese DSL Static Site Generator"
git push -u origin main
```

### 4️⃣ 创建 Release（1 分钟）

```bash
git tag -a v1.0.0 -m "Stello v1.0.0 - First stable release"
git push origin v1.0.0
```

然后在 GitHub 页面上：
1. 点击 **Releases**
2. 点击 **Draft a new release**
3. 选择 tag `v1.0.0`
4. 填写 Release Notes（可复制 CHANGELOG.md 内容）
5. 点击 **Publish release**

---

## ✨ 仓库设置（可选）

### 添加 Topics

Settings → General → Topics

添加这些标签：
- `python`
- `static-site-generator` 
- `markdown`
- `dsl`
- `chinese`
- `ssg`

### 配置 Description

Settings → General → Description

```
Stello - 为中文用户设计的静态网站生成器
```

---

## 📞 发布后

### 立即分享

在以下平台分享：

- **Twitter**: 分享项目链接
- **v2ex**: 发帖介绍
- **掘金**: 发文章讲解
- **开源中国**: 提交项目

### 保持更新

- 监控 Issues 和 PRs
- 回复社区反馈
- 修复 bugs
- 发布新版本

---

## 🎯 示例命令

完整的发布流程：

```bash
# 1. 进入项目目录
cd d:\stello

# 2. 检查 git 状态
git status

# 3. 关联远程仓库（替换 USERNAME）
git remote add origin https://github.com/USERNAME/stello.git
git branch -M main

# 4. 提交所有文件
git add .
git commit -m "Initial commit: Stello v1.0.0"

# 5. 推送到 GitHub
git push -u origin main

# 6. 创建标签
git tag -a v1.0.0 -m "Stello v1.0.0 - First stable release"
git push origin v1.0.0

# 7. 验证
git log --oneline
git tag -l
```

---

## 🔗 重要链接

| 项目 | URL |
|------|-----|
| GitHub 主页 | `https://github.com/USERNAME/stello` |
| README | `https://github.com/USERNAME/stello#readme` |
| Issues | `https://github.com/USERNAME/stello/issues` |
| Discussions | `https://github.com/USERNAME/stello/discussions` |
| Releases | `https://github.com/USERNAME/stello/releases` |

---

## 📚 文档导航

| 文档 | 用途 |
|------|------|
| [README.md](README.md) | 项目介绍和快速开始 |
| [API.md](API.md) | 编程接口文档 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 如何贡献 |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 社区行为准则 |
| [CHANGELOG.md](CHANGELOG.md) | 版本历史 |
| [LICENSE](LICENSE) | MIT 许可证 |

---

## ❓ 常见问题

### Q: 我需要编辑什么？
**A:** 只需在上面步骤中替换 `USERNAME` 为你的 GitHub 用户名。

### Q: 如何更新代码后推送新版本？
**A:** 
```bash
git add .
git commit -m "描述改动"
git push origin main
```

### Q: 如何创建新的 Release？
**A:**
```bash
git tag -a vX.X.X -m "Release vX.X.X"
git push origin vX.X.X
```

### Q: 我的邮箱会暴露吗？
**A:** 不会，GitHub 会隐藏你的邮箱地址。

---

## 🎉 完成！

所有准备工作已完成，立即开始发布吧！

遇到问题？查看 [GITHUB_RELEASE_CHECKLIST.md](GITHUB_RELEASE_CHECKLIST.md) 获取详细说明。

---

**祝你发布顺利！** 🚀
