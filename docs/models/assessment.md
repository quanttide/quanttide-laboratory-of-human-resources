# 评估模型

## 概述

基于 Question-Answer 模型，通过扩展类型覆盖多种评估形式。

## 核心结构

```
Assessment（评估）
    └── Question（问题）
            └── Answer（回答）
```

## Question 类型

| type | 说明 | answer.value 格式 |
|------|------|-------------------|
| text | 文本输入 | string |
| select | 单选 | string |
| multi_select | 多选 | string[] |
| file_upload | 文件上传 | `{ "url": "...", "name": "..." }` |
| code | 代码编写 | `{ "language": "python", "content": "..." }` |
| link | 链接输入 | `{ "url": "...", "title": "..." }` |
| scale | 量表评分 | number |

## Assessment 类型

| type | 说明 | 典型场景 |
|------|------|----------|
| questionnaire | 问卷 | 价值观筛选、动机评估 |
| exam | 考核 | 技术笔试、实操任务、方案设计 |
| interview | 面试 | 结构化面试、半结构化面试 |

## 完整模型

### 问卷（questionnaire）

```json
{
  "id": "assessment_v1",
  "type": "questionnaire",
  "title": "量潮科技准入问卷",
  "description": "请基于真实想法认真作答",
  "questions": [
    {
      "id": "q001",
      "type": "text",
      "category": "basic",
      "order": 1,
      "required": true,
      "label": "您的姓名和专业"
    },
    {
      "id": "q002",
      "type": "select",
      "category": "basic",
      "order": 2,
      "required": true,
      "label": "请选择您的岗位方向",
      "options": [
        { "value": "product_manager", "label": "产品经理" },
        { "value": "data_engineer", "label": "数据工程师" },
        { "value": "hr", "label": "HR" },
        { "value": "other", "label": "其他" }
      ]
    },
    {
      "id": "q003",
      "type": "multi_select",
      "category": "motivation",
      "order": 3,
      "required": true,
      "label": "驱动你这次看机会的最主要原因是什么？",
      "options": [
        { "value": "growth_limit", "label": "看不到成长" },
        { "value": "industry_change", "label": "想换赛道" },
        { "value": "attracted_by_brand", "label": "被量潮吸引" }
      ]
    },
    {
      "id": "q004",
      "type": "text",
      "category": "values",
      "order": 4,
      "required": true,
      "label": "如果你入职后发现实际工作和预期有出入，你会怎么应对？"
    }
  ]
}
```

### 考核（exam）

考核可以是技术笔试，也可以是实操任务，通过 Question 类型组合实现。

**技术笔试示例：**

```json
{
  "id": "assessment_v2",
  "type": "exam",
  "title": "数据工程师笔试",
  "time_limit": 60,
  "questions": [
    {
      "id": "q101",
      "type": "select",
      "category": "technical",
      "order": 1,
      "required": true,
      "label": "以下哪个是列式数据库？",
      "options": [
        { "value": "a", "label": "MySQL" },
        { "value": "b", "label": "PostgreSQL" },
        { "value": "c", "label": "ClickHouse" },
        { "value": "d", "label": "MongoDB" }
      ]
    },
    {
      "id": "q102",
      "type": "code",
      "category": "technical",
      "order": 2,
      "required": true,
      "label": "请用 Python 实现一个函数，输入列表返回去重后的有序列表"
    }
  ]
}
```

**实操任务示例：**

```json
{
  "id": "assessment_v3",
  "type": "exam",
  "title": "数据管道设计",
  "description": "设计一个从 CSV 到 PostgreSQL 的数据管道",
  "time_limit": null,
  "questions": [
    {
      "id": "q201",
      "type": "file_upload",
      "category": "deliverable",
      "order": 1,
      "required": true,
      "label": "请上传设计文档",
      "file_config": {
        "accept": [".md", ".pdf", ".docx"]
      }
    },
    {
      "id": "q202",
      "type": "link",
      "category": "deliverable",
      "order": 2,
      "required": true,
      "label": "请提供代码仓库链接"
    },
    {
      "id": "q203",
      "type": "text",
      "category": "reflection",
      "order": 3,
      "required": false,
      "label": "遇到的主要困难及解决方式"
    }
  ]
}
```

### 面试（interview）

```json
{
  "id": "assessment_v4",
  "type": "interview",
  "title": "技术面试",
  "interviewer": "interviewer_001",
  "scheduled_at": "2024-01-20T14:00:00Z",
  "duration_minutes": 60,
  "questions": [
    {
      "id": "q301",
      "type": "text",
      "category": "behavioral",
      "order": 1,
      "required": true,
      "label": "请介绍一个你主导的项目，遇到的最大挑战是什么？"
    },
    {
      "id": "q302",
      "type": "text",
      "category": "situational",
      "order": 2,
      "required": true,
      "label": "如果团队成员对你的方案有不同意见，你会怎么处理？"
    },
    {
      "id": "q303",
      "type": "scale",
      "category": "evaluation",
      "order": 3,
      "required": true,
      "label": "沟通能力评分",
      "scale_config": {
        "min": 1,
        "max": 5,
        "labels": { "1": "较差", "3": "一般", "5": "优秀" }
      }
    }
  ]
}
```

## 回答模型

```json
{
  "id": "answer_001",
  "assessment_id": "assessment_v1",
  "assessment_type": "questionnaire",
  "candidate_id": "candidate_001",
  "submitted_at": "2024-01-15T10:30:00Z",
  "duration_minutes": 18,
  "answers": [
    { "question_id": "q001", "value": "张三-计算机科学" },
    { "question_id": "q002", "value": "data_engineer" },
    { "question_id": "q003", "value": ["growth_limit", "attracted_by_brand"] },
    { "question_id": "q004", "value": "先和主管沟通，实在无法接受再考虑其他选项。" }
  ]
}
```

### 各类型回答示例

```json
{
  "answers": [
    { "question_id": "q001", "value": "文本内容" },
    { "question_id": "q101", "value": "c" },
    { 
      "question_id": "q102", 
      "value": {
        "language": "python",
        "content": "def unique_sorted(lst):\n    return sorted(set(lst))"
      }
    },
    {
      "question_id": "q201",
      "value": {
        "url": "https://storage.example.com/docs/design.pdf",
        "name": "design.pdf"
      }
    },
    {
      "question_id": "q202",
      "value": {
        "url": "https://github.com/example/project",
        "title": "数据管道项目"
      }
    }
  ]
}
```

## 字段说明

### question.category

| 类别 | 说明 |
|------|------|
| basic | 基本信息 |
| motivation | 动机与预期 |
| values | 价值观与稳定性 |
| technical | 技术能力 |
| deliverable | 交付物 |
| reflection | 反思总结 |
| behavioral | 行为面试（过往经历） |
| situational | 情景面试（假设场景） |
| evaluation | 面试评分 |
