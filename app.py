
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama
import os


# AI-Powered Insights using Mistral through Ollama
def generate_ai_insights(df_summary):
    prompt = f"""
    Analyze the following dataset summary and provide useful insights.

    Explain:
    1. Important patterns
    2. Numerical observations
    3. Missing-value information
    4. Possible relationships between variables
    5. Interesting findings

    Keep the explanation simple and easy to understand.

    Dataset Summary:
    {df_summary}
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


# Generate Data Visualizations
def generate_visualizations(df):
    plot_paths = []

    # Histograms for numerical columns
    for col in df.select_dtypes(include=["number"]).columns:

        plt.figure(figsize=(6, 4))

        sns.histplot(
            df[col],
            bins=30,
            kde=True
        )

        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")

        path = f"{col}_distribution.png"

        plt.savefig(path, bbox_inches="tight")
        plt.close()

        plot_paths.append(path)

    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=["number"])

    if not numeric_df.empty and len(numeric_df.columns) > 1:

        plt.figure(figsize=(8, 5))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            linewidths=0.5
        )

        plt.title("Correlation Heatmap")

        path = "correlation_heatmap.png"

        plt.savefig(path, bbox_inches="tight")
        plt.close()

        plot_paths.append(path)

    return plot_paths


# Perform EDA
def eda_analysis(file_path):

    if file_path is None:
        return "Please upload a CSV file.", []

    # Load dataset
    df = pd.read_csv(file_path)

    # Fill missing numerical values
    for col in df.select_dtypes(include=["number"]).columns:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values
    for col in df.select_dtypes(include=["object"]).columns:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Dataset information
    summary = df.describe(include="all").to_string()

    # Missing values
    missing_values = df.isnull().sum().to_string()

    # AI insights
    try:
        insights = generate_ai_insights(summary)
    except Exception as e:
        insights = f"Ollama Error: {str(e)}"

    # Generate visualizations
    plot_paths = generate_visualizations(df)

    # Final report
    report = f"""
DATA LOADED SUCCESSFULLY!

Dataset Shape:
{df.shape}

COLUMN INFORMATION:
{df.dtypes.to_string()}

SUMMARY:
{summary}

MISSING VALUES:
{missing_values}

AI-GENERATED INSIGHTS:
{insights}
"""

    return report, plot_paths


# Gradio Interface
with gr.Blocks() as demo:

    gr.Markdown(
        """
        # 📊 LLM-Powered Exploratory Data Analysis

        Upload a CSV dataset and automatically generate:

        - 📋 Dataset Summary
        - 🔍 Missing Value Analysis
        - 📈 Data Visualizations
        - 🤖 AI-Generated Insights using Mistral + Ollama
        """
    )

    file_input = gr.File(
        label="Upload CSV Dataset",
        file_types=[".csv"],
        type="filepath"
    )

    analyze_button = gr.Button(
        "🚀 Analyze Dataset"
    )

    report_output = gr.Textbox(
        label="📋 EDA Report",
        lines=25
    )

    gallery_output = gr.Gallery(
        label="📊 Data Visualizations",
        columns=2,
        rows=2,
        height="auto"
    )

    analyze_button.click(
        fn=eda_analysis,
        inputs=file_input,
        outputs=[report_output, gallery_output]
    )


# Launch Application
if __name__ == "__main__":
    demo.launch(share=True)

