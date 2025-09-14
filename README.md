
<p align="center">
  <img src="<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/658210a6-f8b3-4cbf-889b-1669410e24bd" />
" alt="Grab Logo" width="200"/>
</p>

# Project Synapse 🚀  
**Agentic Last-Mile Coordinator for GrabHack Hackathon**  

🔗 **Live Demo:** [Synapse on Render](https://synapse-rej4.onrender.com/)  

---

## 🌍 Problem  
Last-mile delivery faces **real-time disruptions** (traffic jams, unavailable merchants, incorrect addresses) that static rule-based systems cannot handle, leading to **delays and inefficiency**.  

---

## 💡 Vision  
An **autonomous AI agent** that goes beyond flagging errors. It:  
- **Reasons** about the situation  
- **Selects tools** (simulated logistics APIs)  
- **Formulates multi-step plans** to resolve disruptions in real-time  

---

## ⚙️ Tech Stack  
- **LLM Backend:** Hugging Face API (instead of OpenAI)  
- **Frameworks:** LangChain / LangGraph  
- **Core Skills:** Prompt Engineering, Agentic Frameworks  
- **Frontend:** Deployed with Render  

---

## 🔑 Key Features  
- Accepts disruption scenarios as **natural language input**  
- Shows **transparent reasoning process** (agent’s chain-of-thought)  
- Uses simulated tools like:  
  - `check_traffic()`  
  - `get_merchant_status()`  
  - `notify_customer()`  
  - `initiate_mediation_flow()`  
  - `suggest_safe_drop_off()`  

---

## 🚀 Quick Start  

### 1. Clone the repository  
```bash
git clone https://github.com/arry-codes/synapse.git
cd synapse
```

### 2. Install dependencies  
```bash
npm install
```

### 3. Set up environment variables  
Create a `.env` file in the root directory and add your **Hugging Face API key**:  
```env
HUGGINGFACE_API_KEY=your_api_key_here
```

### 4. Run the project  
```bash
npm run dev
```

The app will now be available at **http://localhost:3000** 🎉  

---

## 🚚 Example Use Cases in Grab Ecosystem  
- **GrabFood / GrabMart:** Handle overloaded restaurants, disputes at doorstep  
- **GrabExpress:** Manage unavailable recipients & suggest lockers/safe drops  
- **GrabCar:** Re-route trips in case of sudden traffic jams  

---

## 📜 Expected Outcomes  
- Functional proof-of-concept agent  
- Reasoning + action log visible  
- Logical resolution of multiple disruption scenarios  
- Well-documented codebase  

---

👨‍💻 Built with ❤️ for **GrabHack Hackathon**  
