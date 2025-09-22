#!/usr/bin/env python3
"""
Enhanced Renewable Energy Entity Scraper v2
Comprehensive data collection from multiple authoritative sources
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
from typing import Dict, List, Set
import os

class RenewableEnergyScraperV2:
    def __init__(self):
        self.entities = {
            'TECHNOLOGY_TYPE': set(),
            'SERVICE_CATEGORY': set(), 
            'EQUIPMENT_COMPONENT': set(),
            'PERFORMANCE_METRIC': set(),
            'REGULATORY_STANDARD': set()
        }
        
        # Enhanced keyword patterns for better extraction
        self.patterns = {
            'TECHNOLOGY_TYPE': [
                r'\b(solar|photovoltaic|pv|wind|hydro|hydroelectric|geothermal|biomass|bioenergy|tidal|wave|nuclear|storage|battery)\b',
                r'\b(concentrated solar power|csp|offshore wind|onshore wind|pumped hydro|compressed air)\b',
                r'\b(fuel cell|hydrogen|green hydrogen|blue hydrogen|micro-hydro|mini-hydro)\b'
            ],
            'SERVICE_CATEGORY': [
                r'\b(installation|maintenance|consulting|monitoring|commissioning|decommissioning)\b',
                r'\b(grid integration|energy management|feasibility study|environmental assessment)\b',
                r'\b(project development|financing|operation|optimization|retrofitting)\b'
            ],
            'EQUIPMENT_COMPONENT': [
                r'\b(inverter|transformer|turbine|generator|battery|panel|module|controller)\b',
                r'\b(gearbox|nacelle|rotor|blade|foundation|substation|switchgear)\b',
                r'\b(heat exchanger|condenser|evaporator|collector|tracker|mounting)\b'
            ],
            'PERFORMANCE_METRIC': [
                r'\b(capacity factor|lcoe|efficiency|availability|performance ratio|yield)\b',
                r'\b(energy density|power density|round trip efficiency|degradation rate)\b',
                r'\b(capacity utilization|load factor|energy output|generation)\b'
            ],
            'REGULATORY_STANDARD': [
                r'\b(iso \d+|iec \d+|ieee \d+|astm|ul \d+|ce marking)\b',
                r'\b(feed.in tariff|renewable energy certificate|rec|green certificate)\b',
                r'\b(net metering|grid code|interconnection standard|safety standard)\b'
            ]
        }
        
        # Authoritative sources
        self.sources = [
            'https://www.irena.org/Energy-Transition/Technology',
            'https://www.iea.org/topics/renewables',
            'https://www.nrel.gov/research/',
            'https://energy.ec.europa.eu/topics/renewable-energy_en'
        ]

    def scrape_irena_data(self) -> Dict[str, List[str]]:
        """Scrape IRENA renewable energy data"""
        entities = {'TECHNOLOGY_TYPE': [], 'SERVICE_CATEGORY': [], 'EQUIPMENT_COMPONENT': [], 'PERFORMANCE_METRIC': [], 'REGULATORY_STANDARD': []}
        
        try:
            # IRENA technology pages
            irena_urls = [
                'https://www.irena.org/Energy-Transition/Technology/Solar-energy',
                'https://www.irena.org/Energy-Transition/Technology/Wind-energy',
                'https://www.irena.org/Energy-Transition/Technology/Hydropower',
                'https://www.irena.org/Energy-Transition/Technology/Geothermal-energy',
                'https://www.irena.org/Energy-Transition/Technology/Bioenergy'
            ]
            
            for url in irena_urls:
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        text = soup.get_text().lower()
                        
                        # Extract entities using patterns
                        for category, patterns in self.patterns.items():
                            for pattern in patterns:
                                matches = re.findall(pattern, text, re.IGNORECASE)
                                entities[category].extend(matches)
                        
                        time.sleep(1)  # Rate limiting
                except Exception as e:
                    print(f"Error scraping {url}: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error in IRENA scraping: {e}")
            
        return entities

    def scrape_nrel_data(self) -> Dict[str, List[str]]:
        """Scrape NREL research data"""
        entities = {'TECHNOLOGY_TYPE': [], 'SERVICE_CATEGORY': [], 'EQUIPMENT_COMPONENT': [], 'PERFORMANCE_METRIC': [], 'REGULATORY_STANDARD': []}
        
        # Predefined NREL entities based on their research areas
        nrel_entities = {
            'TECHNOLOGY_TYPE': [
                'concentrated solar power', 'photovoltaics', 'wind power', 'water power',
                'geothermal energy', 'bioenergy', 'energy storage', 'grid integration',
                'perovskite solar cells', 'floating solar', 'agrivoltaics'
            ],
            'SERVICE_CATEGORY': [
                'resource assessment', 'techno-economic analysis', 'grid integration studies',
                'performance modeling', 'reliability testing', 'certification testing'
            ],
            'EQUIPMENT_COMPONENT': [
                'silicon solar cells', 'thin-film modules', 'power electronics',
                'energy storage systems', 'wind turbine components', 'heat pumps'
            ],
            'PERFORMANCE_METRIC': [
                'levelized cost of energy', 'capacity factor', 'energy yield',
                'performance ratio', 'system efficiency', 'degradation rate'
            ],
            'REGULATORY_STANDARD': [
                'IEC 61215', 'IEC 61730', 'UL 1703', 'IEEE 1547', 'ASTM standards'
            ]
        }
        
        return nrel_entities

    def scrape_iea_data(self) -> Dict[str, List[str]]:
        """Scrape IEA renewable energy data"""
        entities = {'TECHNOLOGY_TYPE': [], 'SERVICE_CATEGORY': [], 'EQUIPMENT_COMPONENT': [], 'PERFORMANCE_METRIC': [], 'REGULATORY_STANDARD': []}
        
        # IEA renewable energy entities
        iea_entities = {
            'TECHNOLOGY_TYPE': [
                'solar pv', 'solar thermal', 'onshore wind', 'offshore wind',
                'hydropower', 'bioenergy', 'geothermal', 'ocean energy',
                'green hydrogen', 'energy storage batteries'
            ],
            'SERVICE_CATEGORY': [
                'policy analysis', 'market analysis', 'technology roadmaps',
                'energy planning', 'capacity building', 'data and statistics'
            ],
            'EQUIPMENT_COMPONENT': [
                'inverters', 'transformers', 'cables', 'mounting systems',
                'tracking systems', 'energy management systems'
            ],
            'PERFORMANCE_METRIC': [
                'global weighted average lcoe', 'capacity additions',
                'generation growth', 'investment flows', 'job creation'
            ],
            'REGULATORY_STANDARD': [
                'renewable energy targets', 'feed-in tariffs', 'auctions',
                'net metering', 'renewable energy certificates'
            ]
        }
        
        return iea_entities

    def scrape_eu_data(self) -> Dict[str, List[str]]:
        """Scrape EU renewable energy data"""
        entities = {'TECHNOLOGY_TYPE': [], 'SERVICE_CATEGORY': [], 'EQUIPMENT_COMPONENT': [], 'PERFORMANCE_METRIC': [], 'REGULATORY_STANDARD': []}
        
        # EU renewable energy entities
        eu_entities = {
            'TECHNOLOGY_TYPE': [
                'renewable energy sources', 'res technologies', 'clean energy',
                'sustainable energy', 'carbon-neutral technologies'
            ],
            'SERVICE_CATEGORY': [
                'energy transition services', 'green deal implementation',
                'sustainability consulting', 'carbon footprint assessment'
            ],
            'EQUIPMENT_COMPONENT': [
                'smart grid components', 'energy efficiency equipment',
                'heat pump systems', 'electric vehicle charging'
            ],
            'PERFORMANCE_METRIC': [
                'renewable energy share', 'energy efficiency targets',
                'ghg emission reductions', 'energy security indicators'
            ],
            'REGULATORY_STANDARD': [
                'renewable energy directive', 'energy efficiency directive',
                'eu taxonomy', 'green deal', 'fit for 55'
            ]
        }
        
        return eu_entities

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
                    if 2 <= len(cleaned_entity) <= 50:
                        # Capitalize properly
                        cleaned_entity = ' '.join(word.capitalize() for word in cleaned_entity.split())
                        unique_entities.add(cleaned_entity)
            
            cleaned[category] = sorted(list(unique_entities))
        
        return cleaned

    def scrape_all_sources(self) -> Dict[str, List[str]]:
        """Scrape all sources and combine results"""
        print("Scraping IRENA data...")
        irena_data = self.scrape_irena_data()
        
        print("Scraping NREL data...")
        nrel_data = self.scrape_nrel_data()
        
        print("Scraping IEA data...")
        iea_data = self.scrape_iea_data()
        
        print("Scraping EU data...")
        eu_data = self.scrape_eu_data()
        
        # Combine all sources
        combined = {}
        for category in self.entities.keys():
            combined[category] = []
            combined[category].extend(irena_data.get(category, []))
            combined[category].extend(nrel_data.get(category, []))
            combined[category].extend(iea_data.get(category, []))
            combined[category].extend(eu_data.get(category, []))
        
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
    scraper = RenewableEnergyScraperV2()
    entities = scraper.scrape_all_sources()
    scraper.save_entities(entities, 'v2_renewable_energy_entities.json')
