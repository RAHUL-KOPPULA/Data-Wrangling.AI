# Data Wrangling with AI Integration

A Python command-line tool that allows you to upload datasets and input natural language problem statements to automatically clean and sort your data using AI-powered interpretation.

---

## Features

- Load datasets from local files or URLs (CSV & Excel supported)
- Interactive input for problem statement describing sorting and cleaning
- Leverages OpenAI GPT-4 API to intelligently extract sorting instructions
- Data cleaning: handles null values and fills using mean, median, mode, or fixed value
- Statistical overview: displays null counts, mean, median, standard deviation, variance
- Sort data by multiple columns with ascending/descending order
- Save cleaned and sorted data to CSV for further analysis

---

## Prerequisites

- Python 3.8 or higher
- Install dependencies with:  
- OpenAI API key (sign up at [OpenAI](https://platform.openai.com/account/api-keys))

---

## Setup and Usage

1. Clone the repo:  

2. (Optional) Create virtual environment and activate:  

3. Install requirements:
4. 
4. Set your OpenAI API key:  
- Windows:  
  ```
  setx OPENAI_API_KEY "your_api_key_here"
  ```
- macOS/Linux:  
  ```
  export OPENAI_API_KEY="your_api_key_here"
  ```

5. Run the tool:
6. You will be prompted to enter your problem statement and dataset path or URL.

---

## Statistical Operations

The tool provides a statistical summary of your dataset before and after cleaning:

| Operation           | Description                                   | Example Code                              |
|---------------------|-----------------------------------------------|-------------------------------------------|
| Null Count          | Number of missing values per column           | `df.isnull().sum()`                      |
| Mean (Average)      | Average value of numeric columns               | `df.mean(numeric_only=True)`              |
| Median              | Middle value                                   | `df.median(numeric_only=True)`            |
| Standard Deviation   | Variability of data                            | `df.std(numeric_only=True)`                |
| Variance            | Spread of data (square of std dev)             | `df.var(numeric_only=True)`                |
| Count               | Number of non-null data points                    | `df.count()`                             |

---

## Example Problem Statement

The AI will interpret this instruction and sort your dataset accordingly.

---

## Project Structure

- `main.py` - Entry script integrating data processing and AI
- `requirements.txt` - Dependency list
- `README.md` - Project documentation

---

## License

This project is licensed under the MIT License.

---

## Contact

Created by [Koppula Rahul Babu](rahulrkgs34@gmail.com)  
GitHub: [yourusername]([https://github.com/RAHUL-KOPPULA]) 

---

## Acknowledgments

- OpenAI for GPT API
- Pandas for data handling
- Inspiration from community open-source projects
