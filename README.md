# PYTHON CODING CHALLENGE: REST API ON FASTAPI

## Assumptions

- (1) In this challenge, `author` is just a reference string to "an author". 
- (2) The challenge didn't mention anything about `author`, so I assumed we wouldn't need to query documents using `author` nor care about possible attributes of `author`.
- (3) Users only query using `id` of the book.
- (4) Upon creation, users don't need to send an `id`. The system would automatically generate it.


## Database Design

As stated in the assumptions, `author` is just a reference string & we only query books using `id`. 

So I chose the schema design as follows:
```
- Table: Books
- Partition key: id         (eg: "/books/1aeddb84-24db-4aca-a98f-ae43a2499a8a")
- Sort key: None            (eg: "/authors/d953185e-1ab7-4860-a0e8-31020d6ebb6d")
```

In other cases, if we want to extend the system by introducing `author` or querying using it, I suggest doing the following to show the "relations" between `author` and `book`:
```
a) Redesigning the schema to:
- Partition key: author
- Sort key: book_id

b) Create a separate table `Author` to store authors.
```

## Prerequisites
- Python 3.6+


## Environment Preparation


## Run API Server


## Deployment


## Testing
