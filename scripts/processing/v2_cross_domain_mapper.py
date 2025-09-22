#!/usr/bin/env python3
"""
Enhanced Cross-Domain Mapper v2
Maps relationships between renewable energy and green logistics entities
"""

import json
import pandas as pd
from typing import Dict, List, Tuple
import os

class CrossDomainMapperV2:
    def __init__(self):
        self.mappings = []
        self.relationships = []
        
        # Enhanced mapping rules for better cross-domain connections
        self.mapping_rules = {
            # Energy technologies -> Transport modes
            'energy_to_transport': {
                'Solar': ['Electric Vehicle', 'Ev', 'Zero Emission Vehicles'],
                'Wind': ['Electric Vehicle', 'Ev', 'Green Shipping'],
                'Hydrogen': ['Fuel Cell', 'Hydrogen', 'Alternative Fuel Vehicles'],
                'Battery': ['Electric Vehicle', 'Fleet Electrification'],
                'Grid Integration': ['Electric Vehicle Charging', 'Smart Traffic Management']
            },
            
            # Services -> Supply chain elements
            'services_to_supply': {
                'Installation': ['Sustainable Procurement', 'Supplier Assessment'],
                'Maintenance': ['Reverse Logistics', 'Circular Economy'],
                'Consulting': ['Supply Chain Optimization', 'Sustainability Consulting'],
                'Monitoring': ['Performance Monitoring', 'Impact Measurement']
            },
            
            # Equipment -> Efficiency technology
            'equipment_to_efficiency': {
                'Inverter': ['Energy Management Systems', 'Smart Grid Components'],
                'Battery': ['Energy Storage Systems', 'Fleet Management'],
                'Controller': ['Iot', 'Predictive Analytics'],
                'Smart Grid Components': ['Digital Transport Infrastructure']
            },
            
            # Performance metrics -> Carbon metrics
            'performance_to_carbon': {
                'Efficiency': ['Carbon Intensity', 'Emission Factor'],
                'Lcoe': ['Life Cycle Assessment', 'Carbon Footprint'],
                'Capacity Factor': ['Emission Intensity', 'Co2 Emissions'],
                'Energy Output': ['Well-to-wheel Emissions', 'Ghg Emissions']
            },
            
            # Standards alignment
            'standards_alignment': {
                'Iso 14001': ['Iso 14001 Environmental Management', 'Environmental Management Systems'],
                'Renewable Energy Certificate': ['Carbon Credit', 'Emission Trading System'],
                'Grid Code': ['Sustainable Transport Systems', 'Clean Transport']
            }
        }

    def load_entities(self):
        """Load v2 entity data"""
        with open('data/raw/v2_renewable_energy_entities.json', 'r') as f:
            self.re_entities = json.load(f)
        
        with open('data/raw/v2_green_logistics_entities.json', 'r') as f:
            self.gl_entities = json.load(f)

    def find_semantic_matches(self, re_entity: str, gl_entities: List[str]) -> List[Tuple[str, float]]:
        """Find semantic matches between entities"""
        matches = []
        re_lower = re_entity.lower()
        
        for gl_entity in gl_entities:
            gl_lower = gl_entity.lower()
            
            # Exact match
            if re_lower == gl_lower:
                matches.append((gl_entity, 1.0))
            # Substring match
            elif re_lower in gl_lower or gl_lower in re_lower:
                matches.append((gl_entity, 0.8))
            # Keyword overlap
            else:
                re_words = set(re_lower.split())
                gl_words = set(gl_lower.split())
                overlap = len(re_words.intersection(gl_words))
                if overlap > 0:
                    similarity = overlap / max(len(re_words), len(gl_words))
                    if similarity >= 0.3:
                        matches.append((gl_entity, similarity))
        
        return sorted(matches, key=lambda x: x[1], reverse=True)

    def apply_mapping_rules(self):
        """Apply predefined mapping rules"""
        for rule_type, rules in self.mapping_rules.items():
            for re_pattern, gl_patterns in rules.items():
                # Find matching RE entities
                for re_category, re_entities in self.re_entities.items():
                    for re_entity in re_entities:
                        if any(pattern.lower() in re_entity.lower() for pattern in [re_pattern]):
                            # Find matching GL entities
                            for gl_category, gl_entities in self.gl_entities.items():
                                for gl_entity in gl_entities:
                                    if any(pattern.lower() in gl_entity.lower() for pattern in gl_patterns):
                                        self.mappings.append({
                                            'renewable_energy_entity': re_entity,
                                            'renewable_energy_category': re_category,
                                            'green_logistics_entity': gl_entity,
                                            'green_logistics_category': gl_category,
                                            'relationship_type': rule_type,
                                            'confidence_score': 0.9,
                                            'mapping_source': 'rule_based'
                                        })

    def generate_semantic_mappings(self):
        """Generate mappings using semantic similarity"""
        for re_category, re_entities in self.re_entities.items():
            for re_entity in re_entities:
                for gl_category, gl_entities in self.gl_entities.items():
                    matches = self.find_semantic_matches(re_entity, gl_entities)
                    
                    for gl_entity, similarity in matches[:3]:  # Top 3 matches
                        if similarity >= 0.5:  # Minimum threshold
                            self.mappings.append({
                                'renewable_energy_entity': re_entity,
                                'renewable_energy_category': re_category,
                                'green_logistics_entity': gl_entity,
                                'green_logistics_category': gl_category,
                                'relationship_type': 'semantic_similarity',
                                'confidence_score': similarity,
                                'mapping_source': 'semantic_analysis'
                            })

    def create_relationship_matrix(self):
        """Create relationship matrix for analysis"""
        for mapping in self.mappings:
            self.relationships.append({
                'source_entity': mapping['renewable_energy_entity'],
                'source_category': mapping['renewable_energy_category'],
                'target_entity': mapping['green_logistics_entity'],
                'target_category': mapping['green_logistics_category'],
                'relationship_strength': mapping['confidence_score'],
                'relationship_type': mapping['relationship_type']
            })

    def remove_duplicates(self):
        """Remove duplicate mappings"""
        seen = set()
        unique_mappings = []
        
        for mapping in self.mappings:
            key = (mapping['renewable_energy_entity'], mapping['green_logistics_entity'])
            if key not in seen:
                seen.add(key)
                unique_mappings.append(mapping)
        
        self.mappings = unique_mappings

    def generate_mappings(self):
        """Generate all cross-domain mappings"""
        print("Loading v2 entity data...")
        self.load_entities()
        
        print("Applying mapping rules...")
        self.apply_mapping_rules()
        
        print("Generating semantic mappings...")
        self.generate_semantic_mappings()
        
        print("Removing duplicates...")
        self.remove_duplicates()
        
        print("Creating relationship matrix...")
        self.create_relationship_matrix()
        
        print(f"Generated {len(self.mappings)} cross-domain mappings")

    def save_results(self):
        """Save mapping results"""
        os.makedirs('data/processed', exist_ok=True)
        
        # Save detailed mappings
        with open('data/processed/v2_cross_domain_mappings.json', 'w') as f:
            json.dump(self.mappings, f, indent=2)
        
        # Save relationship matrix as CSV
        df = pd.DataFrame(self.relationships)
        df.to_csv('data/processed/v2_entity_relationships.csv', index=False)
        
        print(f"Saved mappings to v2_cross_domain_mappings.json")
        print(f"Saved relationships to v2_entity_relationships.csv")

if __name__ == "__main__":
    mapper = CrossDomainMapperV2()
    mapper.generate_mappings()
    mapper.save_results()
