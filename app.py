from flask import Flask, render_template

app = Flask(__name__)

# Sample data for the portfolio
portfolio_data = {
    "name": "Anisa Aulia",
    "title": "Information Tecnology Student",
    "tagline": "Transforming raw data into actionable insights",
    "summary_cards": [
        {"title": "Total Projects", "value": "24", "icon": "folder", "trend": "+3 this month"},
        {"title": "Datasets Analyzed", "value": "156", "icon": "database", "trend": "+12 this quarter"},
        {"title": "Models Deployed", "value": "8", "icon": "cpu", "trend": "2 in production"}
    ],
    "skills": ["Python", "SQL", "Pandas", "Power BI", "Machine Learning", "Figma"],
    "projects": [
        {
            "title": "Sales Forecasting Model",
            "description": "Built a time-series forecasting model achieving 94% accuracy",
            "tags": ["Python", "Scikit-learn", "Pandas"],
            "status": "Completed"
        },
        {
            "title": "Customer Segmentation",
            "description": "K-means clustering to identify 5 distinct customer segments",
            "tags": ["Python", "K-Means", "Visualization"],
            "status": "Completed"
        },
        {
            "title": "Real-time Dashboard",
            "description": "Interactive Power BI dashboard for executive reporting",
            "tags": ["Power BI", "DAX", "SQL"],
            "status": "In Progress"
        },
        {
            "title": "Churn Prediction",
            "description": "ML model to predict customer churn with 89% precision",
            "tags": ["Python", "XGBoost", "Feature Engineering"],
            "status": "Completed"
        }
    ],
    "recent_analyses": [
        {"dataset": "E-commerce Transactions", "records": "1.2M", "date": "2024-01"},
        {"dataset": "User Behavior Logs", "records": "850K", "date": "2024-01"},
        {"dataset": "Financial Statements", "records": "45K", "date": "2023-12"},
        {"dataset": "Marketing Campaigns", "records": "320K", "date": "2023-12"},
        {"dataset": "Supply Chain Data", "records": "2.1M", "date": "2023-11"}
    ],
    "nav_links": ["About", "Projects", "Skills"]
}


@app.route("/")
def index():
    return render_template("index.html", data=portfolio_data)


if __name__ == "__main__":
    app.run(debug=True)
