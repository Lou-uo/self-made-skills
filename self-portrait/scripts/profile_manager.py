#!/usr/bin/env python3
"""
Self-Portrait Profile Manager
Handles creation, updating, and management of user self-portrait profiles.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

class ProfileManager:
    """Manages user self-portrait profiles."""

    def __init__(self, workspace_path: str = "."):
        self.workspace_path = Path(workspace_path)
        self.profiles_dir = self.workspace_path / "profiles"
        self.profiles_dir.mkdir(exist_ok=True)

    def create_profile(self, user_id: str, initial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new self-portrait profile."""
        profile = {
            "user_id": user_id,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "version": "1.0",
            "basic_info": {
                "role": initial_data.get("role", ""),
                "experience_years": initial_data.get("experience_years", 0),
                "primary_technologies": initial_data.get("primary_technologies", []),
                "focus_areas": initial_data.get("focus_areas", []),
                "explanation_preference": initial_data.get("explanation_preference", "balanced")
            },
            "technical_profile": {
                "programming_languages": [],
                "frameworks": [],
                "tools": [],
                "learning": [],
                "skill_levels": {}
            },
            "work_style": {
                "approach": "balanced",
                "explanation_flow": "concurrent",
                "code_review_focus": [],
                "collaboration_style": "collaborative"
            },
            "interaction_patterns": {
                "feedback_style": "constructive",
                "question_patterns": [],
                "success_criteria": [],
                "common_requests": []
            },
            "preferences": {
                "documentation_style": "comprehensive",
                "code_organization": "modular",
                "naming_conventions": "descriptive",
                "architecture_preference": "scalable"
            }
        }

        return self.save_profile(user_id, profile)

    def load_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Load an existing profile."""
        profile_path = self.profiles_dir / f"{user_id}.json"
        if profile_path.exists():
            with open(profile_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def save_profile(self, user_id: str, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Save profile to file."""
        profile["updated_at"] = datetime.now().isoformat()
        profile_path = self.profiles_dir / f"{user_id}.json"

        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)

        return profile

    def update_section(self, user_id: str, section: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update a specific section of the profile."""
        profile = self.load_profile(user_id)
        if not profile:
            raise ValueError(f"Profile for user {user_id} not found")

        if section in profile:
            profile[section].update(updates)
        else:
            profile[section] = updates

        return self.save_profile(user_id, profile)

    def add_interaction_example(self, user_id: str, category: str, example: str) -> Dict[str, Any]:
        """Add an interaction example to track patterns."""
        profile = self.load_profile(user_id)
        if not profile:
            raise ValueError(f"Profile for user {user_id} not found")

        if "interaction_examples" not in profile:
            profile["interaction_examples"] = []

        example_entry = {
            "category": category,
            "example": example,
            "timestamp": datetime.now().isoformat()
        }

        profile["interaction_examples"].append(example_entry)
        return self.save_profile(user_id, profile)

    def export_profile(self, user_id: str) -> str:
        """Export profile as formatted text."""
        profile = self.load_profile(user_id)
        if not profile:
            return f"Profile for user {user_id} not found"

        output = []
        output.append(f"# Self-Portrait Profile: {user_id}")
        output.append(f"Last Updated: {profile['updated_at']}")
        output.append("")

        # Basic Info
        output.append("## Basic Information")
        basic = profile.get("basic_info", {})
        output.append(f"- Role: {basic.get('role', 'Not specified')}")
        output.append(f"- Experience: {basic.get('experience_years', 0)} years")
        output.append(f"- Primary Technologies: {', '.join(basic.get('primary_technologies', []))}")
        output.append(f"- Focus Areas: {', '.join(basic.get('focus_areas', []))}")
        output.append(f"- Explanation Preference: {basic.get('explanation_preference', 'balanced')}")
        output.append("")

        # Technical Profile
        output.append("## Technical Profile")
        tech = profile.get("technical_profile", {})
        output.append(f"- Languages: {', '.join(tech.get('programming_languages', []))}")
        output.append(f"- Frameworks: {', '.join(tech.get('frameworks', []))}")
        output.append(f"- Tools: {', '.join(tech.get('tools', []))}")
        output.append(f"- Learning: {', '.join(tech.get('learning', []))}")
        output.append("")

        # Work Style
        output.append("## Work Style")
        work = profile.get("work_style", {})
        output.append(f"- Approach: {work.get('approach', 'balanced')}")
        output.append(f"- Explanation Flow: {work.get('explanation_flow', 'concurrent')}")
        output.append(f"- Code Review Focus: {', '.join(work.get('code_review_focus', []))}")
        output.append("")

        return "\n".join(output)

def main():
    """Command line interface for profile management."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python profile_manager.py <command> [args...]")
        print("Commands: create, load, update, export, add-example")
        return

    manager = ProfileManager()
    command = sys.argv[1]

    try:
        if command == "create":
            if len(sys.argv) < 4:
                print("Usage: create <user_id> <role> [experience_years]")
                return

            user_id = sys.argv[2]
            role = sys.argv[3]
            experience = int(sys.argv[4]) if len(sys.argv) > 4 else 0

            profile = manager.create_profile(user_id, {
                "role": role,
                "experience_years": experience
            })
            print(f"Created profile for {user_id}")

        elif command == "export":
            if len(sys.argv) < 3:
                print("Usage: export <user_id>")
                return

            user_id = sys.argv[2]
            print(manager.export_profile(user_id))

        elif command == "list":
            profiles = list(manager.profiles_dir.glob("*.json"))
            if profiles:
                print("Available profiles:")
                for profile_file in profiles:
                    user_id = profile_file.stem
                    profile = manager.load_profile(user_id)
                    if profile:
                        print(f"- {user_id} (updated: {profile['updated_at'][:10]})")
            else:
                print("No profiles found")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
