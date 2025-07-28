# Share Contact App

## Overview
The Share Contact App is a web application designed to facilitate the sharing of contact information through video recordings. Users can record a video, input their contact details, and share them easily.

## Project Structure
```
share-contact-app
├── src
│   ├── index.html          # Main HTML structure of the application
│   ├── styles
│   │   └── main.css        # CSS styles for the application
│   ├── scripts
│   │   └── main.js         # JavaScript code for functionality
│   ├── manifest.json       # Web app manifest for installation
│   └── service-worker.js    # Service worker for offline capabilities
├── package.json            # npm configuration file
└── README.md               # Project documentation
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd share-contact-app
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the application**:
   You can use a local server to run the application. For example, you can use `live-server` or any other static server of your choice.

## Usage
- Open `index.html` in your web browser.
- Use the video recording feature to capture your message.
- Fill in your contact details in the provided input fields.
- Click the "Send" button to share your contact information.

## Features
- Video recording functionality
- Input fields for phone number and email address
- Responsive design using Tailwind CSS
- Offline capabilities through service worker

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.