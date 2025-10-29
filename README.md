# Go Web Server — Basic REST API

A minimal Go web server demonstrating basic REST API operations (create and fetch users) using the standard library (`net/http`).

## Features

- POST /users — Create a new user
- GET /users/{id} — Fetch a user by ID
- Thread-safe in-memory storage (uses `sync.Mutex`)

## Prerequisites

- Go 1.22 or newer
- A terminal

## Quick start

1. Clone the repository (if needed) and change into the project directory:

```bash
git clone https://github.com/yourusername/go-web-server.git
cd go-web-server
```

2. Run the server:

```bash
go run main.go
```

By default the server listens on http://localhost:8080

## Example requests

Create a user:

```bash
curl -s -X POST -H "Content-Type: application/json" \
   -d '{"name":"Kevin"}' \
   http://localhost:8080/users
```

Get a user by ID:

```bash
curl -s http://localhost:8080/users/1
```

## Project structure

```
.
├── main.go    # Main entry point
└── README.md  # Project documentation
```

## Notes

This project uses in-memory storage. All data is lost when the server restarts.

Possible extensions:

- Add full CRUD (update/delete)
- Replace in-memory storage with a persistent database
- Add input validation and error handling improvements

Author: Kevin Kimutai
License: MIT
