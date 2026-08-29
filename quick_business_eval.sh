#!/bin/bash
# 量潮招聘系统业务评估快速脚本

set -e

echo "🚀 量潮招聘系统业务评估"
echo "========================"
echo ""
echo "业务目标：让邮件从招聘流程里消失，所有流程走自研系统"
echo ""

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3，请先安装Python3"
    exit 1
fi

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "📁 项目路径: $SCRIPT_DIR"
echo ""

# 运行业务评估脚本
echo "🔍 开始业务评估..."
echo ""
python3 business_evaluate.py

# 检查评估结果
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 业务评估完成！"
    echo ""
    echo "📋 生成的文件:"
    echo "  - business_evaluation_report.json (详细评估报告)"
    echo ""
    echo "📖 相关文档:"
    echo "  - BUSINESS_EVALUATION.md (业务评估说明)"
    echo ""
    echo "💡 下一步建议:"
    echo "  1. 查看评估报告: cat business_evaluation_report.json | python3 -m json.tool"
    echo "  2. 根据评估结果制定改进计划"
    echo "  3. 参考 docs/ 目录下的业务需求文档"
else
    echo ""
    echo "❌ 业务评估失败，请检查错误信息"
    exit 1
fi