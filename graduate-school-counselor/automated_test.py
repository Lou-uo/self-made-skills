#!/usr/bin/env python3
"""
Automated Graduate School Counseling Test
Test the system with predefined user data.
"""

from scripts.profile_manager import GradSchoolProfileManager
from scripts.real_web_search import RealGradSchoolWebSearch
from scripts.recommendation_engine import RecommendationEngine

def create_test_user_profile():
    """Create a test user profile with realistic data."""
    print("=== 创建测试用户档案 ===")

    student_id = "zhang_san"

    # 创建档案
    profile_manager = GradSchoolProfileManager('.')
    profile = profile_manager.create_profile(student_id, {
        "major": "计算机科学与技术",
        "university": "某211高校",
        "gpa": 3.7,
        "research_interests": ["机器学习", "计算机视觉", "深度学习"]
    })

    print(f"已创建档案: {student_id}")
    print(f"  专业: {profile['academic_profile']['major']}")
    print(f"  学校: {profile['academic_profile']['university']}")
    print(f"  GPA: {profile['academic_profile']['gpa']}")
    print(f"  研究兴趣: {', '.join(profile['academic_profile']['research_interests'])}")

    # 添加测试成绩
    profile_manager.update_test_scores(student_id, {
        'toefl': 102,
        'gre': 318
    })
    print("\n已添加语言成绩:")
    print("  TOEFL: 102")
    print("  GRE: 318")

    # 添加研究经历
    profile_manager.add_research_experience(student_id, "projects", {
        "title": "基于深度学习的图像识别系统",
        "description": "使用ResNet进行CIFAR-10图像分类，准确率达到95%",
        "duration": "2024.03-2024.08",
        "supervisor": "李教授",
        "outcomes": ["完成项目报告", "学习深度学习技术", "准备发表论文"],
        "skills_used": ["Python", "PyTorch", "OpenCV"]
    })
    print("\n已添加研究经历:")
    print("  项目: 基于深度学习的图像识别系统")
    print("  成果: 完成项目报告，准确率95%")

    # 添加竞赛获奖
    profile_manager.add_achievement(student_id, "competitions", {
        "name": "ACM-ICPC程序设计竞赛",
        "year": "2024",
        "rank": "区域赛银奖",
        "level": "regional",
        "description": "团队编程竞赛，解决算法问题"
    })
    print("\n已添加竞赛获奖:")
    print("  ACM-ICPC区域赛银奖")

    # 添加目标学校跟踪
    profile_manager.track_school(student_id, "清华大学", "目标冲刺学校，AI方向强")
    profile_manager.track_school(student_id, "上海交通大学", "匹配学校，机器学习研究强")
    profile_manager.track_school(student_id, "南京大学", "匹配学校，理论计算机科学强")
    print("\n已添加目标学校跟踪:")
    print("  - 清华大学 (冲刺)")
    print("  - 上海交通大学 (匹配)")
    print("  - 南京大学 (匹配)")

    return student_id

