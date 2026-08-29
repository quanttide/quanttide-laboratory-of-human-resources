#!/usr/bin/env python3
"""
量潮招聘系统业务评估脚本

基于业务需求评估src代码是否可以有效解决生产问题。
业务需求来源：docs/ 目录下的文档。
"""

import re
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
from datetime import datetime
import json


@dataclass
class BusinessCheckResult:
    """业务检查结果"""
    flow: str  # 业务流程
    check_item: str  # 检查项
    business_goal: str  # 业务目标
    status: str  # pass, fail, warning
    evidence: str  # 证据
    gap: str  # 差距


@dataclass
class BusinessEvaluationReport:
    """业务评估报告"""
    timestamp: str
    project_path: str
    results: List[BusinessCheckResult]
    flow_status: Dict[str, Dict[str, Any]]
    conclusion: str
    recommendations: List[str]


class BusinessEvaluator:
    """业务评估器"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.results: List[BusinessCheckResult] = []
        self.site_content = ""
        self.studio_content = ""
        
        # 读取源代码
        site_file = self.project_path / "src" / "site" / "index.html"
        studio_file = self.project_path / "src" / "studio" / "index.html"
        
        if site_file.exists():
            self.site_content = site_file.read_text(encoding='utf-8')
        if studio_file.exists():
            self.studio_content = studio_file.read_text(encoding='utf-8')
    
    def add_result(self, flow: str, check_item: str, business_goal: str, 
                   status: str, evidence: str, gap: str = ""):
        """添加检查结果"""
        self.results.append(BusinessCheckResult(
            flow=flow,
            check_item=check_item,
            business_goal=business_goal,
            status=status,
            evidence=evidence,
            gap=gap
        ))
    
    def evaluate_all(self) -> BusinessEvaluationReport:
        """执行所有业务评估"""
        print("🔍 开始业务评估...")
        print("业务目标：让邮件从招聘流程里消失，所有流程走自研系统")
        print("=" * 60)
        
        # 评估各个业务流程
        self.evaluate_candidate_apply()
        self.evaluate_survey_management()
        self.evaluate_notification_system()
        self.evaluate_review_process()
        self.evaluate_invite_process()
        self.evaluate_exam_process()
        self.evaluate_workflow_automation()
        self.evaluate_data_centralization()
        self.evaluate_remove_email_dependency()
        
        # 生成报告
        return self.generate_report()
    
    def evaluate_candidate_apply(self):
        """评估候选人投递能力"""
        print("\n📋 评估候选人投递能力...")
        
        # 业务需求：候选人访问招聘页面，填写基本信息，上传简历，提交投递
        # 业务目标：替代邮件投递
        
        # 检查是否有投递功能
        if "submit" in self.site_content.lower() or "投递" in self.site_content:
            self.add_result(
                flow="投递",
                check_item="投递功能",
                business_goal="候选人能在系统内完成投递",
                status="pass",
                evidence="候选人门户包含投递相关功能"
            )
        else:
            self.add_result(
                flow="投递",
                check_item="投递功能",
                business_goal="候选人能在系统内完成投递",
                status="fail",
                evidence="未发现投递功能",
                gap="需要实现候选人投递功能"
            )
        
        # 检查投递后是否自动发送问卷通知
        if "survey" in self.site_content.lower() or "问卷" in self.site_content:
            self.add_result(
                flow="投递",
                check_item="问卷通知",
                business_goal="投递后系统自动发送问卷通知",
                status="pass",
                evidence="候选人门户包含问卷相关功能"
            )
        else:
            self.add_result(
                flow="投递",
                check_item="问卷通知",
                business_goal="投递后系统自动发送问卷通知",
                status="fail",
                evidence="未发现问卷通知功能",
                gap="需要实现投递后自动发送问卷通知"
            )
    
    def evaluate_survey_management(self):
        """评估问卷管理能力"""
        print("\n📝 评估问卷管理能力...")
        
        # 业务需求：问卷链接存储到系统，HR可在后台管理
        # 业务目标：替代从邮箱缓存问卷链接
        
        # 检查问卷链接管理
        if "survey" in self.studio_content.lower() and "link" in self.studio_content.lower():
            self.add_result(
                flow="问卷",
                check_item="问卷链接管理",
                business_goal="问卷链接存储到系统，HR可在后台管理",
                status="pass",
                evidence="管理工作台包含问卷链接管理功能"
            )
        else:
            self.add_result(
                flow="问卷",
                check_item="问卷链接管理",
                business_goal="问卷链接存储到系统，HR可在后台管理",
                status="warning",
                evidence="未明确发现问卷链接管理功能",
                gap="需要实现问卷链接管理功能"
            )
        
        # 检查候选人能否在系统内填写问卷
        if "questionnaire" in self.site_content.lower() or "问卷" in self.site_content:
            self.add_result(
                flow="问卷",
                check_item="问卷填写",
                business_goal="候选人在系统内填写问卷",
                status="pass",
                evidence="候选人门户包含问卷填写功能"
            )
        else:
            self.add_result(
                flow="问卷",
                check_item="问卷填写",
                business_goal="候选人在系统内填写问卷",
                status="fail",
                evidence="未发现问卷填写功能",
                gap="需要实现问卷填写功能"
            )
        
        # 检查问卷提交后是否自动记录
        if "submit" in self.site_content.lower() and "assessment" in self.site_content.lower():
            self.add_result(
                flow="问卷",
                check_item="问卷提交记录",
                business_goal="问卷提交后系统自动记录",
                status="pass",
                evidence="候选人门户包含评估提交功能"
            )
        else:
            self.add_result(
                flow="问卷",
                check_item="问卷提交记录",
                business_goal="问卷提交后系统自动记录",
                status="fail",
                evidence="未发现问卷提交记录功能",
                gap="需要实现问卷提交自动记录"
            )
    
    def evaluate_notification_system(self):
        """评估通知能力"""
        print("\n🔔 评估通知能力...")
        
        # 业务需求：所有通知都在系统内完成，不再依赖邮件
        # 业务目标：替代邮件通知
        
        # 检查候选人通知中心
        if "notification" in self.site_content.lower() or "通知" in self.site_content:
            self.add_result(
                flow="通知",
                check_item="候选人通知中心",
                business_goal="候选人在系统内接收通知",
                status="pass",
                evidence="候选人门户包含通知功能"
            )
        else:
            self.add_result(
                flow="通知",
                check_item="候选人通知中心",
                business_goal="候选人在系统内接收通知",
                status="fail",
                evidence="未发现通知功能",
                gap="需要实现候选人通知中心"
            )
        
        # 检查HR通知中心
        if "notification" in self.studio_content.lower() or "通知" in self.studio_content:
            self.add_result(
                flow="通知",
                check_item="HR通知中心",
                business_goal="HR在系统内接收通知",
                status="pass",
                evidence="管理工作台包含通知功能"
            )
        else:
            self.add_result(
                flow="通知",
                check_item="HR通知中心",
                business_goal="HR在系统内接收通知",
                status="fail",
                evidence="未发现HR通知功能",
                gap="需要实现HR通知中心"
            )
        
        # 检查通知已读状态追踪
        if "read" in self.site_content.lower() and "unread" in self.site_content.lower():
            self.add_result(
                flow="通知",
                check_item="通知已读追踪",
                business_goal="追踪通知已读/未读状态",
                status="pass",
                evidence="通知功能包含已读/未读状态"
            )
        else:
            self.add_result(
                flow="通知",
                check_item="通知已读追踪",
                business_goal="追踪通知已读/未读状态",
                status="warning",
                evidence="未明确发现已读/未读状态追踪",
                gap="需要实现通知已读状态追踪"
            )
    
    def evaluate_review_process(self):
        """评估审核能力"""
        print("\n✅ 评估审核能力...")
        
        # 业务需求：HR在系统内审核问卷，提供审核操作（通过/拒绝）
        # 业务目标：替代邮件审核
        
        # 检查HR能否看到问卷答案
        if "answer" in self.studio_content.lower() or "答案" in self.studio_content:
            self.add_result(
                flow="审核",
                check_item="查看问卷答案",
                business_goal="HR在系统内查看候选人问卷答案",
                status="pass",
                evidence="管理工作台包含查看答案功能"
            )
        else:
            self.add_result(
                flow="审核",
                check_item="查看问卷答案",
                business_goal="HR在系统内查看候选人问卷答案",
                status="warning",
                evidence="未明确发现查看问卷答案功能",
                gap="需要实现查看问卷答案功能"
            )
        
        # 检查审核操作
        if "approve" in self.studio_content.lower() or "reject" in self.studio_content.lower():
            self.add_result(
                flow="审核",
                check_item="审核操作",
                business_goal="HR在系统内执行审核操作",
                status="pass",
                evidence="管理工作台包含审核操作功能"
            )
        else:
            self.add_result(
                flow="审核",
                check_item="审核操作",
                business_goal="HR在系统内执行审核操作",
                status="warning",
                evidence="未明确发现审核操作功能",
                gap="需要实现审核操作功能"
            )
    
    def evaluate_invite_process(self):
        """评估邀请能力"""
        print("\n👋 评估邀请能力...")
        
        # 业务需求：审核通过后系统自动发送邀请通知，包含群二维码
        # 业务目标：替代邮件邀请
        
        # 检查邀请通知功能
        if "invite" in self.studio_content.lower() or "邀请" in self.studio_content:
            self.add_result(
                flow="邀请",
                check_item="邀请通知",
                business_goal="审核通过后系统自动发送邀请通知",
                status="pass",
                evidence="管理工作台包含邀请功能"
            )
        else:
            self.add_result(
                flow="邀请",
                check_item="邀请通知",
                business_goal="审核通过后系统自动发送邀请通知",
                status="fail",
                evidence="未发现邀请通知功能",
                gap="需要实现邀请通知功能"
            )
        
        # 检查二维码管理
        if "qr" in self.studio_content.lower() or "二维码" in self.studio_content:
            self.add_result(
                flow="邀请",
                check_item="二维码管理",
                business_goal="群二维码在系统内管理",
                status="pass",
                evidence="管理工作台包含二维码管理功能"
            )
        else:
            self.add_result(
                flow="邀请",
                check_item="二维码管理",
                business_goal="群二维码在系统内管理",
                status="warning",
                evidence="未发现二维码管理功能",
                gap="需要实现二维码管理功能"
            )
    
    def evaluate_exam_process(self):
        """评估考核能力"""
        print("\n📊 评估考核能力...")
        
        # 业务需求：入群后系统自动发送考核通知，候选人能提交考核成果
        # 业务目标：替代邮件考核
        
        # 检查考核通知功能
        if "exam" in self.studio_content.lower() or "考核" in self.studio_content:
            self.add_result(
                flow="考核",
                check_item="考核通知",
                business_goal="入群后系统自动发送考核通知",
                status="pass",
                evidence="管理工作台包含考核功能"
            )
        else:
            self.add_result(
                flow="考核",
                check_item="考核通知",
                business_goal="入群后系统自动发送考核通知",
                status="fail",
                evidence="未发现考核通知功能",
                gap="需要实现考核通知功能"
            )
        
        # 检查考核成果提交
        if "exam" in self.site_content.lower() or "考核" in self.site_content:
            self.add_result(
                flow="考核",
                check_item="考核成果提交",
                business_goal="候选人在系统内提交考核成果",
                status="pass",
                evidence="候选人门户包含考核功能"
            )
        else:
            self.add_result(
                flow="考核",
                check_item="考核成果提交",
                business_goal="候选人在系统内提交考核成果",
                status="fail",
                evidence="未发现考核成果提交功能",
                gap="需要实现考核成果提交功能"
            )
    
    def evaluate_workflow_automation(self):
        """评估流程自动化能力"""
        print("\n🔄 评估流程自动化能力...")
        
        # 业务需求：状态自动流转，超时自动标记
        # 业务目标：替代邮件文件夹管理
        
        # 检查状态流转
        if "statusFlow" in self.studio_content or "status_flow" in self.studio_content:
            self.add_result(
                flow="流程",
                check_item="状态流转",
                business_goal="状态自动流转",
                status="pass",
                evidence="管理工作台包含状态流转逻辑"
            )
        else:
            self.add_result(
                flow="流程",
                check_item="状态流转",
                business_goal="状态自动流转",
                status="warning",
                evidence="未明确发现状态流转逻辑",
                gap="需要实现状态自动流转"
            )
        
        # 检查超时处理
        if "timeout" in self.studio_content.lower() or "超时" in self.studio_content:
            self.add_result(
                flow="流程",
                check_item="超时处理",
                business_goal="超时自动标记",
                status="pass",
                evidence="管理工作台包含超时处理功能"
            )
        else:
            self.add_result(
                flow="流程",
                check_item="超时处理",
                business_goal="超时自动标记",
                status="fail",
                evidence="未发现超时处理功能",
                gap="需要实现超时自动标记功能"
            )
        
        # 检查状态历史记录
        if "history" in self.studio_content.lower() or "历史" in self.studio_content:
            self.add_result(
                flow="流程",
                check_item="状态历史",
                business_goal="HR能看到状态流转历史",
                status="pass",
                evidence="管理工作台包含历史记录功能"
            )
        else:
            self.add_result(
                flow="流程",
                check_item="状态历史",
                business_goal="HR能看到状态流转历史",
                status="warning",
                evidence="未发现状态历史记录功能",
                gap="需要实现状态历史记录功能"
            )
    
    def evaluate_data_centralization(self):
        """评估数据集中能力"""
        print("\n💾 评估数据集中能力...")
        
        # 业务需求：所有数据集中在一个地方
        # 业务目标：替代散落在邮件和飞书表格的数据
        
        # 检查数据存储方式
        if "localStorage" in self.studio_content:
            self.add_result(
                flow="数据",
                check_item="数据存储",
                business_goal="数据集中存储",
                status="warning",
                evidence="使用localStorage存储数据",
                gap="生产环境需要使用数据库替代localStorage"
            )
        else:
            self.add_result(
                flow="数据",
                check_item="数据存储",
                business_goal="数据集中存储",
                status="pass",
                evidence="数据存储在系统内"
            )
        
        # 检查候选人信息完整性
        if "candidate" in self.studio_content.lower() and "email" in self.studio_content.lower():
            self.add_result(
                flow="数据",
                check_item="候选人信息",
                business_goal="HR在系统内查看候选人完整信息",
                status="pass",
                evidence="管理工作台包含候选人信息管理"
            )
        else:
            self.add_result(
                flow="数据",
                check_item="候选人信息",
                business_goal="HR在系统内查看候选人完整信息",
                status="fail",
                evidence="未发现候选人信息管理功能",
                gap="需要实现候选人信息管理功能"
            )
    
    def evaluate_remove_email_dependency(self):
        """评估移除邮件依赖"""
        print("\n🚫 评估移除邮件依赖...")
        
        # 业务目标：完全移除邮件依赖
        
        # 检查是否依赖lark-cli
        if "lark-cli" in self.site_content or "lark-cli" in self.studio_content:
            self.add_result(
                flow="邮件移除",
                check_item="lark-cli依赖",
                business_goal="移除lark-cli依赖",
                status="fail",
                evidence="代码中仍包含lark-cli依赖",
                gap="需要移除lark-cli依赖"
            )
        else:
            self.add_result(
                flow="邮件移除",
                check_item="lark-cli依赖",
                business_goal="移除lark-cli依赖",
                status="pass",
                evidence="代码中未发现lark-cli依赖"
            )
        
        # 检查是否有邮件模板
        if "mail" in self.site_content.lower() or "邮件" in self.site_content:
            self.add_result(
                flow="邮件移除",
                check_item="邮件模板",
                business_goal="移除邮件模板渲染",
                status="warning",
                evidence="可能包含邮件相关代码",
                gap="需要确认并移除邮件模板"
            )
        else:
            self.add_result(
                flow="邮件移除",
                check_item="邮件模板",
                business_goal="移除邮件模板渲染",
                status="pass",
                evidence="未发现邮件模板代码"
            )
    
    def generate_report(self) -> BusinessEvaluationReport:
        """生成评估报告"""
        # 统计各流程状态
        flow_stats = {}
        for result in self.results:
            if result.flow not in flow_stats:
                flow_stats[result.flow] = {"pass": 0, "fail": 0, "warning": 0, "total": 0}
            flow_stats[result.flow][result.status] += 1
            flow_stats[result.flow]["total"] += 1
        
        # 计算各流程通过率
        flow_status = {}
        for flow, stats in flow_stats.items():
            pass_rate = (stats["pass"] / stats["total"] * 100) if stats["total"] > 0 else 0
            if pass_rate >= 80:
                status = "达成"
            elif pass_rate >= 60:
                status = "基本达成"
            elif pass_rate >= 40:
                status = "部分达成"
            else:
                status = "未达成"
            flow_status[flow] = {"pass_rate": pass_rate, "status": status, **stats}
        
        # 计算整体通过率
        total_pass = sum(1 for r in self.results if r.status == "pass")
        total = len(self.results)
        overall_pass_rate = (total_pass / total * 100) if total > 0 else 0
        
        # 确定整体结论
        if overall_pass_rate >= 80:
            conclusion = "完全达成：可以完全替代邮件流程"
        elif overall_pass_rate >= 60:
            conclusion = "基本达成：可以部分替代邮件流程"
        elif overall_pass_rate >= 40:
            conclusion = "部分达成：需要补充功能才能替代"
        else:
            conclusion = "未达成：无法替代邮件流程"
        
        # 生成改进建议
        recommendations = self.generate_recommendations()
        
        return BusinessEvaluationReport(
            timestamp=datetime.now().isoformat(),
            project_path=str(self.project_path),
            results=self.results,
            flow_status=flow_status,
            conclusion=conclusion,
            recommendations=recommendations
        )
    
    def generate_recommendations(self) -> List[str]:
        """生成改进建议"""
        recommendations = []
        
        # 收集所有失败和警告的检查项
        fail_items = [r for r in self.results if r.status == "fail"]
        warning_items = [r for r in self.results if r.status == "warning"]
        
        # 按流程分组
        flow_issues = {}
        for item in fail_items + warning_items:
            if item.flow not in flow_issues:
                flow_issues[item.flow] = []
            flow_issues[item.flow].append(item)
        
        # 生成建议
        for flow, issues in flow_issues.items():
            if any(i.status == "fail" for i in issues):
                recommendations.append(f"🔴 {flow}流程：需要实现{', '.join(i.check_item for i in issues if i.status == 'fail')}")
        
        # 添加通用建议
        recommendations.append("📋 建议：按照ROADMAP.md规划，优先实现v0.1数据层")
        recommendations.append("📋 建议：按照survey.md规划，实现问卷流程自动化")
        recommendations.append("📋 建议：按照notification.md规划，实现通知系统")
        
        return recommendations


def print_report(report: BusinessEvaluationReport):
    """打印评估报告"""
    print("\n" + "=" * 60)
    print("📊 业务评估报告")
    print("=" * 60)
    
    print(f"\n⏰ 评估时间: {report.timestamp}")
    print(f"📁 项目路径: {report.project_path}")
    print(f"🎯 整体结论: {report.conclusion}")
    
    print("\n" + "-" * 60)
    print("📈 各流程评估结果")
    print("-" * 60)
    
    for flow, status in report.flow_status.items():
        print(f"{flow}: {status['status']} (通过率: {status['pass_rate']:.0f}%)")
    
    print("\n" + "-" * 60)
    print("🔍 详细检查结果")
    print("-" * 60)
    
    current_flow = None
    for result in report.results:
        if result.flow != current_flow:
            current_flow = result.flow
            print(f"\n【{current_flow}】")
        
        status_icon = {
            "pass": "✅",
            "fail": "❌",
            "warning": "⚠️"
        }.get(result.status, "❓")
        
        print(f"  {status_icon} {result.check_item}")
        print(f"     业务目标: {result.business_goal}")
        print(f"     证据: {result.evidence}")
        if result.gap:
            print(f"     差距: {result.gap}")
    
    print("\n" + "-" * 60)
    print("💡 改进建议")
    print("-" * 60)
    
    for i, recommendation in enumerate(report.recommendations, 1):
        print(f"{i}. {recommendation}")
    
    print("\n" + "=" * 60)


def save_report(report: BusinessEvaluationReport, output_path: str):
    """保存评估报告"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(asdict(report), f, ensure_ascii=False, indent=2)
    print(f"\n💾 评估报告已保存到: {output_path}")


def main():
    """主函数"""
    project_path = Path(__file__).parent
    
    # 创建评估器
    evaluator = BusinessEvaluator(str(project_path))
    
    # 执行评估
    report = evaluator.evaluate_all()
    
    # 打印报告
    print_report(report)
    
    # 保存报告
    output_path = project_path / "business_evaluation_report.json"
    save_report(report, str(output_path))
    
    # 返回评估结果
    return "达成" in report.conclusion or "基本达成" in report.conclusion


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)