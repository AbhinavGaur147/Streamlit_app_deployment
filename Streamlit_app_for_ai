import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="A.I. Nexus",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for a Futuristic Look ---
def load_css():
    """Inject custom CSS for styling the app."""
    st.markdown("""
        <style>
            /* Main app background and font */
            .stApp {
                background: #000428;  /* fallback for old browsers */
                background: -webkit-linear-gradient(to right, #004e92, #000428);  /* Chrome 10-25, Safari 5.1-6 */
                background: linear-gradient(to right, #004e92, #000428); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
                color: #e0e0e0;
            }

            /* Sidebar styling */
            [data-testid="stSidebar"] {
                background-color: rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
                border-right: 1px solid rgba(0, 240, 255, 0.2);
            }

            /* Chat input styling */
            [data-testid="stChatInput"] {
                background-color: transparent;
            }
            .st-emotion-cache-1c7y2kd { /* Input box */
                background-color: rgba(255, 255, 255, 0.05);
                color: #00f0ff;
                border: 1px solid rgba(0, 240, 255, 0.5);
            }

            /* Button styling */
            .stButton>button {
                background-color: transparent;
                color: #00f0ff;
                border: 1px solid #00f0ff;
                border-radius: 20px;
                transition: all 0.3s ease;
                padding: 10px 20px;
            }
            .stButton>button:hover {
                background-color: #00f0ff;
                color: #0a0a1a;
                box-shadow: 0 0 15px #00f0ff, 0 0 25px #00f0ff;
            }
            
            /* Title with glow effect */
            .title-glow {
                font-size: 3.5rem;
                font-weight: bold;
                color: #ffffff;
                text-align: center;
                margin-top: 20px;
                margin-bottom: 0px;
                text-shadow: 0 0 10px #00f0ff, 0 0 20px #00f0ff, 0 0 30px #00f0ff;
                animation: glow 1.5s ease-in-out infinite alternate;
            }
            
            @keyframes glow {
                from {
                    text-shadow: 0 0 10px #00f0ff, 0 0 20px #00f0ff, 0 0 30px #00f0ff;
                }
                to {
                    text-shadow: 0 0 20px #00f0ff, 0 0 30px #00aaff, 0 0 40px #00aaff;
                }
            }

            /* Subtitle styling */
            .subtitle {
                text-align: center;
                color: #c0c0c0;
                font-style: italic;
                margin-bottom: 40px;
            }
            
            /* Agent message styling */
            [data-testid="stChatMessage"]:has(.agent-avatar) {
                 background-color: rgba(0, 78, 146, 0.2);
                 border-radius: 10px;
                 padding: 10px;
                 border: 1px solid rgba(0, 240, 255, 0.2);
            }

        </style>
    """, unsafe_allow_html=True)

# --- Agent Logic Placeholder ---
# In the future, you can define different agent classes/functions here.
def get_agent_response(agent_name, user_prompt):
    """
    A placeholder function to simulate an agent's response.
    Replace this with actual calls to your AI agent logic.
    """
    # Simulate thinking delay
    time.sleep(1.5)
    
    if agent_name == "Echo Bot":
        return f"Echoing your message: '{user_prompt}'"
    elif agent_name == "Data Analyst":
        return f"Analyzing data related to '{user_prompt}'... The results are promising."
    elif agent_name == "Creative Writer":
        return f"Weaving a tale about '{user_prompt}'... Once upon a time, in a digital realm..."
    else:
        return f"I am {agent_name}. I have received your message: '{user_prompt}'"


# --- UI Rendering ---

# Call the CSS loader
load_css()

# Main Header
st.markdown('<h1 class="title-glow">A.I. Nexus</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Central Hub for Intelligent Agents</p>', unsafe_allow_html=True)


# Sidebar for Agent Selection and Controls
with st.sidebar:
    st.image("https://www.gstatic.com/lamda/images/sparkle_resting_v2_darkmode_23a733772591a615418f4a86f90117b9.gif", width=100)
    st.markdown("## Agent Control Panel")
    
    # In a real app, you would load these from a config or dynamically
    available_agents = ["Nexus Assistant", "Data Analyst", "Creative Writer", "Echo Bot"]
    
    selected_agent = st.selectbox(
        "Select an AI Agent",
        options=available_agents,
        index=0,
        help="Choose the specialized AI agent to interact with."
    )
    
    st.markdown("---")
    st.markdown("### Agent Settings")
    
    # Placeholder for future agent settings
    creativity_level = st.slider("Creativity Level", 0.0, 1.0, 0.5, 0.1)
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        if message["role"] == "assistant":
             st.markdown(f'<div class="agent-avatar">{message["content"]}</div>', unsafe_allow_html=True)
        else:
             st.markdown(message["content"])


# Main Chat Interface
if prompt := st.chat_input(f"Message {selected_agent}..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Display agent response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            # This is where you would call your actual agent logic
            response = get_agent_response(selected_agent, prompt)
            st.markdown(f'<div class="agent-avatar">{response}</div>', unsafe_allow_html=True)
    
    # Add agent response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Welcome message if chat is empty
if not st.session_state.messages:
    st.info("Welcome to the A.I. Nexus! Select an agent from the sidebar and start your conversation.")
