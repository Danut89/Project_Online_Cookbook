## 📋 Table of Contents

- [🔄 Manual Feature Testing](#manual-feature-testing)
- [👥 User Story Testing](#user-story-testing)
- [🧪 Edge Case & Validation Testing](#edge-case--validation-testing)
- [🔐 Admin Access Control Testing](#admin-access-control-testing)
- [❗ Known Bugs](#known-bugs)
- [🛠️ Bugs and Fixes Log](#bugs-and-fixes-log)
- [✅ Validation Results](#validation)
- [📱 Responsiveness Testing](#responsiveness-testing)
- [♿ Accessibility](#accessibility)




## 🧪 Testing

### Manual Testing

Manual testing was performed across the site's major features to ensure expected behavior:

### Manual Feature Testing

| Feature                             | Tested On               | Expected Result                        | Outcome     |
|-------------------------------------|--------------------------|-----------------------------------------|-------------|
| User Registration                   | Desktop / Mobile         | New user created, redirected to home    | ✅ Pass      |
| Login / Logout                      | Desktop / Mobile         | Successful login and logout flow        | ✅ Pass      |
| Create Recipe                       | Desktop / Mobile         | Recipe added and appears in listing     | ✅ Pass      |
| Edit / Delete Recipe                | Desktop / Mobile         | Updates saved / recipe deleted          | ✅ Pass      |
| Comment on Recipe                   | Desktop / Mobile         | Comment added and visible               | ✅ Pass      |
| Like / Unlike Recipe                | Desktop / Mobile         | Like toggles and updates count          | ✅ Pass      |
| Admin Dashboard (delete user/comment) | Desktop                | Admin action successful, database updated | ✅ Pass   |

### UI & Navigation Manual Testing

| Feature Tested                          | Interaction Tested                         | Expected Behavior                                | Outcome   |
|----------------------------------------|--------------------------------------------|--------------------------------------------------|-----------|
| Navigation Links                       | Click "Home", "Explore", "Add Recipe"      | Page loads correctly with scroll to top          | ✅ Pass    |
| Logo Click                              | Click logo from any page                   | Redirects to homepage                            | ✅ Pass    |
| Add Recipe (Empty Form)                | Submit form without fields filled          | WTForms shows error messages                     | ✅ Pass    |
| Edit Recipe (Own)                      | Click “Edit” on own recipe                 | Edit form loads prefilled and saves changes      | ✅ Pass    |
| Delete Recipe                          | Click “Delete” on own recipe → Confirm     | Modal appears, recipe is deleted                 | ✅ Pass    |
| Delete Confirmation Modal              | Click outside modal or "Cancel"            | Modal closes without action                      | ✅ Pass    |
| Responsive Navbar                      | Open on mobile → click burger menu         | Navbar expands and links are accessible          | ✅ Pass    |
| Scroll to Section via TOC              | Click README Table of Contents link        | Page scrolls smoothly to correct section         | ✅ Pass    |
| Like Button                            | Toggle heart icon                          | Like/unlike visually updates, count changes      | ✅ Pass    |
| View Recipe Details                    | Click recipe card                          | Full recipe page loads with title + ingredients  | ✅ Pass    |
| Comment Section Scroll                 | Post new comment                           | Page scrolls to comment section                  | ✅ Pass    |

---

###  Edge Case & Validation Testing

| Scenario                            | Expected Result                        | Outcome |
|-------------------------------------|----------------------------------------|---------|
| Submitting empty registration form  | WTForms shows error messages           | ✅ Pass |
| Password mismatch during register   | WTForms prevents submission            | ✅ Pass |
| Invalid Cloudinary upload URL       | Flask error handler triggered          | ✅ Pass |
| Accessing `/add-recipe` while logged out | Redirects to login page           | ✅ Pass |
| Trying to like recipe while logged out | Redirect to login page              | ✅ Pass |
| Submitting empty comment            | Form shows validation error            | ✅ Pass |
| Visiting deleted recipe URL         | 404 page or handled gracefully         | ✅ Pass |

---

###  Admin Access Control Testing

| Action                                | User Role     | Expected Behavior             | Outcome |
|--------------------------------------|---------------|-------------------------------|---------|
| Accessing admin dashboard            | Admin         | Dashboard loads               | ✅ Pass |
| Accessing admin dashboard            | Regular User  | Access denied or redirected   | ✅ Pass |
| Promote/demote user from dashboard   | Admin         | Role updated in database      | ✅ Pass |
| Delete any user/comment              | Admin         | Successfully removed          | ✅ Pass |

---

###  User Story Testing

Each user story listed in the [UX section](#user-stories) has been manually tested to ensure that all user needs are met by the application features.

| User Role         | User Story                                                                 | Implemented Feature(s)                        | Tested? |
|-------------------|------------------------------------------------------------------------------|-----------------------------------------------|---------|
| Visitor           | I want to browse available recipes without registering                      | Explore page with search & filters            | ✅ Yes  |
| Visitor           | I want to filter recipes by cuisine, difficulty, or category                | Search bar, category grid, filter dropdowns   | ✅ Yes  |
| Visitor           | I want to view full recipe details before registering                       | Public recipe detail pages                    | ✅ Yes  |
| Registered User   | I want to create and share my own recipes                                    | Add recipe form                               | ✅ Yes  |
| Registered User   | I want to edit or delete my submitted recipes                               | Edit/Delete buttons on my recipes             | ✅ Yes  |
| Registered User   | I want to like/favorite recipes I enjoy                                     | Like button (❤️) on recipe cards              | ✅ Yes  |
| Registered User   | I want to comment on other users’ recipes                                   | Comment form below each recipe                | ✅ Yes  |
| Registered User   | I want to view my profile with all my recipes and favorites                 | User profile page                             | ✅ Yes  |
| Admin             | I want to moderate submitted recipes and comments                           | Admin dashboard → manage recipes/comments     | ✅ Yes  |
| Admin             | I want to promote/demote or delete users                                    | Admin dashboard → user management             | ✅ Yes  |
| Mobile User       | I want full functionality on my phone                                       | Responsive layout + mobile nav                | ✅ Yes  |
| Mobile User       | I want the site to be touch-friendly and easy to navigate                   | Button spacing, touch targets, mobile-first   | ✅ Yes  |

---

###  Testing Coverage Summary

| Testing Area               | Coverage         |
|---------------------------|------------------|
| User authentication       | ✔️ Fully tested   |
| Recipe CRUD               | ✔️ Fully tested   |
| Image upload (Cloudinary) | ✔️ Fully tested   |
| Likes & Comments          | ✔️ Fully tested   |
| Admin functionality       | ✔️ Fully tested   |
| Search & Filters          | ✔️ Manually tested |
| Mobile responsiveness     | ✔️ Tested on real devices & DevTools |
| Validation (Forms, HTML)  | ✔️ HTML5, WTForms, Lighthouse |
| User Stories  | ✔️ Fully tested |

---

###  Validation

- **HTML**: Validated using [W3C HTML Validator](https://validator.w3.org/)  
- **CSS**: Validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  
- **Python / Flask**: Code checked with `flake8` for linting and PEP8 compliance  
- **Forms**: Flask-WTF ensures server-side validation with proper feedback  

<details>
<summary>📱 Validation Screenshots (Click to expand)</summary>

- **HTML validation**  
  ![validation-html.png](/app/static/readme-screenshoots/html-validation.png)

- **CSS validation**  
  ![validation-css.png](/app/static/readme-screenshoots/css-validation.png)

- **Python validation**  
  ![flake8-results.png](/app/static/readme-screenshoots/python-validation.png)

</details>

---

###  Responsiveness Testing

Tested across different screen sizes using:
- ✅ Chrome DevTools (mobile + tablet views)
- ✅ Real devices: iPhone 13, iPad Air, Samsung Galaxy S10

All key features (forms, navigation, modals, category cards) function and scale correctly across breakpoints.

<details>
<summary>📱 Responsive Screenshots (Click to expand)</summary>

- **Homepage (Mobile)**  
  ![Homepage Mobile](/app/static/readme-screenshoots/mobile-responsivness.png)

- **Explore Page (Tablet)**  
  ![Explore Tablet](/app/static/readme-screenshoots/tablet-responsivness.png)

- **Recipe Details (Mobile)**  
  ![Recipe Details Mobile](/app/static/readme-screenshoots/mobile-viewrecipe.png)

</details>

---

### 🌐 Browser Compatibility

Tested the application in the following browsers:

| Browser         | Version Tested | Result   |
|----------------|----------------|----------|
| Chrome         | 120+           | ✅ Pass   |
| Firefox        | 118+           | ✅ Pass   |
| Edge           | 116+           | ✅ Pass   |
| Safari (iOS)   | 15+            | ✅ Pass   |
| Brave          | Latest         | ✅ Pass   |

---

###  Accessibility

DishCraft was built with accessibility as a core consideration, ensuring the platform is inclusive and user-friendly for all visitors, including those using assistive technologies.

Key accessibility measures implemented:

- **Semantic HTML Structure**  
- **Keyboard Navigability**  
- **Color Contrast Compliance** (WCAG 2.1 AA)  
- **Descriptive Alt Text**  
- **Accessible Forms with Labels & ARIA**  
- **Modal Accessibility with ARIA roles**  
- **Responsive Typography**  

<details>
<summary>🌐 Lighthouse Accessibility Audit (Click to expand)</summary>

Accessibility audits were performed using Chrome’s Lighthouse tool to validate best practices across different views of the application.

**Add Recipe Page Accessibility Score**  
![Lighthouse Audit](/app/static/readme-screenshoots/accesibility-addrecipe.png)

**Explore Recipe Page Accessibility Score**  
![Lighthouse Audit](/app/static/readme-screenshoots/accesibility-browse_recipe.png)

**Profile Page Accessibility Score**  
![Lighthouse Audit](/app/static/readme-screenshoots/accesibility=profile.png)

</details>

---

###  Bugs and Fixes Log

| Bug Description                           | Resolution                                  |
|-------------------------------------------|----------------------------------------------|
| Cloudinary images not displaying after deploy    | Corrected Cloudinary ENV variables and updated config usage |
| Category seeding caused SyntaxError in Render shell | Used line-by-line safe seeding via Flask shell             |
| Recipe cards overflow on mobile view             | Fixed with `flex-wrap` and custom media query               |
| User session did not persist after login         | Correct Flask-Login configuration and secret key setup      |
| Deployment failed due to missing packages        | Added missing modules (e.g., `cloudinary`) in requirements  |
| Environment variables not loading on Render      | Used `os.getenv` properly and removed `dotenv` in production|
| Comment form not showing errors properly         | Updated WTForms and Jinja2 error logic                      |
  |


###  Known Bugs

- No unresolved bugs remain at the time of submission.
- All known issues identified during development and testing were resolved.
- Any minor usability concerns were addressed with appropriate validation, tooltips, or flash messages.