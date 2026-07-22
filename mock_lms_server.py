"""
Addis Chicken Training LMS - Mock Flask Server
Serves the rebranded Frappe LMS with realistic dummy data.
"""

from flask import Flask, send_from_directory, jsonify, request, redirect
import os

app = Flask(__name__, static_folder=None)

REPO_PATH = "/tmp/poultry-lms"
STATIC_PATH = os.path.join(REPO_PATH, "lms", "public")
FRONTEND_PATH = os.path.join(REPO_PATH, "frontend", "public")

# ---- Dummy Data ----

COURSES = [
    {
        "name": "course-1",
        "title": "Poultry Health & Biosecurity",
        "short_introduction": "Learn essential biosecurity measures to keep your flock healthy and prevent disease outbreaks.",
        "image": "/assets/lms/images/course-home.png",
        "type": "Course",
        "username": "Dr. Almaz Haile",
        "学员count": 234,
        "published": 1,
    },
    {
        "name": "course-2",
        "title": "Broiler Management Basics",
        "short_introduction": "From day-old chicks to market-ready birds — everything you need to know about broiler farming.",
        "image": "/assets/lms/images/course-home.png",
        "type": "Course",
        "username": "Dr. Solomon Kebede",
        "学员count": 189,
        "published": 1,
    },
    {
        "name": "course-3",
        "title": "Layer Hen Management",
        "short_introduction": "Maximize egg production with proper layer hen care, feeding, and housing management.",
        "image": "/assets/lms/images/course-home.png",
        "type": "Course",
        "username": "Dr. Almaz Haile",
        "学员count": 312,
        "published": 1,
    },
    {
        "name": "course-4",
        "title": "Poultry Nutrition & Feed Formulation",
        "short_introduction": "Balance feed costs and nutrition using locally available ingredients for optimal growth.",
        "image": "/assets/lms/images/course-home.png",
        "type": "Course",
        "username": "Dr. Tigist Worku",
        "学员count": 156,
        "published": 1,
    },
    {
        "name": "course-5",
        "title": "Hatchery Management",
        "short_introduction": "Set up and run a successful hatchery with proper egg handling, incubation, and hatching practices.",
        "image": "/assets/lms/images/course-home.png",
        "type": "Course",
        "username": "Dr. Solomon Kebede",
        "学员count": 98,
        "published": 1,
    },
    {
        "name": "course-6",
        "title": "Poultry Business Management",
        "short_introduction": "Turn your poultry farm into a profitable enterprise with smart record-keeping and financial planning.",
        "image": "/assets/lms/images/course-home.png",
        "type": "Course",
        "username": "Dr. Tigist Worku",
        "学员count": 203,
        "published": 1,
    },
]

BATCHES = [
    {"name": "batch-1", "title": "Broiler Starter Batch - Aug 2026", "start_date": "2026-08-01", "end_date": "2026-09-15", "member_count": 42, "course": "Broiler Management Basics"},
    {"name": "batch-2", "title": "Layer Farmers Cohort 3", "start_date": "2026-08-10", "end_date": "2026-11-10", "member_count": 67, "course": "Layer Hen Management"},
    {"name": "batch-3", "title": "Advanced Biosecurity Workshop", "start_date": "2026-09-01", "end_date": "2026-09-20", "member_count": 28, "course": "Poultry Health & Biosecurity"},
]

CERTIFICATES = [
    {"name": "cert-1", "member_name": "Abebe Girma", "course_name": "Poultry Health & Biosecurity", "issue_date": "2026-06-15", "certificate_id": "ACT-2026-00142"},
    {"name": "cert-2", "member_name": "Chala Bekele", "course_name": "Broiler Management Basics", "issue_date": "2026-06-20", "certificate_id": "ACT-2026-00189"},
    {"name": "cert-3", "member_name": "Mulu Tesfaye", "course_name": "Layer Hen Management", "issue_date": "2026-07-01", "certificate_id": "ACT-2026-00234"},
    {"name": "cert-4", "member_name": "Yonas Damtew", "course_name": "Poultry Nutrition & Feed Formulation", "issue_date": "2026-07-10", "certificate_id": "ACT-2026-00301"},
]

USERS = [
    {"name": "user-1", "full_name": "Dr. Almaz Haile", "email": "almaz@addispoultry.com", "role": "Instructor"},
    {"name": "user-2", "full_name": "Dr. Solomon Kebede", "email": "solomon@addispoultry.com", "role": "Instructor"},
    {"name": "user-3", "full_name": "Dr. Tigist Worku", "email": "tigist@addispoultry.com", "role": "Instructor"},
    {"name": "user-4", "full_name": "Abebe Girma", "email": "abebe.girma@email.com", "role": "Student"},
    {"name": "user-5", "full_name": "Chala Bekele", "email": "chala.bekele@email.com", "role": "Student"},
]

