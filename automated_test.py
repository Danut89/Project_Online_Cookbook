from app import create_app
from flask import url_for

# Create app and set test config
app = create_app()
app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False

# Run test client
with app.test_client() as client:
    print("===== Automated Route Testing =====")

    # Home Page
    r = client.get("/")
    print("Home page:", "✅ Pass" if r.status_code == 200 else f"❌ Fail ({r.status_code})")

    # Browse Recipes
    r = client.get("/browse")
    print("Browse page:", "✅ Pass" if r.status_code == 200 else f"❌ Fail ({r.status_code})")

    # View Recipe (might not exist, so 404 is acceptable)
    r = client.get("/recipe/1")
    print("Recipe view (no data):", "✅ Pass" if r.status_code in [200, 404] else f"❌ Fail ({r.status_code})")

    # Contact Page
    r = client.get("/contact")
    print("Contact page:", "✅ Pass" if r.status_code == 200 else f"❌ Fail ({r.status_code})")

    # Add Recipe (requires login → should redirect)
    r = client.get("/add_recipe")
    redirected = r.status_code in [302, 401]
    print("Add recipe (not logged in):", "✅ Pass" if redirected else f"❌ Fail ({r.status_code})")

    # Admin Dashboard (requires admin)
    r = client.get("/admin")
    print("Admin dashboard (unauthorized):", "✅ Pass" if r.status_code in [302, 403] else f"❌ Fail ({r.status_code})")

    # Profile page (should redirect if not logged in)
    r = client.get("/profile")
    print("Profile page (not logged in):", "✅ Pass" if r.status_code in [302, 401] else f"❌ Fail ({r.status_code})")
