## GitLeaks Scan for Twilio API Keys

This project is a GitHub Actions workflow that scans a repository for exposed Twilio API keys using GitLeaks. The workflow is triggered on push and pull request events for the main and master branches.

### Configuration
The workflow uses a custom twilio-gitleaks.toml file to define the rule for detecting Twilio API keys. The rule is configured to search for strings matching the pattern SK[0-9a-fA-F]{32}.

### Workflow
The workflow consists of four steps:

- Checkout code: Checks out the repository code using the actions/checkout@v3 action.
- Install GitLeaks: Installs GitLeaks on the ubuntu-latest environment using a curl command.
- Run GitLeaks scan: Runs the GitLeaks scan using the gitleaks detect command with the custom twilio-gitleaks.toml configuration file.
- Upload GitLeaks report: Uploads the GitLeaks report as an artifact named gitleaks-report.json using the actions/upload-artifact@v3 action.

### Sample Code
A sample Python file send_sms.py is provided to demonstrate how to use a Twilio API key to send an SMS message.

### Testing the GitLeaks Scan Workflow

**To test the workflow:**

- Create a test branch and update send_sms.py with a valid Twilio API key.
- Commit and push changes to trigger the workflow.
- Check the workflow logs for errors.
- Verify the gitleaks-report.json artifact contains the expected results.