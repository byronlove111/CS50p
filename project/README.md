# 📚 Books to Scrape Web Scraper

## 🎥 Video Demo
**https://youtu.be/ivSUDHwBkzs**

## 📝 Description
This project is a **Python web scraper** that automatically extracts book titles from the [Books to Scrape](https://books.toscrape.com) website. The main goal is to demonstrate practical web scraping using Python with the **requests** and **BeautifulSoup4** libraries.

## ✨ Features
The scraper includes the following features:
- Automatic extraction of book titles from all catalog pages
- Connection error handling
- Saving extracted titles to a text file
- Unit tests to validate core functionality

## 📁 Project Structure
The project consists of three main files:

### 1. **project.py**
Contains the core scraper code with three essential functions:
- **`get_page_content()`**: Retrieves HTML content from a webpage
- **`extract_titles()`**: Extracts book titles from HTML content
- **`main()`**: Coordinates the scraping process and data saving

### 2. **test_project.py**
Contains unit tests that verify:
- Correct page content retrieval
- Error handling for invalid URLs
- Proper title extraction from test HTML

### 3. **titles.txt**
Output file that stores all extracted book titles, one per line.

## 🛠️ Technical Choices
- **Requests**: Chosen for its simplicity and reliability in handling HTTP requests.
- **BeautifulSoup4**: Selected for its intuitive HTML parsing API and robustness.
- **Error Handling**: Implemented defensively to prevent program crashes due to network issues or target site changes.
- **Data Storage**: Text file storage was chosen for simplicity and portability, although a database might be more appropriate for a larger-scale project.

## 🚀 Installation and Usage
```bash
pip install -r requirements.txt
```
```bash
python project.py
```
```bash
pytest test_project.py
```
## 🔮 Future Improvements
- **Add a command-line interface** for customizable scraping
- **Extract additional information** (e.g., prices, availability)
- **Implement database storage** for better scalability
- **Add a more detailed logging system** for better debugging and monitoring
- **Implement request delays** to respect site policies and avoid being blocked

## 🤝 Contributing
Contributions are welcome! Feel free to open an **issue** or submit a **pull request**.

## 📄 License
This project is licensed under the **MIT License** - see the **LICENSE** file for details.
