# ATG-round-1

## Task information:
- Scrape(Using Beautiful Soup or Selenium) all product details from https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar
- details needed are Product Name, Price, Rating, Seller Name (If not out of stock)
- The program should create a CSV file with the above columns.
- The code should be well commented and optimized, there will be extra marks for that
- Make a short video explaining and running the task in <10mins. Don't need to show long-running codes.
- Upload your code to a GitHub public repository (tutorial:https://www.youtube.com/watch?v=eGaImwD8fPQ&ab_channel=VedTheMaster)
- Submit the video and the GitHub link for the same in the submission form

## Setup
Simply install the required libraries.
```bash
pip install -r requirements.txt
```
Maintaining a virtual environment is recommended.

## Running The Code
To run the code simply run the following.
```bash
python main.py
```
Once the output is ready, it will be stored in `out/`.

Bonus: Modularity.  
If you have a valid link of listings, you may also link them.
```
python main.py -l <URL>
```

## Methodology
1. Analysis of required data.
2. Building a basic pipeline for scraping.
3. Testing if the current scraping pipeline works (see [scrape.ipynb](scrape.ipynb)).
4. Application of the pipeline (see [scrape.py](scrape.py)).
5. Deployment.