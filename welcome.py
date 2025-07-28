def generate_welcome_page(name):
    welcome_message = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome, {name}!</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
                padding: 50px;
            }}
            .container {{
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                padding: 30px;
                display: inline-block;
            }}
            h1 {{
                color: #007bff;
            }}
            p {{
                font-size: 1.1em;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 0.9em;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome, {name}!</h1>
            <p>We're thrilled to have you here.</p>
            <p>Explore our features and make yourself at home.</p>
            <div class="footer">
                &copy; 2025 Your Company/Site Name. All rights reserved.
            </div>
        </div>
    </body>
    </html>
    """
    return welcome_message

# Example usage
if __name__ == "__main__":
    # Example: Generate welcome page for a user
    name = "Guest"
    html_content = generate_welcome_page(name)
    
    # You can save this to a file or serve it directly
    with open("welcome.html", "w") as f:
        f.write(html_content) 