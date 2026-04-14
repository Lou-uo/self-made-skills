#!/usr/bin/env python3
"""
Personalized Graduate School Counseling Test
Create and test your own graduate school profile.
"""

from scripts.profile_manager import GradSchoolProfileManager
from scripts.real_web_search import RealGradSchoolWebSearch
from scripts.recommendation_engine import RecommendationEngine

def create_your_profile():
    """Create a profile based on user input."""
    print("=== 创建您的研究生申请档案 ===")
    print("请输入您的基本信息 (可以直接回车使用默认值):")

    # 获取用户信息
    student_id = input("\n学生ID (如: your_name): ").strip() or "test_user"
    major = input("专业 (默认: 计算机科学与技术): ").strip() or "计算机科学与技术"
    university = input("本科院校 (默认: 某211高校): ").strip() or "某211高校"
    gpa = float(input("GPA (默认: 3.7): ") or "3.7")

    research_interests_input = input("研究兴趣，用逗号分隔 (默认: 机器学习,人工智能): ").strip()
    research_interests = [interest.strip() for interest in research_interests_input.split(',')] if research_interests_input else ["机器学习", "人工智能"]

    # 创建档案
    profile_manager = GradSchoolProfileManager('.')
    profile = profile_manager.create_profile(student_id, {
        "major": major,
        "university": university,
        "gpa": gpa,
        "research_interests": research_interests
    })

    print(f"\n✅ 已创建档案: {student_id}")

    # 添加详细信息
    print("\n=== 添加详细背景信息 ===")

    # TOEFL/GRE成绩
    print("\n语言成绩:")
    toefl = input("TOEFL分数 (默认: 100): ")
    gre = input("GRE分数 (默认: 315): ")

    if toefl or gre:
        scores = {}
        if toefl:
            scores['toefl'] = int(toefl)
        if gre:
            scores['gre'] = int(gre)
        profile_manager.update_test_scores(student_id, scores)
        print("✅ 已更新语言成绩")

    # 研究经历
    add_research = input("\n是否添加研究经历? (y/n, 默认: y): ").strip().lower() != 'n'
    if add_research:
        print("\n研究经历 (可直接回车跳过):")
        project_title = input("项目标题 (默认: 基于深度学习的图像识别研究): ").strip() or "基于深度学习的图像识别研究"
        project_desc = input("项目描述 (默认: 使用CNN进行图像分类): ").strip() or "使用CNN进行图像分类"
        supervisor = input("指导老师 (默认: 李教授): ").strip() or "李教授"

        if project_title and project_desc:
            profile_manager.add_research_experience(student_id, "projects", {
                "title": project_title,
                "description": project_desc,
                "duration": "2024.03-2024.09",
                "supervisor": supervisor,
                "outcomes": ["完成项目报告", "学习深度学习技术"],
                "skills_used": ["Python", "TensorFlow", "深度学习"]
            })
            print("✅ 已添加研究经历")

    # 竞赛获奖
    add_competition = input("\n是否添加竞赛获奖? (y/n, 默认: y): ").strip().lower() != 'n'
    if add_competition:
        print("\n竞赛获奖 (可直接回车跳过):")
        comp_name = input("竞赛名称 (默认: 全国大学生计算机设计大赛): ").strip() or "全国大学生计算机设计大赛"
        comp_rank = input("获奖等级 (默认: 省级二等奖): ").strip() or "省级二等奖"

        if comp_name and comp_rank:
            profile_manager.add_achievement(student_id, "competitions", {
                "name": comp_name,
                "year": "2024",
                "rank": comp_rank,
                "level": "regional",
                "description": "编程与算法设计竞赛"
            })
            print("✅ 已添加竞赛获奖")

    return student_id

def run_personalized_analysis(student_id):
    """Run personalized analysis for the student."""
    print(f"\n=== 为您 ({student_id}) 进行个性化分析 ===")

    # 初始化各模块
    profile_manager = GradSchoolProfileManager('.')
    web_searcher = RealGradSchoolWebSearch()
    recommender = RecommendationEngine()

    # 加载完整档案
    full_profile = profile_manager.load_profile(student_id)
    if not full_profile:
        print("❌ 找不到学生档案")
        return

    print("\n📊 档案概览:")
    summary = profile_manager.export_profile_summary(student_id)
    print(summary)

    print("\n🔍 网络信息搜索:")
    # 获取最新的院校信息
    print("\n最新CS专业排名:")
    rankings = web_searcher.search_school_rankings_real("CS")
    for tier, schools in rankings.get('rankings', {}).items():
        print(f"  {tier}: {', '.join([s['name'] for s in schools[:3]])}")

    # 获取最新夏令营信息
    print("\n最新夏令营信息:")
    camps = web_searcher.search_summer_camps_real("CS")
    for camp in camps[:2]:
        print(f"  - {camp['university']}: {camp['program_name']}")
        print(f"    截止: {camp['application_deadline']}")

    print("\n🎯 个性化学校推荐:")
    recommendations = recommender.get_recommendations(full_profile)

    for category, schools in recommendations['recommendations'].items():
        print(f"\n  {category.upper()} 学校:")
        for school in schools:
            print(f"    {school['school']}")
            print(f"      匹配度: {school['match_score']:.1f}/100")
            print(f"      研究优势: {', '.join(school['research_strengths'][:2])}")
            print(f"      录取率: {school['acceptance_rate']*100:.1f}%")

    print("\n🔬 研究组推荐:")
    research_groups = recommender.get_research_group_recommendations(full_profile)
    for group in research_groups[:3]:
        print(f"  - {group['school']} - {group['group_name']}")
        print(f"    教授: {', '.join(group['professors'][:2])}")
        print(f"    研究方向: {', '.join(group['research_areas'][:3])}")

    print("\n📈 竞争力分析:")
    analysis = web_searcher.get_competitive_analysis(full_profile)
    print(f"  综合分数: {analysis['total_score']:.0f}/100")
    print(f"  等级: {analysis['level']}")
    print(f"  建议: {analysis['recommendation']}")

    print("\n📋 申请策略:")
    strategy = recommender.generate_application_strategy(full_profile)
    print(f"  目标分布: {strategy['target_schools']}")
    print(f"  优先级行动:")
    for action in strategy['priority_actions']:
        print(f"    - {action}")

    print("\n" + "="*60)
    print(f"{student_id} 的保研咨询分析完成！")
    print("\n基于您的档案，我们为您提供:")
    print("✅ 个性化的学校推荐")
    print("✅ 匹配的研究组建议")
    print("✅ 详细的竞争力分析")
    print("✅ 具体的申请策略")
    print("\n接下来您可以:")
    print("• 根据推荐完善申请材料")
    print("• 关注相关学校的夏令营信息")
    print("• 联系感兴趣的研究组")
    print("• 持续更新档案信息")
    print("="*60)

def main():
    """Main function to run the personalized test."""
    print("欢迎使用研究生申请咨询系统！")
    print("我们将为您创建个性化档案并提供专业的申请建议\n")

    # 创建档案
    student_id = create_your_profile()

    # 进行个性化分析
    run_personalized_analysis(student_id)

if __name__ == "__main__":
    main()
