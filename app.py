from flask import Flask, render_template, request, jsonify
from agents.delivery_agent import DeliveryAgent
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolve', methods=['POST'])
def resolve_scenario():
    data = request.json
    scenario = data.get('scenario', '')
    
    if not scenario:
        return jsonify({'error': 'No scenario provided'}), 400
    
    # Initialize the agent
    agent = DeliveryAgent()
    
    # Process the scenario
    try:
        result = agent.process_scenario(scenario)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug=True)
