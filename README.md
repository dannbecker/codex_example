# codex_example

This is a minimal FastAPI project skeleton.

The list endpoints for books, members and loans support optional query
parameters that act as filters. For example, you can filter books by title or
author, members by name or email and loans by member id, book id or whether the
loan has been returned.

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```
