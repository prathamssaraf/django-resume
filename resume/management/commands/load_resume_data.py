from django.core.management.base import BaseCommand
from resume.models import PersonalInfo, Education, Experience, Project, Research, SkillCategory, Activity

class Command(BaseCommand):
    help = 'Load initial resume data'

    def handle(self, *args, **options):
        # Clear existing data
        PersonalInfo.objects.all().delete()
        Education.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Research.objects.all().delete()
        SkillCategory.objects.all().delete()
        Activity.objects.all().delete()

        # Personal Info
        PersonalInfo.objects.create(
            name="Pratham Saraf",
            email="prathamssaraf@gmail.com",
            phone="+1 347-793-7420",
            location="Brooklyn, New York, USA",
            github="https://github.com/prathamssaraf/"
        )

        # Education
        Education.objects.create(
            institution="New York University",
            degree="Masters in Computer Science",
            location="New York, USA",
            start_date="Expected: May 2026",
            end_date="",
            gpa="CGPA – 3.88/4",
            coursework="Big Data, Artificial Intelligence, Deep Learning, Opensource Development, Information Visualization, DAA – I",
            achievements="TA: Deep Learning — Assisted 120+ graduate students with coursework, assignments, and lab sessions.\nRA: AI & Neuroscience Research — Working with Profs. Banerjee & Froemke on facial morphing detection pipelines and vision models for behavioural neuroscience.",
            order=1
        )

        Education.objects.create(
            institution="Manipal University Jaipur",
            degree="B.Tech in Data Science Engineering",
            location="Jaipur, India",
            start_date="July 2023",
            end_date="July 2024",
            gpa="CGPA - 8.91/10",
            coursework="Data Structures, OOPS, Computer Networks, OS, Machine Learning, NLP, Artificial Intelligence, Big Data Analytics",
            achievements="Received the Dean's List Excellence in Academics Award",
            order=2
        )

        # Experience
        Experience.objects.create(
            company="Hewlett Packard Enterprise (HPE)",
            position="Data Science Intern",
            location="Mumbai, India",
            start_date="July 2024",
            end_date="",
            responsibilities="• Designed server management system using Isolation Forest, reducing potential crashes and vulnerabilities by 30%.\n• Built alert manager with Prometheus, Loki, and Grafana for real-time anomaly detection across distributed servers.\n• Optimized MicroStrategy analytics dashboard, reducing query latency 10x and improving performance for thousands of daily users.\n• Developed YOLO-based document classification pipeline (95% accuracy), automating sensitive info detection & masking.\n• Collaborated with cross-functional teams to deploy anomaly detection pipeline across 100+ enterprise servers.",
            order=1
        )

        Experience.objects.create(
            company="Oil and Natural Gas Company (ONGC)",
            position="Project Intern",
            location="Mumbai, India",
            start_date="June 2023",
            end_date="July 2023",
            responsibilities="• Built predictive maintenance model (Random Forest, XGBoost), lowering equipment downtime by 25%.\n• Partnered with electronics team to refine feature selection, improving analysis precision by 15%.\n• Developed real-time analytics platform for sensor data visualization, increasing decision-making speed by 8%.\n• Streamlined sensor data pipelines using optimized batch processing, reducing storage overhead and improving query efficiency by 12%.",
            order=2
        )

        Experience.objects.create(
            company="OnFees",
            position="App Development Intern",
            location="Mumbai, India",
            start_date="January 2023",
            end_date="February 2023",
            responsibilities="• Integrated news feed and chat widget into mobile app, boosting user engagement by 20%.\n• Contributed to 10 feature updates in EdFly app with a 15-member team, improving release velocity by 25%.",
            order=3
        )

        # Projects
        Project.objects.create(
            name="GuardNet – Intelligent DNS Security Platform",
            technologies="Go, Node.js, React, Docker, Kubernetes, Redis, PostgreSQL",
            description="• Built an enterprise-grade DNS filtering platform blocking malware, phishing, and ads with real-time threat intelligence feeds.\n• Designed a Go-based DNS resolver with caching, achieving <15ms response times in simulated enterprise and family networks.\n• Developed Node.js API gateway and React dashboard for monitoring, analytics, and configuration management.\n• Containerized services with Docker & Kubernetes; implemented end-to-end testing for DNS filtering, ad blocking, and threat detection.",
            order=1
        )

        Project.objects.create(
            name="WholeSight – AI Nutrition & Health Assistant",
            technologies="Flutter, Dart, Firebase, Google Gemini API",
            description="• Developed a cross-platform mobile app with AI-powered food recognition (>90% accuracy) and multimodal logging (camera, barcode, voice, text).\n• Integrated Firebase (Auth, Firestore, Cloud Storage) and applied Clean Architecture + BLoC pattern for scalability and maintainability.\n• Delivered personalized nutrition insights and meal planning features, increasing engagement in pilot tests by 25%.",
            order=2
        )

        # Research
        Research.objects.create(
            title="Facial Morphing Detection (NYU – Forensics AI)",
            professor="Prof. S. Banerjee",
            date="July 2025",
            technologies="Python, PyTorch, Qwen 2.5, Molmo 2, HuggingFace",
            description="• Built ML pipeline using FISWG 19-feature framework and CLIP-based NLP integration for forensic biometric analysis.\n• Active Research: Exploring distillation of Qwen2.5-72B models into lightweight 7B architectures for faster, resource-efficient detection.",
            order=1
        )

        Research.objects.create(
            title="Computational Neuroscience (NYU Langone)",
            professor="Prof. Robert Froemke",
            date="July 2025",
            technologies="TensorFlow, OpenCV",
            description="• Automated social behaviour quantification from video using ML, improving accuracy vs. manual annotations.\n• Active Research: Developing a computer vision model to trace mice movement patterns from video data, enabling precise behavioural mapping in neural circuit studies.",
            order=2
        )

        # Skills
        SkillCategory.objects.create(
            name="Programming Languages",
            skills="Python, C++, Java, JavaScript, Dart, SQL",
            order=1
        )

        SkillCategory.objects.create(
            name="Databases",
            skills="PostgreSQL, MySQL, SQLite, MongoDB",
            order=2
        )

        SkillCategory.objects.create(
            name="Frameworks",
            skills="TensorFlow, PyTorch, Hugging Face, Flask, React, Flutter, Hadoop",
            order=3
        )

        SkillCategory.objects.create(
            name="Tools",
            skills="Firebase, MicroStrategy, Linux, VS Code",
            order=4
        )

        SkillCategory.objects.create(
            name="Cloud & DevOps",
            skills="AWS (EC2, S3, Lambda), Docker, Kubernetes, Git, CI/CD, Prometheus, Grafana",
            order=5
        )

        SkillCategory.objects.create(
            name="AI/ML & Generative AI",
            skills="Computer Vision (YOLO, OpenCV), NLP (Transformers, CLIP), LLM (Gemini API), Model Training & Deployment",
            order=6
        )

        # Activities
        Activity.objects.create(
            description="Mentored 10+ participants at IC Hack IEEE India Council Hackathon, 2023, providing guidance in app development and offering.",
            order=1
        )

        self.stdout.write(self.style.SUCCESS('Successfully loaded resume data!'))