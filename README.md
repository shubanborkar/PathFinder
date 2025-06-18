# 🧪 PathFinder AI: Student Career Pathway Recommender

![PathFinder AI Banner](https://cdn-icons-png.flaticon.com/512/3135/3135768.png)

> **Discover your ideal career path with the power of AI!**

---

## 🚀 Overview
PathFinder AI is an interactive, AI-powered web app that recommends career paths to students based on their interests, hobbies, and academic strengths. Built with Streamlit and Mistral LLM, it provides personalized, actionable guidance in a beautiful, modern UI.

---

## ✨ Features
- 🧑‍🎓 **Conversational career guidance**
- 🎨 **Modern, responsive UI** (dark mode, mobile-friendly)
- 🧠 **LLM-powered recommendations** (Mistral)
- 🗂️ **Predefined career clusters** (STEM, Arts, Sports, Business, Social Sciences)
- 💬 **Explanations for each recommended path**
- 🔄 **Reset and start over anytime**
- ☁️ **Easy deployment to Streamlit Cloud or Render**

---

## 🛠️ Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubanborkar/PathFinder.git
   cd PathFinder
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your Mistral API key:**
   ```bash
   export MISTRAL_API_KEY=your-mistral-key-here
   ```

---

## 💻 Usage

Run the app locally:
```bash
streamlit run streamlit_app.py
```

- Enter your interests, hobbies, and academic strengths.
- Click **Get Recommendations** to see personalized career paths and explanations.
- Use **Reset All** in the sidebar to start over.

---

## 🌐 Deployment

### **Streamlit Community Cloud (Recommended)**
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app from your repo.
3. Set `streamlit_app.py` as the main file.
4. Add your `MISTRAL_API_KEY` as a secret in the app settings.

### **Render**
1. Connect your GitHub repo to [Render](https://render.com/).
2. Use the following start command:
   ```bash
   streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
   ```
3. Add your API key as an environment variable.

---

## 📁 Project Structure

```
├── agent.py           # Core agent logic (LLM, mapping, explanations)
├── career_paths.py    # Career clusters and mapping logic
├── prompts.py         # Prompt templates
├── streamlit_app.py   # Main Streamlit web app
├── main.py            # CLI interface (optional)
├── requirements.txt   # Python dependencies
├── test_agent.py      # Simple test for agent logic
├── README.md          # This file
```

---

## 🙏 Credits
- **Developed by Shuban Borkar**
- Powered by [Mistral AI](https://mistral.ai/) and [Streamlit](https://streamlit.io/)
- UI icons from [Flaticon](https://flaticon.com/)
- GitHub: [shubanborkar](https://github.com/shubanborkar)
- Email: [shubanborkar@gmail.com](mailto:shubanborkar@gmail.com)
- LinkedIn: [shubanborkar](https://www.linkedin.com/in/shuban-borkar/)
---

## 📜 License
MIT 