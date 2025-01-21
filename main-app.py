import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI
import yaml
from datetime import datetime
import requests
import json
from pathlib import Path

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

class MarketResearchAgent:
    def __init__(self):
        self.client = client
        
    def generate_market_insights(self, query, analysis_type="summary"):
        """Generate market insights using OpenAI's GPT model"""
        depth_prompts = {
            "summary": "Provide a brief summary of ",
            "in-depth": "Provide a detailed analysis of ",
            "prediction": "Analyze current trends and predict future developments for "
        }
        
        prompt = f"{depth_prompts[analysis_type]}{query}. Include key metrics, trends, and insights."
        
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a market research expert. Provide analytical, data-driven insights."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    def generate_swot_analysis(self, company_name):
        """Generate SWOT analysis for a given company"""
        prompt = f"Provide a detailed SWOT analysis for {company_name}."
        
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "Generate a professional SWOT analysis with specific, actionable points."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

def main():
    st.set_page_config(page_title="Market Research AI Agent", layout="wide")
    
    st.title("AI Market Research Assistant")
    
    # Initialize the agent
    agent = MarketResearchAgent()
    
    # Sidebar for analysis options
    st.sidebar.header("Analysis Options")
    analysis_type = st.sidebar.selectbox(
        "Select Analysis Type",
        ["summary", "in-depth", "prediction"]
    )
    
    # Main query input
    query = st.text_input("Enter your market research query:")
    
    # File upload option
    uploaded_file = st.file_uploader("Upload market data (CSV)", type=['csv'])
    
    if st.button("Generate Insights"):
        if query:
            with st.spinner("Generating insights..."):
                insights = agent.generate_market_insights(query, analysis_type)
                st.markdown("### Market Insights")
                st.write(insights)
                
                # Generate and display SWOT analysis if company name is provided
                if "company" in query.lower() or "organization" in query.lower():
                    company_name = query.split()[-1]  # Simplified company name extraction
                    st.markdown("### SWOT Analysis")
                    swot = agent.generate_swot_analysis(company_name)
                    st.write(swot)
        
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.markdown("### Data Analysis")
            st.dataframe(df.head())
            
            # Basic data visualization
            if len(df.columns) >= 2:
                numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                if len(numeric_cols) >= 2:
                    fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1],
                                   title="Data Visualization")
                    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
