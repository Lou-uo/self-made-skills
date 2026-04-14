---
name: graduate-school-counselor
description: Provide comprehensive graduate school recommendation and counseling services for undergraduate students. Use this skill when users want to get personalized school recommendations, find relevant research groups, search for graduate school experience posts, check latest program information (like summer camps), and manage their graduate school application profile.
---

# Graduate School Counselor

A comprehensive skill for undergraduate students seeking graduate school recommendations and application guidance.

## What This Skill Does

This skill helps undergraduate students with:
- **Personalized School Recommendations**: Based on academic background, research interests, and career goals
- **Research Group Matching**: Find relevant labs and professors at target schools
- **Experience Sharing**: Search and analyze graduate school application experiences
- **Program Updates**: Monitor latest information about summer camps, application deadlines
- **Application Profile Management**: Track and optimize application materials

## Usage Scenarios

This skill activates when users:
- Share their academic background and want school recommendations
- Ask about specific schools or research groups
- Want to find graduate school application experiences
- Need to track application deadlines and program updates
- Seek advice on application materials and strategies

## Core Features

### 1. Profile Management
- Academic background (GPA, major, courses)
- Research experience and publications
- Competition awards and achievements
- Language test scores (TOEFL, IELTS, GRE)
- Research interests and career goals

### 2. School & Program Recommendations
- Tier-based school suggestions (reach, match, safety)
- Research group matching by interest areas
- Admission statistics and requirements
- Alumni network and placement data

### 3. Information Gathering
- Web search for latest program information
- Experience post analysis from forums
- Admission trend analysis
- Deadline tracking

### 4. Application Support
- Timeline planning
- Document review guidance
- Interview preparation
- Decision making assistance

## Commands

### Create/Update Profile
```
/update-profile [academic_info] [research_experience] [interests]
```

### Get Recommendations
```
/recommend-schools [criteria]
/recommend-research-groups [field]
```

### Search Information
```
/search-experiences [school/program]
/check-deadlines [school]
/find-summer-camps [major]
```

### Track Updates
```
/track-school [school_name]
/get-latest-news [program]
```

## Data Sources

This skill integrates information from:
- University official websites
- Graduate school forums and communities
- Application experience sharing platforms
- Academic ranking systems
- Alumni networks

## Privacy & Security

- All profile data remains local and secure
- Web searches are anonymized
- No personal information shared externally
- Users control what information to store

## Examples

### Profile Creation
**User**: "I'm a Computer Science major with 3.7 GPA, have research experience in machine learning, participated in ACM competitions, and want to pursue AI research in grad school."

**Skill creates**:
```json
{
  "academic_profile": {
    "major": "Computer Science",
    "gpa": 3.7,
    "research_areas": ["Machine Learning", "AI"],
    "competitions": ["ACM"],
    "goals": "AI research"
  }
}
```

### School Recommendations
**User**: "Based on my profile, what schools should I consider for AI research?"

**Skill provides**:
- Reach schools: MIT CSAIL, Stanford AI Lab, CMU ML Department
- Match schools: University of Washington, UC Berkeley, Cornell Tech
- Safety schools: University of Illinois, University of Texas Austin
- Each with specific research groups and professor recommendations

### Experience Analysis
**User**: "Show me recent application experiences for Stanford CS PhD"

**Skill searches** and analyzes:
- Recent admit profiles and their backgrounds
- Common success factors
- Timeline and preparation strategies
- Interview experiences and tips

Let's work together to navigate your graduate school journey! 🎓
