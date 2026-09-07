import streamlit as st
from workflow import run_decision_pipeline

# Page Setup
st.set_page_config(
    page_title="AI Decision Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Decision Assistant")
st.markdown("Automated 6-Step Decision Analysis Workflow powered by Groq & LangChain.")

# Layout Columns
col_inputs, col_output = st.columns([1, 1.3], gap="large")

with col_inputs:
    st.subheader("📋 Decision Inputs")
    
    groq_key_input = st.text_input(
        "Groq API Key (Optional if set in Secrets)",
        type="password",
        placeholder="gsk_..."
    )
    
    situation_input = st.text_area(
        "1. Describe your Situation / Decision Problem",
        placeholder="e.g., Should I quit my job to start a startup, or study for a master's degree abroad?",
        height=150
    )
    
    priority_input = st.text_area(
        "2. Main Priorities / Constraints (Optional)",
        placeholder="e.g., Low financial risk, high long-term growth, 1-year timeline",
        height=90
    )
    
    submit_btn = st.button("🚀 Start Decision Workflow", type="primary", use_container_width=True)

with col_output:
    st.subheader("🎯 Analysis Result")
    
    if submit_btn:
        if not situation_input.strip():
            st.warning("⚠️ Please describe your situation/problem first.")
        else:
            with st.spinner("⏳ Running 6-step AI Decision Workflow... Please wait..."):
                # Execute Workflow
                result = run_decision_pipeline(
                    user_input=situation_input,
                    priorities=priority_input,
                    api_key=groq_key_input
                )
                
                if result.startswith("❌") or result.startswith("⚠️"):
                    st.error(result)
                else:
                    st.markdown(result)
    else:
        st.info("👈 Fill in your decision details on the left and click **Start Decision Workflow**.")
