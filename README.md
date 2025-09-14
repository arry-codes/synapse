
<p align="center">
  <img width="200" height="100" alt="image" src="https://github.com/user-attachments/assets/8c9c89f5-d7c0-4da3-891d-29d61f441acb" />
</p>

# Project Synapse 🚀  
**Agentic Last-Mile Coordinator for GrabHack Hackathon**  

🔗 **Live Demo :** [https://synapse-rej4.onrender.com/]( https://synapse-rej4.onrender.com)


## 🌍 Problem  
Last-mile delivery faces **real-time disruptions** (traffic jams, unavailable merchants, incorrect addresses) that static rule-based systems cannot handle, leading to **delays and inefficiency**.  


## 💡 Vision  
An **autonomous AI agent** that goes beyond flagging errors. It:  
- **Reasons** about the situation  
- **Selects tools** (simulated logistics APIs)  
- **Formulates multi-step plans** to resolve disruptions in real-time  


## ⚙️ Tech Stack  
- **LLM Backend:** Hugging Face API
- **Frameworks:** LangChain / LangGraph  
- **Core Skills:** Prompt Engineering, Agentic Frameworks  
- **Frontend:** Deployed with Render  


## 🔑 Key Features  
- Accepts disruption scenarios as **natural language input**  
- Shows **transparent reasoning process** (agent’s chain-of-thought)  
- Uses simulated tools like:  
  - `check_traffic()`  
  - `get_merchant_status()`  
  - `notify_customer()`  
  - `initiate_mediation_flow()`  
  - `suggest_safe_drop_off()`  


## 🚀 Quick Start  

### 1. Clone the repository  
```bash
git clone https://github.com/arry-codes/synapse.git
cd synapse
```

### 2. Install dependencies  
```bash
pip install requirements.txt
```

### 3. Set up environment variables  
Create a `.env` file in the root directory and add your **Hugging Face API key**:  
```env
HUGGINGFACE_API_KEY=your_api_key_here
```

### 4. Run the file app.py


## 🚚 Example Use Cases in Grab Ecosystem  
- **GrabFood / GrabMart:** Handle overloaded restaurants, disputes at doorstep  
- **GrabExpress:** Manage unavailable recipients & suggest lockers/safe drops  
- **GrabCar:** Re-route trips in case of sudden traffic jams


## 📜 Expected Outcomes 

- Functional proof-of-concept agent  
- Reasoning + action log visible  
- Logical resolution of multiple disruption scenarios  
- Well-documented codebase

## 👥 Collaborators  

- Kavish Bishnoi - [@kavish1919](https://github.com/kavish1919)
- Mayank Agarwal – [#](https://github.com/arry-codes)  

---
<img width="1440" height="900" alt="Screenshot 2025-09-14 at 7 14 21 AM" src="https://github.com/user-attachments/assets/ef29bccd-8f2a-4400-9aba-1329355a3cb0" />
<img width="1440" height="900" alt="Screenshot 2025-09-14 at 7 14 14 AM" src="https://github.com/user-attachments/assets/711e0422-f743-4fff-88c9-1de5296d5a2c" />
<div align="center"> 👨‍💻 Built with ❤️ for GrabHack Hackathon </div>
