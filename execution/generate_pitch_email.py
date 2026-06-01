#!/usr/bin/env python3
"""
Generate Pitch Email Script
Creates personalized pitch emails based on client research

Usage:
    python generate_pitch_email.py --company "Acme Corp" --tone professional
    python generate_pitch_email.py --company "Acme Corp" --focus "automation,data-analytics"
"""

import os
import json
import argparse
from datetime import datetime
from pathlib import Path


class PitchEmailGenerator:
    def __init__(self, company_name, sender_name="Ajinkya Pawale",
                 sender_title="AI Engineer & Application Engineer", tone="professional"):
        self.company_name = company_name
        self.sender_name = sender_name
        self.sender_title = sender_title
        self.tone = tone
        self.profile = None

    def load_client_profile(self):
        """Load client research profile"""
        profile_dir = Path(".tmp/clients")
        profile_path = profile_dir / f"{self.company_name.replace(' ', '_').lower()}_profile.json"

        if not profile_path.exists():
            raise FileNotFoundError(
                f"Client profile not found: {profile_path}\n"
                f"Please run research_client.py first or provide client information."
            )

        with open(profile_path, 'r') as f:
            self.profile = json.load(f)

        return self.profile

    def generate_subject_line(self, focus_areas=None):
        """Generate compelling subject line"""
        company = self.profile.get('company_name', self.company_name)

        if focus_areas:
            focus = focus_areas[0].replace('-', ' ').title()
            return f"AI-Powered {focus} Solution for {company}"

        # Use top pain point or opportunity
        pain_points = self.profile.get('pain_points', [])
        if pain_points:
            main_pain = pain_points[0].get('area', 'Operations')
            return f"Streamlining {main_pain} at {company}"

        return f"Quick Question About AI Solutions for {company}"

    def generate_opening(self):
        """Generate personalized opening"""
        company = self.profile.get('company_name', self.company_name)
        recent_news = self.profile.get('recent_news', '')
        industry = self.profile.get('industry', 'your industry')

        if recent_news:
            return f"I noticed {company} recently {recent_news} - congratulations on the growth!"

        return f"I've been following {company}'s work in {industry} and am impressed by your approach."

    def generate_problem_section(self):
        """Generate problem/opportunity section"""
        pain_points = self.profile.get('pain_points', [])

        if not pain_points:
            return "Many companies in your industry are looking to leverage AI to improve efficiency and outcomes."

        main_pain = pain_points[0]
        area = main_pain.get('area', 'operations')
        description = main_pain.get('description', 'current processes')

        return (
            f"I noticed that many companies in your space face challenges with {area}, "
            f"particularly around {description}. This often results in missed opportunities "
            f"and inefficiencies that could be addressed with the right technical solution."
        )

    def generate_solution_section(self, focus_areas=None):
        """Generate solution overview"""
        solutions = self.profile.get('proposed_solutions', [])

        if focus_areas:
            # Filter solutions by focus areas
            solutions = [s for s in solutions if any(fa in s.get('type', '').lower() for fa in focus_areas)]

        if not solutions:
            return (
                "I specialize in building custom AI and software engineering solutions that automate "
                "workflows, extract insights from data, and create intelligent applications tailored "
                "to your specific needs."
            )

        main_solution = solutions[0]
        solution_type = main_solution.get('type', 'AI solution')
        description = main_solution.get('description', 'custom solution')

        return (
            f"I'd like to propose a {solution_type} that {description}. "
            f"This solution leverages modern AI/ML techniques and robust software engineering "
            f"to deliver measurable results."
        )

    def generate_value_props(self):
        """Generate value proposition bullets"""
        solutions = self.profile.get('proposed_solutions', [])

        if not solutions or not solutions[0].get('benefits'):
            return [
                "Reduce manual work and operational costs by 40-60%",
                "Make data-driven decisions with real-time insights",
                "Scale operations without proportional cost increases"
            ]

        benefits = solutions[0].get('benefits', [])
        return benefits[:3]  # Max 3 bullets

    def generate_credentials(self):
        """Generate credentials section"""
        if self.tone == "technical":
            return (
                f"As an AI and Application Engineer, I work with modern LLMs, deep learning frameworks, "
                f"and full-stack development to build production-ready solutions. I've helped companies "
                f"implement everything from document processing pipelines to predictive analytics systems."
            )
        elif self.tone == "casual":
            return (
                f"I'm an AI engineer who loves solving complex problems with practical technology. "
                f"I've built solutions ranging from customer service automation to data analysis tools, "
                f"always focused on real business outcomes."
            )
        else:  # professional or formal
            return (
                f"I'm an AI Engineer and Application Engineer with extensive experience in machine learning, "
                f"natural language processing, and software development. I focus on building practical, "
                f"production-ready solutions that deliver measurable ROI."
            )

    def generate_cta(self):
        """Generate call to action"""
        if self.tone == "casual":
            return "Would you be open to a quick 15-minute call to explore this? Happy to share examples of similar work."
        elif self.tone == "formal":
            return "I would welcome the opportunity to discuss how this solution could benefit your organization in a brief 15-minute call."
        else:  # professional or technical
            return "Would you be open to a brief 15-minute conversation to discuss how this could work for your team?"

    def generate_signature(self):
        """Generate email signature"""
        return f"""Best regards,
{self.sender_name}
{self.sender_title}
LinkedIn: linkedin.com/in/ajinkyapawale
"""

    def format_email(self, focus_areas=None):
        """Format complete email"""
        subject = self.generate_subject_line(focus_areas)
        opening = self.generate_opening()
        problem = self.generate_problem_section()
        solution = self.generate_solution_section(focus_areas)
        value_props = self.generate_value_props()
        credentials = self.generate_credentials()
        cta = self.generate_cta()
        signature = self.generate_signature()

        # Format value props as bullets
        value_bullets = "\n".join([f"• {prop}" for prop in value_props])

        email_body = f"""Hi {{contact_name}},

{opening}

{problem}

{solution}

This approach can help you:
{value_bullets}

{credentials}

{cta}

{signature}"""

        return subject, email_body

    def save_email(self, subject, body):
        """Save email draft to file"""
        output_dir = Path(".tmp/clients")
        output_dir.mkdir(parents=True, exist_ok=True)

        safe_name = self.company_name.replace(' ', '_').lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = output_dir / f"{safe_name}_pitch_email_{timestamp}.txt"

        with open(output_path, 'w') as f:
            f.write(f"SUBJECT: {subject}\n\n")
            f.write(body)

        print(f"✓ Email draft saved to: {output_path}")
        return output_path


