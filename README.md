# 量潮招聘实验室

招聘流程自研系统的原型验证仓库。

## 目标

让邮件从招聘流程里消失，所有流程走自研系统。

## 文档

- [AGENTS.md](./AGENTS.md) - 核心理解：「自研」的定义
- [ROADMAP.md](./ROADMAP.md) - 开发路线图
- [EVALUATION.md](./EVALUATION.md) - 评估方法说明
- [EVALUATION_README.md](./EVALUATION_README.md) - 评估系统使用说明

## 实验

- [recruitment/](./examples/recruitment/) - 招聘页原型
- [salary/](./examples/salary/) - 薪资计算原型

## 业务评估系统

本项目包含一套基于业务需求的评估系统，用于验证原型代码是否可以有效解决生产问题。

### 业务目标

**让邮件从招聘流程里消失，所有流程走自研系统。**

### 快速开始

```bash
# 运行业务评估
python3 business_evaluate.py
```

### 评估维度

基于 docs/ 目录下的业务需求文档，评估以下业务流程：

1. **投递能力**：候选人能否在系统内完成投递
2. **问卷管理**：问卷链接能否在系统内管理
3. **通知能力**：系统能否自动发送站内信通知
4. **审核能力**：HR能否在系统内审核问卷
5. **邀请能力**：系统能否自动发送实训邀请
6. **考核能力**：候选人能否在系统内提交考核成果
7. **流程自动化**：状态能否自动流转
8. **数据集中**：所有数据能否集中存储
9. **邮件移除**：能否完全移除邮件依赖

### 评估结果

- 业务评估报告：`business_evaluation_report.json`
- 业务评估说明：`BUSINESS_EVALUATION.md`

详细说明请参考 [BUSINESS_EVALUATION.md](./BUSINESS_EVALUATION.md)。
