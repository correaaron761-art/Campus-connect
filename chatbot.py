import streamlit as st
import re
from datetime import datetime

# CampusConnect Knowledge Base
KNOWLEDGE_BASE = {
    "greetings": [
        "Welcome to SJEC CampusConnect! Your digital ID and academic hub. How can I help? 😊",
        "Hi! CampusConnect here - attendance, notices, events, and more. What do you need?"
    ],
    "attendance": [
        "Scan your digital ID or check attendance via student portal. Current status: Present (Demo). Type 'my attendance' for details.",
        "Attendance marked via QR/ID scan. View full records at campusconnect.sjec.edu.in/attendance."
    ],
    "notices": [
        "Latest notices: 1) Exam timetable released (Dec 2025). 2) Cultural fest registration open. 3) Fee payment deadline: Jan 10, 2026.",
        "Check notice board: New hostel rules posted. Full list at campusconnect.sjec.edu.in/notices."
    ],
    "events": [
        "Upcoming: Treasure Hunt (Jan 5), Dance Workshop (Jan 8), Placement Drive (Jan 15). Register via student portal!",
        "Events calendar: Gamified PBL showcase next week. Details at campusconnect.sjec.edu.in/events."
    ],
    "id": [
        "Your Digital ID is active! Scan QR at entry points for attendance/hostel access. Lost ID? Visit admin portal.",
        "CampusConnect Digital ID: Auto-attendance + quick access to library/fees/placements."
    ],
    "fees": [
        "Fee status: Pending ₹15,000 (Demo). Pay via campusconnect.sjec.edu.in/fees. Last date: Jan 10.",
        "Semester fees: UG ₹45,000, PG ₹55,000. Student discounts available."
    ],
    "results": [
        "Latest results: Sem 3 - CGPA 8.2 (Demo). Check full marks at campusconnect.sjec.edu.in/results.",
        "Exam results published. Login with Digital ID to view."
    ],
    "library": [
        "Library: 5 books issued, 2 overdue. Renew via portal. New arrivals: C Programming books.",
        "Digital library access via CampusConnect ID."
    ],
    "placement": [
        "Placements: 75% placed (Demo). Next drive: TCS (Jan 15). Update resume in portal.",
        "Placement cell: Apply via campusconnect.sjec.edu.in/placements."
    ],
    "help": [
        "Commands: attendance, notices, events, id, fees, results, library, placement, bye.",
        "CampusConnect features: Digital ID scan, auto-attendance, gamified points, quick links."
    ]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Pattern matching for CampusConnect features
    if re.search(r'\b(hi|hello|hey|start)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["greetings"])
    elif re.search(r'\b(attendance|present|absent|status)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["attendance"])
    elif re.search(r'\b(notice|announcement|update)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["notices"])
    elif re.search(r'\b(event|fest|workshop|calendar)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["events"])
    elif re.search(r'\b(id|digital id|card|qr)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["id"])
    elif re.search(r'\b(fee|payment|due)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["fees"])
    elif re.search(r'\b(result|mark|grade|cgpa)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["results"])
    elif re.search(r'\b(library|book)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["library"])
    elif re.search(r'\b(placement|job|interview)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["placement"])
    elif re.search(r'\b(help|menu|features)\b', user_input):
        return random.choice(KNOWLEDGE_BASE["help"])
    elif re.search(r'\b(bye|exit|quit|thank)\b', user_input):
        return "Thanks for using CampusConnect! Your smart campus assistant. 👋"
    else:
        return "Sorry, try: attendance, notices, events, fees, results, or 'help'. Powered by CampusConnect!"

# Streamlit App
st.set_page_config(page_title="CampusConnect Chatbot", layout="wide")
st.title("🚀 SJEC CampusConnect Chatbot")
st.markdown("**Your Digital ID & Academic Assistant** - Attendance • Notices • Events • Fees & More")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to CampusConnect! Ask about attendance, notices, events, fees, or type 'help'."}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask about attendance, notices, events..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar info
with st.sidebar:
    st.header("📋 CampusConnect Features")
    st.markdown("""
    - **Digital ID**: QR scan for entry/attendance
    - **Attendance**: Auto-tracking + alerts
    - **Notices**: Real-time updates
    - **Events**: Registration + calendar
    - **Fees**: Payment status + reminders
    - **Results**: Semester marks + CGPA
    - **Gamification**: Points for engagement
    """)
    st.markdown("[Demo Data] For production: Connect to your database/API.[web:15]")