def main():
    parser = argparse.ArgumentParser(description='Generate personalized pitch email')
    parser.add_argument('--company', required=True, help='Company name')
    parser.add_argument('--sender-name', default='Ajinkya Pawale', help='Your name')
    parser.add_argument('--sender-title', default='AI Engineer & Application Engineer', help='Your title')
    parser.add_argument('--tone', choices=['professional', 'casual', 'formal', 'technical'],
                       default='professional', help='Email tone')
    parser.add_argument('--focus', help='Focus areas (comma-separated): automation,analytics,nlp,computer-vision')

    args = parser.parse_args()

    focus_areas = None
    if args.focus:
        focus_areas = [area.strip().lower() for area in args.focus.split(',')]

    try:
        generator = PitchEmailGenerator(
            company_name=args.company,
            sender_name=args.sender_name,
            sender_title=args.sender_title,
            tone=args.tone
        )

        print(f"Loading client profile for {args.company}...")
        generator.load_client_profile()

        print(f"Generating {args.tone} pitch email...")
        subject, body = generator.format_email(focus_areas)

        print("\n" + "="*80)
        print(f"SUBJECT: {subject}")
        print("="*80)
        print(body)
        print("="*80 + "\n")

        output_path = generator.save_email(subject, body)

        print("\nNext steps:")
        print(f"1. Review the email draft: {output_path}")
        print(f"2. Customize {{contact_name}} placeholder with actual name")
        print(f"3. Send via: python execution/send_email.py --to client@example.com --subject '{subject}' --body '...'")
        print(f"   Or use MCP Gmail tools to send")

    except FileNotFoundError as e:
        print(f"✗ Error: {str(e)}")
        exit(1)
    except Exception as e:
        print(f"✗ Error generating email: {str(e)}")
        raise


if __name__ == '__main__':
    main()
