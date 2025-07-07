# Lesson 09 – CI/CD

The final lecture is to automate everything. A **GitHub Actions** or **Azure DevOps**
pipeline will build the project, run the tests and deploy the Azure Function
whenever you push to the `main` branch. Both solutions use a service principal
stored as secrets. With CI/CD in place you can continuously deliver updates with
confidence.

## Purpose of Lesson

Automate testing and deployment so releases are repeatable and reliable.

## Technologies Used

- GitHub Actions or Azure DevOps Pipelines
- Azure Functions

## Personas Involved

- Retail Staff
- Store Manager

## Expected Outcome

Every push triggers a pipeline that tests the code and deploys the function app.

### Lectures

1. [lecture-01-create-workflow-file.md](lecture-01-create-workflow-file.md)
2. [lecture-02-create-azure-pipeline.md](lecture-02-create-azure-pipeline.md)
3. [lecture-03-trigger-pipeline.md](lecture-03-trigger-pipeline.md)
