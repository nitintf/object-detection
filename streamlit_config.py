"""Streamlit configuration and styling module."""

import streamlit as st


def init_page_config():
    """Initialize Streamlit page configuration."""
    st.set_page_config(
        page_title="Advanced Object Segmentation App",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": None,
            "Report a bug": None,
            "About": "Advanced Object Segmentation App - Powered by Streamlit",
        },
    )


def apply_custom_styles():
    """Apply custom CSS styles to the Streamlit app."""
    custom_css = """
    <style>
        /* Main container styling */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 95%;
        }
        
        /* Header styling */
        h1 {
            color: #1f77b4;
            margin-bottom: 0.5rem;
            font-size: 1.8rem;
        }
        
        h2 {
            color: #2c3e50;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
            font-size: 1.3rem;
        }
        
        h3 {
            color: #34495e;
            font-size: 1.1rem;
            margin-top: 0.25rem;
            margin-bottom: 0.25rem;
        }
        
        /* Sidebar styling */
        .css-1d391kg {
            padding-top: 2rem;
        }
        
        /* Compact tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
            margin-bottom: 0.25rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.25rem 0.75rem;
            font-size: 0.9rem;
        }
        
        /* Compact image spacing */
        .stImage {
            margin-top: 0.25rem;
            margin-bottom: 0.25rem;
        }
        
        /* Compact captions */
        .stCaption {
            margin-top: 0.1rem;
            margin-bottom: 0.25rem;
            font-size: 0.8rem;
        }
        
        /* Compact metrics */
        [data-testid="stMetricContainer"] {
            padding: 0.25rem 0;
            margin: 0.25rem 0;
        }
        
        /* Reduce spacing in column containers */
        [data-testid="column"] {
            padding: 0.25rem;
        }
        
        /* Compact subheader spacing */
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stVerticalBlock"] {
            gap: 0.25rem;
        }
        
        /* Button styling */
        .stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        .stButton > button:hover {
            background-color: #1565a0;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Metric cards styling */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.85rem;
        }
        
        /* Image container */
        .stImage > img {
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Reduce spacing in columns */
        .element-container {
            margin-bottom: 0.5rem;
        }
        
        /* Compact dividers */
        hr {
            margin: 0.5rem 0;
        }
        
        /* Success/Info boxes */
        .stSuccess {
            background-color: #d4edda;
            border-left: 4px solid #28a745;
        }
        
        .stInfo {
            background-color: #d1ecf1;
            border-left: 4px solid #17a2b8;
        }
        
        /* Code blocks */
        .stCodeBlock {
            border-radius: 5px;
        }
        
        /* Selectbox and input styling */
        .stSelectbox > div > div {
            background-color: white;
        }
        
        /* Progress bar styling */
        .stProgress > div > div > div {
            background-color: #1f77b4;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def init_app():
    """Initialize the Streamlit app with configuration and styles."""
    init_page_config()
    apply_custom_styles()
