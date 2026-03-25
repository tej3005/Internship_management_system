
-- FILE: database.sql


-- Create database
CREATE DATABASE IF NOT EXISTS internship_management;
USE internship_management;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    department VARCHAR(50),
    year_of_study INT,
    skills TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create companies table
CREATE TABLE IF NOT EXISTS companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    location VARCHAR(100),
    contact_email VARCHAR(100) UNIQUE NOT NULL,
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create internships table
CREATE TABLE IF NOT EXISTS internships (
    internship_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    requirements TEXT,
    duration_weeks INT,
    stipend DECIMAL(10,2),
    status ENUM('Open', 'Closed') DEFAULT 'Open',
    posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Create applications table
CREATE TABLE IF NOT EXISTS applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    internship_id INT,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (internship_id) REFERENCES internships(internship_id) ON DELETE CASCADE
);



-- FILE: database.sql


-- Create database
CREATE DATABASE IF NOT EXISTS internship_management;
USE internship_management;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    department VARCHAR(50),
    year_of_study INT,
    skills TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create companies table
CREATE TABLE IF NOT EXISTS companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    location VARCHAR(100),
    contact_email VARCHAR(100) UNIQUE NOT NULL,
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create internships table
CREATE TABLE IF NOT EXISTS internships (
    internship_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    requirements TEXT,
    duration_weeks INT,
    stipend DECIMAL(10,2),
    status ENUM('Open', 'Closed') DEFAULT 'Open',
    posted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Create applications table
CREATE TABLE IF NOT EXISTS applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    internship_id INT,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (internship_id) REFERENCES internships(internship_id) ON DELETE CASCADE
);


INSERT INTO students 
(student_id, name, email, phone, branch, year, skills, created_at) 
VALUES
(1, 'John Doe', 'john@example.com', '1234567890', 'Computer Science', 3, 'Python, Java, SQL', '2026-03-10 14:39:44'),
(2, 'Jane Smith', 'jane@example.com', '0987654321', 'Information Technology', 4, 'JavaScript, React, Node.js', '2026-03-10 14:39:44'),
(3, 'tsm', 'tsmandaokar@gmail.com', '9834942711', 'E&tc', 1, NULL, '2026-03-10 15:14:26'),
(4, 'Rahul Sharma', 'rahul.sharma@gmail.com', '9876543210', 'Computer Science', 2, 'Java, SQL, Spring Boot', '2026-03-10 15:56:03'),
(5, 'Priya Patel', 'priya.patel@gmail.com', '9876543211', 'Information Technology', 3, 'Python, Django, HTML', '2026-03-10 15:56:03'),
(6, 'Amit Verma', 'amit.verma@gmail.com', '9876543212', 'Electronics', 4, 'Embedded C, IoT, Arduino', '2026-03-10 15:56:03'),
(7, 'Sneha Iyer', 'sneha.iyer@gmail.com', '9876543213', 'Computer Science', 1, 'C, C++, Data Structures', '2026-03-10 15:56:03'),
(8, 'Vikram Singh', 'vikram.singh@gmail.com', '9876543214', 'Mechanical Engineering', 3, 'AutoCAD, SolidWorks', '2026-03-10 15:56:03'),
(9, 'Neha Gupta', 'neha.gupta@gmail.com', '9876543215', 'Information Technology', 2, 'JavaScript, React, Node.js', '2026-03-10 15:56:03'),
(10, 'Arjun Mehta', 'arjun.mehta@gmail.com', '9876543216', 'Computer Science', 4, 'Python, Machine Learning, TensorFlow', '2026-03-10 15:56:03'),
(11, 'Kavya Nair', 'kavya.nair@gmail.com', '9876543217', 'Electronics', 2, 'VHDL, Digital Systems', '2026-03-10 15:56:03'),
(12, 'Rohan Das', 'rohan.das@gmail.com', '9876543218', 'Computer Science', 3, 'Java, Spring Boot, MySQL', '2026-03-10 15:56:03'),
(13, 'Anjali Kulkarni', 'anjali.k@gmail.com', '9876543219', 'Information Technology', 1, 'HTML, CSS, JavaScript', '2026-03-10 15:56:03'),
(14, 'Siddharth Jain', 'sid.jain@gmail.com', '9876543220', 'Computer Science', 4, 'React, Node.js, MongoDB', '2026-03-10 15:56:03'),
(15, 'Meera Reddy', 'meera.reddy@gmail.com', '9876543221', 'Electrical Engineering', 3, 'MATLAB, Circuit Design', '2026-03-10 15:56:03'),
(16, 'Karan Malhotra', 'karan.m@gmail.com', '9876543222', 'Information Technology', 2, 'PHP, Laravel, MySQL', '2026-03-10 15:56:03'),
(17, 'Pooja Chatterjee', 'pooja.c@gmail.com', '9876543223', 'Computer Science', 3, 'Python, Data Analysis, Pandas', '2026-03-10 15:56:03'),
(18, 'Aditya Rao', 'aditya.rao@gmail.com', '9876543224', 'Computer Science', 1, 'C Programming, Linux', '2026-03-10 15:56:03'),
(19, 'Sam', 'sam20@gmail.com', '9754821687', 'CS', 1, 'Python, Java', '2026-03-17 12:27:54');

