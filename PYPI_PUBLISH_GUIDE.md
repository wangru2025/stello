# PyPI 发布指南

> 将 Stello 发布到 PyPI，让用户可以通过 `pip install stello` 安装

---

## 📋 前置准备

### 1. 创建 PyPI 账户

访问 https://pypi.org/account/register/ 注册账户

或使用 https://test.pypi.org/ 测试（推荐先在测试环境尝试）

### 2. 设置本地认证

在 `~/.pypirc` 文件中配置凭证（Windows 用户：`%APPDATA%\pip\pip.ini`）：

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # 你的 PyPI Token

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # 你的测试 Token
```

**更安全的做法：使用 API Token**

1. 登录 PyPI：https://pypi.org/account/
2. 点击 "Account settings" → "API tokens"
3. 创建新 token（选择 "Entire account" 或仅限此项目）
4. 复制 token 到 `~/.pypirc`

---

## 🚀 发布流程

### 方式一：本地发布（推荐用于学习）

#### Step 1: 安装发布工具

```bash
pip install build twine
```

#### Step 2: 验证配置

```bash
cd d:\stello
# 检查 setup.py 是否有效
python setup.py check
```

#### Step 3: 构建分发包

```bash
# 构建 wheel 和 source distribution
python -m build

# 或使用 setup.py（旧方式，不推荐）
# python setup.py sdist bdist_wheel
```

输出文件将在 `dist/` 目录：
- `stello-1.0.0.tar.gz` - 源码包
- `stello-1.0.0-py3-none-any.whl` - Wheel 包

#### Step 4: 验证包内容

```bash
# 检查包元数据
twine check dist/*

# 列出包内容
tar -tzf dist/stello-1.0.0.tar.gz | head -20
unzip -l dist/stello-1.0.0-py3-none-any.whl | head -20
```

#### Step 5: 上传到 PyPI

**测试环境（推荐先测）：**

```bash
twine upload --repository testpypi dist/*
```

验证：https://test.pypi.org/project/stello/

**正式环境：**

```bash
twine upload dist/*
```

验证：https://pypi.org/project/stello/

---

### 方式二：GitHub Actions 自动发布（推荐用于生产）

#### 设置 GitHub Secrets

1. 在 GitHub 仓库设置中：Settings → Secrets and variables → Actions
2. 添加新 Secret：
   - 名称：`PYPI_API_TOKEN`
   - 值：你的 PyPI API Token

#### 创建发布工作流

工作流文件已存在于 `.github/workflows/publish.yml`

#### 触发自动发布

只需在 GitHub 创建新 Release：

1. 访问 https://github.com/wangru2025/stello/releases/new
2. 填写：
   - Tag: `v1.0.1`（对应版本号）
   - Title: `Stello v1.0.1`
   - Description: 更新说明
3. 点击 "Publish release"

GitHub Actions 会自动：
- ✅ 构建分发包
- ✅ 验证包内容
- ✅ 上传到 PyPI
- ✅ 创建 Release 附件

---

## 📦 验证发布成功

发布后，验证包可以安装：

```bash
# 从 PyPI 安装（可能需要几分钟同步）
pip install stello

# 验证命令行工具
stello --help

# 验证包可导入
python -c "import stello; print(stello.__file__)"
```

---

## 🔄 更新版本

### 更新流程

1. **修改版本号**

```toml
# pyproject.toml
[project]
version = "1.0.1"  # 更新版本
```

2. **提交代码**

```bash
git add pyproject.toml
git commit -m "Bump version to 1.0.1"
git push origin main
```

3. **创建 Release**

在 GitHub 创建新 Release（自动触发发布）

或手动发布：

```bash
python -m build
twine upload dist/*
```

---

## 🐛 常见问题

### Q: 如何生成 API Token？

A: 登录 https://pypi.org/account/ → Account settings → API tokens → Add API token

### Q: twine 找不到？

A: 安装：`pip install twine`

### Q: 上传失败："Unauthorized"？

A: 
- 检查 Token 是否正确
- Token 中不能有特殊字符（除了 pypi-）
- 确保 ~/.pypirc 中 password 字段是完整 Token

### Q: 包名已被占用？

A: PyPI 包名全局唯一。如果 `stello` 已被占用：
- 使用 `stello-ssg`、`stello-site-generator` 等变体
- 或 fork 原项目并发布到自己的名字空间

### Q: 如何禁止用户升级到某个版本？

A: 在 PyPI 项目设置中，点击版本 → 删除或标记为"Yanked"

---

## 📚 相关链接

| 资源 | 链接 |
|------|------|
| PyPI 官网 | https://pypi.org/ |
| 创建 Token | https://pypi.org/account/ |
| Twine 文档 | https://twine.readthedocs.io/ |
| Setup.py 指南 | https://setuptools.pypa.io/ |
| Semantic Versioning | https://semver.org/lang/zh-CN/ |

---

## ✨ 发布清单

发布前确认：

- [ ] 版本号已更新（pyproject.toml）
- [ ] CHANGELOG.md 已更新
- [ ] README.md 说明无误
- [ ] 所有测试通过 `pytest`
- [ ] Linting 通过 `flake8`
- [ ] Git 标签已创建 `git tag -a vX.X.X`
- [ ] 代码已推送到 GitHub
- [ ] GitHub Release 已创建

完成以上步骤后，PyPI 发布将自动进行！
