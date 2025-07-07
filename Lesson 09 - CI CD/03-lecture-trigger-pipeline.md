# Trigger the Pipeline

1. Commit all changes and push to `main`:
   ```bash
   git add .
   git commit -m "Set up CI/CD"
   git push origin main
   ```
2. Monitor the GitHub Actions page or Azure DevOps pipeline to ensure the build
   runs and deploys the function app. Any failing tests will stop the
   deployment.

## Why this lecture?

Seeing the pipeline execute reinforces how code changes lead to automated
testing and deployment. Watching for failures helps you respond quickly when
issues arise.
## Theory example
CI/CD encourages small, frequent changes. Each push triggers a new pipeline run, providing rapid feedback on whether the code is ready to deploy.
