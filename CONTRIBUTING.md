# 贡献指南

## 提交规范

### 提交信息格式

```
<type>: <subject>

<body>

<footer>
```

### 类型（type）

| 类型 | 说明 |
|------|------|
| feat | 新功能 |
| fix | 修复 bug |
| docs | 文档更新 |
| style | 代码格式（不影响功能） |
| refactor | 重构 |
| test | 测试相关 |
| chore | 构建/工具相关 |

### 提交流程

```bash
# 1. 查看变更状态
git status

# 2. 添加文件到暂存区
git add <files>

# 3. 提交变更
git commit -m "type: subject"

# 4. 推送到远程仓库
git push origin main
```

### 注意事项

- 提交前确保代码已测试通过
- 每个提交只包含一个逻辑变更
- 提交信息使用中文或英文均可
- 推送到 main 分支前确保本地代码是最新的

## 评估系统

### 业务评估

基于业务需求评估原型代码是否可以解决生产问题。

```bash
# 运行业务评估
python3 business_evaluate.py

# 或使用快速脚本
./quick_business_eval.sh
```

### 评估文档

- [BUSINESS_EVALUATION.md](BUSINESS_EVALUATION.md) - 业务评估说明
- [business_evaluation_report.json](business_evaluation_report.json) - 评估结果

## 文档规范

### 文档结构

```
docs/
├── index.md              # 文档首页
├── dev-guide/            # 开发者指南
│   ├── index.md
│   ├── candidate-experience.md
│   ├── hr-experience.md
│   ├── workflow.md
│   └── notification.md
├── models/               # 数据模型
│   └── assessment.md
├── roadmap/              # 路线图
│   └── survey.md
└── *.md                  # 操作指南
```

### 文档更新

更新文档后，需要：
1. 确保文档格式正确
2. 更新相关索引
3. 提交并推送变更