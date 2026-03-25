import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error

# Page config
st.set_page_config(
    page_title="Internship Management System",
    page_icon="💼",
    layout="wide"
)

# =============================================
# DATABASE CONNECTION
# =============================================
def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # CHANGE THIS
            database="internship_management",
            port=3306
        )
        return connection
    except Error as e:
        st.error(f"Database connection failed: {e}")
        return None

# =============================================
# SESSION STATE
# =============================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.user_id = None
    st.session_state.user_name = None

# =============================================
# TITLE
# =============================================
st.title("🎓 Internship Management System")

# =============================================
# SIDEBAR
# =============================================
with st.sidebar:
    st.header("Navigation")
    
    if not st.session_state.logged_in:
        menu = ["Home", "Student Login", "Student Register", "Company Login", "Company Register", "Admin Login"]
    else:
        if st.session_state.user_type == "Student":
            menu = ["Dashboard", "View Internships", "My Applications", "Profile", "Logout"]
        elif st.session_state.user_type == "Company":
            menu = ["Dashboard", "Post Internship", "View Applications", "My Internships", "Profile", "Logout"]
        else:
            menu = ["Dashboard", "All Students", "All Companies", "All Internships", "All Applications", "Database Stats", "Logout"]
    
    choice = st.selectbox("Menu", menu)

# =============================================
# HELPER FUNCTIONS
# =============================================
def execute_query(query, params=None, fetch=True):
    conn = get_connection()
    if not conn:
        return None if fetch else False
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        
        if fetch:
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        else:
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except Error as e:
        st.error(f"Database error: {e}")
        return None if fetch else False

def get_dataframe(query, params=None):
    conn = get_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn, params=params)
            conn.close()
            return df
        except:
            return pd.DataFrame()
    return pd.DataFrame()

def logout():
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.user_id = None
    st.session_state.user_name = None
    st.rerun()

# =============================================
# HOME PAGE - SHOWS DATABASE DATA
# =============================================
def home():
    st.subheader("📊 System Overview")
    
    # Get statistics from database
    stats = get_dataframe("""
        SELECT 
            (SELECT COUNT(*) FROM students) as students,
            (SELECT COUNT(*) FROM companies) as companies,
            (SELECT COUNT(*) FROM internships) as internships,
            (SELECT COUNT(*) FROM applications) as applications,
            (SELECT COUNT(*) FROM internships WHERE status = 'Open') as open_internships
    """)
    
    if not stats.empty:
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Students", stats['students'].iloc[0])
        col2.metric("Companies", stats['companies'].iloc[0])
        col3.metric("Internships", stats['internships'].iloc[0])
        col4.metric("Applications", stats['applications'].iloc[0])
        col5.metric("Open Internships", stats['open_internships'].iloc[0])
        
        # Show recent data
        st.subheader("Recent Students")
        students = get_dataframe("SELECT name, email, department FROM students ORDER BY created_at DESC LIMIT 5")
        st.dataframe(students)
        
        st.subheader("Recent Companies")
        companies = get_dataframe("SELECT name, industry, location FROM companies ORDER BY created_at DESC LIMIT 5")
        st.dataframe(companies)
    else:
        st.warning("No data found in database")

