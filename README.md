#   DishCraft 👉 [Live Site](https://project-online-cookbook.onrender.com)

---

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

- [Code Structure and Quality](#code-structure-and-quality)

- [Database](#database)
  - [Schema Diagram](#schema-diagram)
  - [Relationships](#relationships)

- [Testing](#testing)
- [Security](#security-considerations)

- [Deployment](#deployment)
  - [Deployment to Render](#deployment-steps-to-render)
  - [Cloning and Running Locally](#cloning-and-running-locally)

- [Future Improvements](#future-improvements)

- [Credits](#credits)
  - [Resources and Tutorials](#resources-and-tutorials)
  - [Inspiration and Acknowledgements](#inspiration-and-acknowledgements)





##  About

**Project Name**: 🍽️ DishCraft  
**Developer**: Danut Grigore  
**Type**: Milestone 3 – Full Stack Web Development (Code Institute)

---

###  Project Overview

**DishCraft** is a full-stack, data-centric web application that allows users to create, discover, and manage recipes in a socially engaging environment. Built using **Flask**, **PostgreSQL**, and **Bootstrap**, the platform delivers a responsive and intuitive experience for users on any device.

Users can register, create and manage their own recipes, like and comment on other posts, and explore recipes filtered by category, cuisine, or difficulty level. Admins have elevated privileges to manage user content and keep the platform safe and respectful.

DishCraft aims to be more than a recipe site — it's a space where cooking becomes collaborative, fun, and accessible.

---

###  Site Purpose

DishCraft was created to solve a common gap in recipe-sharing platforms: Unlike traditional recipe websites that are often static or ad-heavy, DishCraft is designed to be **interactive, personal, and community-driven** — allowing users to contribute their own content, interact with others, and curate their favorite meals in one place.

This platform empowers users by giving them control over their culinary content and encourages interaction with a wider cooking community.

#### The app provides:

- 🧾 **Personal recipe management** – Add, edit, and organize your own creations  
- ❤️ **Social interaction** – Like and comment on recipes from other users  
- 🔍 **Smart discovery tools** – Search and filter recipes by category, difficulty, or cuisine  
- 🛠️ **Content moderation tools** – Admins maintain a safe, curated environment  

By focusing on simplicity, clarity, and community, DishCraft makes recipe sharing a rewarding, user-led experience — for everyone from beginners to passionate food lovers.

---

###  Target Audience

DishCraft is designed for:

-  **Home cooks** who want to organize and share their personal recipes
-  **Hobby chefs** seeking feedback and inspiration from others
-  **Beginners** who need an easy-to-use platform with accessible content
-  **Social users** who enjoy liking, commenting, and discovering new dishes from peers

Whether you're saving your grandmother’s stew, sharing a TikTok-inspired dish, or browsing for quick weekday ideas, **DishCraft is your personal, social cooking companion.**

##  User Experience (UX)

###  User Stories

As a **new visitor**, I want to:
-  Easily browse available recipes without needing to register
-  Filter recipes by cuisine, difficulty, or category
-  View recipe details including ingredients, steps, and cook time

As a **registered user**, I want to:
-  Create and share my own recipes with the community
-  Edit or delete my submitted recipes at any time
-  Like/favorite recipes I enjoy and want to revisit
-  Comment on others’ recipes to share feedback or ask questions
-  View my profile with a list of my own and liked recipes

As an **admin**, I want to:
-  Moderate recipe submissions and comments
-  Delete inappropriate content
-  Manage user roles and promote/demote users

As a **mobile user**, I want to:
-  Access the full app functionality on my phone
-  Navigate easily with a responsive design and mobile-friendly layout


 *All user stories were manually tested. See [ User Story Testing](TESTING.md/#user-story-testing) for full test results.*

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
Additional colours were used along while building the project for vissualy improments.

<details>
<summary>📸 Color Palette in Use (Click to expand)</summary>

![Colour Scheme](/app/static/readme-screenshoots/colour-pallete.png)

</details>


####  Typography

DishCraft uses a modern serif/sans-serif pairing to balance elegance with readability:

- **Headings (h1–h4)**: `Playfair Display`, serif  
  - Stylish and expressive, giving the site a distinctive visual tone  
- **Body Text**: `Playfair`, `Inter` 
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

##  Wireframes

During the planning phase, I created initial wireframes for key pages of **DishCraft**, including:

- Home Page  
- Explore Recipes Page  
- Contact Page  
- Login Page  

These early sketches helped establish the layout, navigation structure, and user flow.  
As development progressed, I refined and expanded the UI while staying true to the core design concepts.  
The final design improves usability, visual appeal, and responsiveness beyond the original wireframes.

---

### 🏠 Home Page

<details>
  <summary>Click to view wireframe</summary>

  ![Homepage Wireframe](/app/static/readme-screenshoots/wireframes/homepage-wireframe.png)

</details>

---

### 🔍 Explore Recipes Page

<details>
  <summary>Click to view wireframe</summary>

  ![Explore Recipes Wireframe](/app/static/readme-screenshoots/wireframes/Explorepage-wireframe.png)

</details>

---

### ✉️ Contact Page

<details>
  <summary>Click to view wireframe</summary>

  ![Contact Wireframe](/app/static/readme-screenshoots/wireframes/contact-wireframe.png)

</details>

---

### 🔐 Login Page

<details>
  <summary>Click to view wireframe</summary>

  ![Login Wireframe](/app/static/readme-screenshoots/wireframes/Login-wireframe.png)

</details>

---

> ✅ These wireframes guided the development process, while allowing room for creativity and UX improvement as the project matured.



---

## Features

#### Homepage and Navigation:
- **Hero Section** with engaging message and clear CTAs:
  - “Browse Recipes” for immediate exploration
  - “Add Recipe” for returning users
- **Recipe of the Month**: A featured card with a highlighted dish
- **Featured Recipes**: Preview cards of the most recent or top-rated dishes
- **Category Explorer**: Grid layout allowing users to filter by category (e.g., Breakfast, Vegan, Dessert)
- **Testimonials Section**: Includes a **responsive carousel** that cycles through real user feedback dynamically.
- **Newsletter Signup** with email input and subscribe button

#### Navigation Bar:
The responsive **sticky navigation bar** stays visible at the top of the screen as the user scrolls, ensuring constant access to key navigation links.

- Includes a **search bar** to allow users to search recipes from anywhere on the site
- Navbar adjusts based on user authentication and screen size:
  - **Unauthenticated Users**: `Home`, `Explore Recipes`, `Login`, `Register`
  - **Authenticated Users**: `Home`, `Explore Recipes`, `Add Recipe`, `Profile`, `Contact`, `Logout`
  - **Admin Users**: All of the above, plus access to `Admin Dashboard`

<details>
<summary>📸 Search Bar from Navbar (Click to expand)</summary>

![Search Field UI](/app/static/readme-screenshoots/navbar-screenshoot.png)

</details>

The navbar is sticky, lightweight, and mobile-friendly. It collapses into a toggle menu on smaller screens and uses subtle hover effects and iconography for clarity.

<details>
<summary>📸 Homepage & Navbar Example (Click to expand)</summary>

![Homepage UI](/app/static/readme-screenshoots/homepage-screenshoot.png)

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
<summary>📸 Log In UI (Click to expand)</summary>

![Login UI](/app/static/readme-screenshoots/login-screenshoot.png)

</details>

<details>
<summary>📸 Register UI (Click to expand)</summary>

![Register UI](/app/static/readme-screenshoots/register-screenshoot.png)

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

![CRUD Example](/app/static/readme-screenshoots/add-recipe-screensoot.png)

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

![User Profile](/app/static/readme-screenshoots/profile-screenshoot%20(1).png)

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

![Contact Page](/app/static/readme-screenshoots/contact-screenshoot.png)

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

##  Code Structure and Quality

- All code follows the **PEP8** style guide and has been validated using `flake8`.
- Files and folders are named using lowercase and underscore conventions for cross-platform compatibility.
- Project is modular, with clearly separated folders for:
  - `routes/` – Flask routes grouped by functionality
  - `templates/` – Jinja2 HTML templates
  - `static/` – CSS, JS, and assets (organized into folders)
  - `models.py` – Database models
- Custom code is documented with **in-line comments** explaining logic where appropriate.
- Codebase uses consistent naming, indentation, and function organization to support maintainability.



## Database

### Schema Diagram

The database schema is designed to support users, their recipes, categories, comments, and likes.

<details>
<summary>📸 Click to view schema diagram</summary>

![Database Schema](/app/static/readme-screenshoots/database-schema-diagram.png)

</details>

### 🔍 Data Schema Explanation

The DishCraft database schema is designed around a **relational model** using **PostgreSQL** and SQLAlchemy ORM. It supports core functionality such as user management, recipe CRUD operations, user interactions (likes, comments), and administrative oversight.

#### 🔗 Key Entities and Relationships:

- **User**  
  - Central to the schema. Each user can own recipes, write comments, and like recipes.  
  - The `is_admin` boolean field allows role-based access control to moderate site content.

- **Recipe**  
  - Represents a single cooking recipe with fields such as title, image, category, cuisine, ingredients, difficulty, prep time, and instructions.  
  - Each recipe is owned by a user (via `user_id` foreign key) and can be liked or commented on by other users.

- **Category**  
  - Recipes can belong to one or multiple categories (e.g., “Vegan”, “Dessert”).  
  - A many-to-many relationship is implemented using the `RecipeCategory` association table, providing scalability for recipe filtering and search.

- **RecipeCategory (Join Table)**  
  - Links recipes and categories in a normalized, efficient structure.  
  - Prevents data duplication and supports multiple category filters per recipe.

- **Comment**  
  - Linked to both the recipe and the authoring user.  
  - This relationship ensures that only logged-in users can comment and supports admin moderation.  
  - Includes timestamp and content for discussion and feedback.

- **Like**  
  - Many-to-many relationship between users and recipes.  
  - Implemented as a standalone table with composite keys (`user_id`, `recipe_id`) to prevent duplicate likes.

#### 📐 Normalization and Integrity:

- The schema is **fully normalized**, reducing data redundancy and improving scalability.  
- All foreign key relationships enforce **referential integrity** and support **cascade delete** where appropriate.  
- Indexed fields (like `created_at`, `title`, and `user_id`) help optimize queries for filtering, sorting, and searching.

#### 🧩 Schema Support for Key Features:

| Feature                       | Schema Elements Involved                  |
|------------------------------|--------------------------------------------|
| User authentication          | `User` model + `is_admin` flag            |
| Recipe CRUD                  | `Recipe`, `User`, `Category`              |
| Likes/favorites              | `Like` (join table)                        |
| Comments                     | `Comment`, `User`, `Recipe`               |
| Admin moderation             | `User.is_admin`, relationships to all     |
| Recipe filtering/search      | `Category`, `RecipeCategory`, indexed fields |
| Profile views                | Linked `User → Recipe`, `User → Like`     |

This schema reflects **real-world content relationships** in a recipe-sharing application and has been thoroughly tested for data integrity, scalability, and performance.

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


### Relationships

- A **User** can have many **Recipes**, **Comments**, and **Likes**
- A **Recipe** belongs to one **User**; has many **Categories**, **Comments**, and **Likes**
- A **Category** can belong to many **Recipes** (Many-to-Many)
- A **Comment** belongs to one **User** and one **Recipe**
- A **Like** represents a single user liking a recipe (Many-to-Many via Likes table)

---

##  Testing

To keep this README concise, all testing documentation including manual testing, validation, edge cases, accessibility, and bug fixes has been moved to a separate file:

👉 [View Full Testing Documentation](./TESTING.md)


---

##  Security Considerations

DishCraft was developed following best practices for secure web application development to protect user data, maintain platform integrity, and comply with Code Institute’s assessment standards.

### 🔑 Secrets & Environment Variables

- All sensitive information, such as:
  - `SECRET_KEY` (used for session security)
  - `DATABASE_URL` (PostgreSQL connection string)
  - `CLOUDINARY_URL` (for image uploads)
- …are stored in an `.env` file and **never committed to GitHub**.  
- The `.env` file is included in `.gitignore` and variables are accessed via `os.getenv()` within the Flask app.

### 🔐 Password Security

- Passwords are **hashed using Flask-Bcrypt** before being stored in the database.
- Plain-text passwords are never stored or logged.
- During login, user input is securely compared against the hashed version using `check_password_hash`.

### 🧱 Authentication & Access Control

- **Flask-Login** handles session management and user authentication.
- Access to restricted routes is controlled using decorators like `@login_required`.
- Admin-only views and dashboard routes are protected using `current_user.is_admin` checks.

### 🛡️ CSRF Protection

- All forms are protected against Cross-Site Request Forgery using **Flask-WTF**.
- Each form includes a CSRF token to prevent malicious form submissions.

### 🧪 Session & Data Safety

- Flask sessions are securely signed using the `SECRET_KEY`.
- Sessions expire when the browser is closed or the user logs out.
- Validation is implemented for all forms using WTForms, providing both frontend and server-side protection against malformed inputs.

### 🚫 Debug Mode Off in Production

- Flask `DEBUG` mode is disabled in the live deployment.
- The `FLASK_ENV=production` setting ensures production safety and suppresses error messages.

---

**Summary**: All key security concerns including **password safety**, **form protection**, **session integrity**, and **admin access control** have been addressed. Sensitive data is safely managed using environment variables, and deployment configurations ensure no secrets are exposed.




##  Deployment

The DishCraft web application is deployed and hosted using **[Render](https://render.com/)**, which offers seamless support for Flask and PostgreSQL in a production environment.

🔗 **Live Link**: [DishCraft Live Site](https://project-online-cookbook.onrender.com)

---

### 🛠️ Technologies Used in Deployment

- **Render Web Service** – Hosts the Flask application.
- **Render PostgreSQL Instance** – Manages the live relational database.
- **GitHub** – Connected as the deployment source for automatic updates.

---

###  Deployment Steps to Render

To deploy the application from GitHub to Render, follow these steps:

1. **Push your project to GitHub**
   - Ensure that your latest code, requirements, and environment setup are committed and pushed to your GitHub repo.

2. **Create a new Web Service on Render**
   - Visit [https://dashboard.render.com](https://dashboard.render.com)
   - Click **"New Web Service"**
   - Connect your **GitHub** account and select the repository containing your Flask project.

3. **Configure Deployment Settings**
   - **Environment**: Python 3.11+
   - **Build Command**:  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:  
     ```bash
     gunicorn app:app
     ```
     > Replace `app:app` if your entry file is named differently (e.g., `run.py:app`).

4. **Add Environment Variables**
   Go to the **Environment tab** in Render and add the following variables securely:

   | Variable Name      | Description                              |
   |--------------------|------------------------------------------|
   | `SECRET_KEY`       | Flask session encryption key             |
   | `DATABASE_URL`     | Render PostgreSQL connection string      |
   | `CLOUDINARY_URL`   | Your Cloudinary API string               |
   | `FLASK_ENV`        | Set to `production`                      |

5. **Database Setup**
   - If not already created, deploy a **PostgreSQL** service via Render
   - Use the provided `DATABASE_URL` as an env variable in your Web Service

6. **Automatic Deployment**
   - Once connected to GitHub, Render will auto-deploy every time you push to the main branch.

---

###  Post-Deployment Checklist

After deployment, ensure:

- ✅ All environment variables are properly configured
- ✅ No secrets (e.g., `.env`, credentials) are pushed to GitHub
- ✅ Application loads without 500 errors
- ✅ Admin and user routes behave securely
- ✅ Static files and images (e.g., via Cloudinary) load correctly
- ✅ Flask `DEBUG` mode is turned off

---

###  Cloning and Running Locally

To clone the repository and run the project locally:

```bash
git clone https://github.com/your-username/dishcraft.git
cd dishcraft
pip install -r requirements.txt
```
Then create a .env file in the root directory with the following keys:
```bash
SECRET_KEY=your-secret-key
DATABASE_URL=your-local-db-url
CLOUDINARY_URL=your-cloudinary-url
FLASK_ENV=development
```
Finally, run the app:
```bash
python run.py
```

---

##  Future Improvements

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

##  Development Process

DishCraft was developed using an **iterative, feature-driven workflow**:

1. Planned wireframes, user stories, and database schema
2. Built core app structure and connected PostgreSQL database
3. Implemented authentication and admin roles
4. Developed CRUD features for recipes, comments, likes
5. Integrated Cloudinary and search/filter functionality
6. Focused on accessibility, responsiveness, and UX
7. Conducted thorough testing, documentation, and deployment

Version control was handled using **Git** and **GitHub**, with frequent, descriptive commits to track progress and isolate features.

📄 Example commit messages:
- `Add comment delete functionality`
- `Fix like toggle logic for logged-in users`

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

