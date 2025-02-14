# LUIT White Cohort - February 2025: Intro to Python 🚀  

Welcome to the **Level Up in Tech (LUIT) White Cohort - February 2025** repository for **Intro to Python**! This repository contains all materials, code samples, and exercises that will guide you through the fundamentals of Python programming.  

---

## 📌 About This Repository  
This repository is designed for the **White Cohort of February 2025** to provide structured learning resources and hands-on coding exercises in Python.  

### 📖 What You'll Learn
- Python Basics: Variables, Data Types, and Operators  
- Control Flow: If-Else Statements and Loops  
- Functions and Modules  
- Lists, Dictionaries, and Tuples  
- File Handling  
- Introduction to Boto3 and AWS SDK for Python  

---

## 📂 Repository Structure  
```
📦 luit-white-feb-2025-python  
 ┣ 📂 week-01/  # Python Fundamentals  
 ┃ ┣ 📜 lesson-1.md  
 ┃ ┣ 📜 lesson-2.md  
 ┃ ┗ 📜 exercises/  
 ┣ 📂 week-02/  # Control Flow & Data Structures  
 ┣ 📂 week-03/  # Working with APIs & AWS (Boto3)  
 ┣ 📜 requirements.txt  # Dependencies (if needed)  
 ┣ 📜 README.md  # You are here!  
 ┗ 📜 .gitignore  # Ignore unnecessary files  
```

---

## 🚀 Getting Started
### 1️⃣ Prerequisites  
Ensure you have the following installed:  
- Python 3.10+  
- Git  
- VS Code (recommended)  

### 2️⃣ Clone the Repository  
```bash
git clone https://github.com/zaireali649/luit-white-feb-2025-python.git
cd luit-white-feb-2025-python
```

### 3️⃣ Set Up a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt  # Install dependencies (if applicable)
```

---

# Troubleshooting

## ModuleNotFoundError: No module named 'matplotlib'

If you encounter the following or similar error:

```
Traceback (most recent call last):
  File "c:\Users\Ziggy\Dropbox\GitHub\luit-white-feb-2025-python\using_imports.py", line 2, in <module>
    import matplotlib3.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
```

### Solution:
1. Ensure you have `matplotlib` installed. Run the following command in your terminal or command prompt:

   ```
   pip install matplotlib
   ```

2. If you're using a virtual environment, activate it first:

   ```
   # Windows (Command Prompt)
   venv\Scripts\activate

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1

   # macOS/Linux
   source venv/bin/activate
   ```

   Then install `matplotlib` inside the virtual environment:

   ```
   pip install matplotlib
   ```

3. Double-check the import statement in your script. The correct import should be:

   ```python
   import matplotlib.pyplot as plt
   ```

   Ensure you are not using `matplotlib3.pyplot`, as that is incorrect.

4. If the issue persists, try upgrading `pip` and reinstalling `matplotlib`:

   ```
   pip install --upgrade pip
   pip uninstall matplotlib
   pip install matplotlib
   ```

After following these steps, try running your script again.

If you continue to experience issues, check your Python environment by running:

```
python -m pip show matplotlib
```

This should display installation details. If `matplotlib` is not found, reinstall it as shown above.

---

## 📌 Contributing
This repo is for educational purposes, and contributions are welcome! Feel free to submit pull requests for improvements or additional examples.

---

## 📞 Support & Questions
- Reach out in the **Level Up in Tech Teams Channel**  
- Post your questions in the **cohort Teams Channel**  
- Open a **GitHub issue** if you encounter any problems  

Let’s Level Up! 🚀💡  
