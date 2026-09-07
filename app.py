import gradio as gr
from workflow import run_decision_pipeline

def create_ui():
    with gr.Blocks(title="AI Decision Assistant") as demo:
        gr.Markdown("# 🧠 Workflow AI Decision Assistant")
        gr.Markdown("Step-by-step automated decision analysis powered by Groq & LangChain.")

        with gr.Row():
            with gr.Column(scale=1):
                groq_key_input = gr.Textbox(
                    label="Groq API Key (Optional if set in environment)",
                    placeholder="gsk_...",
                    type="password"
                )
                situation_input = gr.Textbox(
                    label="1. Describe your Situation / Decision Problem",
                    placeholder="e.g., Should I quit my job to start a startup, or study for a master's degree abroad?",
                    lines=4
                )
                priority_input = gr.Textbox(
                    label="2. Main Priorities / Constraints (Optional)",
                    placeholder="e.g., Low financial risk, high long-term growth, 1-year timeline",
                    lines=2
                )
                submit_btn = gr.Button("🚀 Start Decision Workflow", variant="primary")

            with gr.Column(scale=2):
                output_markdown = gr.Markdown(label="Analysis Result")

        submit_btn.click(
            fn=run_decision_pipeline,
            inputs=[situation_input, priority_input, groq_key_input],
            outputs=[output_markdown]
        )
    return demo

app = create_ui()

if __name__ == "__main__":
    app.launch()