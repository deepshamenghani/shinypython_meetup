Dashboard Creation with Shiny for Python: A Quarto Presentation
This repository contains the resources for a presentation on creating interactive dashboards using Shiny for Python. The presentation is built with Quarto and is designed to be a comprehensive guide for building, customizing, and deploying Shiny applications.

Presentation Overview
This presentation covers:

Basics of Shiny for Python
Environment setup
Shiny app development
Interactivity with widgets
Data visualization
Dashboard customization
Project structure and best practices
Deployment strategies
Repository Structure
graphql
Copy code
/
├── index_files/                # Quarto-generated files
├── quarto_images/              # Images for the presentation
├── dashboardgif.gif            # Animated GIF demo of the dashboard
├── .gitignore                  # Untracked files to ignore
├── .Rhistory                   # R history file
├── _publish.yml                # Quarto publishing configuration
├── index.html                  # Compiled presentation HTML
├── index.qmd                   # Quarto markdown for presentation
├── README.md                   # README documentation
├── shiny_python_meetup.Rproj   # R project file
└── styles.scss                 # Custom presentation styles
Getting Started
Prerequisites
Python >= 3.6
R and RStudio (for Quarto)
Python packages: shiny, pandas, plotly, etc.
R packages: quarto
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Python packages:
bash
Copy code
pip install -r requirements.txt
Render the presentation with Quarto:
r
Copy code
quarto::quarto_render("index.qmd")
Running the Shiny App
The code for the Shiny app is maintained in a separate repository. Clone and follow the setup instructions there:

bash
Copy code
git clone https://github.com/your-username/shiny-app-repo.git
Link to Shiny App Repository

Presentation and Dashboard Demo
To view the presentation, access it at the following link:

Link to Quarto Presentation

Below is a GIF that demonstrates what the interactive dashboard looks like:


Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

License
This project is open-sourced under the MIT License.

Acknowledgments
Dataset provided by the American Kennel Club.
Meetup group shiny_python_meetup.
Contact
For queries, contact [Your Name] at [your-email@example.com].