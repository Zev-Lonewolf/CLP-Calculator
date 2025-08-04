<div align="center">

# 🧮 CLP-Calculator

![Python](https://img.shields.io/badge/Python-3.13-blue) 
![MIT License](https://img.shields.io/badge/license-MIT-green) 
![Academic Project](https://img.shields.io/badge/Academic_Project-University-yellow) 
![Current State](https://img.shields.io/badge/Current%20State-Pre--Finished-orange)

A simple and interactive command-line calculator built with Python, designed for beginners to practice programming and fundamental math operations.

</div>

---

### 📚 About

This project was developed as a personal academic exercise focused on programming fundamentals and basic arithmetic operations using Python. Its goal is simple and practical: **to create a command-line calculator capable of performing sequential arithmetic operations (+, -, *, /) with input validation and error handling**.

Designed with beginners in mind, the project encourages hands-on learning by combining basic math concepts and user interaction through a clean CLI interface.

Python was chosen due to its readability and popularity as a first programming language, making it ideal for educational purposes and quick prototyping.

This calculator is intended for students, educators, and anyone interested in exploring basic programming projects or improving their command-line skills.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white) ![CLI](https://img.shields.io/badge/CLI-Terminal-4A90E2?logo=terminal&logoColor=white)

### 🚀 How to Use / Install

1. **Clone the repository:**

```bash
git clone https://github.com/Zev-Lonewolf/CLP-Calculator.git
cd CLP-Calculator
```

2. **Make sure you have Python 3.13+ installed:**

```bash
python --version
```

3. **Run the calculator script:**
```bash
python src/calculadora.py
```

4. **Follow the instructions on the terminal:**
- Digite valores e operações na sequência.
    - "Enter values and operations in sequence."
- Use "SAIR" para encerrar a calculadora.
    - "Use "EXIT" to end the calculator."
- Use "OK" para calcular o resultado atual.
    - "Use "OK" to calculate the current result."
- Digite valores e operações na sequência.
    - "Enter values and operations in the sequence."
- Use "SAIR" para encerrar a calculadora.
    - "Use "EXIT" to end the calculator."
- Use "OK" para calcular o resultado atual.
    - "Use "OK" to calculate the current result."

> ✅ No external dependencies required

### 🧪 Example of Use

Below is a simple usage example of the CLP-Calculator:
```
Value or "EXIT" to quit: 10
Operation or "OK" to calculate: +
Value: 5
Operation or "OK" to calculate: *
Value: 3
Operation or "OK" to calculate: ok

45.0
```
**Explanation:**
The input `10 + 5 * 3` is processed **in the order entered**, without applying mathematical precedence rules.
The calculator follows a linear logic:
  → `10 + 5 = 15`  
  → `15 * 3 = 45`  
Final result: `45.0`

> ⚠️ **Note**: This calculator performs operations in the exact order they are entered by the user, and **does not follow standard operator precedence** (like parentheses or multiplication before addition).

### 🛠️ Technical Details & Techniques Used

This project implements a basic command-line calculator that performs chained arithmetic operations in the exact order they are entered by the user — without enforcing operator precedence.

Developed in **pure Python**, the calculator adopts a procedural approach within a single script located at `src/calculadora.py`. All user interaction is handled via the terminal, ensuring full portability and zero dependency on external libraries or frameworks.

The calculator processes values and operations sequentially, applying the logic step-by-step, which makes it ideal for educational purposes or lightweight experimentation with Python input/output and control flow.

Key components include:  
- Input validation using loops and exception handling  
- Sequential parsing of numbers and operations  
- Arithmetic logic implemented via conditionals  
- Simple loop structure to allow multiple calculations in a single session

### Techniques Used  
- Command-line interface (CLI) input handling and validation  
- Dynamic list-based storage of values and operations  
- Procedural control flow with error handling  
- Basic arithmetic operation chaining (`+`, `-`, `*`, `/`)  

While simple in scope, this calculator serves as a foundational project for understanding Python syntax, data types, and flow control. Future iterations may include expression parsing, support for parentheses, and more complex features.

### 🙏 Acknowledgments

Special thanks to UFMT and its dedicated professors for their effort in guiding students through the foundations of programming and mathematics.

This project was built upon the work and generosity of open-source communities and tool creators — from the Python language itself to editors like Visual Studio Code that make development more accessible.

And of course, gratitude goes to all the inspirations behind this calculator: from classic programming logic to the simplicity of the command line — and every formula, idea, and concept that helped shape this learning journey.

### 🙌 Help the Developer

If you found this project useful or interesting, consider giving it a ⭐ star on GitHub — it really helps!

Feel free to follow me for more projects, updates, and nerdy adventures.

Every star and follower motivates me to keep creating and sharing cool stuff!

---

## 📎 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it.

**MIT License © 2025 Zev Lonewolf**
