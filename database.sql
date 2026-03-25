
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


INSERT INTO students (name, email, phone, department, year_of_study, skills) VALUES
('John Doe', 'john@example.com', '1234567890', 'Computer Science', 3, 'Python, Java, SQL'),
('Jane Smith', 'jane@example.com', '0987654321', 'Information Technology', 4, 'JavaScript, React, Node.js');

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