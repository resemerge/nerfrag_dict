# Renewable Energy Services and Green Logistics NER Dictionaries

## Project Overview

This project creates two complementary Named Entity Recognition (NER) dictionaries for sustainable technology applications:

1. **Renewable Energy Services Dictionary**: Entities related to renewable energy technologies, services, and applications
2. **Green Logistics Dictionary**: Entities focused on sustainable transportation and supply chain management

## Key Features

- **Cross-domain Mappings**: Links between renewable energy and logistics entities for RAG applications
- **AI-Validated**: Automated validation using semantic similarity and LLM assessment
- **RAG-Optimized**: Structured for Retrieval-Augmented Generation systems
- **Standardized Format**: Consistent categorization and metadata
- **Open Source**: CC BY 4.0 license for research and commercial use

## Dictionary Structure

### Renewable Energy Services Dictionary
- **TECHNOLOGY_TYPE**: Solar, wind, hydro, geothermal, biomass, storage
- **SERVICE_CATEGORY**: Installation, maintenance, consulting, monitoring
- **EQUIPMENT_COMPONENT**: Inverters, turbines, batteries, sensors
- **PERFORMANCE_METRIC**: Capacity factor, LCOE, efficiency ratings
- **REGULATORY_STANDARD**: ISO, IEC, national codes, certifications

### Green Logistics Dictionary  
- **TRANSPORT_MODE**: Electric vehicles, alternative fuels, sustainable transport
- **CARBON_METRIC**: Emissions measurement, footprint calculation, offset programs
- **SUPPLY_CHAIN_ELEMENT**: Sustainable packaging, reverse logistics, green warehousing
- **EFFICIENCY_TECHNOLOGY**: Route optimization, automation, predictive analytics
- **ENVIRONMENTAL_STANDARD**: ISO 14001, LEED, carbon reporting frameworks

## Usage Instructions

### 1. Data Collection
```bash
# Run renewable energy entity scraper
python scripts/scraping/renewable_energy_scraper.py

# Run green logistics entity scraper  
python scripts/scraping/green_logistics_scraper.py
```

### 2. Cross-Domain Mapping
```bash
# Generate entity relationships
python scripts/processing/cross_domain_mapper.py
```

### 3. AI Validation Process
```bash
# Run semantic similarity validation
python scripts/validation/ai_semantic_validator.py

# Run LLM-based validation (requires OpenRouter API key)
export OPENROUTER_API_KEY="your_key"
python scripts/validation/openrouter_validator.py
```

### 4. Final Dictionary Generation
```bash
# Generate publication-ready dictionaries
python scripts/processing/generate_final_dictionaries.py
```

## Applications

### Named Entity Recognition
- Extract renewable energy and logistics entities from documents
- Classify sustainability-related terminology
- Standardize industry vocabulary across domains

### Retrieval-Augmented Generation (RAG)
- Context-aware sustainability consulting
- Cross-domain question answering
- Technology-application relationship discovery

### Research Applications
- Literature analysis and systematic reviews
- Policy document processing
- Industry report mining and analysis

## Data Note Publication

This work is being prepared as a Data Note for submission to:
- **Conference**: ICECO 2025
- **Journal**: Discover Sustainability (Springer)
- **Special Issue**: "Quantitative Methods on Renewable Energy-Economic Growth Nexus"

## File Structure

```
ner_dictionaries/
├── data/
│   ├── raw/                    # Scraped data
│   ├── processed/              # Validated data
│   └── final/                  # Publication-ready dictionaries
├── scripts/
│   ├── scraping/               # Data collection scripts
│   ├── processing/             # Data processing and mapping
│   └── validation/             # Quality assurance tools
├── methodology/                # Documentation of methods
├── documentation/              # Project documentation
└── README.md                   # This file
```

## Quality Assurance

- **Multi-source Validation**: Cross-reference with 4 authoritative sources (IRENA, IEA, NREL, EU)
- **AI-Based Validation**: Semantic similarity and LLM confidence scoring
- **Automated Quality Checks**: Duplicate detection, format validation, category fit assessment
- **Reproducible Process**: Consistent validation results across runs
- **Integrity Verification**: SHA-256 hashes for data integrity

## License

This work is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

## Contact

For questions about the dictionaries or collaboration opportunities, please contact [corresponding author email].

## Acknowledgments

- Industry experts who provided validation feedback
- Open data sources and organizations
- ICECO 2025 conference organizers
- Discover Sustainability editorial team
