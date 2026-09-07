from config import get_llm_instance
import prompts

def run_decision_pipeline(user_input: str, priorities: str, api_key: str) -> str:
    """
    Executes the 6-step decision workflow sequentially.
    Passes output of each step as context into the next step.
    """
    if not user_input or not user_input.strip():
        return "⚠️ Please describe your situation or problem first."

    try:
        # Initialize LLM instance
        llm = get_llm_instance(api_key)
        priorities_clean = priorities.strip() if priorities and priorities.strip() else "Standard balance of risk, time, and reward."

        # Step 1 Execution
        res1 = (prompts.PROMPT_STEP_1 | llm).invoke({"user_input": user_input}).content

        # Step 2 Execution
        res2 = (prompts.PROMPT_STEP_2 | llm).invoke({"step1_output": res1}).content

        # Step 3 Execution
        res3 = (prompts.PROMPT_STEP_3 | llm).invoke({"step2_output": res2}).content

        # Step 4 Execution
        res4 = (prompts.PROMPT_STEP_4 | llm).invoke({"step3_output": res3, "priorities": priorities_clean}).content

        # Step 5 Execution
        res5 = (prompts.PROMPT_STEP_5 | llm).invoke({"step4_output": res4}).content

        # Step 6 Execution
        res6 = (prompts.PROMPT_STEP_6 | llm).invoke({
            "step1_output": res1,
            "step5_output": res5,
            "priorities": priorities_clean
        }).content

        # Structured Output Assembly
        return f"""
# 🎯 AI Decision Analysis Report

### 📌 Step 1: Root Problem Identification
{res1}

---
### 💡 Step 2: Available Options
{res2}

---
### 🔍 Step 3: Pros, Cons & Risk Analysis
{res3}

---
### ⚖️ Step 4: Options Comparison
{res4}

---
### 🛡️ Step 5: Logical Review & Critical Check
{res5}

---
### 🏆 Step 6: Final Recommendation
{res6}
"""

    except Exception as e:
        return f"❌ Error executing workflow: {str(e)}"