# ---- Static Files ----

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    # Try lms public first, then frontend public
    lms_file = os.path.join(STATIC_PATH, filename)
    fe_file = os.path.join(FRONTEND_PATH, filename)
    if os.path.exists(lms_file):
        return send_from_directory(STATIC_PATH, filename)
    if os.path.exists(fe_file):
        return send_from_directory(FRONTEND_PATH, filename)
    # Fallback - serve from lms public
    return send_from_directory(STATIC_PATH, filename)

@app.route("/")
def index():
    return send_from_directory(STATIC_PATH, "index.html")

# ---- API Routes ----

@app.route("/api/method/frappe.boot")
def frappe_boot():
    return jsonify({
        "message": None,
        "EXPIRY": "2030-12-31",
        "home_url": "/app",
        "boot": {
            "user": {
                "name": "Addis Chicken Admin",
                "fullname": "Addis Chicken Admin",
                "user_image": "",
                "email": "admin@addispoultry.com",
                "username": "admin",
                "user_id": "admin",
                "roles": ["System Manager", "LMS Admin"],
                "is_authenticated": True,
            },
            "user_defaults": {},
            "lang": "en",
            "list_runs": {},
            "boot": {
                "css": [],
                "js": [],
                "website": {
                    "name": "Addis Chicken Training",
                    "full_name": "Addis Chicken Training",
                    "brand_html": '<img src="/assets/lms/frontend/learning.svg" style="height:24px;width:24px;" /> Addis Chicken Training',
                },
            },
            "modules": {
                "LMS": {
                    "label": "Addis Chicken Training",
                    "icon": "book",
                    "route": "/lms",
                }
            },
            "assets_json": "/assets/assets.json",
            "boot": {"modules": []},
            "defaults": {},
            "user": {"defaults": {}},
            "doctype_js": {},
            "dict": {},
            "hidden_modules": [],
            "link_title_doctypes": [],
            "server_messages": {},
            "warning_messages": [],
            "sysdefaults": {
                "assume_role": "System Manager",
                "list_page_height": 200,
                "row_count": 50,
                "last_server_date": "2026-07-22",
            },
            "user_info": [[u.get("name",""), u.get("full_name","")] for u in USERS],
        },
        "session": {"user": "admin", "sid": "mock-sid-12345", "email": "admin@addispoultry.com"},
        "fullname": "Addis Chicken Admin",
        "user_image": "",
        "user_id": "admin",
        "headers": {
            "X-Frappe-CSRF-Token": "mock-csrf-token-12345",
        }
    })

@app.route("/api/method/lms.lms.api.get_courses")
def get_courses():
    return jsonify({"message": COURSES, "exc": None})

@app.route("/api/method/lms.lms.api.get_batches")
def get_batches():
    return jsonify({"message": BATCHES, "exc": None})

@app.route("/api/method/lms.lms.api.get_quizzes")
def get_quizzes():
    return jsonify({"message": [], "exc": None})

@app.route("/api/method/lms.lms.api.get_statistics")
def get_stats():
    return jsonify({
        "message": {
            "total_courses": len(COURSES),
            "total_students": sum(c["学员count"] for c in COURSES),
            "total_batches": len(BATCHES),
            "total_certificates": len(CERTIFICATES),
            "active_learners": 412,
            "courses_published": len([c for c in COURSES if c.get("published")]),
        },
        "exc": None
    })

@app.route("/api/method/lms.lms.api.get_enrollments")
def get_enrollments():
    return jsonify({"message": [], "exc": None})

@app.route("/api/method/lms.lms.api.get_branding")
def get_branding():
    return jsonify({
        "app_name": "Addis Chicken Training",
        "app_logo": "/assets/lms/frontend/learning.svg",
        "banner_image": None,
        "favicon": {"file_url": "/assets/lms/frontend/learning.svg"},
    })

@app.route("/api/method/lms.lms.api.check_app_permission")
def check_permission():
    return jsonify({"has_permission": True, "exc": None})

@app.route("/api/method/frappe.auth.get_logged_user")
def get_logged_user():
    return jsonify({"message": "admin"})

@app.route("/api/method/frappe.get_site_config")
def get_site_config():
    return jsonify({
        "site_config": {
            "app_name": "Addis Chicken Training",
            "footer Powered": "Addis Chicken Training",
        }
    })

