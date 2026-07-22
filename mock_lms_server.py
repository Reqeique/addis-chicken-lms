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

COURSES = [
    {"name": "course-1", "title": "Poultry Health & Biosecurity", "short_introduction": "Learn essential biosecurity measures to keep your flock healthy and prevent disease outbreaks.", "image": "/assets/lms/images/course-home.png", "type": "Course", "username": "Dr. Almaz Haile", "student_count": 234, "published": 1},
    {"name": "course-2", "title": "Broiler Management Basics", "short_introduction": "From day-old chicks to market-ready birds — everything you need to know about broiler farming.", "image": "/assets/lms/images/course-home.png", "type": "Course", "username": "Dr. Solomon Kebede", "student_count": 189, "published": 1},
    {"name": "course-3", "title": "Layer Hen Management", "short_introduction": "Maximize egg production with proper layer hen care, feeding, and housing management.", "image": "/assets/lms/images/course-home.png", "type": "Course", "username": "Dr. Almaz Haile", "student_count": 312, "published": 1},
    {"name": "course-4", "title": "Poultry Nutrition & Feed Formulation", "short_introduction": "Balance feed costs and nutrition using locally available ingredients for optimal growth.", "image": "/assets/lms/images/course-home.png", "type": "Course", "username": "Dr. Tigist Worku", "student_count": 156, "published": 1},
    {"name": "course-5", "title": "Hatchery Management", "short_introduction": "Set up and run a successful hatchery with proper egg handling, incubation, and hatching practices.", "image": "/assets/lms/images/course-home.png", "type": "Course", "username": "Dr. Solomon Kebede", "student_count": 98, "published": 1},
    {"name": "course-6", "title": "Poultry Business Management", "short_introduction": "Turn your poultry farm into a profitable enterprise with smart record-keeping and financial planning.", "image": "/assets/lms/images/course-home.png", "type": "Course", "username": "Dr. Tigist Worku", "student_count": 203, "published": 1},
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


@app.route("/assets/<path:filename>")
def serve_assets(filename):
    for base in [STATIC_PATH, FRONTEND_PATH]:
        fpath = os.path.join(base, filename)
        if os.path.exists(fpath):
            return send_from_directory(base, filename)
    return send_from_directory(STATIC_PATH, filename)


@app.route("/")
def lms_app():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Addis Chicken Training</title>
    <link rel="icon" href="/assets/lms/frontend/learning.svg">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f7fa; }
        .topbar { background: #0E7159; color: white; padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; }
        .topbar img { width: 40px; height: 40px; border-radius: 8px; }
        .topbar h1 { font-size: 1.3rem; font-weight: 700; }
        .topbar-user { margin-left: auto; display: flex; align-items: center; gap: 0.75rem; }
        .topbar-user .avatar { width: 32px; height: 32px; border-radius: 50%; background: #E85D2C; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; }
        .topbar-user .name { font-size: 0.9rem; }
        .topbar-user .role { font-size: 0.75rem; opacity: 0.7; }
        .layout { display: flex; min-height: calc(100vh - 65px); }
        .sidebar { width: 230px; background: white; border-right: 1px solid #e5e7eb; padding: 1.5rem 1rem; flex-shrink: 0; }
        .sidebar-section { margin-bottom: 1.5rem; }
        .sidebar-section-title { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; color: #9ca3af; margin-bottom: 0.5rem; padding-left: 0.75rem; }
        .sidebar a { display: flex; align-items: center; gap: 0.6rem; padding: 0.55rem 0.75rem; color: #4b5563; text-decoration: none; border-radius: 6px; font-size: 0.875rem; transition: all 0.15s; }
        .sidebar a:hover { background: #ecfdf5; color: #0E7159; }
        .sidebar a.active { background: #ecfdf5; color: #0E7159; font-weight: 600; }
        .sidebar a .icon { font-size: 1rem; width: 20px; text-align: center; }
        .main { flex: 1; padding: 2rem; max-width: 1200px; }
        .page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
        .page-header h2 { font-size: 1.4rem; color: #111827; }
        .btn { background: #0E7159; color: white; border: none; padding: 0.55rem 1.1rem; border-radius: 6px; cursor: pointer; font-size: 0.875rem; font-weight: 500; }
        .btn:hover { background: #0d5c47; }
        .btn-outline { background: white; color: #0E7159; border: 1.5px solid #0E7159; }
        .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.25rem; margin-bottom: 2.5rem; }
        .stat { background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
        .stat .label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #6b7280; margin-bottom: 0.4rem; }
        .stat .value { font-size: 2rem; font-weight: 700; color: #111827; line-height: 1; }
        .stat .change { font-size: 0.8rem; margin-top: 0.4rem; }
        .stat .change.up { color: #059669; }
        .stat .change.down { color: #dc2626; }
        .section { margin-bottom: 2.5rem; }
        .section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
        .section-header h3 { font-size: 1.1rem; color: #111827; }
        .section-header a { font-size: 0.85rem; color: #0E7159; text-decoration: none; }
        .courses { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; }
        .card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; }
        .card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.12); }
        .card-img { width: 100%; height: 140px; object-fit: cover; background: #e5e7eb; }
        .card-body { padding: 1rem; }
        .card-body h4 { font-size: 0.95rem; color: #111827; margin-bottom: 0.4rem; }
        .card-body p { color: #6b7280; font-size: 0.8rem; line-height: 1.5; margin-bottom: 0.75rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .card-meta { display: flex; justify-content: space-between; align-items: center; font-size: 0.78rem; color: #9ca3af; }
        .card-meta .instructor { display: flex; align-items: center; gap: 0.3rem; }
        .card-meta .count { display: flex; align-items: center; gap: 0.3rem; }
        .badge { background: #ecfdf5; color: #065f46; padding: 0.2rem 0.6rem; border-radius: 99px; font-size: 0.72rem; font-weight: 600; }
        .badge-draft { background: #f3f4f6; color: #374151; }
        .badge-active { background: #dbeafe; color: #1e40af; }
        table { width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
        th { text-align: left; padding: 0.85rem 1.25rem; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: #6b7280; border-bottom: 1px solid #f3f4f6; background: #f9fafb; }
        td { padding: 0.85rem 1.25rem; border-bottom: 1px solid #f3f4f6; font-size: 0.875rem; color: #374151; }
        tr:last-child td { border-bottom: none; }
        tr:hover td { background: #f9fafb; }
        .status { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.2rem 0.65rem; border-radius: 99px; font-size: 0.72rem; font-weight: 600; }
        .status-green { background: #d1fae5; color: #065f46; }
        .status-orange { background: #ffedd5; color: #9a3412; }
        .status-blue { background: #dbeafe; color: #1e40af; }
        .progress-bar { width: 80px; height: 6px; background: #e5e7eb; border-radius: 3px; overflow: hidden; display: inline-block; vertical-align: middle; margin-right: 0.5rem; }
        .progress-fill { height: 100%; background: #0E7159; border-radius: 3px; }
        .footer { text-align: center; padding: 2rem; color: #9ca3af; font-size: 0.8rem; }
        .footer a { color: #0E7159; text-decoration: none; }
        .logo-text { font-size: 0.8rem; font-weight: 700; color: #111827; line-height: 1.2; }
        .logo-sub { font-size: 0.7rem; color: #6b7280; }
    </style>
</head>
<body>
    <div class="topbar">
        <img src="/assets/lms/frontend/learning.svg" alt="Logo">
        <div>
            <h1>Addis Chicken Training</h1>
        </div>
        <div class="topbar-user">
            <div style="text-align:right">
                <div class="name">Addis Admin</div>
                <div class="role">Administrator</div>
            </div>
            <div class="avatar">AA</div>
        </div>
    </div>
    <div class="layout">
        <div class="sidebar">
            <div class="sidebar-section">
                <div class="sidebar-section-title">Main</div>
                <a href="#" class="active"><span class="icon">📊</span> Dashboard</a>
                <a href="#"><span class="icon">📚</span> Courses</a>
                <a href="#"><span class="icon">👥</span> Batches</a>
                <a href="#"><span class="icon">📝</span> Quizzes</a>
                <a href="#"><span class="icon">📋</span> Assignments</a>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">Learning</div>
                <a href="#"><span class="icon">🎓</span> Certificates</a>
                <a href="#"><span class="icon">📈</span> Statistics</a>
                <a href="#"><span class="icon">📅</span> Live Classes</a>
                <a href="#"><span class="icon">💼</span> Job Openings</a>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">Administration</div>
                <a href="#"><span class="icon">⚙️</span> Settings</a>
                <a href="#"><span class="icon">👤</span> Manage Users</a>
                <a href="#"><span class="icon">🔔</span> Notifications</a>
            </div>
        </div>
        <div class="main">
            <div class="page-header">
                <h2>Dashboard</h2>
                <div style="display:flex;gap:0.75rem">
                    <button class="btn btn-outline">📥 Export</button>
                    <button class="btn">+ New Course</button>
                </div>
            </div>

            <div class="stats">
                <div class="stat">
                    <div class="label">Total Courses</div>
                    <div class="value">6</div>
                    <div class="change up">▲ 2 new this month</div>
                </div>
                <div class="stat">
                    <div class="label">Total Students</div>
                    <div class="value">1,192</div>
                    <div class="change up">▲ 143 this week</div>
                </div>
                <div class="stat">
                    <div class="label">Active Batches</div>
                    <div class="value">3</div>
                    <div class="change">137 enrolled</div>
                </div>
                <div class="stat">
                    <div class="label">Certificates Issued</div>
                    <div class="value">4</div>
                    <div class="change up">▲ 12 this month</div>
                </div>
            </div>

            <div class="section">
                <div class="section-header">
                    <h3>Featured Courses</h3>
                    <a href="#">View all →</a>
                </div>
                <div class="courses">
""" + "".join(f"""
                    <div class="card">
                        <img class="card-img" src="{c['image']}" onerror="this.src='/assets/lms/images/course-home.png'" alt="{c['title']}">
                        <div class="card-body">
                            <h4>{c['title']}</h4>
                            <p>{c['short_introduction']}</p>
                            <div class="card-meta">
                                <span class="instructor">👤 {c['username']}</span>
                                <span class="badge">Published</span>
                            </div>
                            <div style="margin-top:0.6rem;font-size:0.78rem;color:#6b7280;">{c['student_count']} students enrolled</div>
                        </div>
                    </div>
""" for c in COURSES) + """
                </div>
            </div>

            <div class="section">
                <div class="section-header">
                    <h3>Recent Enrollments</h3>
                    <a href="#">View all →</a>
                </div>
                <table>
                    <thead><tr><th>Student</th><th>Course</th><th>Batch</th><th>Status</th><th>Progress</th></tr></thead>
                    <tbody>
                        <tr><td><b>Abebe Girma</b></td><td>Broiler Management Basics</td><td>Aug 2026 Batch</td><td><span class="status status-green">● Active</span></td><td><div class="progress-bar"><div class="progress-fill" style="width:65%"></div></div>65%</td></tr>
                        <tr><td><b>Chala Bekele</b></td><td>Layer Hen Management</td><td>Cohort 3</td><td><span class="status status-green">● Active</span></td><td><div class="progress-bar"><div class="progress-fill" style="width:42%"></div></div>42%</td></tr>
                        <tr><td><b>Mulu Tesfaye</b></td><td>Poultry Health & Biosecurity</td><td>Biosecurity Workshop</td><td><span class="status status-green">● Active</span></td><td><div class="progress-bar"><div class="progress-fill" style="width:88%"></div></div>88%</td></tr>
                        <tr><td><b>Yonas Damtew</b></td><td>Feed Formulation</td><td>Aug 2026 Batch</td><td><span class="status status-orange">○ Not Started</span></td><td><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div>0%</td></tr>
                        <tr><td><b>Hiwot Amare</b></td><td>Hatchery Management</td><td>Cohort 3</td><td><span class="status status-blue">✓ Completed</span></td><td><div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div>100%</td></tr>
                        <tr><td><b>Tadesse Alemu</b></td><td>Business Management</td><td>Aug 2026 Batch</td><td><span class="status status-green">● Active</span></td><td><div class="progress-bar"><div class="progress-fill" style="width:30%"></div></div>30%</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="section">
                <div class="section-header">
                    <h3>Active Batches</h3>
                    <a href="#">View all →</a>
                </div>
                <table>
                    <thead><tr><th>Batch Name</th><th>Course</th><th>Start Date</th><th>End Date</th><th>Members</th><th>Status</th></tr></thead>
                    <tbody>
                        <tr><td><b>Broiler Starter Batch - Aug 2026</b></td><td>Broiler Management Basics</td><td>2026-08-01</td><td>2026-09-15</td><td>42</td><td><span class="status status-green">● Ongoing</span></td></tr>
                        <tr><td><b>Layer Farmers Cohort 3</b></td><td>Layer Hen Management</td><td>2026-08-10</td><td>2026-11-10</td><td>67</td><td><span class="status status-green">● Ongoing</span></td></tr>
                        <tr><td><b>Advanced Biosecurity Workshop</b></td><td>Poultry Health & Biosecurity</td><td>2026-09-01</td><td>2026-09-20</td><td>28</td><td><span class="status status-blue">○ Upcoming</span></td></tr>
                    </tbody>
                </table>
            </div>

            <div class="section">
                <div class="section-header">
                    <h3>Recent Certificates Issued</h3>
                </div>
                <table>
                    <thead><tr><th>Student</th><th>Course</th><th>Issued Date</th><th>Certificate ID</th><th>Status</th></tr></thead>
                    <tbody>
""" + "".join(f"""
                        <tr><td><b>{cert['member_name']}</b></td><td>{cert['course_name']}</td><td>{cert['issue_date']}</td><td style="font-family:monospace;font-size:0.8rem;color:#6b7280;">{cert['certificate_id']}</td><td><span class="status status-green">✓ Issued</span></td></tr>
""" for cert in CERTIFICATES) + """
                    </tbody>
                </table>
            </div>

            <div class="footer">
                Powered by <a href="#">Addis Chicken Training</a> LMS — Built on Frappe Framework
            </div>
        </div>
    </div>
</body>
</html>"""


@app.route("/api/method/frappe.boot")
def frappe_boot():
    return jsonify({
        "message": None, "EXPIRY": "2030-12-31", "home_url": "/app",
        "boot": {
            "user": {"name": "Addis Chicken Admin", "fullname": "Addis Chicken Admin", "email": "admin@addispoultry.com", "username": "admin", "user_id": "admin", "roles": ["System Manager", "LMS Admin"], "is_authenticated": True},
            "lang": "en",
            "website": {"name": "Addis Chicken Training"},
            "modules": {"LMS": {"label": "Addis Chicken Training", "icon": "book", "route": "/lms"}},
        },
        "session": {"user": "admin", "sid": "mock-sid-12345", "email": "admin@addispoultry.com"},
        "fullname": "Addis Chicken Admin", "user_image": "", "user_id": "admin",
        "headers": {"X-Frappe-CSRF-Token": "mock-csrf-token-12345"}
    })


@app.route("/api/method/lms.lms.api.get_courses")
def get_courses():
    return jsonify({"message": COURSES, "exc": None})


@app.route("/api/method/lms.lms.api.get_batches")
def get_batches():
    return jsonify({"message": BATCHES, "exc": None})


@app.route("/api/method/lms.lms.api.get_statistics")
def get_stats():
    return jsonify({
        "message": {"total_courses": len(COURSES), "total_students": sum(c["student_count"] for c in COURSES), "total_batches": len(BATCHES), "total_certificates": len(CERTIFICATES), "active_learners": 412, "courses_published": len([c for c in COURSES if c.get("published")])},"exc": None
    })


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


@app.route("/api/method/lms.lms.api.get_certificates")
def get_certificates():
    return jsonify({"message": CERTIFICATES, "exc": None})


@app.route("/api/method/lms.lms.api.get_students")
def get_students():
    return jsonify({"message": [u for u in USERS if u["role"] == "Student"], "exc": None})


@app.route("/api/method/lms.lms.api.get_instructors")
def get_instructors():
    return jsonify({"message": [u for u in USERS if u["role"] == "Instructor"], "exc": None})


if __name__ == "__main__":
    print("Starting Addis Chicken Training LMS on http://localhost:8080")
    app.run(host="0.0.0.0", port=8080, debug=False)