# Lesson 06 – Azure Functions

To deploy the API without managing servers we host the Flask app inside
**Azure Functions v2**. This involves installing the `azure-functions` SDK and
wrapping the WSGI app with `WsgiMiddleware`. We also add `flasgger` so the
running function exposes Swagger documentation at `/apidocs`. After completing
this lesson you can start the function using Azure Functions Core Tools and test
the API in your browser.

## Purpose of Lesson

Deploy the Flask API as a serverless application that scales automatically.

## Technologies Used

- Azure Functions v2
- `WsgiMiddleware`
- `flasgger`

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

The API runs as an Azure Function locally with Swagger UI available.

### Steps

1. [01-install-packages.md](01-install-packages.md)
2. [02-wrap-as-azure-function.md](02-wrap-as-azure-function.md)
3. [03-run-locally.md](03-run-locally.md)
