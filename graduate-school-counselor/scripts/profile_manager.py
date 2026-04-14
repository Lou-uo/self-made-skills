#!/usr/bin/env python3
"""
Graduate School Application Profile Manager
Manages student profiles for graduate school counseling.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

class GradSchoolProfileManager:
    """Manages graduate school application profiles."""

    def __init__(self, workspace_path: str = "."):
        self.workspace_path = Path(workspace_path)
        self.profiles_dir = self.workspace_path / "data" / "profiles"
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.schools_dir = self.workspace_path / "data" / "schools"
        self.schools_dir.mkdir(parents=True, exist_ok=True)

    def create_profile(self, student_id: str, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new graduate school application profile."""
        profile = {
            "student_id": student_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "version": "1.0",
            "academic_profile": {
                "major": initial_data.get("major", ""),
                "university": initial_data.get("university", ""),
                "gpa": initial_data.get("gpa", 0.0),
                "major_gpa": initial_data.get("major_gpa", 0.0),
                "rank": initial_data.get("rank", ""),
                "courses": initial_data.get("courses", []),
                "research_interests": initial_data.get("research_interests", [])
            },
            "research_experience": {
                "publications": [],
                "conferences": [],
                "projects": [],
                "internships": [],
                "lab_experience": []
            },
            "achievements": {
                "competitions": [],
                "awards": [],
                "scholarships": [],
                "certifications": []
            },
            "test_scores": {
                "toefl": initial_data.get("toefl", 0),
                "ielts": initial_data.get("ielts", 0),
                "gre": initial_data.get("gre", 0),
                "sub_gre": initial_data.get("sub_gre", "")
            },
            "target_programs": {
                "phd_programs": [],
                "master_programs": [],
                "research_areas": [],
                "career_goals": ""
            },
            "application_timeline": {
                "summer_camps": [],
                "application_deadlines": [],
                "interview_schedule": []
            },
            "tracked_schools": [],
            "notes": ""
        }

        # Add any additional initial data
        if "additional_info" in initial_data:
            profile.update(initial_data["additional_info"])

        return self.save_profile(student_id, profile)

    def load_profile(self, student_id: str) -> Optional[Dict[str, Any]]:
        """Load an existing profile."""
        profile_path = self.profiles_dir / f"{student_id}.json"
        if profile_path.exists():
            with open(profile_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def save_profile(self, student_id: str, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Save profile to file."""
        profile["updated_at"] = datetime.now().isoformat()
        profile_path = self.profiles_dir / f"{student_id}.json"

        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)

        return profile

    def update_academic_info(self, student_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update academic information."""
        profile = self.load_profile(student_id)
        if not profile:
            raise ValueError(f"Profile for student {student_id} not found")

        profile["academic_profile"].update(updates)
        return self.save_profile(student_id, profile)

    def add_research_experience(self, student_id: str, experience_type: str, experience: Dict[str, Any]) -> Dict[str, Any]:
        """Add research experience."""
        profile = self.load_profile(student_id)
        if not profile:
            raise ValueError(f"Profile for student {student_id} not found")

        if experience_type in profile["research_experience"]:
            experience["added_at"] = datetime.now().isoformat()
            profile["research_experience"][experience_type].append(experience)
        else:
            profile["research_experience"][experience_type] = [experience]

        return self.save_profile(student_id, profile)

    def add_achievement(self, student_id: str, achievement_type: str, achievement: Dict[str, Any]) -> Dict[str, Any]:
        """Add achievement or award."""
        profile = self.load_profile(student_id)
        if not profile:
            raise ValueError(f"Profile for student {student_id} not found")

        if achievement_type in profile["achievements"]:
            achievement["added_at"] = datetime.now().isoformat()
            profile["achievements"][achievement_type].append(achievement)
        else:
            profile["achievements"][achievement_type] = [achievement]

        return self.save_profile(student_id, profile)

    def update_test_scores(self, student_id: str, scores: Dict[str, Any]) -> Dict[str, Any]:
        """Update test scores."""
        profile = self.load_profile(student_id)
        if not profile:
            raise ValueError(f"Profile for student {student_id} not found")

        profile["test_scores"].update(scores)
        return self.save_profile(student_id, profile)

    def add_target_program(self, student_id: str, program_type: str, program: Dict[str, Any]) -> Dict[str, Any]:
        """Add target program."""
        profile = self.load_profile(student_id)
        if not profile:
            raise ValueError(f"Profile for student {student_id} not found")

        if program_type in profile["target_programs"]:
            program["added_at"] = datetime.now().isoformat()
            profile["target_programs"][program_type].append(program)
        else:
            profile["target_programs"][program_type] = [program]

        return self.save_profile(student_id, profile)

    def track_school(self, student_id: str, school_name: str, notes: str = "") -> Dict[str, Any]:
        """Add school to tracking list."""
        profile = self.load_profile(student_id)
        if not profile:
            raise ValueError(f"Profile for student {student_id} not found")

        school_entry = {
            "name": school_name,
            "notes": notes,
            "added_at": datetime.now().isoformat()
        }

        # Avoid duplicates
        existing_schools = [s["name"] for s in profile["tracked_schools"]]
        if school_name not in existing_schools:
            profile["tracked_schools"].append(school_entry)

        return self.save_profile(student_id, profile)

    def export_profile_summary(self, student_id: str) -> str:
        """Export profile as readable summary."""
        profile = self.load_profile(student_id)
        if not profile:
            return f"Profile for student {student_id} not found"

        output = []
        output.append(f"# Graduate School Application Profile: {student_id}")
        output.append(f"Last Updated: {profile['updated_at']}")
        output.append("")

        # Academic Profile
        output.append("## Academic Profile")
        academic = profile.get("academic_profile", {})
        output.append(f"- Major: {academic.get('major', 'Not specified')}")
        output.append(f"- University: {academic.get('university', 'Not specified')}")
        output.append(f"- GPA: {academic.get('gpa', 'Not specified')}")
        output.append(f"- Major GPA: {academic.get('major_gpa', 'Not specified')}")
        output.append(f"- Rank: {academic.get('rank', 'Not specified')}")
        output.append(f"- Research Interests: {', '.join(academic.get('research_interests', []))}")
        output.append("")

        # Test Scores
        output.append("## Test Scores")
        scores = profile.get("test_scores", {})
        output.append(f"- TOEFL: {scores.get('toefl', 'Not taken')}")
        output.append(f"- IELTS: {scores.get('ielts', 'Not taken')}")
        output.append(f"- GRE: {scores.get('gre', 'Not taken')}")
        output.append(f"- Subject GRE: {scores.get('sub_gre', 'Not taken')}")
        output.append("")

        # Research Experience Summary
        output.append("## Research Experience")
        research = profile.get("research_experience", {})
        output.append(f"- Publications: {len(research.get('publications', []))}")
        output.append(f"- Conference Presentations: {len(research.get('conferences', []))}")
        output.append(f"- Research Projects: {len(research.get('projects', []))}")
        output.append(f"- Internships: {len(research.get('internships', []))}")
        output.append("")

        # Achievements Summary
        output.append("## Achievements")
        achievements = profile.get("achievements", {})
        output.append(f"- Competition Awards: {len(achievements.get('competitions', []))}")
        output.append(f"- Academic Awards: {len(achievements.get('awards', []))}")
        output.append(f"- Scholarships: {len(achievements.get('scholarships', []))}")
        output.append("")

        # Tracked Schools
        output.append("## Tracked Schools")
        tracked = profile.get("tracked_schools", [])
        if tracked:
            for school in tracked:
                output.append(f"- {school['name']}")
        else:
            output.append("- No schools tracked yet")
        output.append("")

        return "\n".join(output)

def main():
    """Command line interface for profile management."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python profile_manager.py <command> [args...]")
        print("Commands: create, load, update, export, list")
        return

    manager = GradSchoolProfileManager()
    command = sys.argv[1]

    try:
        if command == "create":
            if len(sys.argv) < 4:
                print("Usage: create <student_id> <major> [university] [gpa]")
                return

            student_id = sys.argv[2]
            major = sys.argv[3]
            university = sys.argv[4] if len(sys.argv) > 4 else ""
            gpa = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0

            profile = manager.create_profile(student_id, {
                "major": major,
                "university": university,
                "gpa": gpa
            })
            print(f"Created profile for {student_id}")

        elif command == "export":
            if len(sys.argv) < 3:
                print("Usage: export <student_id>")
                return

            student_id = sys.argv[2]
            print(manager.export_profile_summary(student_id))

        elif command == "list":
            profiles = list(manager.profiles_dir.glob("*.json"))
            if profiles:
                print("Available profiles:")
                for profile_file in profiles:
                    student_id = profile_file.stem
                    profile = manager.load_profile(student_id)
                    if profile:
                        major = profile.get('academic_profile', {}).get('major', 'Unknown')
                        print(f"- {student_id} ({major}, updated: {profile['updated_at'][:10]})")
            else:
                print("No profiles found")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
