#!/usr/bin/env python3
"""
Enhanced AI-based Semantic Validation for NER Dictionaries v2
Uses sentence transformers for entity validation without human intervention
"""

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
import os
from typing import Dict, List, Tuple

class SemanticValidatorV2:
    def __init__(self):
        # Load open-source sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # 22MB model
        
        # Enhanced category reference descriptions
        self.category_references = {
            'TECHNOLOGY_TYPE': 'renewable energy generation technologies including solar photovoltaic wind turbines hydroelectric geothermal biomass energy storage systems',
            'SERVICE_CATEGORY': 'professional services in renewable energy sector including installation maintenance consulting monitoring grid integration project development',
            'EQUIPMENT_COMPONENT': 'physical equipment and components used in renewable energy systems such as inverters turbines batteries panels transformers controllers',
            'PERFORMANCE_METRIC': 'key performance indicators and measurements for renewable energy systems including capacity factor LCOE efficiency ratings energy output',
            'REGULATORY_STANDARD': 'standards regulations codes and certification programs governing renewable energy sector including ISO IEC IEEE standards',
            'TRANSPORT_MODE': 'sustainable transportation methods including electric vehicles hydrogen fuel cells rail maritime aviation multimodal transport',
            'CARBON_METRIC': 'carbon footprint measurement and greenhouse gas emission indicators including CO2 emissions scope emissions carbon intensity',
            'SUPPLY_CHAIN_ELEMENT': 'sustainable supply chain components including green packaging reverse logistics circular economy sustainable procurement',
            'EFFICIENCY_TECHNOLOGY': 'technology solutions for logistics efficiency including route optimization fleet management IoT predictive analytics automation',
            'ENVIRONMENTAL_STANDARD': 'environmental standards and certifications including ISO 14001 LEED GRI CDP TCFD sustainability reporting frameworks'
        }
    
    def validate_entity_category_fit(self, entity: str, category: str, threshold: float = 0.3) -> Tuple[bool, float]:
        """Validate if entity fits in assigned category using semantic similarity"""
        if category not in self.category_references:
            return False, 0.0
        
        # Get embeddings
        entity_embedding = self.model.encode([entity])
        category_embedding = self.model.encode([self.category_references[category]])
        
        # Calculate similarity
        similarity = cosine_similarity(entity_embedding, category_embedding)[0][0]
        
        return similarity >= threshold, similarity
    
    def detect_duplicates(self, entities: List[str], threshold: float = 0.85) -> List[Tuple[str, str, float]]:
        """Detect semantic duplicates using embeddings"""
        if len(entities) < 2:
            return []
            
        embeddings = self.model.encode(entities)
        duplicates = []
        
        for i in range(len(entities)):
            for j in range(i+1, len(entities)):
                similarity = cosine_similarity([embeddings[i]], [embeddings[j]])[0][0]
                if similarity >= threshold:
                    duplicates.append((entities[i], entities[j], similarity))
        
        return duplicates
    
    def validate_cross_domain_mappings(self, energy_entity: str, logistics_entity: str, threshold: float = 0.2) -> Tuple[bool, float]:
        """Validate cross-domain entity relationships"""
        energy_embedding = self.model.encode([energy_entity])
        logistics_embedding = self.model.encode([logistics_entity])
        
        similarity = cosine_similarity(energy_embedding, logistics_embedding)[0][0]
        
        return similarity >= threshold, similarity
    
    def assess_entity_quality(self, entity: str) -> Dict[str, float]:
        """Assess overall entity quality"""
        quality_metrics = {}
        
        # Length appropriateness (2-50 characters is good)
        length_score = 1.0 if 2 <= len(entity) <= 50 else 0.5
        quality_metrics['length_score'] = length_score
        
        # Word count appropriateness (1-5 words is good)
        word_count = len(entity.split())
        word_score = 1.0 if 1 <= word_count <= 5 else 0.7
        quality_metrics['word_count_score'] = word_score
        
        # Capitalization consistency
        words = entity.split()
        cap_score = 1.0 if all(word[0].isupper() for word in words if word) else 0.8
        quality_metrics['capitalization_score'] = cap_score
        
        # Overall quality
        quality_metrics['overall_quality'] = np.mean(list(quality_metrics.values()))
        
        return quality_metrics
    
    def run_validation(self, entities_dict: Dict[str, List[str]]) -> Dict:
        """Run complete AI validation suite"""
        results = {
            'validation_summary': {},
            'category_validation': {},
            'duplicate_detection': {},
            'quality_assessment': {},
            'cross_domain_validation': {}
        }
        
        total_entities = sum(len(entities) for entities in entities_dict.values())
        valid_entities = 0
        
        # Category validation
        for category, entities in entities_dict.items():
            if not entities:  # Skip empty categories
                results['category_validation'][category] = {
                    'avg_similarity': 0.0,
                    'valid_entities': 0,
                    'total_entities': 0
                }
                continue
                
            category_scores = []
            for entity in entities:
                is_valid, score = self.validate_entity_category_fit(entity, category)
                category_scores.append(score)
                if is_valid:
                    valid_entities += 1
            
            results['category_validation'][category] = {
                'avg_similarity': float(np.mean(category_scores)) if category_scores else 0.0,
                'valid_entities': sum(1 for score in category_scores if score >= 0.3),
                'total_entities': len(entities)
            }
            
            # Duplicate detection
            duplicates = self.detect_duplicates(entities)
            results['duplicate_detection'][category] = [
                {'entity1': dup[0], 'entity2': dup[1], 'similarity': float(dup[2])}
                for dup in duplicates
            ]
            
            # Quality assessment
            quality_scores = []
            for entity in entities:
                quality = self.assess_entity_quality(entity)
                quality_scores.append(quality['overall_quality'])
            
            results['quality_assessment'][category] = {
                'avg_quality': float(np.mean(quality_scores)) if quality_scores else 0.0,
                'high_quality_entities': sum(1 for score in quality_scores if score >= 0.8)
            }
        
        # Validation summary
        results['validation_summary'] = {
            'total_entities': total_entities,
            'valid_entities': valid_entities,
            'validation_rate': valid_entities / total_entities if total_entities > 0 else 0.0,
            'categories_processed': len(entities_dict),
            'avg_category_similarity': float(np.mean([
                cat_data['avg_similarity'] 
                for cat_data in results['category_validation'].values()
                if cat_data['total_entities'] > 0
            ])) if results['category_validation'] else 0.0
        }
        
        return results

if __name__ == "__main__":
    validator = SemanticValidatorV2()
    print("Running enhanced AI semantic validation...")
    
    # Load v2 entities
    with open('data/raw/v2_renewable_energy_entities.json', 'r') as f:
        re_data = json.load(f)
    with open('data/raw/v2_green_logistics_entities.json', 'r') as f:
        gl_data = json.load(f)
    
    # Combine entities
    all_entities = {**re_data, **gl_data}
    
    results = validator.run_validation(all_entities)
    
    output_path = "data/processed/v2_semantic_validation_results.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Custom JSON encoder for numpy types
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            return super().default(obj)
    
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, cls=NumpyEncoder)
    
    print(f"Validation complete. Results saved to {output_path}")
    
    # Print summary
    summary = results['validation_summary']
    print(f"Validated {summary['valid_entities']}/{summary['total_entities']} entities ({summary['validation_rate']:.1%})")
    print(f"Average category similarity: {summary['avg_category_similarity']:.3f}")
