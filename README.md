## OverTrick

OverTrick is a web application to display and analyse club 
[Duplicate Bridge](https://cdn.acbl.org/wp-content/uploads/2014/01/Laws-of-Duplicate-Bridge.pdf)
pairs results. It is intended to be a demonstration of development skill rather
 than something that would necessarily be used in the field.  
 
The data is currently gleaned from the [BridgeNZ](https://bridgenz.co.nz) websiste, which 
collates results data from clubs across New Zealand. Individual pages are scraped
at intervals using Celery and Redis, in order to avoid swamping the website servers. 

I don't have extensive knowledge of Bridge, so the application may not reflect exact play.


## Roadmap

- [ ] results scraping and display
- [ ] unit testing  
- [ ] data analysis and charting
- [ ] member accounts and subscriptions
- [ ] ladders and tournaments
- [ ] partner requires
- [ ] deployment to AWS
- [ ] periodic scraping