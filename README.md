# Immoscrape

The script helps you scraping results from Immobilienscout24.de, the biggest real-estate website in Germany. Basically, it crawls the results of several source pages and export them to a .csv file.


## Project Status

The script was part of a larger, personal project: I needed to scrape the website to pass the results to a target system (SFDC) via a Talend interface. Currently (November 2019) the script works like a charm. I will not maintain the code over time though. Should Immobilienscout24 change the HTML structure, the script will need to be updated accordingly. Feel free to step in as a maintainer.


## Description

By default, when running the script, the results of the following page will be captured:

```bash
https://www.immobilienscout24.de/Suche/S-2/P-1/Wohnung-Kauf/Fahrzeitsuche/Berlin/-/229458/2511138/-/1276003001/60/-/-/EURO--150000,00
```
The listed properties are:
- Apartments on sale ("Kaufen", "Wohnung")
- Located in the Berlin area ("Berlin")
- Within 1 hour distance from the city ("60 min")
- With a price lower than 150.000,00 Euro ("bis 150.000 €")
- Properties are listed from the newest published to the oldest

The initial criteria can be changed. All you have to do is:
1) Apply your own criteria to the search in Immobilienscout24
2) Copy the URL with the results of your search 
3) Replace the "source" in the script with your own URL 

Pay attention to the paging or it will return the results of the first page only!

For each property you are going to store in the .csv file the following information:

- ID of the ad (for later reference; I have also included this to prevent the creation of duplicates in the target system)
- Address (the level of details of this information change from ad to ad)
- Price ("Kaufpreis")
- Square meters ("Wohnfläche")
- Number of rooms ("Zimmer")
- Distance from the city
- Link to the ad (it uses the above mentioned ID)


## Final comments
Please keep in mind I am new to Python and I do not work as a programmer: I am pretty sure it would have been possible to write a better code... But, hey, in the end mine works too and that's what really counts! :-D


## License

[MIT](https://choosealicense.com/licenses/mit/)
