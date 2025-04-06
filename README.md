# Social Media API

This is a social media API built using Django and Django Rest Framework (DRF) that allows users to create, view, and interact with posts, comments, likes, and follow/unfollow users. It also includes features such as user authentication and token-based security.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [User Authentication](#user-authentication)
  - [Post Management](#post-management)
  - [Comment Management](#comment-management)
  - [Like Management](#like-management)
  - [Follow/Unfollow Management](#followunfollow-management)
- [Testing](#testing)
- [License](#license)

---

## Features

- **User Authentication**: Users can register, log in, and authenticate via token-based authentication.
- **Post Management**: Create, view, and delete posts.
- **Comment Management**: Add, edit, and delete comments on posts.
- **Like Management**: Like/unlike posts and comments.
- **Follow/Unfollow**: Follow or unfollow other users.

---

## Technologies Used

- **Django**: The core web framework.
- **Django Rest Framework (DRF)**: For building the API.
- **SQLite/PostgreSQL/MySQL**: Database support (configured for SQLite by default).
- **Token Authentication**: For secure user authentication.
- **Python 3.x**: Programming language used.

---

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository**:

   ```bash
   git clone <repository_url>
   cd Social_Media_API
   ```

2. **Create and Activate a Virtual Environment**:

   For Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   For Mac/Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the root of the project and add the following environment variables:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3  # or PostgreSQL, MySQL configuration
   ```

5. **Run Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (Optional, to access the Django Admin panel):

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

---

## Usage

Once the server is running, you can start interacting with the API. You can use Postman, Insomnia, or any API client to make requests.

---

## API Endpoints

### User Authentication

- **POST** `/api/auth/register/`: Register a new user.
- **POST** `/api/auth/login/`: Log in a user and get an authentication token.
- **GET** `/api/auth/me/`: Get the current user's profile information (requires authentication).

### Post Management

- **GET** `/api/posts/`: Get a list of all posts.
- **POST** `/api/posts/`: Create a new post (requires authentication).
- **GET** `/api/posts/{post_id}/`: Get a specific post.
- **PUT** `/api/posts/{post_id}/`: Update a specific post (requires authentication).
- **DELETE** `/api/posts/{post_id}/`: Delete a specific post (requires authentication).

### Comment Management

- **GET** `/api/posts/{post_id}/comments/`: Get a list of comments for a specific post.
- **POST** `/api/posts/{post_id}/comments/`: Add a comment to a post (requires authentication).
- **PUT** `/api/comments/{comment_id}/`: Update a comment (requires authentication).
- **DELETE** `/api/comments/{comment_id}/`: Delete a comment (requires authentication).

### Like Management

- **POST** `/api/posts/{post_id}/like/`: Like a specific post (requires authentication).
- **POST** `/api/comments/{comment_id}/like/`: Like a specific comment (requires authentication).
- **DELETE** `/api/posts/{post_id}/like/`: Unlike a specific post (requires authentication).
- **DELETE** `/api/comments/{comment_id}/like/`: Unlike a specific comment (requires authentication).

### Follow/Unfollow Management

- **POST** `/api/follow/{user_id}/`: Follow a user (requires authentication).
- **DELETE** `/api/follow/{user_id}/`: Unfollow a user (requires authentication).

---

## Testing

To test the API, you can use Postman, Insomnia, or any other API testing tool. You can test all the available API endpoints and verify the functionality of each feature (like registration, login, creating posts, commenting, liking, following, etc.).

---



