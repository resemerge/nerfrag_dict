#!/usr/bin/env python3
"""
Enhanced Final Dictionary Generator v2
Creates publication-ready NER dictionaries with comprehensive metadata
"""

import json
import os
from datetime import datetime
from typing import Dict, List

class DictionaryGeneratorV2:
    def __init__(self):
        self.re_entities = {}
        self.logistics_entities = {}
        self.cross_mappings = []
        self.validation_results = {}
        
        # Enhanced metadata
        self.metadata = {
            'version': '2.0',
            'creation_date': datetime.now().isoformat(),
            'description': 'Enhanced NER dictionaries for renewable energy and green logistics domains',
            'total_entities': 0,
            'validation_status': 'AI-validated',
            'data_sources': [
                'IRENA (International Renewable Energy Agency)',
                'NREL (National Renewable Energy Laboratory)', 
                'IEA (International Energy Agency)',
                'European Commission Energy',
                'EPA SmartWay Program',
                'GRI Sustainability Standards',
                'ISO Environmental Standards',
                'CDP (Carbon Disclosure Project)'
            ],
            'license': 'CC BY 4.0',
            'citation': 'Enhanced NER Dictionaries for Sustainable Technology Applications - ICECO 2025',
            'contact': 'research@sustainabletech.org'
        }
    
    def load_processed_data(self):
        """Load validated and processed entity data"""
        # Load v2 renewable energy entities
        with open('data/raw/v2_renewable_energy_entities.json', 'r') as f:
            self.re_entities = json.load(f)
        
        # Load v2 green logistics entities
        with open('data/raw/v2_green_logistics_entities.json', 'r') as f:
            self.logistics_entities = json.load(f)
        
        # Load v2 cross-domain mappings
        try:
            with open('data/processed/v2_cross_domain_mappings.json', 'r') as f:
                self.cross_mappings = json.load(f)
        except FileNotFoundError:
            print("Warning: v2_cross_domain_mappings.json not found. Run v2_cross_domain_mapper.py first.")
            self.cross_mappings = []
        
        # Load v2 validation results
        try:
            with open('data/processed/v2_semantic_validation_results.json', 'r') as f:
                self.validation_results = json.load(f)
        except FileNotFoundError:
            print("Warning: v2_semantic_validation_results.json not found. Run v2_ai_semantic_validator.py first.")
            self.validation_results = {}
        
        # Update total entities count
        self.metadata['total_entities'] = (
            sum(len(entities) for entities in self.re_entities.values()) +
            sum(len(entities) for entities in self.logistics_entities.values())
        )
    
    def create_renewable_energy_dictionary(self) -> Dict:
        """Create enhanced renewable energy services dictionary"""
        dictionary = {
            'dictionary_info': {
                'name': 'Renewable Energy Services NER Dictionary v2',
                'domain': 'Renewable Energy Technology and Services',
                'categories': list(self.re_entities.keys()),
                'total_entities': sum(len(entities) for entities in self.re_entities.values()),
                **self.metadata
            },
            'category_definitions': {
                'TECHNOLOGY_TYPE': {
                    'description': 'Renewable energy generation technologies and systems',
                    'examples': ['Solar Photovoltaic', 'Wind Turbine', 'Hydroelectric', 'Geothermal'],
                    'entity_count': len(self.re_entities.get('TECHNOLOGY_TYPE', []))
                },
                'SERVICE_CATEGORY': {
                    'description': 'Professional services in renewable energy sector',
                    'examples': ['Installation', 'Maintenance', 'Consulting', 'Grid Integration'],
                    'entity_count': len(self.re_entities.get('SERVICE_CATEGORY', []))
                },
                'EQUIPMENT_COMPONENT': {
                    'description': 'Physical equipment and components for renewable energy systems',
                    'examples': ['Inverter', 'Battery', 'Transformer', 'Controller'],
                    'entity_count': len(self.re_entities.get('EQUIPMENT_COMPONENT', []))
                },
                'PERFORMANCE_METRIC': {
                    'description': 'Key performance indicators for renewable energy systems',
                    'examples': ['Capacity Factor', 'LCOE', 'Efficiency', 'Energy Output'],
                    'entity_count': len(self.re_entities.get('PERFORMANCE_METRIC', []))
                },
                'REGULATORY_STANDARD': {
                    'description': 'Standards, regulations, and certifications',
                    'examples': ['ISO 14001', 'IEC 61215', 'Grid Code', 'Feed-in Tariff'],
                    'entity_count': len(self.re_entities.get('REGULATORY_STANDARD', []))
                }
            },
            'entities': self.re_entities,
            'validation_metrics': self.validation_results.get('category_validation', {}),
            'quality_assessment': self.validation_results.get('quality_assessment', {})
        }
        
        return dictionary
    
    def create_green_logistics_dictionary(self) -> Dict:
        """Create enhanced green logistics dictionary"""
        dictionary = {
            'dictionary_info': {
                'name': 'Green Logistics NER Dictionary v2',
                'domain': 'Sustainable Transportation and Supply Chain Management',
                'categories': list(self.logistics_entities.keys()),
                'total_entities': sum(len(entities) for entities in self.logistics_entities.values()),
                **self.metadata
            },
            'category_definitions': {
                'TRANSPORT_MODE': {
                    'description': 'Sustainable transportation methods and technologies',
                    'examples': ['Electric Vehicle', 'Hydrogen Fuel Cell', 'Rail Transport', 'Green Shipping'],
                    'entity_count': len(self.logistics_entities.get('TRANSPORT_MODE', []))
                },
                'CARBON_METRIC': {
                    'description': 'Carbon footprint and greenhouse gas emission measurements',
                    'examples': ['CO2 Emissions', 'Carbon Footprint', 'Scope 1 Emissions', 'Net Zero'],
                    'entity_count': len(self.logistics_entities.get('CARBON_METRIC', []))
                },
                'SUPPLY_CHAIN_ELEMENT': {
                    'description': 'Sustainable supply chain components and practices',
                    'examples': ['Green Packaging', 'Reverse Logistics', 'Circular Economy', 'Sustainable Sourcing'],
                    'entity_count': len(self.logistics_entities.get('SUPPLY_CHAIN_ELEMENT', []))
                },
                'EFFICIENCY_TECHNOLOGY': {
                    'description': 'Technology solutions for logistics efficiency and optimization',
                    'examples': ['Route Optimization', 'Fleet Management', 'IoT', 'Predictive Analytics'],
                    'entity_count': len(self.logistics_entities.get('EFFICIENCY_TECHNOLOGY', []))
                },
                'ENVIRONMENTAL_STANDARD': {
                    'description': 'Environmental standards, certifications, and reporting frameworks',
                    'examples': ['ISO 14001', 'GRI Standards', 'CDP', 'TCFD'],
                    'entity_count': len(self.logistics_entities.get('ENVIRONMENTAL_STANDARD', []))
                }
            },
            'entities': self.logistics_entities,
            'validation_metrics': self.validation_results.get('category_validation', {}),
            'quality_assessment': self.validation_results.get('quality_assessment', {})
        }
        
        return dictionary
    
    def create_cross_domain_dictionary(self) -> Dict:
        """Create enhanced cross-domain mappings dictionary"""
        # Organize mappings by relationship type
        mappings_by_type = {}
        for mapping in self.cross_mappings:
            rel_type = mapping.get('relationship_type', 'unknown')
            if rel_type not in mappings_by_type:
                mappings_by_type[rel_type] = []
            mappings_by_type[rel_type].append(mapping)
        
        dictionary = {
            'dictionary_info': {
                'name': 'Cross-Domain Mappings Dictionary v2',
                'domain': 'Renewable Energy ↔ Green Logistics Relationships',
                'total_mappings': len(self.cross_mappings),
                'relationship_types': list(mappings_by_type.keys()),
                **self.metadata
            },
            'mapping_methodology': {
                'rule_based_mappings': 'Predefined semantic rules connecting related concepts',
                'semantic_similarity': 'AI-based similarity analysis using sentence transformers',
                'confidence_scoring': 'Numerical confidence scores for each mapping relationship',
                'validation_process': 'Multi-stage validation using semantic analysis'
            },
            'relationship_types': {
                rel_type: {
                    'description': f'Mappings of type: {rel_type}',
                    'count': len(mappings),
                    'avg_confidence': sum(m.get('confidence_score', 0) for m in mappings) / len(mappings) if mappings else 0
                }
                for rel_type, mappings in mappings_by_type.items()
            },
            'cross_domain_mappings': self.cross_mappings,
            'usage_guidelines': {
                'rag_applications': 'Use for context-aware retrieval in sustainability consulting',
                'ner_enhancement': 'Improve entity recognition across renewable energy and logistics',
                'knowledge_graphs': 'Build semantic relationships for domain knowledge representation',
                'research_applications': 'Support interdisciplinary research in sustainable technology'
            }
        }
        
        return dictionary
    
    def save_dictionaries(self):
        """Save all enhanced dictionaries"""
        os.makedirs('data/final', exist_ok=True)
        
        # Save renewable energy dictionary
        re_dict = self.create_renewable_energy_dictionary()
        with open('data/final/v2_renewable_energy_services_dictionary.json', 'w') as f:
            json.dump(re_dict, f, indent=2)
        
        # Save green logistics dictionary
        gl_dict = self.create_green_logistics_dictionary()
        with open('data/final/v2_green_logistics_dictionary.json', 'w') as f:
            json.dump(gl_dict, f, indent=2)
        
        # Save cross-domain mappings dictionary
        cd_dict = self.create_cross_domain_dictionary()
        with open('data/final/v2_cross_domain_mappings_dictionary.json', 'w') as f:
            json.dump(cd_dict, f, indent=2)
        
        # Create project summary
        summary = {
            'project_overview': {
                'title': 'Enhanced NER Dictionaries for Sustainable Technology Applications v2',
                'total_entities': self.metadata['total_entities'],
                'renewable_energy_entities': sum(len(entities) for entities in self.re_entities.values()),
                'green_logistics_entities': sum(len(entities) for entities in self.logistics_entities.values()),
                'cross_domain_mappings': len(self.cross_mappings),
                'data_sources': len(self.metadata['data_sources']),
                'validation_status': self.metadata['validation_status']
            },
            'dictionary_files': [
                'v2_renewable_energy_services_dictionary.json',
                'v2_green_logistics_dictionary.json', 
                'v2_cross_domain_mappings_dictionary.json'
            ],
            'metadata': self.metadata,
            'validation_summary': self.validation_results.get('validation_summary', {})
        }
        
        with open('data/final/v2_project_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"Enhanced dictionaries saved successfully!")
        print(f"Total entities: {summary['project_overview']['total_entities']}")
        print(f"Renewable Energy: {summary['project_overview']['renewable_energy_entities']} entities")
        print(f"Green Logistics: {summary['project_overview']['green_logistics_entities']} entities")
        print(f"Cross-domain mappings: {summary['project_overview']['cross_domain_mappings']}")

if __name__ == "__main__":
    generator = DictionaryGeneratorV2()
    print("Generating enhanced final NER dictionaries v2...")
    
    generator.load_processed_data()
    generator.save_dictionaries()
    
    print("Enhanced final dictionaries generated successfully!")
