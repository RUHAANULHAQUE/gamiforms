import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="FINX Career Form",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    /* Main styling */
    .main {
        background: #f8fafc;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom button styling */
    .stButton > button {
        width: 100%;
        border-radius: 1rem;
        font-weight: 600;
        padding: 0.85rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    /* Progress bar */
    .xp-bar {
        width: 100%;
        height: 14px;
        border-radius: 999px;
        background: #e2e8f0;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    
    .xp-progress {
        height: 100%;
        background: linear-gradient(90deg, #38bdf8, #0ea5e9);
        border-radius: inherit;
        transition: width 0.4s ease;
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 1.5rem;
        padding: 2.5rem;
        box-shadow: 0 20px 45px rgba(15,23,42,0.12);
        margin-bottom: 1rem;
    }
    
    .option-card {
        border: 2px solid #e2e8f0;
        border-radius: 1rem;
        padding: 1rem;
        background: white;
        cursor: pointer;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .option-card:hover {
        border-color: #38bdf8;
        transform: scale(1.02);
        box-shadow: 0 15px 25px rgba(14,165,233,0.15);
    }
    
    .option-card.selected {
        border-color: #38bdf8;
        background: #ecfeff;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: linear-gradient(180deg, #38bdf8, #0ea5e9);
        border-radius: 1.5rem;
        padding: 2rem;
        color: white;
        box-shadow: 0 30px 60px rgba(14,165,233,0.35);
    }
    
    .avatar {
        width: 120px;
        height: 120px;
        border-radius: 999px;
        background: rgba(255,255,255,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        margin: 0 auto 1.25rem;
        box-shadow: 0 10px 30px rgba(15,23,42,0.25);
    }
    
    .bot-message {
        background: rgba(255,255,255,0.15);
        border-radius: 1rem;
        padding: 1rem;
        font-size: 1rem;
        line-height: 1.4;
    }
    
    /* Tag styling */
    .tag {
        display: inline-block;
        background: #bae6fd;
        color: #0c4a6e;
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        font-size: 0.75rem;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }
    
    /* Breadcrumb styling */
    .breadcrumb {
        display: flex;
        align-items: center;
        gap: 0.35rem;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
    }
    
    .breadcrumb-item {
        padding: 0.35rem 0.85rem;
        border-radius: 999px;
        font-weight: 600;
        font-size: 0.9rem;
        display: inline-block;
    }
    
    .breadcrumb-item.current {
        background: #0ea5e9;
        color: white;
    }
    
    .breadcrumb-item.completed {
        background: #bfdbfe;
        color: #0f172a;
    }
    
    .breadcrumb-item.future {
        background: #e2e8f0;
        color: #94a3b8;
    }
    
    /* Success screen */
    .success-screen {
        text-align: center;
        padding: 3rem 1.5rem;
    }
    
    .success-screen .check {
        font-size: 4rem;
    }
</style>
""", unsafe_allow_html=True)

# Data
industries_data = [
    {'name': 'Investment Banking', 'tags': ['deals', 'sell-side'], 'category': 'Deals'},
    {'name': 'Asset Management', 'tags': ['buy-side', 'portfolio'], 'category': 'Investing'},
    {'name': 'Private Equity', 'tags': ['deals', 'growth'], 'category': 'Deals'},
    {'name': 'Venture Capital', 'tags': ['innovation', 'startup'], 'category': 'Investing'},
    {'name': 'Hedge Funds', 'tags': ['quant', 'alpha'], 'category': 'Investing'},
    {'name': 'Corporate Finance', 'tags': ['strategy', 'internal'], 'category': 'Corporate'},
    {'name': 'Financial Planning', 'tags': ['advice', 'clients'], 'category': 'Client-Facing'},
    {'name': 'Risk Management', 'tags': ['controls', 'governance'], 'category': 'Risk'},
    {'name': 'Insurance', 'tags': ['protection', 'actuarial'], 'category': 'Risk'},
    {'name': 'Fintech', 'tags': ['tech', 'innovation'], 'category': 'Technology'},
    {'name': 'Wealth Management', 'tags': ['clients', 'portfolio'], 'category': 'Client-Facing'},
    {'name': 'Trading & Sales', 'tags': ['execution', 'markets'], 'category': 'Markets'},
]

sub_industries_data = [
    {'name': 'M&A Advisory', 'tags': ['deals', 'strategic']},
    {'name': 'Equity Research', 'tags': ['analysis', 'reporting']},
    {'name': 'Fixed Income', 'tags': ['bonds', 'income']},
    {'name': 'Derivatives', 'tags': ['futures', 'options']},
    {'name': 'Real Estate', 'tags': ['property', 'alternative']},
    {'name': 'Infrastructure', 'tags': ['project', 'long-term']},
    {'name': 'Credit Analysis', 'tags': ['credit', 'risk']},
    {'name': 'Portfolio Management', 'tags': ['allocations', 'buy-side']},
    {'name': 'Compliance', 'tags': ['regulations', 'controls']},
    {'name': 'Quantitative Analysis', 'tags': ['modeling', 'math']},
    {'name': 'ESG Investing', 'tags': ['impact', 'sustainability']},
    {'name': 'Digital Assets', 'tags': ['crypto', 'innovation']},
]

job_roles_data = [
    {'name': 'Investment Analyst', 'tags': ['analysis', 'junior']},
    {'name': 'Portfolio Manager', 'tags': ['strategy', 'senior']},
    {'name': 'Financial Advisor', 'tags': ['clients', 'advice']},
    {'name': 'Risk Analyst', 'tags': ['controls', 'risk']},
    {'name': 'Trader', 'tags': ['markets', 'execution']},
    {'name': 'Investment Banker', 'tags': ['deals', 'sell-side']},
    {'name': 'Wealth Manager', 'tags': ['clients', 'relationship']},
    {'name': 'Quant Analyst', 'tags': ['quant', 'modeling']},
    {'name': 'Research Analyst', 'tags': ['insights', 'reporting']},
    {'name': 'Fund Manager', 'tags': ['allocation', 'leadership']},
    {'name': 'M&A Specialist', 'tags': ['deals', 'strategic']},
    {'name': 'CFO/Finance Director', 'tags': ['leadership', 'strategic']},
]

job_functions_data = [
    {'name': 'Analysis & Research', 'tags': ['insights', 'data']},
    {'name': 'Client Relations', 'tags': ['service', 'engagement']},
    {'name': 'Deal Execution', 'tags': ['implementation', 'deals']},
    {'name': 'Portfolio Construction', 'tags': ['strategy', 'allocation']},
    {'name': 'Risk Assessment', 'tags': ['controls', 'insight']},
    {'name': 'Trading & Execution', 'tags': ['markets', 'fast-paced']},
    {'name': 'Strategic Planning', 'tags': ['big-picture', 'leadership']},
    {'name': 'Compliance & Regulatory', 'tags': ['governance', 'standards']},
    {'name': 'Team Leadership', 'tags': ['people', 'management']},
    {'name': 'Product Development', 'tags': ['innovation', 'design']},
    {'name': 'Technology & Innovation', 'tags': ['engineering', 'future']},
    {'name': 'Operations Management', 'tags': ['processes', 'efficiency']},
]

reason_options = [
    {'name': 'To upgrade skills', 'subtitle': 'Pick up in-demand tools and frameworks that hiring managers value.'},
    {'name': 'To learn about the industry', 'subtitle': 'Get guided exposure to finance sectors and career pathways.'},
    {'name': 'To learn', 'subtitle': 'Absorb core finance concepts and build a strong foundation.'},
]

courses = [
    {
        'title': 'Financial Modeling & Valuation Mastery',
        'discount': '20% OFF',
        'uplift': '30% job chance increase',
        'description': 'Build wall-street ready financial models and valuations with live case studies.',
    },
    {
        'title': 'Investment Banking Fundamentals',
        'discount': '15% OFF',
        'uplift': '20% job chance increase',
        'description': 'Master pitch books, deal structuring, and the IB workflow from pros.',
    },
    {
        'title': 'Portfolio Management Essentials',
        'discount': '10% OFF',
        'uplift': '10% job chance increase',
        'description': 'Design resilient portfolios, asset allocation strategies, and reporting tools.',
    },
]

breadcrumb_steps = [
    {'id': 0, 'label': '👤 Personal Info'},
    {'id': 1, 'label': '🎓 Education'},
    {'id': 2, 'label': '🏢 Industries'},
    {'id': 3, 'label': '🎯 Specialization'},
    {'id': 4, 'label': '💼 Experience'},
    {'id': 5, 'label': '📅 Years'},
    {'id': 6, 'label': '🚀 Career Goals'},
    {'id': 7, 'label': '⚙️ Functions'},
    {'id': 8, 'label': '💡 Your Why'},
    {'id': 9, 'label': '📚 Courses'},
]

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.form_data = {
        'name': '',
        'email': '',
        'education': '',
        'industries': [],
        'sub_industries': [],
        'has_experience': None,
        'years_experience': 1,
        'aspiring_jobs': [],
        'job_functions': [],
        'reason': '',
    }
    st.session_state.completed_step = 0
    st.session_state.show_welcome = True

# Welcome screen
if st.session_state.show_welcome:
    st.markdown("""
    <div style="position: fixed; inset: 0; background: #38bdf8; display: flex; align-items: center; 
                justify-content: center; z-index: 1000;">
        <div style="text-align: center; color: white;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">✦</div>
            <h1>Hi! Welcome to FINX</h1>
            <p style="font-size: 1.2rem;">A bright future awaits you</p>
        </div>
    </div>
    <script>
        setTimeout(function() {
            window.location.reload();
        }, 3000);
    </script>
    """, unsafe_allow_html=True)
    time.sleep(3)
    st.session_state.show_welcome = False
    st.rerun()

# Helper functions
def filter_by_search(items, search_term):
    if not search_term:
        return items
    search_term = search_term.lower().strip()
    filtered = []
    for item in items:
        if search_term in item['name'].lower():
            filtered.append(item)
        elif any(search_term in tag.lower() for tag in item['tags']):
            filtered.append(item)
    return filtered

def render_tags(tags):
    html = ""
    for tag in tags[:2]:
        html += f'<span class="tag">{tag}</span>'
    return html

def calculate_xp_completion(step):
    total_steps = 10
    return round((1 - pow(1 - min(step, total_steps) / total_steps, 0.6)) * 100)

def can_advance(step):
    validations = {
        0: st.session_state.form_data['name'].strip() and '@' in st.session_state.form_data['email'],
        1: bool(st.session_state.form_data['education']),
        2: 1 <= len(st.session_state.form_data['industries']) <= 3,
        3: 1 <= len(st.session_state.form_data['sub_industries']) <= 3,
        4: st.session_state.form_data['has_experience'] is not None,
        5: st.session_state.form_data['years_experience'] >= 1,
        6: 1 <= len(st.session_state.form_data['aspiring_jobs']) <= 3,
        7: 1 <= len(st.session_state.form_data['job_functions']) <= 3,
        8: bool(st.session_state.form_data['reason']),
        9: True,
    }
    return validations.get(step, False)

# Progress bar
xp_completion = calculate_xp_completion(st.session_state.step)
st.markdown(f"""
<div class="xp-bar">
    <div class="xp-progress" style="width: {xp_completion}%"></div>
</div>
<div style="text-align: right; font-size: 0.85rem; color: #94a3b8; margin-bottom: 1rem;">
    XP Boost: {xp_completion}% complete
</div>
""", unsafe_allow_html=True)

# Breadcrumb navigation
breadcrumb_html = '<div class="breadcrumb">'
for i, crumb in enumerate(breadcrumb_steps):
    if st.session_state.step == crumb['id']:
        state_class = 'current'
    elif st.session_state.step > crumb['id']:
        state_class = 'completed'
    else:
        state_class = 'future'
    
    breadcrumb_html += f'<span class="breadcrumb-item {state_class}">{crumb["label"]}'
    if state_class == 'completed':
        breadcrumb_html += ' ✓'
    breadcrumb_html += '</span>'
    
    if i < len(breadcrumb_steps) - 1:
        breadcrumb_html += '<span style="color: #94a3b8; font-weight: 600;">›</span>'

breadcrumb_html += '</div>'
st.markdown(breadcrumb_html, unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Step 0: Personal Information
    if st.session_state.step == 0:
        st.markdown("## Personal Information")
        st.markdown("---")
        
        name = st.text_input("Name", value=st.session_state.form_data['name'], 
                            placeholder="e.g., John Smith", key="name_input")
        st.session_state.form_data['name'] = name
        st.caption("We'll use this to personalize your experience.")
        
        email = st.text_input("Email", value=st.session_state.form_data['email'],
                             placeholder="e.g., john@example.com", key="email_input")
        st.session_state.form_data['email'] = email
        
        if '@' in email and '.' in email:
            st.success("✔ Valid email")
        else:
            st.error("✕ Invalid email")
        
        st.caption("Your email will be used to send course details and career resources.")
    
    # Step 1: Education
    elif st.session_state.step == 1:
        st.markdown("## Education Level")
        st.markdown("---")
        
        education_options = [
            {'title': '12th Grade', 'description': 'Strengthen foundational finance skills.'},
            {'title': 'Undergraduate (UG)', 'description': 'Bridge academic knowledge to finance careers.'},
            {'title': 'Postgraduate (PG)', 'description': 'Level up advanced finance capabilities.'},
        ]
        
        cols = st.columns(3)
        for idx, option in enumerate(education_options):
            with cols[idx]:
                if st.button(f"**{option['title']}**\n\n{option['description']}", 
                           key=f"edu_{idx}", use_container_width=True):
                    st.session_state.form_data['education'] = option['title']
                    st.session_state.step = 2
                    st.session_state.completed_step = max(st.session_state.completed_step, 1)
                    st.rerun()
    
    # Step 2: Industries
    elif st.session_state.step == 2:
        st.markdown("## Industries")
        st.markdown(f"**{len(st.session_state.form_data['industries'])}/3 selected**")
        st.markdown("---")
        
        search = st.text_input("🔍 Search industries or tags", placeholder="e.g., 'buy-side', 'deals'", 
                              key="industry_search")
        
        filtered_industries = filter_by_search(industries_data, search)
        
        cols = st.columns(3)
        for idx, industry in enumerate(filtered_industries):
            with cols[idx % 3]:
                selected = industry['name'] in st.session_state.form_data['industries']
                button_type = "primary" if selected else "secondary"
                
                if st.button(
                    f"{'✓ ' if selected else ''}{industry['name']}\n\n{render_tags(industry['tags'])}", 
                    key=f"ind_{idx}", 
                    use_container_width=True,
                    disabled=not selected and len(st.session_state.form_data['industries']) >= 3
                ):
                    if selected:
                        st.session_state.form_data['industries'].remove(industry['name'])
                    else:
                        if len(st.session_state.form_data['industries']) < 3:
                            st.session_state.form_data['industries'].append(industry['name'])
                    st.rerun()
    
    # Step 3: Sub-Industries
    elif st.session_state.step == 3:
        st.markdown("## Sub-Industries")
        st.markdown(f"**{len(st.session_state.form_data['sub_industries'])}/3 selected**")
        st.markdown("---")
        
        search = st.text_input("🔍 Search sub-industries or tags", 
                              placeholder="e.g., 'strategic', 'analysis'", key="subind_search")
        
        filtered_sub = filter_by_search(sub_industries_data, search)
        
        cols = st.columns(3)
        for idx, sub in enumerate(filtered_sub):
            with cols[idx % 3]:
                selected = sub['name'] in st.session_state.form_data['sub_industries']
                
                if st.button(
                    f"{'✓ ' if selected else ''}{sub['name']}\n\n{render_tags(sub['tags'])}", 
                    key=f"sub_{idx}", 
                    use_container_width=True,
                    disabled=not selected and len(st.session_state.form_data['sub_industries']) >= 3
                ):
                    if selected:
                        st.session_state.form_data['sub_industries'].remove(sub['name'])
                    else:
                        if len(st.session_state.form_data['sub_industries']) < 3:
                            st.session_state.form_data['sub_industries'].append(sub['name'])
                    st.rerun()
    
    # Step 4: Experience
    elif st.session_state.step == 4:
        st.markdown("## Do you have work experience?")
        st.markdown("---")
        
        col_yes, col_no = st.columns(2)
        
        with col_yes:
            if st.button("**Yes**\n\nI bring work experience.", key="exp_yes", use_container_width=True):
                st.session_state.form_data['has_experience'] = True
                st.session_state.step = 5
                st.session_state.completed_step = max(st.session_state.completed_step, 4)
                st.rerun()
        
        with col_no:
            if st.button("**No**\n\nI am new to the industry.", key="exp_no", use_container_width=True):
                st.session_state.form_data['has_experience'] = False
                st.session_state.step = 6
                st.session_state.completed_step = max(st.session_state.completed_step, 4)
                st.rerun()
    
    # Step 5: Years of Experience
    elif st.session_state.step == 5:
        st.markdown("## Years of Experience")
        st.caption("Gradient slider blends early gains with advanced mastery.")
        st.markdown("---")
        
        years = st.slider("Years", min_value=0, max_value=20, 
                         value=st.session_state.form_data['years_experience'],
                         key="years_slider")
        st.session_state.form_data['years_experience'] = years
        
        st.markdown(f"### {years} years")
    
    # Step 6: Aspiring Jobs
    elif st.session_state.step == 6:
        st.markdown("## Aspiring Jobs")
        st.markdown(f"**{len(st.session_state.form_data['aspiring_jobs'])}/3 selected**")
        st.markdown("---")
        
        search = st.text_input("🔍 Search job roles or tags", 
                              placeholder="e.g., 'analysis', 'senior'", key="jobs_search")
        
        filtered_jobs = filter_by_search(job_roles_data, search)
        
        cols = st.columns(3)
        for idx, job in enumerate(filtered_jobs):
            with cols[idx % 3]:
                selected = job['name'] in st.session_state.form_data['aspiring_jobs']
                
                if st.button(
                    f"{'✓ ' if selected else ''}{job['name']}\n\n{render_tags(job['tags'])}", 
                    key=f"job_{idx}", 
                    use_container_width=True,
                    disabled=not selected and len(st.session_state.form_data['aspiring_jobs']) >= 3
                ):
                    if selected:
                        st.session_state.form_data['aspiring_jobs'].remove(job['name'])
                    else:
                        if len(st.session_state.form_data['aspiring_jobs']) < 3:
                            st.session_state.form_data['aspiring_jobs'].append(job['name'])
                    st.rerun()
    
    # Step 7: Job Functions
    elif st.session_state.step == 7:
        st.markdown("## Job Functions")
        st.markdown(f"**{len(st.session_state.form_data['job_functions'])}/3 selected**")
        st.markdown("---")
        
        search = st.text_input("🔍 Search functions or tags", 
                              placeholder="e.g., 'strategy', 'markets'", key="func_search")
        
        filtered_funcs = filter_by_search(job_functions_data, search)
        
        cols = st.columns(3)
        for idx, func in enumerate(filtered_funcs):
            with cols[idx % 3]:
                selected = func['name'] in st.session_state.form_data['job_functions']
                
                if st.button(
                    f"{'✓ ' if selected else ''}{func['name']}\n\n{render_tags(func['tags'])}", 
                    key=f"func_{idx}", 
                    use_container_width=True,
                    disabled=not selected and len(st.session_state.form_data['job_functions']) >= 3
                ):
                    if selected:
                        st.session_state.form_data['job_functions'].remove(func['name'])
                    else:
                        if len(st.session_state.form_data['job_functions']) < 3:
                            st.session_state.form_data['job_functions'].append(func['name'])
                    st.rerun()
    
    # Step 8: Reason
    elif st.session_state.step == 8:
        st.markdown("## Reason for Joining FINX")
        st.markdown("---")
        
        cols = st.columns(3)
        for idx, reason in enumerate(reason_options):
            with cols[idx]:
                if st.button(f"**{reason['name']}**\n\n{reason['subtitle']}", 
                           key=f"reason_{idx}", use_container_width=True):
                    st.session_state.form_data['reason'] = reason['name']
                    st.session_state.step = 9
                    st.session_state.completed_step = max(st.session_state.completed_step, 8)
                    st.rerun()
    
    # Step 9: Courses
    elif st.session_state.step == 9:
        st.markdown("## Course Recommendations")
        st.caption("Hover each card to see details")
        st.markdown("---")
        
        for course in courses:
            with st.expander(f"**{course['title']}** - {course['discount']}", expanded=True):
                st.write(course['description'])
                st.success(f"📈 {course['uplift']}")
        
        st.markdown("---")
        if st.button("🎉 Complete Registration", use_container_width=True, type="primary"):
            st.session_state.step = 10
            st.session_state.completed_step = 10
            st.rerun()
    
    # Step 10: Success
    elif st.session_state.step == 10:
        st.markdown("""
        <div class="success-screen">
            <div class="check">✅</div>
            <h2>Welcome to FINX!</h2>
            <p style="color: #94a3b8;">Your journey to a brighter future starts now.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.step = 0
            st.session_state.completed_step = 0
            st.session_state.form_data = {
                'name': '',
                'email': '',
                'education': '',
                'industries': [],
                'sub_industries': [],
                'has_experience': None,
                'years_experience': 1,
                'aspiring_jobs': [],
                'job_functions': [],
                'reason': '',
            }
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    if st.session_state.step not in [1, 4, 8, 9, 10]:
        col_back, col_next = st.columns(2)
        
        with col_back:
            if st.button("⬅️ Back", use_container_width=True, disabled=st.session_state.step == 0):
                if st.session_state.step == 6 and not st.session_state.form_data['has_experience']:
                    st.session_state.step = 4
                else:
                    st.session_state.step = max(0, st.session_state.step - 1)
                st.rerun()
        
        with col_next:
            if st.button("Continue ➡️", use_container_width=True, 
                        disabled=not can_advance(st.session_state.step),
                        type="primary"):
                if st.session_state.step == 4 and not st.session_state.form_data['has_experience']:
                    st.session_state.step = 6
                else:
                    st.session_state.step += 1
                st.session_state.completed_step = max(st.session_state.completed_step, st.session_state.step)
                st.rerun()

# Sidebar
with col2:
    st.markdown("""
    <div class="sidebar-content">
        <div class="avatar">✨</div>
        <div class="bot-message">
    """, unsafe_allow_html=True)
    
    if 4 <= st.session_state.step <= 6:
        st.write("You're halfway there to a bright future!")
    else:
        st.write("Looking great! Your personalized recommendations are being prepared")
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Show summary
    if st.session_state.step > 0:
        st.markdown("---")
        st.markdown("### Your Progress")
        
        if st.session_state.form_data['name']:
            st.write(f"👤 **Name:** {st.session_state.form_data['name']}")
        
        if st.session_state.form_data['education']:
            st.write(f"🎓 **Education:** {st.session_state.form_data['education']}")
        
        if st.session_state.form_data['industries']:
            st.write(f"🏢 **Industries:** {len(st.session_state.form_data['industries'])} selected")
        
        if st.session_state.form_data['sub_industries']:
            st.write(f"🎯 **Specializations:** {len(st.session_state.form_data['sub_industries'])} selected")
        
        if st.session_state.form_data['has_experience'] is not None:
            exp_text = "Yes" if st.session_state.form_data['has_experience'] else "No"
            st.write(f"💼 **Experience:** {exp_text}")
        
        if st.session_state.form_data['has_experience'] and st.session_state.form_data['years_experience'] > 0:
            st.write(f"📅 **Years:** {st.session_state.form_data['years_experience']}")
        
        if st.session_state.form_data['aspiring_jobs']:
            st.write(f"🚀 **Career Goals:** {len(st.session_state.form_data['aspiring_jobs'])} selected")
        
        if st.session_state.form_data['job_functions']:
            st.write(f"⚙️ **Functions:** {len(st.session_state.form_data['job_functions'])} selected")
        
        if st.session_state.form_data['reason']:
            st.write(f"💡 **Reason:** {st.session_state.form_data['reason']}")
