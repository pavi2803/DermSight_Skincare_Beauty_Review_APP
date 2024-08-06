## DermSight - Skincare and Beauty Insights
DermSight is an innovative application designed to help users make informed decisions about skincare and makeup products. By providing concise and precise product details, including reviews and ratings, DermSight ensures you get an accurate overall performance assessment of each product.

### About This Application
In the vast world of skincare and makeup, choosing the right product can be overwhelming due to the sheer number of options available. User reviews play a crucial role in determining whether a product is worth trying, as they offer insights into the pros and cons from real-world experiences.

DermSight simplifies this process by fetching real-time reviews for a wide range of skincare and makeup products. Using API calls and JSON data parsing, the application provides up-to-date information and ratings, giving users a comprehensive view of product performance. Automation via GitHub Actions ensures that the data is continuously updated, maintaining the accuracy and relevance of the information provided.

### Features
* **Real-Time Reviews:** Fetches and displays up-to-date reviews for both skincare and makeup products.
* **Comprehensive Ratings:** Provides an overall performance rating for each product based on user feedback.
* **Automated Updates:** Utilizes GitHub Actions to automate data retrieval and update processes, ensuring the latest information is always available.
* **User-Friendly Interface:** Presents product details in a concise and precise manner, making it easy for users to evaluate and compare products.

### Tech Stack
* **API:** Utilizes HTTP GET requests to fetch data from external sources.
* **JSON:** Parses JSON data to extract relevant product details and reviews.
* **Python:** The core programming language used for developing the application, handling data processing, and integrating various components.
* **GitHub Actions:** Automates the workflow for data updates, ensuring the application stays current with the latest product reviews.
* **Gemini Pro API:** A powerful API that provides access to detailed product information and reviews.
* **Prompt Engineering:** Enhances the user experience by designing effective prompts for data retrieval and presentation.

### Getting Started
**Prerequisites**
* Python 3.x
* Git
* GitHub account with access to GitHub Actions
  
**Installation**
Clone the Repository:
git clone https://github.com/yourusername/DermSight.git
cd DermSight

**Install Dependencies:**
pip install -r requirements.txt

Set Up Environment Variables:
Create a .env file in the root directory and add your API keys and other necessary configuration:
GEMINI_PRO_API_KEY=your_api_key_here

### Usage
Run the Application:
python app.py
Fetch Product Details:
Enter the product name or category in the search bar to retrieve real-time reviews and ratings.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For questions or suggestions, please open an issue or contact us at pavi2468kuk@gmail.com

