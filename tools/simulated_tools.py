import random
import time
from datetime import datetime, timedelta

class ToolKit:
    def get_tools_description(self):
        return """
        Available Tools:
        - check_traffic(location): Checks traffic conditions at a specified location
        - get_merchant_status(merchant_id): Gets the current status of a merchant
        - notify_customer(order_id, message): Sends a notification to a customer
        - re_route_driver(driver_id, new_route): Reroutes a driver to a new route
        - get_nearby_merchants(location, cuisine): Finds nearby merchants of a specific cuisine
        - initiate_mediation_flow(order_id): Initiates a mediation flow for a dispute
        - collect_evidence(order_id, question): Collects evidence for a dispute
        - analyze_evidence(evidence): Analyzes collected evidence
        - issue_instant_refund(order_id, amount): Issues an instant refund to a customer
        - exonerate_driver(driver_id): Clears a driver of fault
        - log_merchant_packaging_feedback(merchant_id, feedback): Logs packaging feedback for a merchant
        - notify_resolution(order_id, resolution): Notifies parties of a resolution
        - contact_recipient_via_chat(order_id, message): Contacts a recipient via chat
        - suggest_safe_drop_off(order_id, location): Suggests a safe drop-off location
        - find_nearby_locker(location): Finds nearby parcel lockers
        - calculate_alternative_route(origin, destination, avoid): Calculates an alternative route
        - notify_passenger_and_driver(trip_id, message): Notifies both passenger and driver
        - check_flight_status(flight_number): Checks the status of a flight
        """
    
    def check_traffic(self, location):
        time.sleep(0.5)
        
        conditions = ["clear", "moderate", "heavy", "severe"]
        traffic_level = random.choice(conditions)
        
        if traffic_level == "clear":
            return f"Traffic conditions at {location} are clear. No significant delays expected."
        elif traffic_level == "moderate":
            return f"Moderate traffic at {location}. Expect minor delays of 5-10 minutes."
        elif traffic_level == "heavy":
            return f"Heavy traffic at {location}. Expect delays of 15-20 minutes."
        else:
            return f"Severe traffic congestion at {location} due to an accident. Expect delays of 30+ minutes. Consider alternative routes."
    
    def get_merchant_status(self, merchant_id):
        time.sleep(0.5)
        
        statuses = [
            "Normal operations",
            "Busy - 10-15 minute delay",
            "Very busy - 20-30 minute delay",
            "Extremely busy - 40+ minute delay",
            "Temporarily closed"
        ]
        
        status = random.choice(statuses)
        wait_time = "Unknown"
        
        if "10-15" in status:
            wait_time = "12"
        elif "20-30" in status:
            wait_time = "25"
        elif "40+" in status:
            wait_time = "40"
        
        return f"Merchant {merchant_id} status: {status}. Estimated preparation time: {wait_time} minutes."
    
    def notify_customer(self, order_id, message):
        time.sleep(0.5)
        return f"Notification sent to customer for order {order_id}: '{message}'"
    
    def re_route_driver(self, driver_id, new_route):
        time.sleep(0.5)
        return f"Driver {driver_id} has been rerouted to: {new_route}. Estimated time savings: {random.randint(5, 15)} minutes."
    
    def get_nearby_merchants(self, location, cuisine):
        time.sleep(0.5)
        
        merchants = {
            "Chinese": ["Golden Dragon", "Panda Express", "China Palace"],
            "Italian": ["Mama Mia", "Italiano's", "Pasta Paradise"],
            "American": ["Burger King", "McDonald's", "Wendy's"],
            "Mexican": ["Taco Bell", "Chipotle", "Qdoba"]
        }
        
        if cuisine in merchants:
            options = merchants[cuisine]
            return f"Nearby {cuisine} restaurants in {location}: {', '.join(options)}"
        else:
            return f"No {cuisine} restaurants found nearby. Try a different cuisine type."
    
    def initiate_mediation_flow(self, order_id):
        time.sleep(0.5)
        return f"Mediation flow initiated for order {order_id}. Both driver and customer have been notified to provide evidence."
    
    def collect_evidence(self, order_id, question):
        time.sleep(0.5)
        
        responses = {
            "Was the bag sealed by the merchant?": ["Yes", "No"],
            "Was the seal intact upon handover?": ["Yes", "No", "Partially"],
            "Please describe the damage": ["Spilled drink", "Crushed packaging", "Missing items"]
        }
        
        if question in responses:
            response = random.choice(responses[question])
            return f"For order {order_id}, question '{question}': {response}"
        else:
            return f"No predefined response for question: {question}"
    
    def analyze_evidence(self, evidence):
        time.sleep(0.5)
        
        # Simple evidence analysis simulation
        if "sealed: Yes" in evidence and "intact: No" in evidence:
            return "Evidence suggests driver mishandling. Driver is at fault."
        elif "sealed: No" in evidence:
            return "Evidence suggests merchant packaging issue. Merchant is at fault."
        else:
            return "Evidence is inconclusive. Further investigation needed."
    
    def issue_instant_refund(self, order_id, amount):
        time.sleep(0.5)
        return f"Instant refund of ${amount} issued for order {order_id}. Customer has been notified."
    
    def exonerate_driver(self, driver_id):
        time.sleep(0.5)
        return f"Driver {driver_id} has been exonerated of fault. No penalty will be applied to their record."
    
    def log_merchant_packaging_feedback(self, merchant_id, feedback):
        time.sleep(0.5)
        return f"Packaging feedback logged for merchant {merchant_id}: {feedback}"
    
    def notify_resolution(self, order_id, resolution):
        time.sleep(0.5)
        return f"Resolution notified for order {order_id}: {resolution}"
    
    def contact_recipient_via_chat(self, order_id, message):
        time.sleep(0.5)
        
        responses = [
            "I'm not home. Please leave it with the concierge.",
            "I'll be there in 5 minutes. Please wait.",
            "Please reschedule for tomorrow.",
            "You can leave it at the door."
        ]
        
        response = random.choice(responses)
        return f"Message sent to recipient for order {order_id}: '{message}'. Response: '{response}'"
    
    def suggest_safe_drop_off(self, order_id, location):
        time.sleep(0.5)
        return f"Safe drop-off location suggested for order {order_id}: {location}. Waiting for customer confirmation."
    
    def find_nearby_locker(self, location):
        time.sleep(0.5)
        
        lockers = [
            "LockerHub - 123 Main St (0.3 miles)",
            "ParcelPoint - 456 Oak Ave (0.5 miles)",
            "SafeDrop - 789 Pine Rd (0.7 miles)"
        ]
        
        return f"Nearby parcel lockers at {location}: {', '.join(lockers)}"
    
    def calculate_alternative_route(self, origin, destination, avoid):
        time.sleep(0.5)
        
        time_savings = random.randint(5, 25)
        return f"Alternative route calculated from {origin} to {destination}, avoiding {avoid}. Estimated time savings: {time_savings} minutes."
    
    def notify_passenger_and_driver(self, trip_id, message):
        time.sleep(0.5)
        return f"Notification sent to both passenger and driver for trip {tripid}: '{message}'"
    
    def check_flight_status(self, flight_number):
        time.sleep(0.5)
        
        statuses = [
            "On time",
            "Delayed by 15 minutes",
            "Delayed by 30 minutes",
            "Delayed by 1 hour",
            "Cancelled"
        ]
        
        status = random.choice(statuses)
        return f"Flight {flight_number} status: {status}"