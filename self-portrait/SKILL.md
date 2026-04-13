---
name: self-portrait
description: Create and maintain user self-portrait profiles based on conversation history and user interactions. Use this skill whenever the user wants to build, update, or reference their personal profile, preferences, work style, or any aspect of their digital identity. This skill helps capture and organize user characteristics for better personalization.
---

# Self-Portrait Skill

A skill for creating and maintaining comprehensive user self-portrait profiles based on conversation history, preferences, and interaction patterns.

## What is a Self-Portrait?

A self-portrait is a structured representation of user characteristics including:
- Personal preferences and interests
- Work style and communication patterns
- Technical expertise and experience level
- Goals and objectives
- Learning style and pace preferences
- Decision-making approaches

## Usage

This skill triggers when users want to:
- Create their initial self-portrait profile
- Update existing profile information
- Reference their documented preferences
- Understand their interaction patterns with Claude
- Set up personalized assistance parameters

## Profile Structure

Self-portrait profiles contain the following sections:

### 1. Basic Information
- Role/Position
- Experience Level
- Primary Goals
- Communication Preferences

### 2. Technical Profile
- Programming Languages & Frameworks
- Tools & Technologies
- Skill Level Assessments
- Learning Preferences

### 3. Work Style
- Problem-solving Approach
- Preferred Explanation Depth
- Code Review Style
- Collaboration Preferences

### 4. Interaction Patterns
- Feedback Style
- Question Patterns
- Success Criteria
- Common Request Types

### 5. Preferences
- Documentation Style
- Code Organization
- Naming Conventions
- Architecture Preferences

## Commands

### Create New Profile
```
/create-profile [role] [experience-level] [primary-goals]
```

### Update Profile Section
```
/update-profile [section] [updates...]
```

### View Profile
```
/view-profile [section]
```

### Add Interaction Example
```
/add-example [category] [description]
```

### Generate Insights
```
/generate-insights [focus-area]
```

## Profile Storage

Profiles are stored in the user's workspace and can be:
- Exported as JSON for backup
- Imported from previous sessions
- Shared across different Claude instances
- Version controlled alongside project code

## Examples

### Creating a New Profile
**User:** "I'm a senior software engineer with 8 years of experience in React and Node.js. I'm working on improving my system design skills and prefer detailed explanations with practical examples."

**Skill creates:**
```json
{
  "basic_info": {
    "role": "Senior Software Engineer",
    "experience_years": 8,
    "primary_technologies": ["React", "Node.js"],
    "focus_areas": ["System Design"],
    "explanation_preference": "detailed_with_examples"
  }
}
```

### Updating Technical Skills
**User:** "Add Python and Docker to my technical skills, and I'm also learning GraphQL."

**Skill updates:**
```json
{
  "technical_profile": {
    "programming_languages": ["JavaScript", "Python"],
    "frameworks": ["React", "Node.js"],
    "tools": ["Docker"],
    "learning": ["GraphQL"]
  }
}
```

### Adding Work Style Preferences
**User:** "I prefer to see the big picture first, then dive into details. When reviewing code, I focus on maintainability and performance."

**Skill updates:**
```json
{
  "work_style": {
    "approach": "top-down",
    "explanation_flow": "big_picture_first",
    "code_review_focus": ["maintainability", "performance"]
  }
}
```

## Best Practices

1. **Be Specific**: Provide concrete examples and details
2. **Update Regularly**: Keep your profile current as you grow
3. **Include Examples**: Share actual interaction patterns
4. **Set Preferences**: Define your ideal assistance style
5. **Review Periodically**: Check and refine your profile monthly

## Integration

This skill integrates with other Claude Code features:
- **Memory System**: References stored user information
- **Project Context**: Considers current work and goals
- **Interaction History**: Analyzes past conversations
- **Skill Recommendations**: Suggests relevant skills based on profile

## Privacy & Security

- All profile data stays local to your workspace
- No personal information is transmitted externally
- You control what information is stored and shared
- Profiles can be encrypted or excluded from backups

Start building your self-portrait to get more personalized and effective assistance from Claude!
