API Documentation for Posts and Comments Endpoints

Posts Endpoint

 List Posts
GET /posts/
Response:
{
    "count": 10,
    "next": "http://example.com/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "username",
            "title": "Post Title",
            "content": "Post content...",
            "created_at": "2024-12-13T12:34:56Z",
            "updated_at": "2024-12-13T12:34:56Z"
        }
    ]
}

Create a Post
POST /posts/
Request:
{
    "title": "New Post",
    "content": "This is the content of the new post."
}
Response:
{
    "id": 2,
    "author": "username",
    "title": "New Post",
    "content": "This is the content of the new post.",
    "created_at": "2024-12-13T12:34:56Z",
    "updated_at": "2024-12-13T12:34:56Z"
}

Retrieve a Post
GET /posts/{id}/**
Response:
{
    "id": 1,
    "author": "username",
    "title": "Post Title",
    "content": "Post content...",
    "created_at": "2024-12-13T12:34:56Z",
    "updated_at": "2024-12-13T12:34:56Z"
}
 Update a Post
PUT /posts/{id}/**
Request:
{
    "title": "Updated Post",
    "content": "Updated content."
}
Response:
{
    "id": 1,
    "author": "username",
    "title": "Updated Post",
    "content": "Updated content.",
    "created_at": "2024-12-13T12:34:56Z",
    "updated_at": "2024-12-13T12:45:56Z"
}

Delete a Post
DELETE /posts/{id}/**
Response:
204 No Content

Comments Endpoint
List Comments
GET /comments/
Response:
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "post": 1,
            "author": "username",
            "content": "Comment content...",
            "created_at": "2024-12-13T12:34:56Z",
            "updated_at": "2024-12-13T12:34:56Z"
        }
    ]
}

Create a Comment
POST /comments/**
Request:
{
    "post": 1,
    "content": "This is a comment."
}
Response:
{
    "id": 2,
    "post": 1,
    "author": "username",
    "content": "This is a comment.",
    "created_at": "2024-12-13T12:34:56Z",
    "updated_at": "2024-12-13T12:34:56Z"
}

Retrieve a Comment
GET /comments/{id}/
Response:
{
    "id": 1,
    "post": 1,
    "author": "username",
    "content": "Comment content...",
    "created_at": "2024-12-13T12:34:56Z",
    "updated_at": "2024-12-13T12:34:56Z"
}
Update a Comment
PUT /comments/{id}/
Request:
{
    "content": "Updated comment content."
}
Response:
{
    "id": 1,
    "post": 1,
    "author": "username",
    "content": "Updated comment content.",
    "created_at": "2024-12-13T12:34:56Z",
    "updated_at": "2024-12-13T12:45:56Z"
}

Delete a Comment
DELETE /comments/{id}/
Response:
204 No Content


Endpoints

1. Follow User

URL: /follow/<int:user_id>/

Method: POST

Description: Allows an authenticated user to follow another user.

Request Example:

POST /follow/2/
Authorization: Token <your_token>
Content-Type: application/json

Response Example:

Success:

{
    "message": "You are now following john_doe."
}

Error:

{
    "error": "You cannot follow yourself."
}

2. Unfollow User

URL: /unfollow/<int:user_id>/

Method: POST

Description: Allows an authenticated user to unfollow another user.

Request Example:

POST /unfollow/2/ 
Authorization: Token <your_token>
Content-Type: application/json

Response Example:

Success:

{
    "message": "You have unfollowed john_doe."
}

Error:

{
    "error": "You cannot unfollow yourself."
}

3. User Feed

URL: /feed/

Method: GET

Description: Retrieves posts from users that the authenticated user is following, ordered by the creation date (most recent first).

Request Example:

GET /feed/
Authorization: Token <your_token>

Response Example:

[
    {
        "id": 1,
        "user": "john_doe",
        "content": "This is a test post.",
        "created_at": "2024-12-14T12:00:00Z"
    },
    {
        "id": 2,
        "user": "jane_doe",
        "content": "Another post here.",
        "created_at": "2024-12-13T11:30:00Z"
    }
]

Testing and Usage

Authentication

All endpoints require the user to be authenticated. Include the Authorization header with a valid token when making requests.

Follow and Unfollow

Users can follow or unfollow others by making POST requests to /follow/<user_id>/ and /unfollow/<user_id>/.

Proper permissions ensure that users can only modify their own follow relationships.

Feed

Use the /feed/ endpoint to view posts from followed users, sorted by the most recent.

Changelog

CustomUser Model: Added a following field (Many-to-Many relationship) to manage user follow relationships.

Post Model: Ensure the Post model includes user (ForeignKey) and created_at (DateTimeField).

New Endpoints:

/follow/<user_id>/: Follow a user.

/unfollow/<user_id>/: Unfollow a user.

/feed/: View the content feed from followed users.

The Likes and Notifications systems are designed to increase user engagement by allowing users to interact with posts and stay informed about important activities.





LIKE SYSTEM

The likes system enables users to like or unlike posts, providing a simple and interactive way to engage with content.

Endpoints

Like a Post

URL: /posts/<int:pk>/like/

Method: POST

Authentication: Required

Request Body: None

Response:

{
  "success": true,
  "likes_count": 10
}

Description: Likes the specified post. Increments the like count.

Unlike a Post

URL: /posts/<int:pk>/unlike/

Method: POST

Authentication: Required

Request Body: None

Response:

{
  "success": true,
  "likes_count": 9
}

Description: Removes the user’s like from the specified post. Decrements the like count.

Fetch Likes for a Post

URL: /posts/<int:pk>/likes/

Method: GET

Authentication: Optional

Response:

{
  "likes_count": 10,
  "liked_by": [
    {"id": 1, "username": "user1"},
    {"id": 2, "username": "user2"}
  ]
}

Description: Fetches the total likes and the list of users who liked the post.

Benefits

Encourages interaction with content.

Allows users to express appreciation for posts.

Notifications System

The notifications system alerts users about significant events, such as new likes, comments, and followers.

Endpoints

Fetch Notifications

URL: /notifications/

Method: GET

Authentication: Required

Response:

[
  {
    "id": 1,
    "actor": {"id": 2, "username": "user2"},
    "verb": "liked your post",
    "target": {"id": 5, "type": "post", "title": "Sample Post"},
    "timestamp": "2024-12-15T10:30:00Z",
    "read": false
  },
  {
    "id": 2,
    "actor": {"id": 3, "username": "user3"},
    "verb": "commented on your post",
    "target": {"id": 5, "type": "post", "title": "Sample Post"},
    "timestamp": "2024-12-15T11:00:00Z",
    "read": true
  }
]

Description: Fetches all notifications for the authenticated user, with unread notifications shown prominently.

Mark Notification as Read

URL: /notifications/<int:pk>/read/

Method: POST

Authentication: Required

Response:

{
  "success": true,
  "message": "Notification marked as read."
}

Description: Marks the specified notification as read.

Mark All Notifications as Read

URL: /notifications/read-all/

Method: POST

Authentication: Required

Response:

{
  "success": true,
  "message": "All notifications marked as read."
}

Description: Marks all notifications for the user as read.

Benefits

Keeps users informed about interactions with their posts.

Encourages users to engage more by highlighting activity.

Improves the social experience by fostering timely responses to activities.

Interaction Workflow Examples

1. Liking a Post

Request:

POST /posts/1/like/
Authorization: Token <your_token>

Response:

{
  "success": true,
  "likes_count": 20
}

2. Fetching Notifications

Request:

GET /notifications/
Authorization: Token <your_token>

Response:

[
  {
    "id": 1,
    "actor": {"id": 2, "username": "user2"},
    "verb": "liked your post",
    "target": {"id": 5, "type": "post", "title": "Sample Post"},
    "timestamp": "2024-12-15T10:30:00Z",
    "read": false
  }
]

3. Marking a Notification as Read

Request:

POST /notifications/1/read/
Authorization: Token <your_token>

Response:

{
  "success": true,
  "message": "Notification marked as read."
}




