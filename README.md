# Artstation Artwork Analysis

## Content
100.000 artwork links (just links) which are equivalent to ~30 days time period from the day that links were gathered.
There're 50.000 artworks that were scraped and contain data, ~40.000+ unique (*artwork from the same artist*).
 
Dataset includes such columns:
- Role
- Company work at (if mentioned or extracted)
- Date artwork was posted
- Number of views
- Number of likes
- Number of comments
- Which software was used
- Which tags were used
- Artwork title
- Artwork URL

Kaggle dataset available [here](https://www.kaggle.com/dimitryzub/artstation).

As you see the disclaimer, it's the first time I'm doing this. I want anyone who will be using this dataset to keep artists privacy by **not** using **artist's email addresses** in any way even though it's publicly available data published by them. Correct me if I said something wrong here.

### Goals

The goal of this project was to better understand the process of gathering data, processing, cleaning, analyzing, and visualizing. 
Besides that, I wanted to understand what is the most popular software, tag, affiliation among artists.

### Inspiration

While transitioning from 3D modeling to Data Analytics and Python Programming I decided to create a personal project to analyze something I have a close connection with. I really enjoyed seeing progression in the 3D world (games, feature films, etc).

### To scrape data these Python libraries/packages were used:
- `requests`
- `json`
- `googlesheets api`
- `selenium`
- `regex`

### To clean, analyze and visualize data:
- `googlesheets`
- `tableau`

## Visualization 

Note: *following visualizations contains data bias. Not every tag, affiliation has taken to count due to the difficulties of data extraction, and the mistakes I made.*
[Tableau public dashboard](https://public.tableau.com/app/profile/dimitry.zub/viz/Artstationanalysis/ArtstationDashboard)

![image](https://user-images.githubusercontent.com/78694043/119978304-23cb0380-bfc2-11eb-8b70-e84100fa7630.png)

![image](https://user-images.githubusercontent.com/78694043/119978269-1ada3200-bfc2-11eb-981f-b8ad2c2c0ff1.png)

![image](https://user-images.githubusercontent.com/78694043/119978237-101f9d00-bfc2-11eb-9285-e0d9bcf688ee.png)
