# AI Native Pursuit - Fact-Checker Project

A comprehensive AI-powered fact-checking system with multiple interfaces and a quiz mode for educational purposes.

## 🚀 Project Overview

This project demonstrates the development of an intelligent fact-checking system with both claim verification and interactive quiz capabilities. It includes a Python backend with an enhanced matching algorithm and multiple web interfaces for different use cases.

## 📁 Project Structure

```
ai-native-pursuit/
├── get_user_words.py                    # Original word input functionality
├── My Mini Project                      # Original HTML file
├── My_Mini_Project_lists/
│   └── dict.py                         # Enhanced fact-checker with 18 entries
├── fact_checker_web.html               # Modern web interface for claim verification
├── fact_checker_quiz.html              # Interactive quiz mode interface
├── README_Quiz_Mode.html               # Quiz mode documentation
└── README.md                           # This comprehensive project documentation
```

## 🎯 Features

### 🔍 Fact-Checker (Claim Verification Mode)
- **18 fact-checking entries** covering 7 subject areas
- **Enhanced matching algorithm** with best-match logic
- **Confidence scoring** from 0% to 99%
- **Three verdict types**: Likely True, Likely False, Cannot Verify
- **Modern web interface** with real-time results
- **Example claims** for easy testing

### 🧠 Quiz Mode
- **Interactive question-and-answer format**
- **5 general knowledge questions**
- **Instant feedback** with confidence levels
- **Auto-advancing questions** every 3 seconds
- **Responsive design** using Tailwind CSS
- **Educational justifications** for each answer

## 🛠️ Technologies Used

- **Python 3** - Backend logic and data processing
- **HTML5** - Structure and content
- **CSS3** - Styling and animations
- **JavaScript** - Interactive functionality
- **Tailwind CSS** - Modern UI framework
- **Git** - Version control

## 📊 Fact-Checker Database

The system includes 18 fact-checking entries across these categories:

### 🔬 Science Facts (4 entries)
- Earth's shape and flat Earth misconceptions
- Water boiling point and dinosaur extinction
- **Keywords**: earth, round, flat, water, boil, dinosaurs, extinct

### 💻 Technology Facts (2 entries)
- iPhone history and internet invention myths
- **Keywords**: iphone, first, 2007, internet, invented, al gore

### 🏥 Health Facts (2 entries)
- Vaccine safety and vitamin C effectiveness
- **Keywords**: vaccines, autism, vitamin, c, cold

### 📚 History Facts (2 entries)
- Columbus discovery myth and WWII end date
- **Keywords**: columbus, discovered, america, world, war, 2, 1945

### 🌌 Space Facts (2 entries)
- Sun classification and Mars characteristics
- **Keywords**: sun, star, mars, red, planet

### ❌ Common Misconceptions (2 entries)
- 10% brain myth and carrot eyesight claims
- **Keywords**: humans, use, 10, percent, brain, carrots, improve, eyesight

### 🌍 Environmental Facts (2 entries)
- Climate change reality and plastic decomposition
- **Keywords**: climate, change, real, plastic, decompose, years

## 🎮 Quiz Mode Questions

The quiz mode includes 5 educational questions:

1. **"What is the capital of France?"** → Answer: "paris"
2. **"Which planet is known as the Red Planet?"** → Answer: "mars"
3. **"What is the largest ocean on Earth?"** → Answer: "pacific ocean"
4. **"How many continents are there in the world?"** → Answer: "7"
5. **"What is the chemical symbol for water?"** → Answer: "h2o"

## 🚀 How to Use

### Fact-Checker Web Interface
1. Open `fact_checker_web.html` in any web browser
2. Enter any claim in the input field
3. Click "Check Claim" or press Enter
4. View results with confidence levels and justifications
5. Try the example cards for quick testing

### Quiz Mode
1. Open `fact_checker_quiz.html` in any web browser
2. Read the displayed question
3. Type your answer in the text area
4. Click "Verify Answer" or press Enter
5. See immediate feedback and wait for the next question

### Python Backend
1. Navigate to the project directory
2. Run: `python3 My_Mini_Project_lists/dict.py`
3. Enter claims for fact-checking
4. Type 'quit' to exit

## 🔧 Technical Implementation

### Enhanced Matching Algorithm
The fact-checker uses a sophisticated matching system:
- **Best-match logic**: Finds the fact with the most keyword matches
- **Partial matching**: Works even when not all keywords are present
- **Confidence scoring**: Provides accuracy levels for each result
- **Default responses**: Handles unknown claims gracefully

### Web Interface Features
- **Responsive design**: Works on all device sizes
- **Real-time processing**: Instant results with loading animations
- **Color-coded results**: Visual indicators for different verdict types
- **Interactive examples**: Clickable cards for easy testing

## 📈 Project Evolution

1. **Initial Setup**: Basic word input functionality
2. **Fact-Checker Development**: Enhanced Python backend with 18 entries
3. **Web Interface**: Modern HTML/CSS/JS interface for claim verification
4. **Quiz Mode**: Interactive question-and-answer format
5. **Documentation**: Comprehensive README files

## 🎯 Learning Outcomes

This project demonstrates:
- **Data structure design** with dictionaries and lists
- **Algorithm implementation** for pattern matching
- **Web development** with modern frameworks
- **User interface design** principles
- **Version control** with Git
- **Documentation** best practices

## 🔮 Future Enhancements

Potential improvements could include:
- **More fact-checking entries** across additional subjects
- **API integration** for real-time fact verification
- **User accounts** and progress tracking
- **Mobile app** development
- **Machine learning** integration for improved accuracy
- **Multi-language support**

## 📝 License

© 2025 AI Mini-Project. All Rights Reserved.

## 🤝 Contributing

This is a learning project demonstrating AI and web development concepts. Feel free to use this code as a reference for your own educational projects.

---

**Note**: This tool is for preliminary, personal use and cannot replace expert analysis. It is designed for simple, unambiguous claims and relies on predefined knowledge bases.
