from langchain_core.prompts import ChatPromptTemplate

# Step 1: Root Problem Identification
PROMPT_STEP_1 = ChatPromptTemplate.from_template("""
You are an expert AI Decision Assistant.
User Situation: {user_input}

Task (Step 1): Analyze the situation and clearly identify the root problem or core dilemma. Keep it focused and precise.
""")

# Step 2: Generate Options
PROMPT_STEP_2 = ChatPromptTemplate.from_template("""
Root Problem Identified: {step1_output}

Task (Step 2): Generate 3 to 4 realistic, actionable options/choices to solve this problem.
""")

# Step 3: Pros, Cons, Risks & Benefits
PROMPT_STEP_3 = ChatPromptTemplate.from_template("""
Options Available: {step2_output}

Task (Step 3): Analyze each option individually. Detail the Pros, Cons, Risks, and Long-term Benefits for each.
""")

# Step 4: Compare based on Priorities
PROMPT_STEP_4 = ChatPromptTemplate.from_template("""
Analysis of Options: {step3_output}
User Priorities / Constraints: {priorities}

Task (Step 4): Compare these options side-by-side using the user's priorities/constraints. Highlight trade-offs clearly.
""")

# Step 5: Logical Review & Self-Critique
PROMPT_STEP_5 = ChatPromptTemplate.from_template("""
Comparison Output: {step4_output}

Task (Step 5): Critically review the analysis so far. Identify missing risks, biased assumptions, or weak logical steps. Adjust the evaluation accordingly.
""")

# Step 6: Final Recommendation
PROMPT_STEP_6 = ChatPromptTemplate.from_template("""
Full Analysis & Review:
- Problem: {step1_output}
- Reviewed Comparison: {step5_output}
User Priorities: {priorities}

Task (Step 6): Provide the final, clear recommendation. State clearly WHICH option to pick and WHY, followed by 2 immediate next steps.
""")