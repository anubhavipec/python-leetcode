# Complete the rest of the resume in PDF format
from fpdf import FPDF
pdf = FPDF()
# Key Skills
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='Key Skills', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
- Languages & Frameworks: Java, Python, Go, Spring Boot, Hibernate
- Cloud & DevOps: AWS, Google Cloud Platform, Kubernetes, Prometheus, Grafana
- Databases: PostgreSQL, MongoDB, DynamoDB, MySQL
- Messaging & Streaming: SQS/SNS, Redis
- Other Tools: Docker, PySpark, SAP Cloud, Microservices Architecture
""")

# Professional Experience
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='Professional Experience', ln=True, align='L')

# AlphaSense
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='AlphaSense - Senior Software Engineer', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
August 2021 – Present (Pune, Maharashtra, India)

- Spearheaded data ingestion solutions from multiple vendor sources (public RSS feeds, private streams, custom crawls) into AlphaSense’s system.
- Collaborated with cross-functional teams to enhance scraper capabilities, leveraging technologies like Python, Redis, DynamoDB, and Kubernetes.
- Utilized Prometheus and Grafana to define and implement KPIs, improving system performance and reliability.
- Tech Stack: Spring Boot, Java 17, SQS/SNS, DynamoDB, S3, MySQL, Kubernetes, Prometheus, Grafana, Python, Redis.
""")

# BuzzyBrains Software
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='BuzzyBrains Software - Senior Software Engineer', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
January 2020 – August 2021 (Pune, India)

- Led the migration of a microservices architecture from a private data center to Google Cloud for viu.com, a content management system serving over 42 million users globally.
- Optimized PostgreSQL database queries, reducing response time from minutes to seconds for over 600 million data sets.
- Revamped data pipelines using Google Cloud DataProc and PySpark, achieving significant performance improvements.
- Deployed a sharded MongoDB cluster on AWS to handle high-volume queries across 500 million+ data sets.
- Tech Stack: Google Cloud Platform, PySpark, MongoDB, PostgreSQL, Spring Boot.
""")

# Incture Technologies
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='Incture Technologies - Software Engineer', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
January 2019 – December 2019 (Bangalore, India)

- Developed Workbox, a unified platform that integrates on-premise and cloud-based SAP workflows.
- Worked extensively with Java, Spring, and Hibernate in developing core components of the platform.
- Tech Stack: Java, Spring, Hibernate, SAP Cloud.
""")

# Deloitte
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='Deloitte - Business Technology Analyst', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
August 2017 – January 2019 (Bangalore, India)

- Analyzed and implemented business technology solutions for enterprise clients.
- Worked on the backend infrastructure for various client projects, providing technical solutions and optimizations.
""")

# Infosys
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='Infosys - System Engineer', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
February 2016 – August 2017

- Contributed to the development of the Goods and Services Tax (GST) project for the Government of India.
- Developed a common framework used in multiple modules of the GST application, including Back Office and Registration APIs.
- Tech Stack: Java, Spring, Hibernate.
""")

# Education
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt='Education', ln=True, align='L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""
Inderprastha Engineering College  
Bachelor of Technology (BTech), Computer Science (2011 – 2015)
""")

# Save the PDF
pdf_file_path = "anubhav_gupta_resume.pdf"
pdf.output(pdf_file_path)

pdf_file_path
