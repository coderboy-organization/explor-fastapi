## Explorer FastAPI

Development setup

1. Frok this repository
2. Clone on your local machine
   ```bash
   https://github.com/coderboy-organization/explorer-fastapi.git
   ```
3. Create a VENV
   ```bash
   python -m venv env
   ```
4. Run your Virtual Env
   - For windows (**Bash Terminal**)
   ```bash
   source env/Scripts/activate
   ```
   - For Mac or Linux
   ```bash
   source env/bin/activate
   ```
5. Install all dependency which we mention on `requirements.txt` file
   ```bash
   pip install -r requirements.txt
   ```
6. Run development server with `uvicorn`
   ```bash
   uvicorn main:app --port 5000 --reload
   ```
