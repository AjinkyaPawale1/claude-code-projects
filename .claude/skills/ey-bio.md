# EY Bio PowerPoint Generator

## Description
Creates a professional EY bio PowerPoint presentation using the Alexandre Truong bio as a template. The bio organizes experience by work category (not by company) with AI/ML/Data work prioritized.

## Usage
Invoke with `/ey-bio` or ask to "create my EY bio" or "update my EY bio"

## Files

### Template
- **Source Template**: `data/CV - Alexandre Truong 3.pptx`
- **Output File**: `data/Ajinkya_Pawale_EY_Bio.pptx`
- **Photo**: `/Users/ajinkyapawale/Downloads/Ajinkya_Profile_Picture_Copy.jpg`
- **Resume Reference**: `data/Ajinkya_Resume_AIML_v7.pdf`

### Script
- **Generator Script**: `execution/create_ey_bio.py`

## Current Bio Content

### Header
- Name: Ajinkya Pawale
- Title: Senior Consultant
- Practice: Analytics & Insights
- Phone: 763-306-4790
- Email: pawaleajinkya7@gmail.com

### Background
Ajinkya joined the Analytics & Insights Practice of EY Chicago in January 2026. He brings extensive experience in AI/ML engineering, GenAI solutions, and data pipeline development. Prior to EY, he worked as an AI Engineer at Elevance Health and as a Data Engineer at Course5 Intelligence.

Qualifications:
- Master of Science in Data Science, Indiana University Bloomington

### Skills
- Industries: Healthcare, E-commerce, Retail Banking
- Technical: Machine Learning, Generative AI, LLM Fine-Tuning, Predictive Analytics, Deep Learning, NLP
- Data Engineering, Cloud Architecture, MLOps
- Programming: Python, PySpark, R, SQL, PyTorch, TensorFlow, Langchain, OpenAI, Hugging Face
- Cloud: AWS (S3, EC2, Lambda, EMR), Kubernetes, Docker, Airflow
- Databases: PostgreSQL, MongoDB, Hadoop, Hive

### Experience Categories (AI/ML First)

**Generative AI**
- Led end-to-end GenAI solution for automated call summarization using OpenAI GPT models
- Augmented call wrap-up API with RAG pipelines and autonomous agent workflows
- Fine-tuned open-source LLMs (Llama) using LoRA on healthcare call transcripts for domain-adapted summarization
- Architected multi-agent GPT-4.1-based document compliance system

**Machine Learning & Predictive Analytics**
- Enhanced data retrieval for Inpatient Claims using PySpark with PyTorch features
- Developed neural network and Bayesian optimization (BOHB) models using TensorFlow and PyTorch
- Conducted statistical analysis with R, pandas, scikit-learn

**Data Engineering & Optimization**
- Automated data pipelines in Airflow
- Designed Kinesis Consumer Application with Redis cache
- Migrated to AWS EMR cluster
- Implemented data validation tool for drift detection

**Analytics & Monitoring**
- Established 20+ Datadog and Splunk dashboards
- Statistical analysis on 100,000+ data entries with Tableau
- Created pymongo analytics framework

**Testing & Quality Assurance**
- Orchestrated pytest framework with 50+ test scenarios
- Executed LoadRunner stress tests

## Template Formatting Reference

### Fonts
- **Section Headers**: EYInterstate, 14pt, Bold
- **Header Box**: EYInterstate, 9pt (name bold)
- **Background/Skills**: EYInterstate, 10pt
- **Experience**: EYInterstate Light, 10pt

### Layout
- Slide: 13.34" x 7.50" (widescreen)
- Photo: 0.85" x 1.134" at position (0.694", 0.244")
- Left column: Background + Skills
- Middle column: Experience (Generative AI, ML)
- Right column: Experience (Data Engineering, Analytics, Testing)

## How to Update

1. Edit the content in `execution/create_ey_bio.py`
2. Run: `python3 execution/create_ey_bio.py`
3. Output saved to `data/Ajinkya_Pawale_EY_Bio.pptx`

## Commands

```bash
# Generate/regenerate bio
cd "/Users/ajinkyapawale/Claude Code Projects"
python3 execution/create_ey_bio.py
```
