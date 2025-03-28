#   DishCraft 

 ![DishCraft Logo](/app/static/readme-screenshoots/amiresponsiv.png)


## 📋 Table of Contents

- [About](#about)
  - [Project Overview](#project-overview)
  - [Site Purpose](#site-purpose)
  - [Target Audience](#target-audience)

- [User Experience UX](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design Choices](#design-choices)
    - [Colour Palette](#colour-palette)
    - [Typography](#typography)
    - [Icons](#icons)
    - [Animations and Interactivity](#animations)
    - [Responsive Design](#responsive-design)
  - [Wireframes](#wireframes)

- [Features](#features)
  - [Homepage and Navigation](#homepage-and-navigation)
  - [Authentication LoginSignup](#authentication-loginsignup)
  - [Recipe CRUD Create Read Update Delete](#recipe-crud-create-read-update-delete)
  - [Image Upload via Cloudinary](#image-upload-via-cloudinary)
  - [Category Filtering and Search](#category-filtering-and-search)
  - [LikeFavorite Recipes](#likefavorite-recipes)
  - [Comments](#comments)
  - [Admin Dashboard](#admin-dashboard)
  - [User Profiles](#user-profiles)
  - [Contact Page](#contact-page)

- [Technologies Used](#technologies-used)
  - [Languages and Frameworks](#languages-and-frameworks)
  - [Libraries and Packages](#libraries-and-packages)
  - [Development Tools](#development-tools)

- [Database](#database)
  - [Schema Diagram](#schema-diagram)
  - [Relationships](#relationships)

- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validation](#validation)
  - [Responsiveness Testing](#responsiveness-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Accessibility](#accessibility)
  - [Bugs and Fixes](#bugs-and-fixes)

- [Deployment](#deployment)
  - [Deployment to Render](#deployment-to-render)
  - [Cloning and Running Locally](#cloning-and-running-locally)
  - [Environment Variables](#environment-variables)

  - [Future Improvements](#future-improvements)

- [Credits](#credits)
  - [Resources and Tutorials](#resources-and-tutorials)
  - [Inspiration and Acknowledgements](#inspiration-and-acknowledgements)





##  About

**Project Name**: 🍽️ DishCraft  
**Developer**: [Danut Grigore]  
**Type**: Milestone 3 - Full Stack Web Development (Code Institute)
 

###  Project Overview

**DishCraft** is a full-stack, data-centric web application built using Flask and PostgreSQL that empowers users to discover, share, and manage recipes from around the world. The application features a clean, responsive interface designed with Bootstrap, and provides an intuitive user experience across all devices.

Users can register, log in, and interact with a community of food lovers by posting, liking, and commenting on recipes. Admins have additional privileges to manage users, content, and comments through a dedicated dashboard. Whether you're a passionate home cook or just looking for new culinary inspiration, **DishCraft** makes it easy to explore and contribute to a growing collection of diverse, delicious dishes.


###  Site Purpose

The core purpose of DishCraft is to create an open and welcoming space for food lovers to share their creations, discover new ideas, and connect with others through cooking. Unlike generic recipe sites, DishCraft emphasizes user interaction — turning recipe-sharing into a dynamic, community-driven experience.

Users can:
- 👨‍🍳 Create, edit, and manage their personal recipes
- ❤️ Like and comment on other users’ dishes
- 🌍 Browse recipes by category, difficulty, or cuisine
- 🛠️ Access moderation tools (admin only) to keep content curated and respectful


###  Target Audience

DishCraft is built for:
-  **Home cooks** looking to organize and share their favorite recipes
-  **Food enthusiasts and hobby chefs** interested in feedback and inspiration
-  **Beginners** who want a clean and simple way to browse easy-to-follow recipes
-  **Community-focused users** who enjoy social engagement through food

Whether you're a seasoned chef or a kitchen novice, DishCraft provides the tools and platform to share your passion for food with others.

##  User Experience (UX)

###  User Stories

As a **new visitor**, I want to:
-  Easily browse available recipes without needing to register
-  Filter recipes by cuisine, difficulty, or category
-  View recipe details including ingredients, steps, and cook time

As a **registered user**, I want to:
- 🧾 Create and share my own recipes with the community
- ✏️ Edit or delete my submitted recipes at any time
- ❤️ Like/favorite recipes I enjoy and want to revisit
- 💬 Comment on others’ recipes to share feedback or ask questions
- 👤 View my profile with a list of my own and liked recipes

As an **admin**, I want to:
-  Moderate recipe submissions and comments
-  Delete inappropriate content
-  Manage user roles and promote/demote users

As a **mobile user**, I want to:
-  Access the full app functionality on my phone
-  Navigate easily with a responsive design and mobile-friendly layout

---

###  Design Choices

####  Colour Palette

| Colour Use        | Hex Code | Preview     |
|-------------------|----------|-------------|
| Primary Accent    | #FF7F50  | Coral       |
| Background        | #FFFFF2  | Soft Peach  |
| Card Background   | #FFFFFF  | White       |
| Text (Primary)    | #333333  | Charcoal    |
| Icon Accent       | #F4B400  | Amber       |
| Button Hover      | #FF5722  | Deep Orange |

These colours were selected to evoke **warmth**, **freshness**, and a **clean, appetizing** look appropriate for a recipe-sharing platform. They also provide high contrast and meet accessibility standards for readability.

<details>
<summary>📸 Color Palette in Use (Click to expand)</summary>

![Colour Scheme](/app/static/readme-screenshoots/colour-pallete.png)

</details>


####  Typography

DishCraft uses a modern serif/sans-serif pairing to balance elegance with readability:

- **Headings (h1–h4)**: `Playfair Display`, serif  
  - Stylish and expressive, giving the site a distinctive visual tone  
- **Body Text**: `Inter`, sans-serif  
  - Clean, modern, and highly legible for paragraphs and UI elements  
- **Fallback Fonts**: `serif` and `sans-serif` are defined for cross-browser compatibility  
- **Font Weights**:  
  - Headings: Bold (700)  
  - Body: Regular (400)  

This typography combination ensures strong visual hierarchy, clarity, and an appealing user experience across all devices.


<details>
<summary>📸 Font Example in UI (Click to expand)</summary>

![Typography Example](/app/static/readme-screenshoots/fonts-screenshoot.png)

</details>


####  Icons

DishCraft uses icons thoughtfully to enhance usability and provide visual cues without overwhelming the interface.

- **Source**: [Font Awesome](https://fontawesome.com/)  
- **Usage Areas**:
  - Navigation bar (e.g., profile, logout)
  - Category and recipe tags (e.g., 🍽️ Breakfast, 🧁 Dessert)
  - Buttons and CTAs (e.g., comment, like, view recipe)
  - Admin dashboard actions (e.g., edit, delete, user control)

Icons were chosen to:
- Improve scanability and recognition of key functions
- Provide context (e.g., a heart icon for likes, pencil for edit)
- Maintain a friendly, visual feel in both desktop and mobile views

<details>
<summary>📸 Example of Icon Usage (Click to expand)</summary>

![Icon Usage](/app/static/readme-screenshoots/icons-screenshoot.png)

</details>


####  Animations

DishCraft uses subtle animations and transitions to enhance interactivity and user engagement, without distracting from the content.

- **AOS (Animate on Scroll)**  
  - Used to fade in recipe cards and homepage elements as they enter the viewport  
  - Creates a smooth, polished browsing experience  

- **Hover Effects**  
  - Buttons and interactive icons scale slightly and change color on hover  
  - Enhances clarity of clickable areas  

- **Modals**  
  - Modal pop-ups are used for actions like deleting recipes or confirming sensitive operations  
  - Styled using Bootstrap and enhanced with soft transitions for accessibility and clarity  

- **Scroll Behavior**  
  - `scroll-behavior: smooth` applied site-wide for fluid navigation  

<details>
<summary>📸 Modal Animation Example (Click to expand)</summary>

![Delete Confirmation Modal](/app/static/readme-screenshoots/modal-screenshoot.png)

</details>

These animations provide instant visual feedback and elevate the perceived responsiveness of the application across both desktop and mobile devices.


####  Responsive Design

DishCraft was designed with a mobile-first approach and is fully responsive across all modern devices and screen sizes.

Key responsiveness features include:

- **Media Queries**: Custom breakpoints at `768px` and `576px` adapt layouts for tablets and mobile devices.
- **Fluid Layouts**: Content containers, buttons, cards, and forms adjust spacing and alignment dynamically.
- **Mobile Navigation**: The navbar collapses into a toggle menu on smaller screens for easier access.
- **Responsive Hero & Cards**: Homepage hero sections, category cards, and recipe previews all scale and rearrange for optimal usability.
- **Form Adaptability**: Search filters, form fields, and buttons adjust to full-width layouts on small screens.
- **Newsletter Section**: Stacks and centers all elements while retaining visual balance on mobile.
- **Touch-Friendly Elements**: Buttons and interactive areas include generous padding and clear hover/focus states.

<details>
<summary>📸 Responsive Design Example (Click to expand)</summary>

![Responsive View](/app/static/readme-screenshoots/responsive-design-screenshoot.png)

</details>

These adaptations ensure a smooth and intuitive experience for both mobile and desktop users, making DishCraft a pleasure to use anywhere.

---

## Wireframes



To guide the layout and design of DishCraft, a series of wireframes were created for key pages. These wireframes helped establish user flow, component hierarchy, and responsive structure before development began.

Each screen was designed with mobile responsiveness and intuitive interaction in mind.


<details>
<summary>📄 Homepage Wireframe (Click to expand)</summary>

![Homepage Wireframe](/app/static/readme-screenshoots/wireframes/homepage.png)

</details>

<details>
<summary>📄 Explore Recipes Wireframe (Click to expand)</summary>

![Explore Recipes Wireframe](/app/static/readme-screenshoots/wireframes/explore.png)

</details>

<details>
<summary>📄 Login & Register Wireframe (Click to expand)</summary>

![Login Register Wireframe](/app/static/readme-screenshoots/wireframes/login-register.png)

</details>

<details>
<summary>📄 Profile Page Wireframe (Click to expand)</summary>

![Profile Wireframe](/app/static/readme-screenshoots/wireframes/profile.png)

</details>

<details>
<summary>📄 Admin Dashboard Wireframe (Click to expand)</summary>

![Admin Wireframe](/app/static/readme-screenshoots/wireframes/admin.png)

</details>

<details>
<summary>📄 Contact Page Wireframe (Click to expand)</summary>

![Contact Page Wireframe](/app/static/readme-screenshoots/wireframes/contact.png)

</details>

Wireframes were iterated based on usability testing and layout refinements during development.

---

## Features

### Homepage and Navigation

The DishCraft homepage serves as the entry point to the application and is designed to immediately engage users with vibrant visuals, calls to action, and recipe highlights.

#### Homepage Highlights:
- **Hero Section** with engaging message and clear CTAs:
  - “Browse Recipes” for immediate exploration
  - “Add Recipe” for returning users
- **Recipe of the Month**: A featured card with a highlighted dish
- **Featured Recipes**: Preview cards of the most recent or top-rated dishes
- **Category Explorer**: Grid layout allowing users to filter by category (e.g., Breakfast, Vegan, Dessert)
- **User Testimonials** section (optional) for community feedback
- **Newsletter Signup** with email input and subscribe button

#### Navigation Bar:
The responsive navigation bar adjusts based on user authentication and screen size.

- **Unauthenticated Users**:
  - `Home`, `Explore Recipes`, `Login`, `Register`

- **Authenticated Users**:
  - `Home`, `Explore Recipes`, `Add Recipe`, `Profile`, `Logout`

- **Admin Users**:
  - All of the above, plus access to `Admin Dashboard`

The navbar is sticky, lightweight, and mobile-friendly. It collapses into a toggle menu on smaller screens and uses subtle hover effects and iconography for clarity.

<details>
<summary>📸 Homepage & Navbar Example (Click to expand)</summary>

![Homepage UI](/app/static/readme-screenshoots/home-page.png)

</details>


### Authentication LoginSignup

DishCraft features a secure and user-friendly authentication system built with Flask-Login and Flask-WTF.

#### Features:
- **User Registration**:
  - Accessible via the `Register` link in the navbar
  - Users provide a username, email, and password (with confirmation)
  - Form validation handles missing fields, password mismatch, and duplicate emails
  - On success, users are automatically logged in and redirected to the homepage

- **User Login**:
  - Secure login with email and password
  - Flask sessions maintain user authentication across pages
  - Users are redirected back to the last visited page or homepage after login

- **User Logout**:
  - Clears the session securely using `logout_user()`
  - Navbar updates to reflect logged-out state

#### Validation and Feedback:
- WTForms validation with error messages for all fields
- Flash messages inform users of success or error (e.g., “Invalid login”, “Welcome back!”)
- Form fields include accessibility features like `aria-labels` and `focus-visible` outlines

#### Security:
- Passwords are hashed before storage using Werkzeug
- Sessions are protected by secret keys set via environment variables
- Route access is restricted:
  - Only logged-in users can add/edit recipes
  - Only admins can access admin dashboard

<details>
<summary>📸 Authentication UI (Click to expand)</summary>

![Login Register UI](/app/static/readme-screenshoots/register.png)

</details>


### Recipe CRUD Create Read Update Delete

DishCraft allows authenticated users to fully manage their own recipes using CRUD operations — a core requirement for full-stack interactivity.

#### Create:
- Users can create a new recipe using a rich form interface
- Fields include:
  - Title, Image (Cloudinary upload), Cuisine, Category, Difficulty, Prep Time
  - Ingredients (multi-line), Instructions/Steps
- Recipes are saved to PostgreSQL via SQLAlchemy
- Validation is handled using Flask-WTF

#### Read:
- Recipes are displayed in card format on the homepage and explore page
- Each recipe can be opened to view full details:
  - Title, author, cuisine, difficulty, duration, ingredients, instructions
  - Comments, likes, and recipe badges

#### Update:
- Logged-in users can edit their own recipes from their profile or recipe page
- The form is pre-filled with current recipe data
- Changes are validated and saved back to the database

#### Delete:
- Only the recipe owner (or admin) can delete a recipe
- Deletion triggers a **confirmation modal** to prevent accidental loss
- The record is removed from the database, and a flash message confirms success

#### Permissions:
- All CRUD operations are protected by Flask-Login
- Admins can manage all recipes; regular users can only manage their own

<details>
<summary>📸 Recipe CRUD Interface (Click to expand)</summary>

![CRUD Example](/app/static/readme-screenshoots/add_recipe.png)

</details>
<details>
<summary>📸 Recipe CRUD Interface (Click to expand)</summary>

![CRUD Example](/app/static/readme-screenshoots/CRUD-screenshoot2.png)

</details>


### Image Upload via Cloudinary

DishCraft integrates **Cloudinary** to handle secure and scalable image hosting for recipe submissions.

#### How it Works:
- Users upload an image during recipe creation or editing
- Images are uploaded directly to a linked Cloudinary account via a secure POST request
- On success, the image URL is stored in the database and used throughout the app

#### Benefits:
- Offloads image storage from the backend server
- Automatically handles file compression, CDN delivery, and versioning
- Ensures fast image load times with responsive rendering

#### Upload Flow:
- Recipe form includes an image upload input
- Backend validates file type and integrates with Cloudinary’s API
- Image preview is displayed on the recipe detail page or card

#### Security:
- Image uploads are signed using environment-protected credentials
- Only authenticated users can upload images

<details>
<summary>📸 Image Upload Integration (Click to expand)</summary>

![Cloudinary Upload](/app/static/readme-screenshoots/cloudinary-screenshoot.png)

</details>


### Category Filtering and Search

DishCraft allows users to efficiently search and filter recipes to discover dishes that suit their preferences, dietary needs, or available ingredients.

#### Search & Filter Features:
- **Search Bar**:
  - Users can search recipes by keyword (e.g., “pasta”, “vegan”, “chicken”)
  - Partial match support across titles, ingredients, and cuisine type
  - Case-insensitive

- **Filter by Category**:
  - Categories include: Breakfast, Lunch, Dinner, Dessert, Snack, Vegan, Vegetarian
  - Category filters are displayed in a grid with icons on the homepage
  - Clicking a category dynamically shows related recipes

- **Filter by Difficulty**:
  - Options: Easy, Medium, Hard
  - Helps users find recipes based on their skill level

- **Sort Options**:
  - Newest first
  - Most liked 
  - Alphabetical 

#### Responsive & Accessible:
- Dropdown filters collapse gracefully on mobile
- All filter controls are keyboard accessible
- Form uses semantic `<label>`s and `aria` attributes for usability

#### Backend Integration:
- Flask routes query the PostgreSQL database with dynamic filters
- Queries are constructed securely with SQLAlchemy

<details>
<summary>📸 Filtering & Search UI (Click to expand)</summary>

![Search and Filters](/app/static/readme-screenshoots/filter-screenshoot.png)

</details>


### LikeFavorite Recipes

DishCraft enables users to express appreciation for recipes by "liking" them — effectively adding them to their list of favorite dishes.

#### How it Works:
- Every recipe includes a **like (heart)** button
- Logged-in users can:
  - ❤️ Like a recipe (adds to their profile’s favorite list)
  - 💔 Unlike a recipe to remove it from favorites
- Likes are updated in real-time via form submission

#### Visual Feedback:
- Filled heart icon indicates a recipe is liked
- Count of total likes is displayed next to the icon
- Button uses subtle animation or color feedback on interaction

#### Data Model:
- Many-to-many relationship between users and recipes
- Likes are stored in a separate table (`likes`) with user and recipe foreign keys
- Prevents duplicate likes per user

#### Profile Integration:
- A user's profile includes a section displaying their liked recipes
- Encourages users to save favorites for later access

#### Permissions:
- Only authenticated users can like/unlike recipes
- Unauthenticated users are prompted to log in

<details>
<summary>📸 Like Feature UI (Click to expand)</summary>

![Like Recipes](/app/static/readme-screenshoots/like-screenshoot.png)

</details>


### Comments

DishCraft allows authenticated users to leave comments on any recipe, encouraging discussion, feedback, and community interaction.

#### Core Features:
- Users can:
  - 💬 Add a new comment to any recipe
  - 🗑️ Delete their own comments
- Comments display:
  - Author name
  - Timestamp 
  - Content in clean readable format

#### Form Behavior:
- Comment form is positioned beneath each recipe detail page
- Includes textarea input, submit button, and flash message feedback
- Validation ensures empty comments are not submitted

#### Moderation (Admin Role):
- Admin users can:
  - View and delete any comment for moderation
  - Access comments through the admin dashboard

#### Backend Handling:
- Comments are stored in a relational table linked to both:
  - The **user** who posted it
  - The **recipe** it belongs to
- Flask and SQLAlchemy handle form submission, validation, and storage

#### UX Considerations:
- New comments appear in real-time upon submission
- Each comment has a minimal, clean layout with user-friendly spacing

<details>
<summary>📸 Comments UI (Click to expand)</summary>

![Recipe Comments](/app/static/readme-screenshoots/comment-screenshoot.png)

</details>


### Admin Dashboard

DishCraft includes a powerful admin interface that allows site administrators to manage users, recipes, comments, and maintain the platform’s content quality.

#### Access Control:
- Only users with the `admin` role can access the dashboard
- Access is protected via Flask-Login and checked on every admin route

#### Dashboard Features:
- 📊 Overview cards for:
  - Total users
  - Total recipes
  - Total comments
  - Total likes 
- 🧑‍💼 User Management:
  - View all registered users
  - Promote or demote user roles
  - Delete inactive or inappropriate users
- 📋 Recipe Management:
  - View all submitted recipes
  - Edit or delete any recipe
- 💬 Comment Moderation:
  - View all comments site-wide
  - Delete inappropriate comments

#### Design:
- Dashboard uses responsive tables and styled cards for data visibility
- Tooltips and icons clarify available actions
- Sortable or searchable tables improve admin workflow (optional enhancement)

#### Backend Logic:
- Role checking with conditionals (e.g., `current_user.is_admin`)
- All admin views query models using SQLAlchemy with pagination if needed

<details>
<summary>📸 Admin Dashboard UI (Click to expand)</summary>

![Admin Dashboard](/app/static/readme-screenshoots/admin-screenshoot.png)

</details>


### User Profiles

Each registered user on DishCraft has a personalized profile page that displays their contributions and saved favorites.

#### Profile Page Features:
- 👤 Display username and profile avatar 
- 🧾 List of user-submitted recipes, each with:
  - Title, category, likes, and edit/delete options
- ❤️ Liked Recipes:
  - Section showing recipes the user has favorited
  - Allows quick access to saved dishes

#### Functionality:
- Logged-in users can access their profile from the navbar
- Profile route is protected — users can only access their own page
- Recipes listed have action buttons:
  - `Edit` and `Delete` for the user's own content
- Uses pagination or scroll-based loading if the user has many recipes

#### Backend Integration:
- Profile queries recipes and likes based on `current_user.id`
- Admins may access all profiles for moderation if necessary

#### UX Touches:
- Profile layout adapts responsively for mobile
- Clean grid or card layout for recipes and favorites
- Flash messages confirm successful updates or deletions

<details>
<summary>📸 Profile Page UI (Click to expand)</summary>

![User Profile](/app/static/readme-screenshoots/profile.html.png)

</details>

### Contact Page

The Contact page allows users to get in touch with the DishCraft team for feedback, inquiries, or support.

- Users can fill out a form with their **name**, **email**, and **message**.
- Form includes:
  - Client-side input validation
  - Clear confirmation on successful submission
- Styled consistently with the rest of the application
- Protected with CSRF (Flask-WTF) for security

<details>
<summary>📸 Contact Page Screenshot (Click to expand)</summary>

![Contact Page](/app/static/readme-screenshoots/contact-page.png)

</details>


---

## Technologies Used

### Languages and Frameworks

- **HTML5** – Semantic markup for structure and accessibility
- **CSS3** – Custom styling, layout, and responsive design with media queries
- **JavaScript** – Frontend interactivity and dynamic elements
- **Python 3** – Backend logic and routing using Flask
- **Flask** – Lightweight Python web framework powering the app's backend
- **Jinja2** – Template engine used to render dynamic content from Flask

### Libraries and Packages

- **Flask-WTF** – Form rendering and CSRF protection
- **Flask-Login** – User session management and authentication
- **Flask-SQLAlchemy** – ORM for handling PostgreSQL models and queries
- **Flask-Migrate** – Handling database migrations with Alembic.
- **WTForms** – Form validation and field management
- **Cloudinary** – Image upload and hosting via its Python SDK
- **AOS (Animate on Scroll)** – For smooth fade and slide animations
- **Bootstrap 5** – Frontend framework for responsive grid system and components
- **Font Awesome** – Icon library used for visual cues
- **dotenv** – Secure environment variable management
- **Flask-Bcrypt** – Password hashing.

### Development Tools

- **VS Code** – Main code editor with extensions for Python, linting, and Git
- **Git & GitHub** – Version control and source code hosting
- **Render** – Platform-as-a-Service (PaaS) used to deploy the live site
- **Render** – Deployment platform for live hosting, Hosted PostgreSQL database instance
- **Chrome DevTools** – For responsive testing and debugging
- **Lighthouse** – For performance, accessibility, and SEO checks
- **Postman** – For testing API endpoints and form submissions
- **PostgreSQL** – Production database (via Render).
- **SQLite** – Local development database.
- **TinyPNG** – Used to compress and optimize image assets before uploading to Cloudinary
<
## Database

### Schema Diagram

The database schema is designed to support users, their recipes, categories, comments, and likes.

<details>
<summary>📸 Click to view schema diagram</summary>

![Database Schema](/app/static/readme-screenshoots/database-schema-diagram.png)

</details>

---

### Table Overview

- **User**
  - `id` (PK)
  - `username`
  - `email`
  - `password_hash`
  - `is_admin`
  - `created_at`

- **Recipe**
  - `id` (PK)
  - `title`, `description`, `ingredients`, `steps`
  - `cuisine`, `prep_time`, `difficulty`, `image_url`, `created_at`
  - `user_id` (FK → User)

- **Category**
  - `id` (PK)
  - `name` (unique)

- **RecipeCategory** (association table)
  - `recipe_id` (FK → Recipe)
  - `category_id` (FK → Category)

- **Comment**
  - `id` (PK)
  - `content`, `created_at`
  - `user_id` (FK → User)
  - `recipe_id` (FK → Recipe)

- **Like**
  - `id` (PK)
  - `user_id` (FK → User)
  - `recipe_id` (FK → Recipe)


### Relationships Summary

- A **User** can have many **Recipes**, **Comments**, and **Likes**
- A **Recipe** belongs to one **User**; has many **Categories**, **Comments**, and **Likes**
- A **Category** can belong to many **Recipes** (Many-to-Many)
- A **Comment** belongs to one **User** and one **Recipe**
- A **Like** represents a single user liking a recipe (Many-to-Many via Likes table)

---

## Testing

### Manual Testing

Manual testing was performed across the site's major features to ensure expected behavior:

| Feature                             | Tested On               | Expected Result                        | Outcome     |
|-------------------------------------|--------------------------|-----------------------------------------|-------------|
| User Registration                   | Desktop / Mobile         | New user created, redirected to home    | ✅ Pass      |
| Login / Logout                      | Desktop / Mobile         | Successful login and logout flow        | ✅ Pass      |
| Create Recipe                       | Desktop / Mobile         | Recipe added and appears in listing     | ✅ Pass      |
| Edit / Delete Recipe                | Desktop / Mobile         | Updates saved / recipe deleted          | ✅ Pass      |
| Comment on Recipe                   | Desktop / Mobile         | Comment added and visible               | ✅ Pass      |
| Like / Unlike Recipe                | Desktop / Mobile         | Like toggles and updates count          | ✅ Pass      |
| Admin Dashboard (delete user/comment) | Desktop                | Admin action successful, database updated | ✅ Pass   |

#### UI & Navigation Manual Testing

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


> Additional edge case testing was conducted (e.g., empty form fields, invalid image URL) and handled via WTForms validation and Flask flash messages.

### Validation

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

### Responsiveness Testing

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


### Browser Compatibility

Tested the application in the following browsers:

| Browser         | Version Tested | Result   |
|----------------|----------------|----------|
| Chrome         | 120+           | ✅ Pass   |
| Firefox        | 118+           | ✅ Pass   |
| Edge           | 116+           | ✅ Pass   |
| Safari (iOS)   | 15+            | ✅ Pass   |
| Brave          | Latest         | ✅ Pass   |

### Accessibility

DishCraft was built with accessibility as a core consideration, ensuring the platform is inclusive and user-friendly for all visitors, including those using assistive technologies.

Key accessibility measures implemented:

- **Semantic HTML Structure**  
  All pages utilize semantic HTML5 elements such as `<main>`, `<nav>`, `<header>`, and `<section>` to enhance document structure and assistive tool readability.

- **Keyboard Navigability**  
  All interactive elements (e.g., navigation links, buttons, forms) are accessible via keyboard (Tab/Shift+Tab and Enter) with visible focus states for clarity.

- **Color Contrast Compliance**  
  The color scheme was selected with accessibility in mind, maintaining strong foreground/background contrast ratios to meet [WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/) standards.

- **Descriptive Alt Text**  
  All images include relevant `alt` attributes to provide visual context for screen reader users.

- **Accessible Forms**  
  All form fields include associated `<label>` tags, and use `aria-` attributes where needed for improved screen reader support.

- **Modal Accessibility**  
  Confirmation modals (e.g., delete recipe) are built using Bootstrap and enhanced with ARIA roles to ensure focus trapping and proper keyboard control.

- **Responsive Typography**  
  Font sizes and spacing are responsive and legible across all screen sizes without the need for zoom.

<details>
<summary>🌐 Lighthouse Accessibility Audit (Click to expand)</summary>

Accessibility audits were performed using Chrome’s Lighthouse tool to validate best practices across different views of the application.

**Add_recipe page Accessibility Score**  
![Lighthouse Audit](/app/static/readme-screenshoots/accesibility-addrecipe.png)

**Explore_Recipe Page Accessibility Score**  
![Lighthouse Audit](/app/static/readme-screenshoots/accesibility-browse_recipe.png)

**Profile Page Accessibility Score**  
![Lighthouse Audit](/app/static/readme-screenshoots/accesibility=profile.png)

</details>


### Bugs and Fixes

| Bug Description                           | Resolution                                  |
|-------------------------------------------|----------------------------------------------|
| Cloudinary images not displaying after deploy    | Corrected Cloudinary ENV variables and updated config usage |
| Category seeding caused SyntaxError in Render shell | Used line-by-line safe seeding via Flask shell             |
| Recipe cards overflow on mobile view             | Fixed with `flex-wrap` and custom media query               |
| User session did not persist after login         | Correct Flask-Login configuration and secret key setup      |
| Deployment failed due to missing packages        | Added missing modules (e.g., `cloudinary`) in requirements  |
| Environment variables not loading on Render      | Used `os.getenv` properly and removed `dotenv` in production|
| Comment form not showing errors properly         | Updated WTForms and Jinja2 error logic                      |


## Deployment

The DishCraft application is deployed on [Render](https://render.com/) and is accessible publicly via the following link:  
👉 [Live Site](https://project-online-cookbook.onrender.com)

### Deployment to Render

Steps to deploy the application on Render:

1. **Push your project to GitHub** with all required files and folders.
2. **Create a new Web Service** in Render:
   - Connect your GitHub repo
   - Select Python environment
3. **Add environment variables**:
   - `SECRET_KEY`
   - `DATABASE_URL` (PostgreSQL)
   - `CLOUDINARY_URL`
4. Set the **Build Command**:  
   ```bash
   pip install -r requirements.txt

---

## 🚀 Future Improvements

While DishCraft already provides a solid foundation for sharing and discovering recipes, there are several enhancements planned for future development:

- **Advanced Search & Filters**  
  Implement multi-tag filters, dietary filters (e.g., gluten-free, keto), and better ingredient-based search.

- **Recipe Rating System**  
  Allow users to rate recipes with a 1–5 star system to help surface the best content.

- **Recipe Collections**  
  Let users save and organize recipes into custom collections (e.g., “Meal Prep,” “Holiday Dishes”).

- **Private Recipes / Draft Mode**  
  Enable users to save recipes privately or work on drafts before publishing them.

- **Newsletter Integration**  
  Store emails and build functionality to send periodic recipe newsletters.

- **Accessibility Enhancements**  
  Improve color contrast and keyboard navigation to meet WCAG AA+ standards.

- **Dark Mode**  
  Provide a toggle to switch between light and dark themes for better user preference.

These improvements aim to elevate the user experience, expand engagement, and make DishCraft more dynamic and user-centric over time.

---

## Credits

### Resources & Tutorials

- This project was developed as part of the [Code Institute Full Stack Web Development Diploma](https://codeinstitute.net/) — Milestone Project 3.
- Code Institute’s **Flask Blog walkthrough** served as the foundation for structuring the app and understanding key concepts such as routes, blueprints, and authentication.
- General guidance and solutions were inspired by community Q&As on **[Stack Overflow](https://stackoverflow.com/)**.
- Additional tips and problem-solving strategies were learned through various YouTube tutorials, including:
  - [Corey Schafer – Flask Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
  - [Pretty Printed – Flask Series](https://www.youtube.com/playlist?list=PLXmMXHVSvS-DtYl4ZTkZzYpblh3yI2W1F)

---

### Images & Icons

- **Recipe images** and background visuals were sourced from:
  - [Unsplash](https://unsplash.com/)
  - [FoodieBook](https://www.foodiebook.io/) (for example recipes)
- **Icons** throughout the site are provided by [Font Awesome](https://fontawesome.com/).
- **Cloudinary** is used to handle image uploads from users.

### Inspiration & Acknowledgements

- All design decisions, layout structure, and interactive elements were custom-designed for this project by the developer.
- The concept of DishCraft was created to bring together community-driven cooking and elegant, user-friendly web application design.
- Huge thanks to my **Code Institute tutor** for their invaluable feedback and support throughout the project, to my **mentor** for their guidance and to the **Code Institute Slack community** for their helpful discussions, resources, and peer reviews during development.

---

