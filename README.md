# Querying-and-forecasting-with-Natural-Language

The project has the potential to democratize access to insights using natural language. Users will now be empowered to ask questions about their data directly using free form text and will be given real-time answers in the form of charts and visuals. With this solution, data analysts can focus on automating ETL pipelines and other innovative data modeling tasks rather than responding to every new question from the end-user. Also, this solution has a plethora of use cases but most notably, this solution can be used to replace the Frequently Asked Questions (FAQ) sections of most apps today.

This project will leverage the models from this https://arxiv.org/pdf/1909.00786.pdf paper to develop a text-to-SQL dashboard application for users. The SparC dataset would be used to train our model. The SParC dataset is a multi-domain or multi-context dataset that contains over 200 databases from over 100 different domains. The dataset can be downloaded from the official page of the challenge https://yale-lily.github.io/sparc. 

This project will also go the extra mile of enabling users to generate forecasts on their data which would be the key differentiator from other implementations seen in the industry and academia. In addition, an interactive web application dashboard would be developed based on the custom data where users can query to generate insights. The following Dataset https://www.kaggle.com/roopahegde/cryptocurrency-timeseries-2020 would be used to tune the text-to-SQL model and to develop the time-series forecasting model. 


Finally, The notebook and Python files provided here, once completed, result in a simple web app dashboard which interacts with a deployed text-to-SQL model generating queries from user's questions typed in English, and visualizes the answers. The dashboard can also forecast based on user's questions.