INSERT INTO companies 
(company_id, name, industry, location, contact_email, contact_phone, created_at) 
VALUES
(1, 'Tech Corp', 'Technology', 'New York', 'hr@techcorp.com', '1112223333', '2026-03-10 14:39:44'),
(2, 'Data Solutions', 'Data Analytics', 'San Francisco', 'careers@datasolutions.com', '4445556666', '2026-03-10 14:39:44'),
(3, 'InnovateTech', 'Software Development', 'Bangalore', 'hr@innovatetech.com', '9876500001', '2026-03-10 15:56:53'),
(4, 'CloudNet Systems', 'Cloud Computing', 'Hyderabad', 'careers@cloudnet.com', '9876500002', '2026-03-10 15:56:53'),
(5, 'AI Future Labs', 'Artificial Intelligence', 'Pune', 'jobs@aifuturelabs.com', '9876500003', '2026-03-10 15:56:53'),
(6, 'NextGen Robotics', 'Robotics', 'Chennai', 'hr@nextgenrobotics.com', '9876500004', '2026-03-10 15:56:53'),
(7, 'FinEdge Solutions', 'FinTech', 'Mumbai', 'careers@finedge.com', '9876500005', '2026-03-10 15:56:53'),
(8, 'CyberSecure Ltd', 'Cyber Security', 'Delhi', 'jobs@cybersecure.com', '9876500006', '2026-03-10 15:56:53'),
(9, 'GreenEnergy Tech', 'Renewable Energy', 'Ahmedabad', 'hr@greenenergy.com', '9876500007', '2026-03-10 15:56:53'),
(10, 'HealthTech Systems', 'Healthcare Technology', 'Bangalore', 'careers@healthtech.com', '9876500008', '2026-03-10 15:56:53'),
(11, 'SmartData Corp', 'Big Data Analytics', 'Hyderabad', 'jobs@smartdata.com', '9876500009', '2026-03-10 15:56:53'),
(12, 'WebWorks Studio', 'Web Development', 'Kolkata', 'hr@webworks.com', '9876500010', '2026-03-10 15:56:53'),
(13, 'TechMax', 'IT', 'Pune, India', 'techmax@gmail.com', '9857411348', '2026-03-10 16:10:23');

INSERT INTO internships 
(internship_id, company_id, title, description, required_skills, duration_months, stipend, status, created_at) 
VALUES
(1, 1, 'Software Developer Intern', 'Full stack development internship', 'Python, SQL', 12, 15000.00, 'Open', '2026-03-10 14:39:44'),
(2, 2, 'Data Analyst Intern', 'Data analysis and visualization', 'Excel, Python', 8, 12000.00, 'Open', '2026-03-10 14:39:44'),
(3, 13, 'Mtech Intern', 'Must having basic domain knowledge', 'C, C++, JavaScript, Python', 12, 12000.00, 'Open', '2026-03-10 16:16:31'),

(4, 1, 'Frontend Developer Intern', 'Work on UI development using modern frameworks', 'HTML, CSS, JavaScript, React', 10, 12000.00, 'Open', '2026-03-17 13:04:26'),
(5, 2, 'Machine Learning Intern', 'Build ML models and work on datasets', 'Python, Pandas, Scikit-learn', 12, 15000.00, 'Open', '2026-03-17 13:04:26'),
(6, 3, 'Backend Developer Intern', 'Develop APIs and handle server logic', 'Node.js, Express, MySQL', 12, 14000.00, 'Open', '2026-03-17 13:04:26'),
(7, 4, 'Cybersecurity Intern', 'Assist in vulnerability testing and security audits', 'Networking, Linux, Security Basics', 8, 10000.00, 'Open', '2026-03-17 13:04:26'),
(8, 5, 'Mobile App Developer Intern', 'Develop Android applications', 'Java, Kotlin, Android Studio', 10, 13000.00, 'Open', '2026-03-17 13:04:26'),
(9, 6, 'Cloud Computing Intern', 'Work with AWS services and deployment', 'AWS, Docker, Linux', 12, 16000.00, 'Open', '2026-03-17 13:04:26'),
(10, 7, 'UI/UX Design Intern', 'Design user interfaces and improve UX', 'Figma, Adobe XD, Creativity', 8, 9000.00, 'Open', '2026-03-17 13:04:26'),
(11, 8, 'Data Science Intern', 'Analyze data and build predictive models', 'Python, NumPy, Pandas, ML', 12, 15000.00, 'Open', '2026-03-17 13:04:26'),
(12, 9, 'DevOps Intern', 'Work on CI/CD pipelines and automation', 'Git, Docker, Jenkins', 10, 14000.00, 'Open', '2026-03-17 13:04:26'),
(13, 10, 'QA Testing Intern', 'Perform testing and bug tracking', 'Manual Testing, Selenium Basics', 8, 8000.00, 'Open', '2026-03-17 13:04:26'),

