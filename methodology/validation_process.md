# Dictionary Validation Methodology

## AI-Based Validation Framework

### 1. Semantic Similarity Validation
- **Model**: Sentence Transformers (all-MiniLM-L6-v2)
- **Category Fit Assessment**: Cosine similarity between entities and category definitions
- **Duplicate Detection**: Semantic similarity threshold (0.85) for near-duplicates
- **Cross-Domain Mapping**: Validate energy-logistics entity relationships

### 2. LLM-Based Quality Assessment
- **Model**: Meta Llama 3.2 3B Instruct (via OpenRouter.ai free tier)
- **Entity Categorization**: LLM validates entity-category assignments
- **Quality Scoring**: Automated assessment of entity clarity and specificity
- **Reasoning**: LLM provides explanations for validation decisions

### 3. Quality Metrics

#### AI Validation Metrics
- **Semantic Similarity Scores**: Category fit confidence (0.0-1.0)
- **LLM Confidence Ratings**: Entity validation confidence scores
- **Duplicate Detection Rate**: Percentage of semantic duplicates identified
- **Cross-Domain Mapping Accuracy**: Relationship validation scores

#### Coverage Metrics
- **Domain Completeness**: % of key domain concepts covered
- **Source Diversity**: Number of different source types (4 sources per dictionary)
- **Geographic Coverage**: US (EPA, NREL), EU (EC), International (IRENA, IEA, ISO)
- **Temporal Relevance**: Currency of terminology (2020-2024)

#### Reproducibility Metrics
- **Model Consistency**: Same validation results across runs
- **Threshold Sensitivity**: Validation stability across similarity thresholds
- **API Reliability**: Success rate of LLM validation calls
- **Processing Speed**: Entities validated per minute

## AI Validation Tools

### Semantic Validation Script
```python
from sentence_transformers import SentenceTransformer
validator = SemanticValidator()
results = validator.run_validation(entities_dict)
```

### LLM Validation Interface
```python
validator = OpenRouterValidator(api_key="your_key")
results = validator.run_validation(entities_dict, max_per_category=10)
```

### Validation Pipeline
1. **Semantic Similarity Check**: Category fit validation (threshold: 0.3)
2. **LLM Quality Assessment**: Entity clarity and specificity scoring
3. **Duplicate Detection**: Semantic similarity analysis (threshold: 0.85)
4. **Cross-Domain Validation**: Energy-logistics relationship scoring

## Validation Results Documentation

### Required Outputs
1. **Validation Report**: Detailed quality assessment
2. **Expert Feedback Summary**: Consolidated reviewer comments  
3. **Quality Metrics Dashboard**: Quantitative validation results
4. **Improvement Recommendations**: Areas for enhancement
5. **Version Control Log**: Changes and rationale

### Acceptance Criteria
- Minimum 0.3 semantic similarity score for category fit
- LLM confidence score ≥ 0.7 for entity validation
- Less than 5% semantic duplicate entities (similarity > 0.85)
- 100% format consistency through automated processing
- Cross-domain mapping confidence ≥ 0.2 for sustainability relationships
- Reproducible validation results across multiple runs
