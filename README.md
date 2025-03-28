# 📘 – DishCraft –


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
  - [Bugs and Fixes](#bugs-and-fixes)

- [Deployment](#deployment)
  - [Deployment to Render](#deployment-to-render)
  - [Cloning and Running Locally](#cloning-and-running-locally)
  - [Environment Variables](#environment-variables)

- [Credits](#credits)
  - [Resources and Tutorials](#resources-and-tutorials)
  - [Inspiration and Acknowledgements](#inspiration-and-acknowledgements)



##  About

**Project Name**: Online Cookbook  
**Developer**: [Danut Grigore]  
**Type**: Milestone 3 - Full Stack Web Development (Code Institute)

# 🍽️ DishCraft

###  Project Overview

**DishCraft** is a full-stack, data-centric web application built using Flask and PostgreSQL that empowers users to discover, share, and manage recipes from around the world. The application features a clean, responsive interface designed with Bootstrap, and provides an intuitive user experience across all devices.

Users can register, log in, and interact with a community of food lovers by posting, liking, and commenting on recipes. Admins have additional privileges to manage users, content, and comments through a dedicated dashboard. Whether you're a passionate home cook or just looking for new culinary inspiration, **DishCraft** makes it easy to explore and contribute to a growing collection of diverse, delicious dishes.

---

###  Site Purpose

The core purpose of DishCraft is to create an open and welcoming space for food lovers to share their creations, discover new ideas, and connect with others through cooking. Unlike generic recipe sites, DishCraft emphasizes user interaction — turning recipe-sharing into a dynamic, community-driven experience.

Users can:
- 👨‍🍳 Create, edit, and manage their personal recipes
- ❤️ Like and comment on other users’ dishes
- 🌍 Browse recipes by category, difficulty, or cuisine
- 🛠️ Access moderation tools (admin only) to keep content curated and respectful

---

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

---

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

---

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

---

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

---

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


## Wireframes

To guide the layout and design of DishCraft, a series of wireframes were created for key pages. These wireframes helped establish user flow, component hierarchy, and responsive structure before development began.

Each screen was designed with mobile responsiveness and intuitive interaction in mind.

---

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

---

Wireframes were iterated based on usability testing and layout refinements during development.


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

![Homepage UI](/app/static/readme-screenshoots/home-page-screenshoot.png)

</details>

---

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

![Login Register UI](/app/static/readme-screenshoots/login.register-screenshoot.png)

</details>

---

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

![CRUD Example](/app/static/readme-screenshoots/CRUD-screenshoot.png)

</details>
<details>
<summary>📸 Recipe CRUD Interface (Click to expand)</summary>

![CRUD Example](/app/static/readme-screenshoots/CRUD-screenshoot2.png)

</details>

---

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
