# Japanese-Reconditioned-Car-Listings-Analysis-

The goal of this project is to gather information and insights on depreciation and market trends of Japanese reconditioned cars based on data available as of September 2025. We utilized the scraped data to understand the following aspects and correlations using the provided dashboards.

**Dashboard 1: Market Snapshot: Japanese Reconditioned Cars (Sep 2025)**  
1. Japanese listings based on different brands and models.  
2. Most popular brands and models based on listing frequency.  
3. Which years of reconditioned cars dominate the listings.  
4. Fuel type price premium. 
 

**Dashboard 2: Price and Value Trends: Japanese Reconditioned Cars (Sep 2025)**  
1. Identification of trends in pricing based on vehicle age and condition.  
2. Analysis of price-to-mileage ratios to assess value for money.  
3. How quickly car prices drop as cars age.  
4. Top value models by price-to-features ratio.  
5. Price comparison across various models and grades.  

**Dashboard 3: Advanced Analysis: Depreciation and Niche Trends (Sep 2025)**  
1. A chart of models with lower depreciation over age.  
2. A scatter plot of models with unusually high prices based on median mileage.  
3. The impact of engine capacity on depreciation.  
4. The effect of color premium on price by age. 



**You can visit the public dashboards here:**

Tableau public view : https://public.tableau.com/app/profile/taiob.md.ridwan/viz/Book1_17553251098180/MarketSnapshotJapaneseReconditionedCarsSep2025?publish=yes



**Findings and Observations from the Dashboards**

**Dashboard 1: Market Snapshot: Japanese Reconditioned Cars (Sep 2025)**  
1. Listings are dominated by a variety of brands, with Toyota, Honda, and Nissan leading the counts.  
2. Toyota emerges as the most popular brand, followed by Honda, based on listing frequency.  
3. Reconditioned cars from the years 2019-2021 dominate the current listings.  
4. Hybrid and octane fuel types show a noticeable price premium compared to other fuel types.
  

**Dashboard 2: Price and Value Trends: Japanese Reconditioned Cars (Sep 2025)**  
1. Pricing trends reveal a strong correlation with vehicle age and condition, with newer and well-conditioned cars retaining higher values.  
2. Price-to-mileage ratios suggest better value for money in cars with moderate mileage.  
3. Car prices drop most sharply within the first few years of age.  
4. Top value models are identified based on an optimal price-to-features ratio.  
5. Price variations are notable across different models and grades, with some grades commanding higher prices.  

**Dashboard 3: Advanced Analysis: Depreciation and Niche Trends (Sep 2025)**  
1. Certain models exhibit lower depreciation rates over age, as shown in the chart.  
2. Some models show unusually high prices despite higher median mileage, indicated by the scatter plot.  
3. Larger engine capacities tend to have a more significant impact on depreciation rates.  
4. Color premiums appear to influence price more significantly in younger vehicles.

Build From Sources
1.Clone the repo
```bash
git clone https://github.com/tmridwan/Japanese-Reconditioned-Car-Listings-Analysis-.git
```
2. Initialize and activate virtual env
```bash
virtualenv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download the chromedriver from: https://developer.chrome.com/docs/chromedriver/downloads

5. Check the Scraped data: https://github.com/tmridwan/Japanese-Reconditioned-Car-Listings-Analysis-/blob/main/car-import/gari_import.csv

![Market Snapshot](https://github.com/user-attachments/assets/0489f2f9-012c-4b0b-bd51-5cebae733449)
![price and values](https://github.com/user-attachments/assets/68e2649d-8d3c-4f1f-aed5-c9c4dd909ef1)
![Advance analysis](https://github.com/user-attachments/assets/d6a4d63a-4a37-4e81-983e-00e65b93fd2d)
