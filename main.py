from scrape import scrape
import sys

TASK_LINK = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

data = []

# check if CLI arguments has `-l <link>`
# - 1 because `-l` can't be the last arg
for i in range(len(sys.argv) - 1):
    if sys.argv[i] == "-l":
        data = scrape(sys.argv[i])
else:
    data = scrape(TASK_LINK)

print(data)

# convert the data to CSV

"""
NOTE:
After some reverse engineering (for the lack of a better term) I've observed this:
The given link is equivalent to
`https://www.amazon.in/s?&rh=n%3A6612025031&fs=true&qid=1701960523`
So in theory you can replace this link with something else by:
    1. Selecting a category from the search bar.
    2. Hitting enter and selecting a sub-category recursively (if any).
    3. Select bestselling.
The link should be or have elements like this for example (link for tablets):
`https://www.amazon.in/s?bbn=976420031&rh=n%3A976419031%2Cn%3A1375458031&qid=1701961716`
This does *not* always work, sadly.
"""