@app.route("/api/method/lms.lms.api.get_certificates")
def get_certificates():
    return jsonify({"message": CERTIFICATES, "exc": None})

@app.route("/api/method/lms.lms.api.get_students")
def get_students():
    return jsonify({"message": [u for u in USERS if u["role"] == "Student"], "exc": None})

@app.route("/api/method/lms.lms.api.get_instructors")
def get_instructors():
    return jsonify({"message": [u for u in USERS if u["role"] == "Instructor"], "exc": None})

@app.route("/api/method/lms.lms.api.get_lms_course/<course_name>")
def get_course(course_name):
    for c in COURSES:
        if c["name"] == course_name:
            return jsonify({"message": c, "exc": None})
    return jsonify({"message": None, "exc": "Course not found"})

@app.route("/app")
def lms_app():
    """Serve the LMS app entry point"""
    index_path = os.path.join(STATIC_PATH, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(STATIC_PATH, "index.html")
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Addis Chicken Training</title>
        <link rel="icon" href="/assets/lms/frontend/learning.svg">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f7fa; }}
            .header {{ background: #0E7159; color: white; padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; }}
            .header img {{ width: 40px; height: 40px; border-radius: 8px; }}
            .header h1 {{ font-size: 1.4rem; }}
            .sidebar {{ width: 220px; background: white; min-height: 100vh; padding: 1rem; border-right: 1px solid #e5e7eb; position: fixed; top: 0; left: 0; overflow-y: auto; }}
            .sidebar nav a {{ display: flex; align-items: center; gap: 0.5rem; padding: 0.6rem 0.8rem; color: #374151; text-decoration: none; border-radius: 6px; margin-bottom: 0.25rem; font-size: 0.9rem; }}
            .sidebar nav a:hover, .sidebar nav a.active {{ background: #ecfdf5; color: #0E7159; }}
            .main {{ margin-left: 220px; padding: 2rem; }}
            .stat-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-bottom: 2rem; }}
            .stat-card {{ background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
            .stat-card .label {{ color: #6b7280; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; }}
            .stat-card .value {{ font-size: 2rem; font-weight: 700; color: #111827; }}
            .stat-card .sub {{ color: #0E7159; font-size: 0.85rem; margin-top: 0.25rem; }}
            .section-title {{ font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; color: #111827; }}
            .course-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
            .course-card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: transform 0.2s; }}
            .course-card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}
            .course-card img {{ width: 100%; height: 140px; object-fit: cover; }}
            .course-card .body {{ padding: 1rem; }}
            .course-card h3 {{ font-size: 1rem; margin-bottom: 0.5rem; color: #111827; }}
            .course-card p {{ color: #6b7280; font-size: 0.85rem; margin-bottom: 0.75rem; line-height: 1.4; }}
            .course-card .meta {{ display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: #9ca3af; }}
            .course-card .badge {{ background: #ecfdf5; color: #0E7159; padding: 0.25rem 0.6rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600; }}
            .table-wrap {{ background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 2rem; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th {{ text-align: left; padding: 0.75rem 1rem; color: #6b7280; font-size: 0.8rem; text-transform: uppercase; border-bottom: 2px solid #f3f4f6; }}
            td {{ padding: 0.85rem 1rem; border-bottom: 1px solid #f3f4f6; color: #374151; font-size: 0.9rem; }}
            tr:last-child td {{ border-bottom: none; }}
            .badge-green {{ background: #d1fae5; color: #065f46; padding: 0.2rem 0.6rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600; }}
            .badge-orange {{ background: #ffedd5; color: #9a3412; padding: 0.2rem 0.6rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600; }}
            .badge-blue {{ background: #dbeafe; color: #1e40af; padding: 0.2rem 0.6rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600; }}
            .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }}
            .top-bar h2 {{ font-size: 1.3rem; }}
            .btn {{ background: #0E7159; color: white; border: none; padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem; }}
            .btn:hover {{ background: #0d5c47; }}
        </style>
    </head>
    <body>
        <div class="sidebar">
            <div style="display:flex;align-items:center;gap:0.75rem;padding:0.5rem 0.8rem;margin-bottom:1rem;border-bottom:1px solid #e5e7eb;">
                <img src="/assets/lms/frontend/learning.svg" width="32" height="32" style="border-radius:6px;">
                <div style="font-size:0.85rem;font-weight:700;color:#111827;line-height:1.2;">Addis Chicken<br>Training</div>
            </div>
            <nav>
                <a href="#" class="active"><span>📊</span> Dashboard</a>
                <a href="#"><span>📚</span> Courses</a>
                <a href="#"><span>👥</span> Batches</a>
                <a href="#"><span>📝</span> Quizzes</a>
                <a href="#"><span>🎓</span> Certificates</a>
                <a href="#"><span>📈</span> Statistics</a>
                <a href="#"><span>⚙️</span> Settings</a>
            </nav>
        </div>
        <div class="main">
            <div class="header" style="margin: -2rem -2rem 2rem -2rem; border-radius:0;">
                <img src="/assets/lms/frontend/learning.svg">
                <div>
                    <h1>Addis Chicken Training LMS</h1>
                    <div style="font-size:0.85rem;opacity:0.8;margin-top:0.15rem;">Welcome back, Admin</div>
                </div>
            </div>

            <div class="stat-grid">
                <div class="stat-card">
                    <div class="label">Total Courses</div>
                    <div class="value">6</div>
                    <div class="sub">6 published</div>
                </div>
                <div class="stat-card">
                    <div class="label">Total Students</div>
                    <div class="value">1,192</div>
                    <div class="sub">412 active learners</div>
                </div>
                <div class="stat-card">
                    <div class="label">Active Batches</div>
                    <div class="value">3</div>
                    <div class="sub">137 enrolled</div>
                </div>
                <div class="stat-card">
                    <div class="label">Certificates Issued</div>
                    <div class="value">4</div>
                    <div class="sub">+12 this month</div>
                </div>
            </div>

            <div class="top-bar">
                <h2 class="section-title">📚 Featured Courses</h2>
                <button class="btn">+ New Course</button>
            </div>
            <div class="course-grid">
                {''.join(f'''
                <div class="course-card">
                    <img src="{c['image']}" onerror="this.src='/assets/lms/images/course-home.png'">
                    <div class="body">
                        <h3>{c["title"]}</h3>
                        <p>{c["short_introduction"]}</p>
                        <div class="meta">
                            <span>👤 {c["username"]}</span>
                            <span class="badge">Published</span>
                        </div>
                        <div style="margin-top:0.75rem;font-size:0.8rem;color:#6b7280;">{c["学员count"]} students enrolled</div>
                    </div>
                </div>''' for c in COURSES[:6])}
            </div>

            <h2 class="section-title" style="margin-top:2rem;">👥 Recent Enrollments</h2>
            <div class="table-wrap">
                <table>
                    <thead><tr><th>Student</th><th>Course</th><th>Batch</th><th>Status</th><th>Progress</th></tr></thead>
                    <tbody>
                        <tr><td>Abebe Girma</td><td>Broiler Management Basics</td><td>Aug 2026 Batch</td><td><span class="badge-green">Active</span></td><td>65%</td></tr>
                        <tr><td>Chala Bekele</td><td>Layer Hen Management</td><td>Cohort 3</td><td><span class="badge-green">Active</span></td><td>42%</td></tr>
                        <tr><td>Mulu Tesfaye</td><td>Poultry Health & Biosecurity</td><td>Workshop</td><td><span class="badge-green">Active</span></td><td>88%</td></tr>
                        <tr><td>Yonas Damtew</td><td>Feed Formulation</td><td>Aug 2026 Batch</td><td><span class="badge-orange">Not Started</span></td><td>0%</td></tr>
                        <tr><td>Hiwot Amare</td><td>Hatchery Management</td><td>Cohort 3</td><td><span class="badge-blue">Completed</span></td><td>100%</td></tr>
                        <tr><td>Tadesse Alemu</td><td>Business Management</td><td>Aug 2026 Batch</td><td><span class="badge-green">Active</span></td><td>30%</td></tr>
                    </tbody>
                </table>
            </div>

            <h2 class="section-title">🎓 Recent Certificates</h2>
            <div class="table-wrap">
                <table>
                    <thead><tr><th>Student</th><th>Course</th><th>Issued</th><th>Certificate ID</th><th>Status</th></tr></thead>
                    <tbody>
                        {''.join(f'''<tr><td>{cert["member_name"]}</td><td>{cert["course_name"]}</td><td>{cert["issue_date"]}</td><td style="font-family:monospace;font-size:0.8rem;">{cert["certificate_id"]}</td><td><span class="badge-green">Issued</span></td></tr>''' for cert in CERTIFICATES)}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("Starting Addis Chicken Training LMS on http://localhost:8080")
    app.run(host="0.0.0.0", port=8080, debug=False)