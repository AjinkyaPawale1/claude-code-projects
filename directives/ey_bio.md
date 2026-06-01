# EY Bio PowerPoint Generator

## Goal
Generate a professional EY bio PowerPoint for Ajinkya Pawale using the Alexandre Truong template.

## Inputs
- Template: `data/CV - Alexandre Truong 3.pptx`
- Resume: `data/Ajinkya_Resume_AIML_v7.pdf`
- Photo: `/Users/ajinkyapawale/Downloads/Ajinkya_Profile_Picture_Copy.jpg`

## Execution Tool
`execution/create_ey_bio.py`

## Output
`data/Ajinkya_Pawale_EY_Bio.pptx`

## Key Requirements
1. Use exact template formatting (fonts, positions, sizes)
2. Organize experience by **work category**, not by company
3. Prioritize AI/ML/Data work first
4. Categories: Generative AI, ML & Predictive Analytics, Data Engineering, Analytics, Testing

## Content Structure

### Header
- Name: Ajinkya Pawale
- Title: Senior Consultant
- Practice: Analytics & Insights
- Contact: 763-306-4790, pawaleajinkya7@gmail.com

### Background
- Joined EY Chicago January 2026
- Prior: AI Engineer at Elevance Health, Data Engineer at Course5 Intelligence
- Education: MS Data Science, Indiana University Bloomington

### Skills
- Industries: Healthcare, E-commerce, Retail Banking
- Technical: ML, GenAI, LLM Fine-Tuning, Predictive Analytics, Deep Learning, NLP
- Programming: Python, PySpark, PyTorch, TensorFlow, Langchain
- Cloud: AWS, Kubernetes, Docker, Airflow
- Databases: PostgreSQL, MongoDB, Hadoop, Hive

### Experience (by category)
1. **Generative AI** - GPT models, RAG pipelines, LLM fine-tuning (LoRA), multi-agent systems
2. **Machine Learning** - PySpark, PyTorch, BOHB, TensorFlow
3. **Data Engineering** - Airflow, Kinesis, AWS EMR, data validation
4. **Analytics** - Datadog, Splunk, Tableau, pymongo
5. **Testing** - pytest, LoadRunner

## Template Specs
- Slide: 13.34" x 7.50"
- Fonts: EYInterstate (headers/body), EYInterstate Light (experience)
- Photo: 0.85" x 1.134" at (0.694", 0.244")

## Edge Cases
- If photo not found, script will print warning but continue
- Text must fit within shape bounds to avoid overlap
- Paragraph count must match template structure

## Learnings
- Use EMU values for precise positioning
- Preserve existing paragraph structure, only update text/font
- Category headers should be bold within EYInterstate Light
