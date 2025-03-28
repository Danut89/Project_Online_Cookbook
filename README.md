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
