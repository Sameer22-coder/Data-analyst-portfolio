
import streamlit as st
from pathlib import Path
import html

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
        page_title="Data Prism Portfolio",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>
.stApp {
    background-color: #0F172A;
}

h1, h2, h3, h4 {
    color: #94EAF5;
}

p, li, label {
    color: #CBD5E1;
    background-color: #0F172A;
}

.hero {
    padding: 40px 20px;
    text-align: center=Left;
}

.hero h1 {
    color: #94EAF5;
    font-size: 3rem;
    margin-bottom: 1px;
}

.hero h3 {
    color: #FFFFFF;
}

.hero p {
    color: #CBD5E1;
    font-size: 1.05rem;
    line-height: 1.8;
    max-width: 1500px;
    margin: 5px auto;
}

.skill-card {
    background-color: #204b6f;
    border-radius: 80px;
    padding: 20px;
    text-align: center;
    margin: 2px;
    color: #E2E8F0;
}

.project-card {
    background: linear-gradient(145deg, #172442, #111A30);
    border: 1px solid #263B5C;
    border-radius: 18px;
    padding: 24px;
    min-height: 250px;
    height: 100%;
    box-sizing: border-box;
    margin-bottom: 20px;
    overflow-wrap: break-word;
}

.project-card h3 {
    color: #FFFFFF;
    font-size: 1.15rem;
    margin-top: 0;
    margin-bottom: 16px;
}

.project-card p {
    color: #E2E8F0;
    font-size: 1rem;
    line-height: 1.7;
}

.project-tools {
    margin-top: 18px;
    color: #94EAF5 !important;
    font-size: 0.9rem !important;
}

.timeline {
    background-color: #111A30;
    border-left: 3px solid #38BDF8;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
}

.timeline h3 {
    color: #94EAF5;
}

.footer {
    text-align: center;
    padding: 25px 10px;
    color: #94A3B8;
}

.stButton > button,
.stDownloadButton > button {
    background-color: #2563EB;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #1D4ED8;
    color: #FFFFFF;
}

.bottom-links {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    padding: 25px 0;
    margin-top: 20px;
    margin-bottom: 20px;
}

.bottom-links a {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 42px;
    padding: 10px 16px;
    border: 1px solid #334155;
    border-radius: 8px;
    background-color: #131923;
    color: #E2E8F0;
    text-decoration: none;
    text-align: center;
    font-size: 14px;
    box-sizing: border-box;
}

.bottom-links a:hover {
    background-color: #1E293B;
    border-color: #38BDF8;
    color: #94EAF5;
}

@media (max-width: 640px) {
    .bottom-links {
        flex-direction: column;
        gap: 10px;
    }

    .bottom-links a {
        width: 100%;
    }
}

</style>
""", unsafe_allow_html=True)    
# ----------------------
# HERO SECTION
# ----------------------
st.markdown("""
<div class='hero'>
<h5>Sameer Patil - Data Analyst | MIS Analyst | Business Intelligence Analyst</h5>
<h1>
Transforming Data into Insights.Insights into Impact.
</h1>   

</div>
""", unsafe_allow_html=True)
st.divider()

# =====================================================
# ABOUT ME
# =====================================================

st.header("👨‍💼 About Me")

st.write("""
Hi there! I'm a Data Analyst who enjoys turning raw data into meaningful insights. I specialize in exploring datasets, uncovering patterns, and building interactive dashboards that make complex information easier to understand. I take pride in maintaining data accuracy, solving analytical challenges, and paying attention to the details that turn good analysis into valuable business insights. I enjoy working at the intersection of data, technology, and business, where analytical thinking meets practical problem-solving.

Currently, I'm working at **Tata Consultancy Services (TCS)**, where I focus on data validation, large-scale data processing, and Python-based automation to improve data quality and streamline operational workflows. Previously, as a Data Analyst Intern, I worked with SQL, Python, Power BI, and Excel to analyze datasets, explore trends, and develop data-driven visualizations. Across my professional experience and projects, I enjoy combining technical skills with curiosity to transform complex data into clear, actionable insights that support better decision-making.""")

st.divider()


# =====================================================
# TECHNICAL SKILLS
# =====================================================

st.header("🛠 Technical Skills")

# Exactly five skills per category.
skills = {
    "Advanced Excel & Data Analysis": [
        "Data Cleaning",
        "Data Validation",
        "Charts & Dashboards",
        "Power Pivot"
    ],

    "SQL, Python & Data Management": [
        "Joins & Subqueries",
        "Window Functions",
        "Python",
        "Pandas"
    ],

    "Data Visualization & Business Intelligence": [
        "Data Modeling",
        "Tableau",
        "Matplotlib",
        "Seaborn"
    ]
}

NUM_COLUMNS = 4

for category, items in skills.items():
    st.subheader(category)

    # Display four cards per row.
    # Center the remaining cards in the final row.
    for start in range(0, len(items), NUM_COLUMNS):
        row_items = items[start:start + NUM_COLUMNS]
        cols = st.columns(NUM_COLUMNS, gap="medium")

        if len(row_items) < NUM_COLUMNS:
            start_col = (NUM_COLUMNS - len(row_items)) // 2
        else:
            start_col = 0

        for i, skill in enumerate(row_items):
            with cols[start_col + i]:
                st.markdown(
                    f'<div class="skill-card">'
                    f'{html.escape(skill)}'
                    f'</div>',
                    unsafe_allow_html=True
                )

st.divider()


# =====================================================
# PROJECTS
# =====================================================

st.header("📊 Projects")

# To add a project later, add another dictionary to this list.
# Keep the same keys: name, description, and tools.

projects = [
    {
        "name": "Sales Analytics Dashboard",
        "description": (
            "An interactive dashboard to analyze sales performance, "
            "track revenue trends, monitor KPIs, and explore "
            "business performance."
        ),
        "tools": "Power BI, SQL, Excel"
    },
    {
        "name": "Customer Churn Analysis",
        "description": (
            "An analytical project focused on understanding customer "
            "churn patterns, exploring customer behavior, and identifying "
            "potential retention opportunities."
        ),
        "tools": "Python, Pandas, SQL"
    },
    {
        "name": "HR Analytics Dashboard",
        "description": (
            "A dashboard designed to explore workforce trends, "
            "analyze employee attrition, and present key human "
            "resource performance indicators."
        ),
        "tools": "Power BI, Excel"
    }
]

# Automatically creates a new row after every three projects.
for start in range(0, len(projects), 3):
    row_projects = projects[start:start + 3]
    cols = st.columns(3, gap="medium")

    for col, project in zip(cols, row_projects):
        with col:
            project_name = html.escape(project["name"])
            project_description = html.escape(project["description"])
            project_tools = html.escape(project["tools"])

            st.markdown(
                f"""
                <div class="project-card">
                    <h3>{project_name}</h3>
                    <p>{project_description}</p>
                    <p class="project-tools">
                        <strong>Tools:</strong> {project_tools}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

# =====================================================
# EXPERIENCE
# =====================================================

st.header("💼 Experience")

st.markdown("""
<div class="timeline">
    <h3>Software Configuration Expert (SCE)</h3>
    <p><strong>Tata Consultancy Services (TCS) · Mumbai, India - September 2025 Present</strong></p>
    <p>Supporting data-driven operational workflows through large-scale data processing, validation, and automation.</p>
    <ul>
        <li>Process and validate 100K–500K candidate records using Python and Excel, performing data cleaning, formatting, and consistency checks.</li>
        <li>Automate repetitive processing tasks using Python, Pandas, NumPy, and Excel-processing libraries.</li>
        <li>Apply rule-based analysis to candidate preferences and test-centre availability to support accurate allocation.</li>
        <li>Use SQL joins, filtering, and subqueries to retrieve and validate backend data.</li>
        <li>Collaborate with project managers and cross-functional teams to resolve data discrepancies and deliver accurate outputs.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline">
    <h3>Data Analyst Intern July 2024 – June 2025</h3>
    <p>Developed practical experience in SQL analytics, dashboard development, and Python-based data exploration.</p>
    <ul>
        <li>Analyzed and cleaned 100K+ healthcare records using MySQL to explore disease patterns and mortality-related trends.</li>
        <li>Built interactive Power BI dashboards using Power Query and DAX for KPI analysis and visualization.</li>
        <li>Processed and analyzed 300K+ COVID-19 records using Python data analysis libraries.</li>
        <li>Developed analytical case studies and presented findings through SQL analysis and data visualizations.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =====================================================
# BOTTOM NAVIGATION LINKS
# =====================================================

st.markdown("""
<div class="bottom-links">
    <a href="https://www.linkedin.com/in/sameerpatil0/"
       target="_blank">LinkedIn</a>
    <a href="https://github.com/Sameer22-coder/"
       target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    <p>© 2026 Sameer Patil | Data Analyst Portfolio</p>
    <p>Turning Data into Meaningful Insights</p>
</div>
""", unsafe_allow_html=True)
