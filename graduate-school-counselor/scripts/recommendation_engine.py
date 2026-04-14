#!/usr/bin/env python3
"""
Graduate School Recommendation Engine
Provides intelligent school and program recommendations based on student profiles.
"""

import json
import math
from typing import List, Dict, Any, Tuple
from datetime import datetime

class RecommendationEngine:
    """Intelligent recommendation system for graduate schools."""

    def __init__(self):
        # 学校数据库（CS专业）
        self.schools_db = {
            '清华大学': {
                'tier': 'tier1',
                'difficulty': 'reach',
                'min_gpa': 3.8,
                'min_toefl': 105,
                'min_gre': 325,
                'research_strengths': ['人工智能', '计算机系统', '理论计算机科学'],
                'acceptance_rate': 0.06,
                'funding_availability': 'high',
                'location': '北京'
            },
            '北京大学': {
                'tier': 'tier1',
                'difficulty': 'reach',
                'min_gpa': 3.7,
                'min_toefl': 100,
                'min_gre': 320,
                'research_strengths': ['人工智能', '软件工程', '理论计算机科学'],
                'acceptance_rate': 0.08,
                'funding_availability': 'high',
                'location': '北京'
            },
            '上海交通大学': {
                'tier': 'tier1',
                'difficulty': 'reach',
                'min_gpa': 3.7,
                'min_toefl': 100,
                'min_gre': 320,
                'research_strengths': ['机器学习', '计算机视觉', '分布式系统'],
                'acceptance_rate': 0.07,
                'funding_availability': 'high',
                'location': '上海'
            },
            '浙江大学': {
                'tier': 'tier1',
                'difficulty': 'reach',
                'min_gpa': 3.6,
                'min_toefl': 95,
                'min_gre': 315,
                'research_strengths': ['人工智能', '计算机图形学', '软件工程'],
                'acceptance_rate': 0.09,
                'funding_availability': 'high',
                'location': '杭州'
            },
            '复旦大学': {
                'tier': 'tier1',
                'difficulty': 'reach',
                'min_gpa': 3.6,
                'min_toefl': 95,
                'min_gre': 315,
                'research_strengths': ['人工智能', '数据科学', '网络安全'],
                'acceptance_rate': 0.08,
                'funding_availability': 'high',
                'location': '上海'
            },
            '南京大学': {
                'tier': 'tier2',
                'difficulty': 'match',
                'min_gpa': 3.5,
                'min_toefl': 95,
                'min_gre': 315,
                'research_strengths': ['人工智能', '理论计算机科学', '软件工程'],
                'acceptance_rate': 0.12,
                'funding_availability': 'medium',
                'location': '南京'
            },
            '中国科学技术大学': {
                'tier': 'tier2',
                'difficulty': 'match',
                'min_gpa': 3.5,
                'min_toefl': 90,
                'min_gre': 310,
                'research_strengths': ['人工智能', '量子计算', '理论计算机科学'],
                'acceptance_rate': 0.15,
                'funding_availability': 'medium',
                'location': '合肥'
            },
            '哈尔滨工业大学': {
                'tier': 'tier2',
                'difficulty': 'match',
                'min_gpa': 3.4,
                'min_toefl': 90,
                'min_gre': 310,
                'research_strengths': ['人工智能', '机器人学', '计算机系统'],
                'acceptance_rate': 0.13,
                'funding_availability': 'medium',
                'location': '哈尔滨'
            },
            '西安交通大学': {
                'tier': 'tier2',
                'difficulty': 'match',
                'min_gpa': 3.4,
                'min_toefl': 85,
                'min_gre': 305,
                'research_strengths': ['人工智能', '软件工程', '计算机网络'],
                'acceptance_rate': 0.14,
                'funding_availability': 'medium',
                'location': '西安'
            },
            '华中科技大学': {
                'tier': 'tier2',
                'difficulty': 'match',
                'min_gpa': 3.4,
                'min_toefl': 85,
                'min_gre': 305,
                'research_strengths': ['计算机系统', '人工智能', '计算机网络'],
                'acceptance_rate': 0.16,
                'funding_availability': 'medium',
                'location': '武汉'
            },
            '中山大学': {
                'tier': 'tier3',
                'difficulty': 'safety',
                'min_gpa': 3.2,
                'min_toefl': 80,
                'min_gre': 300,
                'research_strengths': ['软件工程', '人工智能', '计算机网络'],
                'acceptance_rate': 0.25,
                'funding_availability': 'medium',
                'location': '广州'
            },
            '天津大学': {
                'tier': 'tier3',
                'difficulty': 'safety',
                'min_gpa': 3.2,
                'min_toefl': 80,
                'min_gre': 300,
                'research_strengths': ['人工智能', '软件工程', '计算机系统'],
                'acceptance_rate': 0.28,
                'funding_availability': 'medium',
                'location': '天津'
            },
            '大连理工大学': {
                'tier': 'tier3',
                'difficulty': 'safety',
                'min_gpa': 3.0,
                'min_toefl': 75,
                'min_gre': 295,
                'research_strengths': ['软件工程', '人工智能', '计算机网络'],
                'acceptance_rate': 0.30,
                'funding_availability': 'medium',
                'location': '大连'
            },
            '华南理工大学': {
                'tier': 'tier3',
                'difficulty': 'safety',
                'min_gpa': 3.0,
                'min_toefl': 75,
                'min_gre': 295,
                'research_strengths': ['人工智能', '软件工程', '计算机系统'],
                'acceptance_rate': 0.32,
                'funding_availability': 'medium',
                'location': '广州'
            },
            '电子科技大学': {
                'tier': 'tier3',
                'difficulty': 'safety',
                'min_gpa': 3.0,
                'min_toefl': 75,
                'min_gre': 295,
                'research_strengths': ['计算机网络', '人工智能', '信息安全'],
                'acceptance_rate': 0.35,
                'funding_availability': 'medium',
                'location': '成都'
            }
        }

    def calculate_match_score(self, profile: Dict[str, Any], school_name: str) -> Tuple[float, Dict[str, Any]]:
        """Calculate how well a student profile matches a school."""
        if school_name not in self.schools_db:
            return 0.0, {}

        school = self.schools_db[school_name]
        academic = profile.get('academic_profile', {})
        test_scores = profile.get('test_scores', {})
        research_exp = profile.get('research_experience', {})
        achievements = profile.get('achievements', {})

        score_details = {}
        total_score = 0.0

        # GPA匹配度 (30%)
        gpa = academic.get('gpa', 0.0)
        min_gpa = school['min_gpa']
        if gpa >= min_gpa:
            gpa_score = 30.0
            score_details['gpa'] = f"GPA达标: {gpa} >= {min_gpa} (+30)"
        elif gpa >= min_gpa - 0.1:
            gpa_score = 25.0
            score_details['gpa'] = f"GPA接近: {gpa} ≈ {min_gpa} (+25)"
        elif gpa >= min_gpa - 0.2:
            gpa_score = 20.0
            score_details['gpa'] = f"GPA略低: {gpa} < {min_gpa} (+20)"
        else:
            gpa_score = 10.0
            score_details['gpa'] = f"GPA偏低: {gpa} << {min_gpa} (+10)"

        total_score += gpa_score

        # 语言成绩匹配度 (20%)
        toefl = test_scores.get('toefl', 0)
        min_toefl = school['min_toefl']
        if toefl >= min_toefl:
            toefl_score = 20.0
            score_details['toefl'] = f"TOEFL达标: {toefl} >= {min_toefl} (+20)"
        elif toefl >= min_toefl - 5:
            toefl_score = 15.0
            score_details['toefl'] = f"TOEFL接近: {toefl} ≈ {min_toefl} (+15)"
        elif toefl >= min_toefl - 10:
            toefl_score = 10.0
            score_details['toefl'] = f"TOEFL略低: {toefl} < {min_toefl} (+10)"
        else:
            toefl_score = 5.0
            score_details['toefl'] = f"TOEFL偏低: {toefl} << {min_toefl} (+5)"

        total_score += toefl_score

        # 研究经历匹配度 (30%)
        research_strengths = school['research_strengths']
        student_interests = academic.get('research_interests', [])

        # 研究方向匹配
        interest_match = len(set(research_strengths) & set(student_interests))
        research_score = min(15.0, interest_match * 5.0)

        # 研究经历丰富度
        pub_count = len(research_exp.get('publications', []))
        project_count = len(research_exp.get('projects', []))
        research_exp_score = min(15.0, (pub_count * 5.0 + project_count * 3.0))

        total_research_score = research_score + research_exp_score
        total_score += total_research_score
        score_details['research'] = f"研究匹配度: {total_research_score:.1f}/30 (方向匹配: {research_score:.1f}, 经历丰富度: {research_exp_score:.1f})"

        # 竞赛获奖加分 (10%)
        comp_count = len(achievements.get('competitions', []))
        award_score = min(10.0, comp_count * 3.0)
        total_score += award_score
        score_details['achievements'] = f"竞赛获奖: {award_score:.1f}/10 ({comp_count}项)"

        # 录取率调整 (10%)
        acceptance_rate = school['acceptance_rate']
        acceptance_score = acceptance_rate * 100  # 将录取率转换为分数
        total_score += acceptance_score
        score_details['acceptance'] = f"录取率调整: {acceptance_score:.1f}/10 ({acceptance_rate*100:.1f}%)"

        return total_score, score_details

    def get_recommendations(self, profile: Dict[str, Any], num_recommendations: int = 10) -> Dict[str, Any]:
        """Get personalized school recommendations."""
        recommendations = []
        academic = profile.get('academic_profile', {})
        research_interests = academic.get('research_interests', [])

        # 计算每个学校的匹配分数
        for school_name, school_info in self.schools_db.items():
            match_score, score_details = self.calculate_match_score(profile, school_name)

            recommendation = {
                'school': school_name,
                'tier': school_info['tier'],
                'difficulty': school_info['difficulty'],
                'match_score': match_score,
                'score_details': score_details,
                'research_strengths': school_info['research_strengths'],
                'location': school_info['location'],
                'acceptance_rate': school_info['acceptance_rate'],
                'funding_availability': school_info['funding_availability']
            }

            recommendations.append(recommendation)

        # 按匹配分数排序
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)

        # 分类推荐
        reach_schools = [r for r in recommendations if r['difficulty'] == 'reach']
        match_schools = [r for r in recommendations if r['difficulty'] == 'match']
        safety_schools = [r for r in recommendations if r['difficulty'] == 'safety']

        # 选择最优推荐组合
        final_recommendations = {
            'reach': reach_schools[:2],  # 2所冲刺学校
            'match': match_schools[:3],  # 3所匹配学校
            'safety': safety_schools[:2]  # 2所保底学校
        }

        return {
            'profile_summary': {
                'major': academic.get('major', 'Unknown'),
                'gpa': academic.get('gpa', 0.0),
                'research_interests': research_interests
            },
            'recommendations': final_recommendations,
            'all_schools': recommendations[:num_recommendations],
            'generation_date': datetime.now().isoformat()
        }

    def get_research_group_recommendations(self, profile: Dict[str, Any], school_name: str = None) -> List[Dict[str, Any]]:
        """Get research group recommendations based on research interests."""
        academic = profile.get('academic_profile', {})
        research_interests = academic.get('research_interests', [])

        # 研究组数据库（示例）
        research_groups = {
            '清华大学': [
                {
                    'group_name': '智能技术与系统国家重点实验室',
                    'professors': ['张钹院士', '朱小燕教授', '马少平教授'],
                    'research_areas': ['人工智能', '机器学习', '自然语言处理'],
                    'notable_achievements': ['多篇顶会论文', '国家科技进步奖'],
                    'lab_size': 'large',
                    'funding_status': 'well_funded'
                },
                {
                    'group_name': '计算机网络技术研究所',
                    'professors': ['吴建平院士', '李星教授'],
                    'research_areas': ['计算机网络', '互联网体系结构', '网络安全'],
                    'notable_achievements': ['下一代互联网技术', '国际标准制定'],
                    'lab_size': 'large',
                    'funding_status': 'well_funded'
                }
            ],
            '北京大学': [
                {
                    'group_name': '计算语言学研究所',
                    'professors': ['王厚峰教授', '常宝宝教授'],
                    'research_areas': ['自然语言处理', '机器翻译', '信息抽取'],
                    'notable_achievements': ['多个NLP工具包', '工业界合作项目'],
                    'lab_size': 'medium',
                    'funding_status': 'well_funded'
                },
                {
                    'group_name': '软件工程研究所',
                    'professors': ['金芝教授', '孙艳春教授'],
                    'research_areas': ['软件工程', '程序分析', '软件测试'],
                    'notable_achievements': ['自动化测试工具', '工业合作项目'],
                    'lab_size': 'medium',
                    'funding_status': 'well_funded'
                }
            ],
            '上海交通大学': [
                {
                    'group_name': '机器学习研究中心',
                    'professors': ['俞凯教授', '张伟楠教授'],
                    'research_areas': ['机器学习', '语音识别', '自然语言处理'],
                    'notable_achievements': ['语音技术产业化', '多个创业公司'],
                    'lab_size': 'large',
                    'funding_status': 'well_funded'
                }
            ]
        }

        # 如果没有指定学校，返回所有相关研究组
        if not school_name:
            all_groups = []
            for school, groups in research_groups.items():
                for group in groups:
                    # 计算研究方向匹配度
                    group_areas = set(group['research_areas'])
                    student_areas = set(research_interests)
                    match_score = len(group_areas & student_areas) / len(group_areas) if group_areas else 0

                    if match_score > 0:  # 有匹配的研究方向
                        group['match_score'] = match_score
                        group['school'] = school
                        all_groups.append(group)

            # 按匹配度排序
            all_groups.sort(key=lambda x: x['match_score'], reverse=True)
            return all_groups[:10]  # 返回前10个最匹配的

        # 如果指定了学校，只返回该学校的研究组
        if school_name in research_groups:
            return research_groups[school_name]

        return []

    def generate_application_strategy(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate personalized application strategy."""
        academic = profile.get('academic_profile', {})
        gpa = academic.get('gpa', 0.0)
        research_exp = profile.get('research_experience', {})
        test_scores = profile.get('test_scores', {})

        strategy = {
            'timeline': [],
            'priority_actions': [],
            'target_schools': {},
            'improvement_areas': []
        }

        # 时间线规划
        strategy['timeline'] = [
            {'phase': '准备阶段（现在-5月）', 'tasks': ['提升GPA', '准备语言考试', '积累科研经历', '联系推荐人']},
            {'phase': '申请阶段（6-9月）', 'tasks': ['夏令营申请', '准备申请材料', '联系导师', '完成语言考试']},
            {'phase': '冲刺阶段（10-12月）', 'tasks': ['正式推免申请', '面试准备', '材料完善', '导师沟通']},
            {'phase': '决定阶段（次年3-5月）', 'tasks': ['录取结果确认', '学校选择', '入学准备']}
        ]

        # 根据背景确定优先级
        if gpa < 3.5:
            strategy['priority_actions'].append('重点提升GPA至3.5+')

        toefl = test_scores.get('toefl', 0)
        if toefl < 100:
            strategy['priority_actions'].append('TOEFL目标100+')

        pub_count = len(research_exp.get('publications', []))
        if pub_count == 0:
            strategy['priority_actions'].append('积累科研经历，争取发表论文')

        # 确定目标学校策略
        if gpa >= 3.8 and toefl >= 105:
            strategy['target_schools'] = {'reach': 2, 'match': 3, 'safety': 1}
        elif gpa >= 3.6 and toefl >= 95:
            strategy['target_schools'] = {'reach': 1, 'match': 3, 'safety': 2}
        else:
            strategy['target_schools'] = {'reach': 1, 'match': 2, 'safety': 3}

        # 改进建议
        if gpa < 3.6:
            strategy['improvement_areas'].append('GPA提升计划')
        if toefl < 100:
            strategy['improvement_areas'].append('语言成绩提升')
        if len(research_exp.get('projects', [])) < 2:
            strategy['improvement_areas'].append('丰富科研经历')

        return strategy

def main():
    """Test the recommendation engine."""
    engine = RecommendationEngine()

    # 示例学生档案
    sample_profile = {
        'academic_profile': {
            'major': 'Computer Science',
            'gpa': 3.8,
            'research_interests': ['Machine Learning', 'Artificial Intelligence']
        },
        'test_scores': {
            'toefl': 105,
            'gre': 325
        },
        'research_experience': {
            'publications': [],
            'projects': ['Deep Learning Image Recognition']
        },
        'achievements': {
            'competitions': ['ACM-ICPC Regional Silver']
        }
    }

    print("=== 推荐引擎测试 ===")

    # 测试学校推荐
    recommendations = engine.get_recommendations(sample_profile)
    print(f"\n学校推荐结果:")
    for category, schools in recommendations['recommendations'].items():
        print(f"\n{category.upper()} Schools:")
        for school in schools:
            print(f"  - {school['school']}: {school['match_score']:.1f}/100")

    # 测试研究组推荐
    research_groups = engine.get_research_group_recommendations(sample_profile)
    print(f"\n研究组推荐 (前5个):")
    for group in research_groups[:5]:
        print(f"  - {group['school']} - {group['group_name']}")
        print(f"    研究方向: {', '.join(group['research_areas'])}")

    print("\n推荐引擎测试完成!")

if __name__ == "__main__":
    main()
