# Lesson 08 – Security

Once the API is reachable by others we must protect it. You will implement a
`require_jwt` decorator using the **pyjwt** library so local requests must
include a valid token. In Azure we rely on EasyAuth to provide the same
validation automatically. When finished the endpoints are secured both locally
and in the cloud.

## Purpose of Lesson

Add authentication so only authorised clients can access the API.

## Technologies Used

- pyjwt
- Azure EasyAuth

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

Endpoints require JWTs locally and rely on EasyAuth when deployed.

### Steps

1. [01-install-pyjwt.md](01-install-pyjwt.md)
2. [02-add-jwt-decorator.md](02-add-jwt-decorator.md)
3. [03-configure-easyauth.md](03-configure-easyauth.md)
