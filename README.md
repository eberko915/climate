# Parametric Climate Insurance Decision Prototype

This project was inspired by the work of Arbol which operates at the forefront of parametric climate isnurance. Using synthetic climate and claims data to automate payout decisions, I mimicked a simplified workflow of an Arbol insurance claim. While I have significant geospatial analysis experience, I had not yet delved into the mechanics of insurance payouts and wanted to devise a mini-project to learn more. This project blends structured environmental data with unstructured natural language claims to mirror real-world operations at platforms like Arbol.

---

## Key Features of the Streamlit app

- **Rolling climate triggers**: Detects streaks of extreme heat or rainfall using customizable rolling window logic.
- **Claim classification**: Rule-based classifier analyzes synthetic claim text to determine if a payout-worthy event is described.
-  **Payout merger logic**: Combines trigger and claim outputs to simulate final insurance decisions.
-  **Streamlit app**: Upload data, adjust thresholds, and get instant feedback on triggered payouts 
---

##  Why This Matters

**Parametric insurance** provides automatic, data-driven payouts based on objective triggers like rainfall or temperature. No human adjustment needed. This project simulates that process — ideal for climate-vulnerable areas or fast, scalable underwriting.

---

## Future Work 

- **Add AI-powered claim classification**
- **Include probabalisitic models**
- **Integrate with real climate data, specifically an API**



