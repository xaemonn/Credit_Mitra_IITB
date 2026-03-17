# CreditMitra  
### India’s Privacy-Preserving Agentic AI System for Automated Credit Underwriting  

---

##  Overview  
CreditMitra is an AI-powered system designed to automate **credit underwriting** from **heterogeneous bank statements** while ensuring **user privacy**.

Traditional systems rely on:
- Manual review  
- Expensive third-party tools (e.g., Perfios)  
- Static credit risk models  

 CreditMitra solves this using:
- Agentic AI pipeline  
- Distributed LLM architecture  
- Privacy-preserving techniques  

---

##  Problem Statement  

Indian bank statements:
- Have **no standard format**
- Contain **noisy transaction descriptions**
-  Require **manual or rule-based parsing**
-  Pose **privacy risks via third-party tools**

Additionally:
- Only ~10% transactions are **merchant-related**
- Credit models are **static** and outdated

---

## 💡 Our Solution  

CreditMitra introduces a **dynamic, privacy-first AI pipeline**:

-  Extract structured data from unstructured bank statements  
-  Identify payees using fine-tuned SLMs  
-  Classify transactions into merchant/non-merchant  
-  Integrate real-time merchant insights into credit scoring  
-  Preserve privacy using Differential Privacy + on-device processing  
-  Use distributed LLMs for scalability and low latency  

---

## 🧩 Key Features  

- Bank statement parsing across formats  
- Payee extraction from transaction strings  
- Merchant classification (High Recall Model)  
- Real-time merchant intelligence  
-  Dynamic credit risk modeling  
-  Privacy-preserving AI (DP-SGD, on-device inference)  
-  Distributed LLM architecture  
- Merchant caching using vector database  

---

##  System Architecture  

> Add architecture diagram here  

The system consists of:
- On-device lightweight SLMs  
- Backend LLM nodes  
- Merchant knowledge base + LangSearch fallback  
- Secure processing pipeline  

---

## 🔄 Pipeline  

> Add pipeline diagram here  

1. Upload bank statement  
2. Extract transaction data  
3. Identify payees  
4. Classify merchants  
5. Fetch merchant details (LLM / LangSearch)  
6. Update credit risk model  
7. Generate insights  

---

## 📊 Prototype  

> Add UI screenshot here  

We have developed an initial prototype where:
- Users upload bank statements  
- Transactions are automatically categorized  
- Insights are generated in real-time  

---

## 🛠️ Tech Stack  

- **AI/ML**: LLMs, SLMs, DP-SGD  
- **NLP**: Payee extraction, classification  
- **Backend**: Distributed architecture  
- **Database**: Vector DB for merchant storage  
- **Privacy**: Differential Privacy frameworks  
- **Tools**: LangSearch (RAG-based retrieval)  

---

## 📅 Project Roadmap  

| Phase | Description |
|------|------------|
| Phase 1 | Dataset collection & pipeline setup |
| Phase 2 | SLM fine-tuning (payee + classification) |
| Phase 3 | Merchant extraction pipeline |
| Phase 4 | Dynamic credit risk modeling |
| Phase 5 | End-to-end testing & optimization |
| Phase 6 | GUI & scalable deployment |

---

## ⚠️ Challenges  

- Limited availability of real bank datasets  
- Highly imbalanced merchant vs non-merchant data  
- High compute cost for SLM fine-tuning  
- Privacy risks in financial data  

---

## 🔐 Privacy & Security  

- On-device processing of sensitive data  
- Differential Privacy (DP-SGD)  
- No raw financial data leakage  
- Compliant with:
  - RBI guidelines  
  - GDPR  
  - SOC2  

---

## 👥 Team  

- **Disha Kwatra** (Team Lead)  
- Gargi Kalia  
- Shivansh Katiyar  

**Mentors:**  
- Dr. Sandesh Jain  
- Dr. Somesh Kumar  

---

## 📌 Future Scope  

- Integration with banks/NBFCs  
- Real-time underwriting APIs  
- Fraud detection modules  
- Expansion to global financial systems  

---

##  Why CreditMitra?  

- 91% merchant classification accuracy  
- Privacy-first AI  
- Faster & cheaper than existing solutions  
- Dynamic & adaptive credit scoring  

---

## 📎 References  

- TabSniper (Bank statement parsing)  
- RAG (Retrieval-Augmented Generation)  
- Differential Privacy in LLMs  
- LangSearch  

---