# =============================================
# STUDENT REGISTRATION
# =============================================
def student_register():
    st.subheader("📝 Student Registration")
    
    with st.form("student_register"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        department = st.text_input("Department")
        year = st.number_input("Year of Study", 1, 5, 1)
        skills = st.text_area("Skills")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Register"):
            if name and email and password:
                existing = execute_query("SELECT * FROM students WHERE email = %s", (email,))
                if existing:
                    st.error("Email already exists")
                else:
                    success = execute_query("""
                        INSERT INTO students (name, email, phone, department, year_of_study, skills)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (name, email, phone, department, year, skills), fetch=False)
                    
                    if success:
                        st.success("Registration successful! Please login.")
                        st.balloons()

# =============================================
# COMPANY REGISTRATION
# =============================================
def company_register():
    st.subheader("🏢 Company Registration")
    
    with st.form("company_register"):
        name = st.text_input("Company Name")
        industry = st.text_input("Industry")
        location = st.text_input("Location")
        contact_email = st.text_input("Contact Email")
        contact_phone = st.text_input("Contact Phone")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Register"):
            if name and contact_email and password:
                existing = execute_query("SELECT * FROM companies WHERE contact_email = %s", (contact_email,))
                if existing:
                    st.error("Email already exists")
                else:
                    success = execute_query("""
                        INSERT INTO companies (name, industry, location, contact_email, contact_phone)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (name, industry, location, contact_email, contact_phone), fetch=False)
                    
                    if success:
                        st.success("Registration successful! Please login.")
                        st.balloons()

# =============================================
# STUDENT LOGIN
# =============================================
def student_login():
    st.subheader("🔐 Student Login")
    
    with st.form("student_login"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Login"):
            result = execute_query("SELECT * FROM students WHERE email = %s", (email,))
            if result:
                student = result[0]
                st.session_state.logged_in = True
                st.session_state.user_type = "Student"
                st.session_state.user_id = student['student_id']
                st.session_state.user_name = student['name']
                st.rerun()
            else:
                st.error("Invalid email")

# =============================================
# COMPANY LOGIN
# =============================================
def company_login():
    st.subheader("🔐 Company Login")
    
    with st.form("company_login"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Login"):
            result = execute_query("SELECT * FROM companies WHERE contact_email = %s", (email,))
            if result:
                company = result[0]
                st.session_state.logged_in = True
                st.session_state.user_type = "Company"
                st.session_state.user_id = company['company_id']
                st.session_state.user_name = company['name']
                st.rerun()
            else:
                st.error("Invalid email")

# =============================================
# ADMIN LOGIN
# =============================================
def admin_login():
    st.subheader("🔐 Admin Login")
    
    with st.form("admin_login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Login"):
            if username == "admin" and password == "admin123":
                st.session_state.logged_in = True
                st.session_state.user_type = "Admin"
                st.session_state.user_name = "Administrator"
                st.rerun()
            else:
                st.error("Invalid credentials")

# =============================================
# STUDENT DASHBOARD
# =============================================
def student_dashboard():
    st.subheader(f"Welcome {st.session_state.user_name}!")
    
    apps = get_dataframe("""
        SELECT status, COUNT(*) as count 
        FROM applications 
        WHERE student_id = %s 
        GROUP BY status
    """, (st.session_state.user_id,))
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Applications", apps['count'].sum() if not apps.empty else 0)
    
    pending = apps[apps['status'] == 'Pending']['count'].sum() if not apps.empty else 0
    col2.metric("Pending", pending)
    
    accepted = apps[apps['status'] == 'Accepted']['count'].sum() if not apps.empty else 0
    col3.metric("Accepted", accepted)

# =============================================
# VIEW INTERNSHIPS
# =============================================
def view_internships():
    st.subheader("Available Internships")
    
    # internships = get_dataframe("""
    #     SELECT i.*, c.name as company_name, c.location 
    #     FROM internships i
    #     JOIN companies c ON i.company_id = c.company_id
    #     WHERE i.status = 'Open'
    # """)
    
    internships = get_dataframe("""
    SELECT i.*, c.name as company_name, c.location 
    FROM internships i
    JOIN companies c ON i.company_id = c.company_id
    WHERE i.status = 'Open'
    AND i.internship_id IN (
        SELECT MAX(internship_id)
        FROM internships
        GROUP BY company_id
    )
""")
    
    
    if not internships.empty:
        for _, row in internships.iterrows():
            with st.expander(f"{row['title']} at {row['company_name']}"):
                st.write(f"*Description:* {row['description']}")
                st.write(f"*Requirements:* {row['requirements']}")
                st.write(f"*Location:* {row['location']}")
                st.write(f"*Duration:* {row['duration_weeks']} weeks")
                st.write(f"*Stipend:* ₹{row['stipend']:,.2f}")
                
                # Check if already applied
                applied = execute_query("""
                    SELECT * FROM applications 
                    WHERE student_id = %s AND internship_id = %s
                """, (st.session_state.user_id, row['internship_id']))
                
                if not applied:
                    if st.button("Apply", key=f"apply_{row['internship_id']}"):
                        execute_query("""
                            INSERT INTO applications (student_id, internship_id) 
                            VALUES (%s, %s)
                        """, (st.session_state.user_id, row['internship_id']), fetch=False)
                        st.success("Applied successfully!")
                        st.rerun()
                else:
                    st.info("Already applied")
    else:
        st.info("No internships available")

# =============================================
# MY APPLICATIONS
# =============================================
def my_applications():
    st.subheader("My Applications")
    
    apps = get_dataframe("""
        SELECT a.*, i.title, i.stipend, c.name as company_name
        FROM applications a
        JOIN internships i ON a.internship_id = i.internship_id
        JOIN companies c ON i.company_id = c.company_id
        WHERE a.student_id = %s
        ORDER BY a.application_date DESC
    """, (st.session_state.user_id,))
    
    if not apps.empty:
        for _, row in apps.iterrows():
            status_color = "🟡" if row['status'] == 'Pending' else "🟢" if row['status'] == 'Accepted' else "🔴"
            st.write(f"{status_color} *{row['title']}* at {row['company_name']}")
            st.write(f"Status: {row['status']} | Stipend: ₹{row['stipend']:,.2f}")
            st.write(f"Applied: {row['application_date']}")
            st.divider()
    else:
        st.info("No applications yet")

# =============================================
# STUDENT PROFILE
# =============================================
def student_profile():
    st.subheader("My Profile")
    
    student = execute_query("SELECT * FROM students WHERE student_id = %s", (st.session_state.user_id,))[0]
    
    with st.form("update_profile"):
        name = st.text_input("Name", student['name'])
        phone = st.text_input("Phone", student['phone'] or "")
        department = st.text_input("Department", student['department'] or "")
        year = st.number_input("Year", 1, 5, student['year_of_study'] or 1)
        skills = st.text_area("Skills", student['skills'] or "")
        
        if st.form_submit_button("Update"):
            execute_query("""
                UPDATE students 
                SET name=%s, phone=%s, department=%s, year_of_study=%s, skills=%s
                WHERE student_id=%s
            """, (name, phone, department, year, skills, st.session_state.user_id), fetch=False)
            st.success("Profile updated!")

# =============================================
# POST INTERNSHIP
# =============================================
def post_internship():
    st.subheader("Post Internship")
    
    with st.form("post_internship"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        requirements = st.text_area("Requirements")
        duration = st.number_input("Duration (weeks)", 1, 52, 12)
        stipend = st.number_input("Stipend (₹)", 0, 100000, 15000)
        
        if st.form_submit_button("Post"):
            execute_query("""
                INSERT INTO internships (company_id, title, description, requirements, duration_weeks, stipend)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (st.session_state.user_id, title, description, requirements, duration, stipend), fetch=False)
            st.success("Internship posted!")
            st.rerun()

# =============================================
# COMPANY VIEW APPLICATIONS
# =============================================
def company_view_applications():
    st.subheader("Applications Received")
    
    apps = get_dataframe("""
        SELECT a.*, s.name, s.email, s.department, s.skills, i.title
        FROM applications a
        JOIN students s ON a.student_id = s.student_id
        JOIN internships i ON a.internship_id = i.internship_id
        WHERE i.company_id = %s
        ORDER BY a.application_date DESC
    """, (st.session_state.user_id,))
    
    if not apps.empty:
        for _, row in apps.iterrows():
            with st.expander(f"{row['name']} - {row['title']}"):
                st.write(f"Email: {row['email']}")
                st.write(f"Department: {row['department']}")
                st.write(f"Skills: {row['skills']}")
                st.write(f"Status: {row['status']}")
                
                if row['status'] == 'Pending':
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Accept", key=f"acc_{row['application_id']}"):
                            execute_query("UPDATE applications SET status='Accepted' WHERE application_id=%s", 
                                        (row['application_id'],), fetch=False)
                            st.rerun()
                    with col2:
                        if st.button("Reject", key=f"rej_{row['application_id']}"):
                            execute_query("UPDATE applications SET status='Rejected' WHERE application_id=%s", 
                                        (row['application_id'],), fetch=False)
                            st.rerun()
    else:
        st.info("No applications")

# =============================================
# COMPANY MY INTERNSHIPS
# =============================================
def company_my_internships():
    st.subheader("My Internships")
    
    # internships = get_dataframe("""
    #     SELECT i.*, COUNT(a.application_id) as applications
    #     FROM internships i
    #     LEFT JOIN applications a ON i.internship_id = a.internship_id
    #     WHERE i.company_id = %s
    #     GROUP BY i.internship_id
    # """, (st.session_state.user_id,))
    
    
    internships = get_dataframe("""
    SELECT i.*, COUNT(a.application_id) as applications
    FROM internships i
    LEFT JOIN applications a ON i.internship_id = a.internship_id
    WHERE i.company_id = %s
    GROUP BY i.internship_id
    ORDER BY i.internship_id DESC
    LIMIT 1
""", (st.session_state.user_id,))
    
    if not internships.empty:
        for _, row in internships.iterrows():
            with st.expander(f"{row['title']} - {row['applications']} applications"):
                st.write(f"Status: {row['status']}")
                st.write(f"Duration: {row['duration_weeks']} weeks")
                st.write(f"Stipend: ₹{row['stipend']:,.2f}")
    else:
        st.info("No internships posted")

# =============================================
# COMPANY PROFILE
# =============================================
def company_profile():
    st.subheader("Company Profile")
    
    company = execute_query("SELECT * FROM companies WHERE company_id = %s", (st.session_state.user_id,))[0]
    
    with st.form("update_company"):
        name = st.text_input("Name", company['name'])
        industry = st.text_input("Industry", company['industry'] or "")
        location = st.text_input("Location", company['location'] or "")
        phone = st.text_input("Phone", company['contact_phone'] or "")
        
        if st.form_submit_button("Update"):
            execute_query("""
                UPDATE companies 
                SET name=%s, industry=%s, location=%s, contact_phone=%s
                WHERE company_id=%s
            """, (name, industry, location, phone, st.session_state.user_id), fetch=False)
            st.success("Profile updated!")

# =============================================
# ADMIN PAGES
# =============================================
def admin_dashboard():
    st.subheader("Admin Dashboard")
    
    stats = get_dataframe("""
        SELECT 'Students' as type, COUNT(*) as count FROM students
        UNION SELECT 'Companies', COUNT(*) FROM companies
        UNION SELECT 'Internships', COUNT(*) FROM internships
        UNION SELECT 'Applications', COUNT(*) FROM applications
    """)
    
    for _, row in stats.iterrows():
        col1, col2 = st.columns(2)
        with col1:
            st.metric(row['type'], row['count'])

def admin_all_students():
    st.subheader("All Students")
    df = get_dataframe("SELECT * FROM students")
    st.dataframe(df)

def admin_all_companies():
    st.subheader("All Companies")
    df = get_dataframe("SELECT * FROM companies")
    st.dataframe(df)

def admin_all_internships():
    st.subheader("All Internships")
    df = get_dataframe("""
        SELECT i.*, c.name as company 
        FROM internships i
        JOIN companies c ON i.company_id = c.company_id
    """)
    st.dataframe(df)

def admin_all_applications():
    st.subheader("All Applications")
    df = get_dataframe("""
        SELECT a.*, s.name as student, i.title as internship, c.name as company
        FROM applications a
        JOIN students s ON a.student_id = s.student_id
        JOIN internships i ON a.internship_id = i.internship_id
        JOIN companies c ON i.company_id = c.company_id
    """)
    st.dataframe(df)

def admin_database_stats():
    st.subheader("Database Statistics")
    
    tables = ['students', 'companies', 'internships', 'applications']
    for table in tables:
        count = get_dataframe(f"SELECT COUNT(*) as c FROM {table}")['c'].iloc[0]
        st.metric(table.capitalize(), count)

# =============================================
# MAIN ROUTER
# =============================================
if choice == "Home":
    home()
elif choice == "Student Login":
    student_login()
elif choice == "Student Register":
    student_register()
elif choice == "Company Login":
    company_login()
elif choice == "Company Register":
    company_register()
elif choice == "Admin Login":
    admin_login()
elif choice == "Logout":
    logout()
else:
    if st.session_state.user_type == "Student":
        if choice == "Dashboard":
            student_dashboard()
        elif choice == "View Internships":
            view_internships()
        elif choice == "My Applications":
            my_applications()
        elif choice == "Profile":
            student_profile()
    elif st.session_state.user_type == "Company":
        if choice == "Dashboard":
            st.subheader(f"Welcome {st.session_state.user_name}")
        elif choice == "Post Internship":
            post_internship()
        elif choice == "View Applications":
            company_view_applications()
        elif choice == "My Internships":
            company_my_internships()
        elif choice == "Profile":
            company_profile()
    elif st.session_state.user_type == "Admin":
        if choice == "Dashboard":
            admin_dashboard()
        elif choice == "All Students":
            admin_all_students()
        elif choice == "All Companies":
            admin_all_companies()
        elif choice == "All Internships":
            admin_all_internships()
        elif choice == "All Applications":
            admin_all_applications()
        elif choice == "Database Stats":
            admin_database_stats()