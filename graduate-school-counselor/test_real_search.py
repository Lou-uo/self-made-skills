#!/usr/bin/env python3
"""
Test script for real web search functionality
"""

from scripts.real_web_search import RealGradSchoolWebSearch

def test_real_search():
    """Test the real web search functionality."""
    print("=== 真实网络搜索功能测试 ===")

    searcher = RealGradSchoolWebSearch()

    # 测试排名搜索
    print("\n1. 获取CS专业排名信息:")
    rankings = searcher.search_school_rankings_real("CS")
    print(f"来源: {rankings.get('source', '未知')}")

    if rankings.get('rankings'):
        for tier, schools in rankings['rankings'].items():
            print(f"\n{tier}:")
            for school in schools[:2]:  # 显示前2所
                print(f"  - {school['name']}: {school['difficulty']}")
                print(f"    要求: {school.get('requirements', 'N/A')}")

    # 测试夏令营搜索
    print("\n2. 获取夏令营最新信息:")
    camps = searcher.search_summer_camps_real("CS")
    for camp in camps[:2]:
        print(f"  - {camp['university']}: {camp['program_name']}")
        print(f"    报名截止: {camp['application_deadline']}")
        print(f"    研究领域: {', '.join(camp['research_areas'][:2])}")

    # 测试经验分享搜索
    print("\n3. 获取申请经验:")
    experiences = searcher.search_experience_posts_real("CS")
    for exp in experiences[:1]:
        print(f"  - {exp['title']}")
        print(f"    背景: {exp['background']['undergraduate']}, GPA {exp['background']['gpa']}")
        print(f"    成功因素: {', '.join(exp['success_factors'][:2])}")

    # 测试项目信息搜索
    print("\n4. 获取具体项目信息:")
    program_info = searcher.search_program_info_real("清华大学", "phd")
    if program_info.get('programs'):
        program = program_info['programs'][0]
        print(f"  - {program['program_name']}")
        print(f"    研究方向: {', '.join(program['research_areas'][:3])}")
        print(f"    录取要求: {len(program['admission_requirements'])}项")

    print("\n真实网络搜索测试完成!")

if __name__ == "__main__":
    test_real_search()
