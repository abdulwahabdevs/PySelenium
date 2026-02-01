# PySelenium GitHub Automation

A Selenium project to automate GitHub login using cookies and a robust Page Object Model. Supports:

- Cookie-based login to skip UI login if session is valid
- Verification of login state by username
- Reusable page objects for Login and Home pages
- Page objects like Repos to get info about repositories owned and their names.
- Page Details POM to get specified repos description and readme file.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/abdulwahabdevs/PySelenium.git

   ```

2. Install dependencies(using pipenv)
   pipenv install
   pipenv shell

3. Set environment variables for credentials
   export GITHUB_USERNAME="your_username"
   export GITHUB_PASSWORD="your_password"

---

### **Usage**

`````markdown
## Usage

Run the automation:

````bash
python main.py


---

### **Project Structure**
```markdown
## Project Structure

PySelenium/
├── main.py
├── config.py         # Environment variables for username/password
├── pages/            # Page Objects
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── repos_page.py
│   └── repo_details_page.py
│
├── cookies.json      # Generated session cookies (gitignored)
└── Pipfile / Pipfile.lock


# Notes
- `cookies.json` is gitignored for security
- Do **not** commit credentials
````
`````

```

```
