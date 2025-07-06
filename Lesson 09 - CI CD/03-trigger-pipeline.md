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