def run_comprehensive_analysis(student_id):
    """Run comprehensive analysis for the test user."""
    print(f"\n=== 为 {student_id} 进行全面分析 ===")

    # 初始化各模块
    profile_manager = GradSchoolProfileManager('.')
    web_searcher = RealGradSchoolWebSearch()
    recommender = RecommendationEngine()

    # 加载完整档案
    full_profile = profile_manager.load_profile(student_id)
    if not full_profile:
        print("找不到学生档案")
        return

    print("\n档案概览:")
    summary = profile_manager.export_profile_summary(student_id)
    print(summary)

    print("\n网络信息搜索:")
    print("\n1. 最新CS专业院校排名:")
    rankings = web_searcher.search_school_rankings_real("CS")
    print(f"数据来源: {rankings.get('source', '未知')}")
    for tier, schools in rankings.get('rankings', {}).items():
        print(f"\n  {tier}:")
        for school in schools[:3]:
            print(f"    - {school['name']}: {school['difficulty']}")
            print(f"      要求: {school.get('requirements', 'N/A')}")

    print("\n2. 最新夏令营信息:")
    camps = web_searcher.search_summer_camps_real("CS")
    for camp in camps[:3]:
        print(f"\n  - {camp['university']}: {camp['program_name']}")
        print(f"    报名截止: {camp['application_deadline']}")
        print(f"    研究领域: {', '.join(camp['research_areas'][:2])}")
        print(f"    状态: {camp.get('status', '未知')}")

    print("\n3. 申请经验分享:")
    experiences = web_searcher.search_experience_posts_real("CS")
    for exp in experiences[:2]:
        print(f"\n  - {exp['title']}")
        print(f"    背景: {exp['background']['undergraduate']}, GPA {exp['background']['gpa']}")
        print(f"    成功因素: {', '.join(exp['success_factors'][:2])}")
        print(f"    关键策略: {', '.join(exp['key_strategies'][:2])}")

    print("\n个性化学校推荐:")
    recommendations = recommender.get_recommendations(full_profile)

    for category, schools in recommendations['recommendations'].items():
        print(f"\n  {category.upper()} 学校:")
        for school in schools:
            print(f"\n    学校: {school['school']}")
            print(f"    匹配度: {school['match_score']:.1f}/100")
            print(f"    研究优势: {', '.join(school['research_strengths'][:3])}")
            print(f"    录取率: {school['acceptance_rate']*100:.1f}%")
            print(f"    位置: {school['location']}")

    print("\n研究组 研究组推荐:")
    research_groups = recommender.get_research_group_recommendations(full_profile)
    for group in research_groups[:3]:
        print(f"\n  - {group['school']} - {group['group_name']}")
        print(f"    教授: {', '.join(group['professors'][:2])}")
        print(f"    研究方向: {', '.join(group['research_areas'][:3])}")
        print(f"    匹配度: {group.get('match_score', 'N/A')}")

    print("\n竞争力 竞争力分析:")
    analysis = web_searcher.get_competitive_analysis(full_profile)
    print(f"\n  综合竞争力分数: {analysis['total_score']:.0f}/100")
    print(f"  竞争力等级: {analysis['level']}")
    print(f"  申请建议: {analysis['recommendation']}")
    print(f"\n  评分详情:")
    for factor in analysis['factors']:
        print(f"    {factor}")

    print("\n📋 申请策略建议:")
    strategy = recommender.generate_application_strategy(full_profile)
    print(f"\n  申请时间线:")
    for phase in strategy['timeline']:
        print(f"    - {phase['phase']}: {', '.join(phase['tasks'][:2])}...")

    print(f"\n  目标学校分布: {strategy['target_schools']}")
    print(f"\n  优先级行动:")
    for action in strategy['priority_actions']:
        print(f"    - {action}")

    print(f"\n  需要改进的领域:")
    for area in strategy['improvement_areas']:
        print(f"    - {area}")

    print("\n" + "="*80)
    print(f"研究生申请咨询分析完成！")
    print(f"\n学生 {student_id} 的完整分析报告:")
    print("\n✅ 已完成:")
    print("  • 个性化档案创建和背景分析")
    print("  • 实时网络信息搜索和整合")
    print("  • 智能学校和研究组推荐")
    print("  • 详细竞争力评估和策略制定")

    print("\n📊 关键发现:")
    print(f"  • 综合竞争力: {analysis['total_score']:.0f}/100 ({analysis['level']})")
    print(f"  • 推荐策略: {analysis['recommendation']}")
    print(f"  • 目标学校: {len(recommendations['recommendations']['reach'])}冲刺 + {len(recommendations['recommendations']['match'])}匹配 + {len(recommendations['recommendations']['safety'])}保底")

    print("\n🚀 下一步建议:")
    print("  1. 关注推荐的夏令营申请截止日期")
    print("  2. 联系感兴趣的研究组教授")
    print("  3. 根据策略建议完善申请材料")
    print("  4. 持续更新档案信息跟踪进度")
    print("="*80)

def main():
    """Main function to run the automated test."""
    print("研究生申请咨询系统 - 自动化测试")
    print("="*60)

    # 创建测试用户档案
    student_id = create_test_user_profile()

    # 进行全面分析
    run_comprehensive_analysis(student_id)

if __name__ == "__main__":
    main()
