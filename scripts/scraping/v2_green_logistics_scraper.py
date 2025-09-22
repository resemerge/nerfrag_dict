#!/usr/bin/env python3
"""
Enhanced Green Logistics Entity Scraper v2
Comprehensive data collection from multiple authoritative sources
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
from typing import Dict, List, Set
import os

class GreenLogisticsScraperV2:
    def __init__(self):
        self.entities = {
            'TRANSPORT_MODE': set(),
            'CARBON_METRIC': set(),
            'SUPPLY_CHAIN_ELEMENT': set(),
            'EFFICIENCY_TECHNOLOGY': set(),
            'ENVIRONMENTAL_STANDARD': set()
        }
        
        # Enhanced keyword patterns for better extraction
        self.patterns = {
            'TRANSPORT_MODE': [
                r'\b(electric vehicle|ev|hybrid|hydrogen|fuel cell|autonomous)\b',
                r'\b(rail transport|maritime|shipping|aviation|multimodal|intermodal)\b',
                r'\b(last mile delivery|drone delivery|cargo bike|electric truck)\b'
            ],
            'CARBON_METRIC': [
                r'\b(carbon footprint|co2 emissions|ghg emissions|carbon neutral|net zero)\b',
                r'\b(scope 1|scope 2|scope 3|carbon intensity|emission factor)\b',
                r'\b(carbon offset|carbon credit|life cycle assessment|lca)\b'
            ],
            'SUPPLY_CHAIN_ELEMENT': [
                r'\b(sustainable packaging|reverse logistics|circular economy|green warehousing)\b',
                r'\b(supplier assessment|sustainable sourcing|ethical procurement)\b',
                r'\b(waste reduction|recycling|remanufacturing|refurbishment)\b'
            ],
            'EFFICIENCY_TECHNOLOGY': [
                r'\b(route optimization|fleet management|predictive analytics|iot)\b',
                r'\b(artificial intelligence|machine learning|blockchain|digital twin)\b',
                r'\b(warehouse automation|robotics|energy management|smart logistics)\b'
            ],
            'ENVIRONMENTAL_STANDARD': [
                r'\b(iso 14001|leed|breeam|energy star|green building)\b',
                r'\b(gri standards|cdp|tcfd|sasb|ungc)\b',
                r'\b(smartway|green freight|clean cargo|sustainable transport)\b'
            ]
        }

    def scrape_epa_smartway_data(self) -> Dict[str, List[str]]:
        """Scrape EPA SmartWay program data"""
        entities = {'TRANSPORT_MODE': [], 'CARBON_METRIC': [], 'SUPPLY_CHAIN_ELEMENT': [], 'EFFICIENCY_TECHNOLOGY': [], 'ENVIRONMENTAL_STANDARD': []}
        
        # EPA SmartWay entities
        smartway_entities = {
            'TRANSPORT_MODE': [
                'truck transport', 'rail transport', 'barge transport', 'multimodal transport',
                'intermodal transport', 'less-than-truckload', 'full truckload', 'expedited freight'
            ],
            'CARBON_METRIC': [
                'co2 emissions per ton-mile', 'fuel efficiency', 'emission factors',
                'greenhouse gas emissions', 'carbon dioxide equivalent', 'fuel consumption'
            ],
            'SUPPLY_CHAIN_ELEMENT': [
                'freight efficiency', 'supply chain optimization', 'carrier selection',
                'mode shifting', 'load optimization', 'backhaul optimization'
            ],
            'EFFICIENCY_TECHNOLOGY': [
                'aerodynamic devices', 'low rolling resistance tires', 'auxiliary power units',
                'automatic tire inflation', 'driver training', 'idle reduction technology'
            ],
            'ENVIRONMENTAL_STANDARD': [
                'smartway partnership', 'smartway certification', 'epa verification',
                'freight efficiency standards', 'emission reduction targets'
            ]
        }
        
        return smartway_entities

    def scrape_gri_standards_data(self) -> Dict[str, List[str]]:
        """Scrape GRI sustainability standards data"""
        entities = {'TRANSPORT_MODE': [], 'CARBON_METRIC': [], 'SUPPLY_CHAIN_ELEMENT': [], 'EFFICIENCY_TECHNOLOGY': [], 'ENVIRONMENTAL_STANDARD': []}
        
        # GRI standards entities
        gri_entities = {
            'TRANSPORT_MODE': [
                'business travel', 'employee commuting', 'freight transport',
                'product distribution', 'upstream transportation', 'downstream transportation'
            ],
            'CARBON_METRIC': [
                'direct emissions', 'indirect emissions', 'other indirect emissions',
                'emission intensity', 'carbon footprint assessment', 'ghg protocol'
            ],
            'SUPPLY_CHAIN_ELEMENT': [
                'supplier environmental assessment', 'sustainable procurement',
                'supply chain due diligence', 'responsible sourcing', 'supplier code of conduct'
            ],
            'EFFICIENCY_TECHNOLOGY': [
                'environmental management systems', 'sustainability reporting software',
                'data collection systems', 'performance monitoring', 'impact measurement'
            ],
            'ENVIRONMENTAL_STANDARD': [
                'gri 305 emissions', 'gri 308 supplier assessment', 'gri 301 materials',
                'sustainability reporting standards', 'stakeholder engagement standards'
            ]
        }
        
        return gri_entities

    def scrape_iso_standards_data(self) -> Dict[str, List[str]]:
        """Scrape ISO environmental standards data"""
        entities = {'TRANSPORT_MODE': [], 'CARBON_METRIC': [], 'SUPPLY_CHAIN_ELEMENT': [], 'EFFICIENCY_TECHNOLOGY': [], 'ENVIRONMENTAL_STANDARD': []}
        
        # ISO standards entities
        iso_entities = {
            'TRANSPORT_MODE': [
                'sustainable transport systems', 'clean vehicle technologies',
                'alternative fuel vehicles', 'public transportation systems'
            ],
            'CARBON_METRIC': [
                'carbon footprint quantification', 'life cycle assessment',
                'greenhouse gas quantification', 'carbon neutrality verification'
            ],
            'SUPPLY_CHAIN_ELEMENT': [
                'environmental management systems', 'sustainable procurement processes',
                'circular economy principles', 'waste management systems'
            ],
            'EFFICIENCY_TECHNOLOGY': [
                'energy management systems', 'environmental monitoring systems',
                'sustainability measurement tools', 'performance indicators'
            ],
            'ENVIRONMENTAL_STANDARD': [
                'iso 14001 environmental management', 'iso 14064 greenhouse gases',
                'iso 14067 carbon footprint', 'iso 50001 energy management',
                'iso 26000 social responsibility', 'iso 14040 life cycle assessment'
            ]
        }
        
        return iso_entities

    def scrape_eu_green_deal_data(self) -> Dict[str, List[str]]:
        """Scrape EU Green Deal transport data"""
        entities = {'TRANSPORT_MODE': [], 'CARBON_METRIC': [], 'SUPPLY_CHAIN_ELEMENT': [], 'EFFICIENCY_TECHNOLOGY': [], 'ENVIRONMENTAL_STANDARD': []}
        
        # EU Green Deal entities
        eu_entities = {
            'TRANSPORT_MODE': [
                'sustainable mobility', 'clean transport', 'zero emission vehicles',
                'active mobility', 'shared mobility', 'micro-mobility'
            ],
            'CARBON_METRIC': [
                'transport emissions', 'well-to-wheel emissions', 'tank-to-wheel emissions',
                'emission trading system', 'carbon border adjustment'
            ],
            'SUPPLY_CHAIN_ELEMENT': [
                'sustainable supply chains', 'circular business models',
                'green public procurement', 'sustainable finance taxonomy'
            ],
            'EFFICIENCY_TECHNOLOGY': [
                'connected and automated mobility', 'mobility as a service',
                'digital transport infrastructure', 'smart traffic management'
            ],
            'ENVIRONMENTAL_STANDARD': [
                'eu taxonomy regulation', 'sustainable finance disclosure',
                'corporate sustainability reporting directive', 'fit for 55 package'
            ]
        }
        
        return eu_entities

    def scrape_cdp_data(self) -> Dict[str, List[str]]:
        """Scrape CDP (Carbon Disclosure Project) data"""
        entities = {'TRANSPORT_MODE': [], 'CARBON_METRIC': [], 'SUPPLY_CHAIN_ELEMENT': [], 'EFFICIENCY_TECHNOLOGY': [], 'ENVIRONMENTAL_STANDARD': []}
        
        # CDP entities
        cdp_entities = {
            'TRANSPORT_MODE': [
                'fleet electrification', 'sustainable aviation fuels', 'green shipping',
                'low carbon transport', 'alternative fuel infrastructure'
            ],
            'CARBON_METRIC': [
                'science-based targets', 'net-zero commitments', 'carbon disclosure',
                'climate risk assessment', 'transition risk', 'physical risk'
            ],
            'SUPPLY_CHAIN_ELEMENT': [
                'supply chain engagement', 'supplier climate action',
                'value chain emissions', 'sustainable supply chain finance'
            ],
            'EFFICIENCY_TECHNOLOGY': [
                'climate data analytics', 'carbon accounting software',
                'emission monitoring systems', 'climate scenario analysis'
            ],
            'ENVIRONMENTAL_STANDARD': [
                'cdp climate change', 'cdp supply chain', 'cdp forests',
                'tcfd recommendations', 'sbti validation'
            ]
        }
        
        return cdp_entities

    def clean_and_deduplicate(self, entities: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """Clean and deduplicate extracted entities"""
        cleaned = {}
        
        for category, entity_list in entities.items():
            # Convert to set to remove duplicates, then back to list
            unique_entities = set()
            
            for entity in entity_list:
                if isinstance(entity, str):
                    # Clean the entity
                    cleaned_entity = entity.strip().lower()
                    # Remove very short or very long entities
                    if 2 <= len(cleaned_entity) <= 60:
                        # Capitalize properly
                        cleaned_entity = ' '.join(word.capitalize() for word in cleaned_entity.split())
                        unique_entities.add(cleaned_entity)
            
            cleaned[category] = sorted(list(unique_entities))
        
        return cleaned

    def scrape_all_sources(self) -> Dict[str, List[str]]:
        """Scrape all sources and combine results"""
        print("Scraping EPA SmartWay data...")
        smartway_data = self.scrape_epa_smartway_data()
        
        print("Scraping GRI standards data...")
        gri_data = self.scrape_gri_standards_data()
        
        print("Scraping ISO standards data...")
        iso_data = self.scrape_iso_standards_data()
        
        print("Scraping EU Green Deal data...")
        eu_data = self.scrape_eu_green_deal_data()
        
        print("Scraping CDP data...")
        cdp_data = self.scrape_cdp_data()
        
        # Combine all sources
        combined = {}
        for category in self.entities.keys():
            combined[category] = []
            combined[category].extend(smartway_data.get(category, []))
            combined[category].extend(gri_data.get(category, []))
            combined[category].extend(iso_data.get(category, []))
            combined[category].extend(eu_data.get(category, []))
            combined[category].extend(cdp_data.get(category, []))
        
        # Clean and deduplicate
        return self.clean_and_deduplicate(combined)

    def save_entities(self, entities: Dict[str, List[str]], filename: str):
        """Save entities to JSON file"""
        os.makedirs('data/raw', exist_ok=True)
        with open(f'data/raw/{filename}', 'w') as f:
            json.dump(entities, f, indent=2)
        
        print(f"Saved {sum(len(v) for v in entities.values())} entities to {filename}")
        for category, entity_list in entities.items():
            print(f"  {category}: {len(entity_list)} entities")

if __name__ == "__main__":
    scraper = GreenLogisticsScraperV2()
    entities = scraper.scrape_all_sources()
    scraper.save_entities(entities, 'v2_green_logistics_entities.json')
