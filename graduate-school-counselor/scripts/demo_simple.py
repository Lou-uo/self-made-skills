#!/usr/bin/env python3
"""
Graduate School Counselor Demo
Demonstrates the complete functionality of the graduate school counselor skill.
"""

import json
from profile_manager import GradSchoolProfileManager
from web_search import GradSchoolWebSearch
from recommendation_engine import RecommendationEngine

def run_demo():
    """Run a comprehensive demo of the graduate school counselor skill."""
    print("=" * 60)
    print("研究生申请咨询技能演示")
    print("=" * 60)

    # 初始化各个模块
    profile_manager = GradSchoolProfileManager('.')
    web_searcher = GradSchoolWebSearch()
    recommender = RecommendationEngine()

    print("\n第一步：创建学生档案")
    print("-" * 40)

    # 创建演示学生档案
    demo_profile = profile_manager.create_profile("demo_student", {
        "major": "计算机科学与技术",
        "university": "某985高校",
        "gpa": 3.75,
        "research_interests": ["机器学习", "计算机视觉", "深度学习"]
    })

    print(f"已创建学生档案: demo_student")
    print(f"   专业: {demo_profile['academic_profile']['major']}")
    print(f"   GPA: {demo_profile['academic_profile']['gpa']}")
    print(f"   研究兴趣: {', '.join(demo_profile['academic_profile']['research_interests'])}")

    # 添加详细信息
    profile_manager.add_research_experience("demo_student", "projects", {
        "title": "基于深度学习的图像分类系统",
        "description": "使用ResNet进行CIFAR-10图像分类，准确率达到95%",
        "duration": "2024.03-2024.08",
        "supervisor": "李教授",
        "outcomes": ["完成项目报告", "准备发表论文", "获得优秀项目奖"],
        "skills_used": ["Python", "PyTorch", "OpenCV"]
    })

    profile_manager.add_achievement("demo_student", "competitions", {
        "name": "全国大学生计算机设计大赛",
        "year": "2024",
        "rank": "国家级二等奖",
        "level": "national",
        "description": "AI图像识别项目，获得评委好评"
    })

    profile_manager.update_test_scores("demo_student", {
        "toefl": 102,
        "gre": 318
    })

    profile_manager.track_school("demo_student", "清华大学", "目标冲刺学校，AI方向强")
    profile_manager.track_school("demo_student", "上海交通大学", "匹配学校，机器学习研究强")

    print("\n第二步：档案信息概览")
    print("-" * 40)
    profile_summary = profile_manager.export_profile_summary("demo_student")
    print(profile_summary)

    print("\n第三步：网络信息搜索")
    print("-" * 40)

    # 搜索学校排名
    rankings = web_searcher.search_school_rankings("CS")
    print("CS专业院校排名:")
    for tier, schools in rankings['rankings'].items():
        print(f"  {tier.upper()}:")
        for school in schools[:3]:  # 显示前3所
            print(f"    - {school['name']} ({school['difficulty']})")

    # 搜索夏令营信息
    camps = web_searcher.search_summer_camps("CS")
    print(f"\n夏令营信息 (显示3个):")
    for camp in camps[:3]:
        print(f"  - {camp['university']}: {camp['program']}")
        print(f"    截止日期: {camp['deadline']}")
        print(f"    研究领域: {', '.join(camp['research_areas'][:2])}")

    # 搜索经验分享
    experiences = web_searcher.search_experience_posts("CS")
    print(f"\n申请经验分享 (显示2个):")
    for exp in experiences[:2]:
        print(f"  - {exp['title']}")
        print(f"    背景: {exp['background']}")
        print(f"    关键要点: {', '.join(exp['key_points'][:2])}")

    print("\n第四步：智能推荐")
    print("-" * 40)

    # 加载完整档案进行推荐
    full_profile = profile_manager.load_profile("demo_student")

    if full_profile:
        # 获取学校推荐
        recommendations = recommender.get_recommendations(full_profile)

        print("个性化学校推荐:")
        for category, schools in recommendations['recommendations'].items():
            print(f"\n  {category.upper()} 学校:")
            for school in schools:
                print(f"    - {school['school']}")
                print(f"      匹配度: {school['match_score']:.1f}/100")
                print(f"      研究优势: {', '.join(school['research_strengths'][:2])}")
                print(f"      录取率: {school['acceptance_rate']*100:.1f}%")

        # 获取研究组推荐
        research_groups = recommender.get_research_group_recommendations(full_profile)
        print(f"\n研究组推荐 (显示3个):")
        for group in research_groups[:3]:
            print(f"  - {group['school']} - {group['group_name']}")
            print(f"    教授: {', '.join(group['professors'][:2])}")
            print(f"    研究方向: {', '.join(group['research_areas'][:3])}")

        # 生成申请策略
        strategy = recommender.generate_application_strategy(full_profile)
        print(f"\n申请策略建议:")
        print(f"  目标学校分布: {strategy['target_schools']}")
        print(f"  优先级行动:")
        for action in strategy['priority_actions']:
            print(f"    - {action}")

        print(f"  需要改进的领域:")
        for area in strategy['improvement_areas']:
            print(f"    - {area}")

    print("\n第五步：竞争力分析")
    print("-" * 40)

    if full_profile:
        analysis = web_searcher.get_competitive_analysis(full_profile)
        print(f"综合竞争力分数: {analysis['total_score']:.0f}/100")
        print(f"竞争力等级: {analysis['level']}")
        print(f"申请建议: {analysis['recommendation']}")
        print(f"\n评分因素:")
        for factor in analysis['factors']:
            print(f"  - {factor}")

    print("\n" + "=" * 60)
    print("演示完成！研究生申请咨询技能已全部展示")
    print("\n这个技能可以帮助学生：")
    print("- 管理个人申请档案")
    print("- 搜索学校信息和申请经验")
    print("- 获得个性化学校推荐")
    print("- 发现匹配的研究组和导师")
    print("- 分析竞争力并制定策略")
    print("- 跟踪重要时间节点")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()
