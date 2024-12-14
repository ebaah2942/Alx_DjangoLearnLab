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



