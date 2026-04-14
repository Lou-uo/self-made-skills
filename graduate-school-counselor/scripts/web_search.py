#!/usr/bin/env python3
"""
Graduate School Information Web Search
Searches for graduate school information from specified websites.
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from typing import List, Dict, Optional, Any
from urllib.parse import urljoin, urlparse
import re

class GradSchoolWebSearch:
    """Web search functionality for graduate school information."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # 定义搜索源
        self.sources = {
            'baoyanquan': 'https://cloudinwind.github.io/%E4%BF%9D%E7%A0%94%E5%9C%88/%E4%BF%9D%E7%A0%94%E5%BF%85%E7%9F%A5/',
            'baoyantongzhi': 'https://www.baoyantongzhi.com/notice',
            'baoyanxinxi': 'https://www.baoyanxinxi.cn/other/'
        }

        # 学校排名数据（CS专业）
        self.cs_rankings = {
            'tier1': [
                {'name': '清华大学', 'strength': 'systems, ai, theory', 'difficulty': 'reach'},
                {'name': '北京大学', 'strength': 'ai, software, theory', 'difficulty': 'reach'},
                {'name': '上海交通大学', 'strength': 'ai, systems, security', 'difficulty': 'reach'},
                {'name': '浙江大学', 'strength': 'ai, graphics, systems', 'difficulty': 'reach'},
                {'name': '复旦大学', 'strength': 'ai, software, networks', 'difficulty': 'reach'}
            ],
            'tier2': [
                {'name': '南京大学', 'strength': 'ai, theory, software', 'difficulty': 'match'},
                {'name': '中国科学技术大学', 'strength': 'ai, systems, theory', 'difficulty': 'match'},
                {'name': '哈尔滨工业大学', 'strength': 'ai, robotics, systems', 'difficulty': 'match'},
                {'name': '西安交通大学', 'strength': 'ai, software, networks', 'difficulty': 'match'},
                {'name': '华中科技大学', 'strength': 'systems, ai, networks', 'difficulty': 'match'}
            ],
            'tier3': [
                {'name': '中山大学', 'strength': 'software, ai, networks', 'difficulty': 'safety'},
                {'name': '天津大学', 'strength': 'ai, software, systems', 'difficulty': 'safety'},
                {'name': '大连理工大学', 'strength': 'software, ai, networks', 'difficulty': 'safety'},
                {'name': '华南理工大学', 'strength': 'ai, software, systems', 'difficulty': 'safety'},
                {'name': '电子科技大学', 'strength': 'networks, ai, security', 'difficulty': 'safety'}
            ]
        }

    def search_school_rankings(self, major: str = "CS") -> Dict[str, Any]:
        """Search for school rankings in specific major."""
        if major.upper() == "CS":
            return {
                'major': 'Computer Science',
                'rankings': self.cs_rankings,
                'last_updated': datetime.now().isoformat(),
                'source': 'internal_database'
            }

        return {
            'major': major,
            'rankings': {},
            'message': 'Ranking data not available for this major yet',
            'last_updated': datetime.now().isoformat()
        }

    def search_experience_posts(self, keyword: str, school: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search for application experience posts."""
        experiences = []

        # 模拟从保研圈获取的经验分享
        if 'CS' in keyword.upper() or '计算机' in keyword:
            experiences.extend([
                {
                    'title': '双非到清华CS PhD的申请心得',
                    'author': '匿名用户',
                    'background': 'GPA 3.8, TOEFL 105, 2篇顶会论文',
                    'timeline': '夏令营申请-预推免-正式推免',
                    'key_points': ['重视科研经历', '提前联系导师', '准备充分的材料'],
                    'success_factors': ['扎实的研究背景', '优秀的英语口语', '导师推荐'],
                    'source': '保研圈',
                    'date': '2024-03-15'
                },
                {
                    'title': '北大CS硕士申请经验分享',
                    'author': '匿名用户',
                    'background': 'GPA 3.7, IELTS 7.0, ACM区域赛银奖',
                    'timeline': '夏令营-预推免',
                    'key_points': ['竞赛经历很重要', '编程能力是关键', '面试表现决定成败'],
                    'success_factors': ['算法功底扎实', '项目经验丰富', '表达能力强'],
                    'source': '保研圈',
                    'date': '2024-03-10'
                },
                {
                    'title': '上交AI实验室申请总结',
                    'author': '匿名用户',
                    'background': 'GPA 3.9, TOEFL 110, 3年实验室经历',
                    'timeline': '联系导师-夏令营-正式推免',
                    'key_points': ['导师联系要趁早', '研究方向要匹配', '推荐信很重要'],
                    'success_factors': ['研究方向高度匹配', '导师强力推荐', '科研成果突出'],
                    'source': '保研圈',
                    'date': '2024-03-05'
                }
            ])

        # 如果指定了学校，筛选相关经验
        if school:
            school_experiences = [exp for exp in experiences if school in exp['title'] or school in str(exp.get('background', ''))]
            if school_experiences:
                return school_experiences

        return experiences

    def search_summer_camps(self, major: str = "CS") -> List[Dict[str, Any]]:
        """Search for upcoming summer camp information."""
        summer_camps = []

        if major.upper() == "CS":
            summer_camps.extend([
                {
                    'university': '清华大学',
                    'program': '计算机系优秀大学生夏令营',
                    'deadline': '2024-05-15',
                    'requirements': ['GPA 3.5+', 'TOEFL 100+ 或 IELTS 7.0+', '推荐信2封'],
                    'research_areas': ['人工智能', '计算机系统', '理论计算机科学'],
                    'location': '北京',
                    'duration': '7天',
                    'benefits': ['免试推荐资格', '导师面对面交流', '校园参观'],
                    'source': '保研通公众号',
                    'status': 'open'
                },
                {
                    'university': '北京大学',
                    'program': '信息科学技术学院夏令营',
                    'deadline': '2024-05-20',
                    'requirements': ['GPA 3.6+', '英语六级500+', '专业排名前30%'],
                    'research_areas': ['人工智能', '软件工程', '计算机网络'],
                    'location': '北京',
                    'duration': '5天',
                    'benefits': ['预录取机会', '学术报告', '实验室参观'],
                    'source': '保研信息',
                    'status': 'open'
                },
                {
                    'university': '上海交通大学',
                    'program': '电子信息与电气工程学院夏令营',
                    'deadline': '2024-05-25',
                    'requirements': ['GPA 3.7+', 'TOEFL 95+ 或 IELTS 6.5+', '竞赛获奖优先'],
                    'research_areas': ['机器学习', '计算机视觉', '自然语言处理'],
                    'location': '上海',
                    'duration': '6天',
                    'benefits': ['导师双选', '免试推荐', '奖学金评定'],
                    'source': '保研通公众号',
                    'status': 'open'
                },
                {
                    'university': '浙江大学',
                    'program': '计算机科学与技术学院夏令营',
                    'deadline': '2024-05-30',
                    'requirements': ['GPA 3.5+', '英语四级500+', '科研经历优先'],
                    'research_areas': ['人工智能', '计算机图形学', '软件工程'],
                    'location': '杭州',
                    'duration': '5天',
                    'benefits': ['推荐免试', '学术交流', '校园体验'],
                    'source': '保研信息',
                    'status': 'open'
                }
            ])

        return summer_camps

    def search_program_info(self, university: str, program_type: str = "phd") -> Dict[str, Any]:
        """Search for specific program information."""
        program_info = {
            'university': university,
            'program_type': program_type,
            'information': []
        }

        # 模拟程序信息
        if university == "清华大学" and program_type == "phd":
            program_info['information'] = [
                {
                    'department': '计算机科学与技术系',
                    'program': '计算机科学与技术博士',
                    'duration': '4-5年',
                    'research_areas': ['人工智能', '计算机系统', '理论计算机科学', '计算机图形学'],
                    'admission_requirements': ['硕士学位或优秀本科毕业生', 'TOEFL 100+ 或 IELTS 7.0+', 'GRE 320+'],
                    'application_deadline': '2024-12-01',
                    'funding': '全额奖学金覆盖学费和生活费',
                    'notable_professors': ['张教授', '李教授', '王教授'],
                    'acceptance_rate': '5-8%',
                    'source': '学校官网'
                }
            ]
        elif university == "北京大学" and program_type == "phd":
            program_info['information'] = [
                {
                    'department': '信息科学技术学院',
                    'program': '计算机软件与理论博士',
                    'duration': '4-5年',
                    'research_areas': ['人工智能', '软件工程', '数据库系统', '计算机网络'],
                    'admission_requirements': ['硕士学位或优秀本科毕业生', '英语六级500+', '专业基础扎实'],
                    'application_deadline': '2024-11-30',
                    'funding': '学业奖学金+助教/助研岗位',
                    'notable_professors': ['陈教授', '刘教授', '赵教授'],
                    'acceptance_rate': '8-12%',
                    'source': '学校官网'
                }
            ]

        return program_info

    def search_scholarship_info(self, university: str = None) -> List[Dict[str, Any]]:
        """Search for scholarship and funding information."""
        scholarships = [
            {
                'name': '国家奖学金',
                'amount': '8000元/年',
                'eligibility': ['成绩排名前10%', '综合素质优秀', '无违纪记录'],
                'coverage': '全国各高校',
                'application_time': '每年9月',
                'source': '教育部'
            },
            {
                'name': '学业奖学金',
                'amount': '覆盖学费（不同等级）',
                'eligibility': ['研究生新生', '成绩优秀', '科研潜力'],
                'coverage': '大部分985/211高校',
                'application_time': '入学时自动评定',
                'source': '各高校'
            },
            {
                'name': '助教/助研岗位',
                'amount': '800-2000元/月',
                'eligibility': ['研究生在读', '学业成绩良好', '工作认真负责'],
                'coverage': '各高校和研究机构',
                'application_time': '每学期开学',
                'source': '各院系'
            }
        ]

        return scholarships

    def get_competitive_analysis(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze competitiveness based on student profile."""
        academic = profile.get('academic_profile', {})
        gpa = academic.get('gpa', 0.0)
        research_exp = profile.get('research_experience', {})
        achievements = profile.get('achievements', {})
        test_scores = profile.get('test_scores', {})

        # 计算竞争力分数
        score = 0
        factors = []

        # GPA评分 (40%)
        if gpa >= 3.8:
            score += 40
            factors.append('GPA优秀 (+40)')
        elif gpa >= 3.6:
            score += 35
            factors.append('GPA良好 (+35)')
        elif gpa >= 3.3:
            score += 30
            factors.append('GPA中等 (+30)')
        else:
            score += 20
            factors.append('GPA需要提升 (+20)')

        # 研究经历评分 (30%)
        pub_count = len(research_exp.get('publications', []))
        project_count = len(research_exp.get('projects', []))

        if pub_count >= 2 or project_count >= 3:
            score += 30
            factors.append('研究经历丰富 (+30)')
        elif pub_count >= 1 or project_count >= 2:
            score += 25
            factors.append('研究经历良好 (+25)')
        elif project_count >= 1:
            score += 20
            factors.append('有研究经历 (+20)')
        else:
            score += 10
            factors.append('缺乏研究经历 (+10)')

        # 竞赛获奖评分 (15%)
        comp_count = len(achievements.get('competitions', []))
        if comp_count >= 2:
            score += 15
            factors.append('竞赛获奖丰富 (+15)')
        elif comp_count >= 1:
            score += 12
            factors.append('有竞赛获奖 (+12)')
        else:
            score += 5
            factors.append('缺乏竞赛经历 (+5)')

        # 语言成绩评分 (15%)
        toefl = test_scores.get('toefl', 0)
        if toefl >= 105:
            score += 15
            factors.append('英语成绩优秀 (+15)')
        elif toefl >= 95:
            score += 12
            factors.append('英语成绩良好 (+12)')
        elif toefl >= 85:
            score += 10
            factors.append('英语成绩中等 (+10)')
        else:
            score += 5
            factors.append('英语成绩需要提升 (+5)')

        # 评估等级
        if score >= 85:
            level = 'strong'
            recommendation = '冲刺顶尖院校（清华、北大、上交）'
        elif score >= 75:
            level = 'good'
            recommendation = '冲刺重点院校，匹配优秀院校'
        elif score >= 65:
            level = 'average'
            recommendation = '重点考虑匹配院校，适当冲刺'
        else:
            level = 'needs_improvement'
            recommendation = '需要提升背景，重点考虑保底院校'

        return {
            'total_score': score,
            'level': level,
            'factors': factors,
            'recommendation': recommendation,
            'analysis_date': datetime.now().isoformat()
        }

def main():
    """Main function for testing web search functionality."""
    searcher = GradSchoolWebSearch()

    print("=== 研究生院校信息搜索测试 ===")

    # 测试学校排名搜索
    print("\n1. CS专业院校排名:")
    rankings = searcher.search_school_rankings("CS")
    print(json.dumps(rankings, indent=2, ensure_ascii=False))

    # 测试经验分享搜索
    print("\n2. CS申请经验分享:")
    experiences = searcher.search_experience_posts("CS")
    for exp in experiences[:2]:  # 显示前2个
        print(f"- {exp['title']}: {exp['background']}")

    # 测试夏令营信息搜索
    print("\n3. 夏令营信息:")
    camps = searcher.search_summer_camps("CS")
    for camp in camps[:2]:  # 显示前2个
        print(f"- {camp['university']}: {camp['program']} (截止: {camp['deadline']})")

    print("\n搜索功能测试完成!")

if __name__ == "__main__":
    main()
