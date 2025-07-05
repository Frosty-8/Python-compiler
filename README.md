# 🌐 CodeStorm Compiler

A sleek, web-based code compiler built with Flask and Judge0 API, supporting multiple programming languages with real-time output.

## ✨ Features

- **Multi-language Support**: Python, C++, Java, JavaScript
- **Real-time Code Execution**: Get instant feedback on your code
- **Custom Input**: Test your code with custom stdin
- **Performance Metrics**: View execution time and memory usage
- **Modern UI**: Animated, responsive design with dark theme
- **Live Clock**: Displays current time in the header

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: Judge0 (for code execution)
- **Styling**: CSS Animations, Gradients, Glassmorphism effect

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- RapidAPI account (for Judge0 API key)

### Steps
1. Clone the repository:
```bash
git clone https://github.com/Frosty-8/Python-compiler.git
cd Python-compiler
```

2.Install dependencies:
```bash
pip install -r requirements.txt
```

3.Create a .env file in the root directory and add your Judge0 API key:
```bash
JUDGE0_API_KEY=your_api_key_here
```

4.Run the application:
```bash
python app.py
```

5.Open your browser and navigate to:
```bash
http://localhost:5000
```

### 📂 Project Structure
```bash
frosty-8-python-compiler/
├── app.py               # Flask application entry point
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not tracked)
├── static/
│   └── style.css        # All CSS styles
└── templates/
    └── index.html       # Main HTML template
```


### 🌈 UI Components
- **Header**: Animated typing effect with live clock

- **Control Panel**: Language selection and stdin input

- **Code Editor**: Main coding area with syntax highlighting

- **Output Panel**: Displays execution results with metrics

### 🔧 API Configuration
- The application uses Judge0 API for code execution. To configure:

- Sign up at RapidAPI Judge0

- Get your API key

- Add it to the .env file as JUDGE0_API_KEY

### 🛡️ Security Notes
- **Keep your API key confidential** (never commit .env to version control)

- **The application is designed for development use** (debug mode is enabled)


### 🤝 Contributing
Contributions are welcome! Please follow these steps:

- **Fork the repository**

- **Create a feature branch** 
```bash
git checkout -b feature/amazing-feature
```

- **Commit your changes** 
```bash
git commit -m 'Add some amazing feature'
```

- **Push to the branch** 
```bash
git push origin feature/amazing-feature
```

- **Open a Pull Request**