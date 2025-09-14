import re
import random
import requests
import json
from tools.simulated_tools import ToolKit
from config import Config

class DeliveryAgent:
    def __init__(self):
        self.toolkit = ToolKit()
        self.available_tools = self.toolkit.get_tools_description()
        self.headers = {"Authorization": f"Bearer {Config.HUGGING_FACE_TOKEN}"}
        self.api_url = Config.HUGGING_FACE_API_URL
    
    def query_huggingface(self, prompt):
        """
        Query Hugging Face API for AI response with better error handling
        """
        try:
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 500,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    if 'generated_text' in result[0]:
                        return result[0]['generated_text']
                    return str(result[0])
                return str(result)
            else:
                print(f"Hugging Face API error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Hugging Face API error: {e}")
            return None
    
    def process_scenario(self, scenario):
        # First, extract key information using pattern matching
        scenario_type, entities = self._analyze_scenario(scenario)
        
        # Use API for complex scenarios, fallback to rule-based for simple ones
        if self._is_complex_scenario(scenario):
            ai_response = self._get_ai_analysis(scenario, scenario_type)
            reasoning = ai_response if ai_response else self._get_rule_based_reasoning(scenario_type, entities)
        else:
            reasoning = self._get_rule_based_reasoning(scenario_type, entities)
        
        # Determine tools to use based on scenario type
        tools_to_call = self._determine_tools(scenario_type, entities)
        
        # Execute the tools
        steps = []
        for tool_name, params in tools_to_call:
            try:
                if hasattr(self.toolkit, tool_name):
                    tool_func = getattr(self.toolkit, tool_name)
                    result = tool_func(*params)
                    steps.append({
                        "action": f"Called {tool_name} with params {params}",
                        "observation": result
                    })
            except Exception as e:
                steps.append({
                    "action": f"Attempted to call {tool_name} with params {params}",
                    "observation": f"Error: {str(e)}"
                })
        
        resolution = self._generate_resolution(scenario_type, steps, entities)
        
        return {
            "scenario": scenario,
            "steps": steps,
            "resolution": resolution,
            "reasoning": reasoning
        }
    
    def _analyze_scenario(self, scenario):
        """
        Analyze the scenario to determine its type and extract entities
        """
        scenario_lower = scenario.lower()
        entities = self._extract_entities(scenario)
        
        # Determine scenario type
        if any(word in scenario_lower for word in ["damage", "spill", "broken", "torn", "leak", "dispute"]):
            scenario_type = "damage"
        elif any(word in scenario_lower for word in ["delay", "late", "wait", "busy", "overload", "slow"]):
            scenario_type = "delay"
        elif any(word in scenario_lower for word in ["traffic", "accident", "congestion", "road", "block", "obstruction"]):
            scenario_type = "traffic"
        elif any(word in scenario_lower for word in ["not home", "unavailable", "absent", "closed", "missing"]):
            scenario_type = "unavailable"
        elif any(word in scenario_lower for word in ["payment", "refund", "charge", "bill", "price", "cost"]):
            scenario_type = "payment"
        elif any(word in scenario_lower for word in ["address", "location", "wrong", "incorrect", "find"]):
            scenario_type = "location"
        elif any(word in scenario_lower for word in ["weather", "rain", "storm", "snow", "flood", "wind"]):
            scenario_type = "weather"
        else:
            scenario_type = "general"
        
        return scenario_type, entities
    
    def _extract_entities(self, scenario):
        """
        Extract potential entities from the scenario
        """
        entities = {
            "merchant": re.findall(r'(restaurant|store|shop|merchant|McDonalds|Burger King|KFC|Pizza Hut|Mcdonald)', scenario, re.IGNORECASE),
            "driver": re.findall(r'(driver|rider|courier|delivery person|delivery guy)', scenario, re.IGNORECASE),
            "customer": re.findall(r'(customer|recipient|client|user|guest|passenger)', scenario, re.IGNORECASE),
            "location": re.findall(r'(\b\d+\s+\w+\s+\w+|\b\w+\s+Street|\b\w+\s+Avenue|\b\w+\s+Boulevard|\b\w+\s+Road|\bairport|\bhotel|\boffice)', scenario, re.IGNORECASE),
            "item": re.findall(r'(food|package|parcel|order|item|product|delivery|drink|meal)', scenario, re.IGNORECASE),
            "time": re.findall(r'(\d+\s*min|\d+\s*hour|\d+\s*:\d+|\d+\s*[ap]m|urgent|asap)', scenario, re.IGNORECASE),
        }
        
        # Clean up entities
        for key, value in entities.items():
            entities[key] = list(set([v.lower() for v in value if v])) or ["unknown"]
        
        return entities
    
    def _is_complex_scenario(self, scenario):
        """
        Determine if a scenario is complex enough to warrant AI analysis
        """
        scenario_lower = scenario.lower()
        
        # Complex scenarios have multiple details or specific conditions
        complex_indicators = [
            "urgent", "airport", "major accident", "planned route", 
            "doorstep", "unclear", "dispute", "spilled drink",
            "valuable package", "flight status", "alternative route"
        ]
        
        return any(indicator in scenario_lower for indicator in complex_indicators) or len(scenario.split()) > 15
    
    def _get_ai_analysis(self, scenario, scenario_type):
        """
        Get AI analysis for complex scenarios
        """
        prompt = f"""
        You are an intelligent delivery coordinator AI. Analyze this delivery disruption scenario and provide a concise analysis:

        Scenario: {scenario}

        Please provide:
        1. A brief analysis of the main issues
        2. The priority level (High/Medium/Low)
        3. Key factors to consider

        Keep your response under 100 words.
        """
        
        try:
            response = self.query_huggingface(prompt)
            if response:
                return f"AI Analysis: {response}"
        except:
            pass
        
        return None
    
    def _get_rule_based_reasoning(self, scenario_type, entities):
        """
        Get rule-based reasoning for the scenario
        """
        reasoning_map = {
            "damage": "Analyzing package damage scenario. This appears to be a dispute about damaged goods that requires evidence collection and mediation.",
            "delay": "Analyzing delivery delay scenario. This appears to be a merchant overload or traffic situation causing extended wait times.",
            "traffic": "Analyzing traffic obstruction scenario. This requires checking current traffic conditions and finding alternative routes.",
            "unavailable": "Analyzing recipient unavailable scenario. This requires contacting the recipient and finding alternative delivery options.",
            "payment": "Analyzing payment-related scenario. This involves resolving billing issues or processing refunds.",
            "location": "Analyzing location-related scenario. This involves verifying addresses and finding correct delivery locations.",
            "weather": "Analyzing weather-related scenario. This involves assessing weather impacts on delivery operations.",
            "general": "Analyzing general delivery scenario. Using standard approach to resolve the issue."
        }
        
        return reasoning_map.get(scenario_type, "Analyzing the delivery scenario to determine the best resolution approach.")
    
    def _determine_tools(self, scenario_type, entities):
        """
        Determine which tools to call based on the scenario type
        """
        tools_map = {
            "damage": [
                ("initiate_mediation_flow", ["ORDER001"]),
                ("collect_evidence", ["ORDER001", "Was the bag sealed by the merchant?"]),
                ("collect_evidence", ["ORDER001", "Was the seal intact upon handover?"]),
                ("analyze_evidence", ["Collected evidence from both parties"])
            ],
            "delay": [
                ("get_merchant_status", ["RESTAURANT001"]),
                ("check_traffic", ["current_location"]),
                ("notify_customer", ["ORDER002", "Your order is experiencing a delay. We apologize for the inconvenience."])
            ],
            "traffic": [
                ("check_traffic", ["current_route"]),
                ("calculate_alternative_route", ["current_location", "destination", "congested_route"]),
                ("notify_passenger_and_driver", ["TRIP001", "Route changed due to traffic conditions. ETA updated."]),
                ("check_flight_status", ["FLIGHT123"] if "airport" in str(entities["location"]).lower() else [])
            ],
            "unavailable": [
                ("contact_recipient_via_chat", ["ORDER003", "We're at your location but you seem unavailable. What would you like us to do with your package?"]),
                ("find_nearby_locker", ["current_location"]),
                ("suggest_safe_drop_off", ["ORDER003", "secure location"])
            ],
            "payment": [
                ("issue_instant_refund", ["ORDER004", "10.00"])
            ],
            "location": [
                ("check_traffic", [entities["location"][0] if entities["location"][0] != "unknown" else "area"]),
                ("notify_customer", ["ORDER005", "We're verifying your delivery location. Thank you for your patience."])
            ],
            "weather": [
                ("check_traffic", ["area"]),
                ("notify_customer", ["ORDER006", "Your delivery may be delayed due to weather conditions. We appreciate your patience."])
            ],
            "general": [
                ("check_traffic", ["area"]),
                ("notify_customer", ["ORDER007", "We're addressing the issue with your delivery. Thank you for your patience."])
            ]
        }
        
        tools = tools_map.get(scenario_type, [])
        
        # Add flight status check for airport scenarios
        if "airport" in str(entities.get("location", [])).lower():
            tools.append(("check_flight_status", ["FLIGHT456"]))
        
        return tools
    
    def _generate_resolution(self, scenario_type, steps, entities):
        """
        Generate a resolution based on the scenario type and steps taken
        """
        resolution_map = {
            "damage": "Damage issue resolved. Evidence collected and analyzed. Appropriate compensation provided to customer based on fault determination.",
            "delay": "Delay situation handled. Customer notified and alternative solutions considered to minimize impact.",
            "traffic": "Traffic obstruction addressed. Alternative route calculated and all parties notified of updated ETA.",
            "unavailable": "Recipient unavailable situation handled. Alternative delivery options provided and customer preferences respected.",
            "payment": "Payment issue resolved. Refund processed and customer notified of resolution.",
            "location": "Location issue addressed. Correct delivery location verified and route updated accordingly.",
            "weather": "Weather situation assessed. Contingency plans activated and customers notified of potential delays.",
            "general": "Situation assessed and appropriate actions taken. Customer notified of resolution."
        }
        
        resolution = resolution_map.get(scenario_type, "Appropriate actions taken to resolve the delivery issue.")
        
        # Add specific details for traffic scenarios with airports
        if scenario_type == "traffic" and "airport" in str(entities.get("location", [])).lower():
            resolution += " Flight status checked and passenger informed about potential flight implications."
        
        return resolution