(14, 1, 'Frontend Developer Intern', 'Work on UI development using modern frameworks', 'HTML, CSS, JavaScript, React', 10, 12000.00, 'Open', '2026-03-17 13:04:46'),
(15, 2, 'Machine Learning Intern', 'Build ML models and work on datasets', 'Python, Pandas, Scikit-learn', 12, 15000.00, 'Open', '2026-03-17 13:04:46'),
(16, 3, 'Backend Developer Intern', 'Develop APIs and handle server logic', 'Node.js, Express, MySQL', 12, 14000.00, 'Open', '2026-03-17 13:04:46'),
(17, 4, 'Cybersecurity Intern', 'Assist in vulnerability testing and security audits', 'Networking, Linux, Security Basics', 8, 10000.00, 'Open', '2026-03-17 13:04:46'),
(18, 5, 'Mobile App Developer Intern', 'Develop Android applications', 'Java, Kotlin, Android Studio', 10, 13000.00, 'Open', '2026-03-17 13:04:46'),
(19, 6, 'Cloud Computing Intern', 'Work with AWS services and deployment', 'AWS, Docker, Linux', 12, 16000.00, 'Open', '2026-03-17 13:04:46'),
(20, 7, 'UI/UX Design Intern', 'Design user interfaces and improve UX', 'Figma, Adobe XD, Creativity', 8, 9000.00, 'Open', '2026-03-17 13:04:46'),
(21, 8, 'Data Science Intern', 'Analyze data and build predictive models', 'Python, NumPy, Pandas, ML', 12, 15000.00, 'Open', '2026-03-17 13:04:46'),
(22, 9, 'DevOps Intern', 'Work on CI/CD pipelines and automation', 'Git, Docker, Jenkins', 10, 14000.00, 'Open', '2026-03-17 13:04:46'),
(23, 10, 'QA Testing Intern', 'Perform testing and bug tracking', 'Manual Testing, Selenium Basics', 8, 8000.00, 'Open', '2026-03-17 13:04:46');

-- Insert sample applications
INSERT INTO applications (student_id, internship_id, status) VALUES
(1, 1, 'Accepted'),
(2, 2, 'Pending');

-- Show confirmation
SELECT 'Database setup complete!' as Message;
SELECT CONCAT('Students: ', COUNT(*)) FROM students
UNION SELECT CONCAT('Companies: ', COUNT(*)) FROM companies
UNION SELECT CONCAT('Internships: ', COUNT(*)) FROM internships
UNION SELECT CONCAT('Applications: ', COUNT(*)) FROM applications;

INSERT INTO companies (name, industry, location, contact_email, contact_phone) VALUES
('Tech Corp', 'Technology', 'New York', 'hr@techcorp.com', '1112223333'),
('Data Solutions', 'Data Analytics', 'San Francisco', 'careers@datasolutions.com', '4445556666');

INSERT INTO internships (company_id, title, description, requirements, duration_weeks, stipend) VALUES
(1, 'Software Developer Intern', 'Full stack development internship', 'Python, SQL', 12, 15000.00),
(2, 'Data Analyst Intern', 'Data analysis and visualization', 'Excel, Python', 8, 12000.00);

-- Insert sample applications
INSERT INTO applications (student_id, internship_id, status) VALUES
(1, 1, 'Accepted'),
(2, 2, 'Pending');

-- Show confirmation
SELECT 'Database setup complete!' as Message;
SELECT CONCAT('Students: ', COUNT(*)) FROM students
UNION SELECT CONCAT('Companies: ', COUNT(*)) FROM companies
UNION SELECT CONCAT('Internships: ', COUNT(*)) FROM internships
UNION SELECT CONCAT('Applications: ', COUNT(*)) FROM applications;