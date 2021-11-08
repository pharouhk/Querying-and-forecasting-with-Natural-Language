# Querying-and-forecasting-with-Natural-Language

The project has the potential to democratize access to insights using natural language. Users will now be empowered to ask questions about their data directly using free form text and will be given real-time answers in the form of charts and visuals. With this solution, data analysts can focus on automating ETL pipelines and other innovative data modeling tasks rather than responding to every new question from the end-user. Also, this solution has a plethora of use cases but most notably, this solution can be used to replace the Frequently Asked Questions (FAQ) sections of most apps today.

This project will leverage the pre-trained model from  https://huggingface.co/mrm8488/t5-base-finetuned-wikiSQL  to develop a text-to-SQL dashboard application for users.This project will also go the extra mile of enabling users to generate forecasts on their data which would be the key differentiator from other implementations seen in the industry and academia. In addition, an interactive web application dashboard would be developed based on the custom data where users can query to generate insights. The following Dataset https://www.kaggle.com/roopahegde/cryptocurrency-timeseries-2020 would be used to tune the text-to-SQL model and to develop the time-series forecasting model. 


Finally, The notebook and Python files provided here, once completed, result in a simple web app dashboard which interacts with a deployed text-to-SQL model generating queries from user's questions typed in English, and visualizes the answers. The dashboard can also forecast based on user's questions.

Note:
Screenshots from the web app are the images named:
1. Result_forecast_query(1),2,3
2. Result_query(1),2,3

In addition the capstone proposal and project report are the following files named:
1. Proposal.pdf
2. Project Report.pdf
