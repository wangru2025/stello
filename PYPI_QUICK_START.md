# PyPI 发布快速开始

> 3 步发布 Stello 到 PyPI

---

## ✅ 已完成的准备

```
✓ pyproject.toml 已配置
✓ setup.py 已简化
✓ 分发包已生成
  - stello-1.0.0-py3-none-any.whl (10.3 KB)
  - stello-1.0.0.tar.gz (14.6 KB)
✓ 包验证通过
✓ GitHub Actions 工作流已配置
```

---

## 🚀 发布步骤

### 步骤 1️⃣: 获取 PyPI Token

1. 访问 https://pypi.org/account/register/ 注册账户（如已有则跳过）
2. 登录 https://pypi.org/account/
3. 点击左侧 "API tokens"
4. 点击 "Create API token"
5. 选择 "Entire account"（或仅限 Stello 项目）
6. 生成 token，复制保存（形如：`pypi-AgEIcHlwaS5vcmc...`）

### 步骤 2️⃣: 在 GitHub 配置 Secret

1. 访问 https://github.com/wangru2025/stello
2. 点击 Settings → Secrets and variables → Actions
3. 点击 "New repository secret"
4. 名称：`PYPI_API_TOKEN`
5. 值：粘贴你的 PyPI Token
6. 点击 "Add secret"

### 步骤 3️⃣: 创建 GitHub Release（自动触发发布）

选择以下其中一种方式：

#### 方式 A：网页界面（推荐）

1. 访问 https://github.com/wangru2025/stello/releases/new
2. 填写：
   - **Tag**: `v1.0.0`
   - **Title**: `Stello v1.0.0`
   - **Description**: 输入发布说明（可复制 CHANGELOG.md 内容）
3. 点击 "Publish release"

GitHub Actions 会自动：
- ✅ 构建分发包
- ✅ 验证包完整性
- ✅ 上传到 PyPI
- ✅ 上传到 GitHub Release

#### 方式 B：命令行

```bash
# 创建 git 标签
git tag -a v1.0.0 -m "Stello v1.0.0"

# 推送标签（自动触发 GitHub Release）
git push origin v1.0.0
```

---

## 🔍 验证发布成功

等待 5-10 分钟后，访问：

https://pypi.org/project/stello/

### 本地测试安装

```bash
# 等待 PyPI 同步后运行
pip install stello

# 验证
stello --help
```

---

## 📝 更新版本

当需要发布新版本时：

1. 更新 `pyproject.toml` 中的版本号：
   ```toml
   version = "1.0.1"
   ```

2. 更新 `CHANGELOG.md`

3. 提交并推送：
   ```bash
   git add pyproject.toml CHANGELOG.md
   git commit -m "Bump version to 1.0.1"
   git push origin main
   ```

4. 创建新 Release（自动发布）

---

## 🐛 常见问题

### Q: PyPI 上找不到包？
A: 可能还在同步中。等待 5-10 分钟后重试。

### Q: Token 被拒绝？
A: 检查：
- Token 是否正确复制（可能被截断）
- Token 是否包含 `pypi-` 前缀
- 是否已添加到 GitHub Secrets

### Q: 构建失败？
A: 查看 GitHub Actions 日志：
- 访问 https://github.com/wangru2025/stello/actions
- 点击失败的工作流
- 查看错误信息

### Q: 想删除已发布的版本？
A: 在 PyPI 项目页面点击版本 → "Delete" 或 "Yank"（标记为弃用）

---

## 🔗 相关链接

| 资源 | 链接 |
|------|------|
| PyPI 项目页 | https://pypi.org/project/stello/ |
| PyPI 账户 | https://pypi.org/account/ |
| 创建 Token | https://pypi.org/account/#api-tokens |
| GitHub Actions | https://github.com/wangru2025/stello/actions |
| 详细指南 | [PYPI_PUBLISH_GUIDE.md](PYPI_PUBLISH_GUIDE.md) |

---

## ✨ 包信息

```
Package Name: stello
Version: 1.0.0
License: MIT
Python: >=3.8
Dependencies:
  - Jinja2>=3.1.4
  - Markdown>=3.6
```

---

**现在就可以发布到 PyPI 了！** 🎉
