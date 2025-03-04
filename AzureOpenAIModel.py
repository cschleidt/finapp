import os
import json  
from openai import AzureOpenAI  

class AzureOpenAIModel:
    def __init__(self, system_prompt, temperature=0, stop=None):

        self.endpoint = os.getenv("ENDPOINT_URL", "https://oai-jbtest.openai.azure.com/")
        self.deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")  
        self.subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "5674bc2f361c47f2a9e61158254c0640")  
        self.api_version="2024-05-01-preview"

        self.system_prompt = system_prompt
        self.temperature = temperature
        self.stop = stop

    def generate_text(self, prompt):

        # Initialize Azure OpenAI Service client with key-based authentication    
        client = AzureOpenAI(  
            azure_endpoint=self.endpoint,  
            api_key=self.subscription_key,  
            api_version=self.api_version,
        )
    
        #Prepare the chat prompt 
        chat_prompt = [
        {
                "role": "system",
                "content": self.system_prompt
                #"content": "Retrieve financial key figures from the past 5 years for a specific public company.\n\nThe key figures to include are:  \n- Revenue  \n- Net Income  \n- Earnings Per Share (EPS)  \n- Total Assets  \n- Total Liabilities  \n\nIf possible, provide the data for each of the last 5 fiscal years. If data is missing for a specific year, note it clearly in the output.\n\n# Steps\n\n1. Identify the public company based on the name provided in the input.  \n2. Gather key financial figures (Revenue, Net Income, EPS, Total Assets, Total Liabilities) for the past 5 fiscal years.  \n3. If a figure is unavailable for a specific year, replace it with \"Unavailable\" and mark it explicitly.  \n4. Format the data in a clear, structured table or JSON format for easy readability.  \n\n# Output Format\n\nThe output should include financial data in JSON format as follows:\n\n```json\n{\n  \"company\": \"Company Name\",\n  \"financials\": [\n    {\n      \"year\": 2022,\n      \"revenue\": \"Value or Unavailable\",\n      \"net_income\": \"Value or Unavailable\",\n      \"EPS\": \"Value or Unavailable\",\n      \"total_assets\": \"Value or Unavailable\",\n      \"total_liabilities\": \"Value or Unavailable\"\n    },\n    {\n      \"year\": 2021,\n      \"revenue\": \"Value or Unavailable\",\n      \"net_income\": \"Value or Unavailable\",\n      \"EPS\": \"Value or Unavailable\",\n      \"total_assets\": \"Value or Unavailable\",\n      \"total_liabilities\": \"Value or Unavailable\"\n    },\n    ...\n  ]\n}\n```\n\n# Example\n\n### Input\n\"Retrieve the financial key figures for Apple Inc.\"\n\n### Output\n```json\n{\n  \"company\": \"Apple Inc.\",\n  \"financials\": [\n    {\n      \"year\": 2022,\n      \"revenue\": \"394B\",\n      \"net_income\": \"99.8B\",\n      \"EPS\": \"6.15\",\n      \"total_assets\": \"381B\",\n      \"total_liabilities\": \"283B\"\n    },\n    {\n      \"year\": 2021,\n      \"revenue\": \"366B\",\n      \"net_income\": \"94.6B\",\n      \"EPS\": \"5.61\",\n      \"total_assets\": \"351B\",\n      \"total_liabilities\": \"267B\"\n    },\n    {\n      \"year\": 2020,\n      \"revenue\": \"274B\",\n      \"net_income\": \"57.4B\",\n      \"EPS\": \"3.28\",\n      \"total_assets\": \"323B\",\n      \"total_liabilities\": \"258B\"\n    },\n    {\n      \"year\": 2019,\n      \"revenue\": \"260B\",\n      \"net_income\": \"55.3B\",\n      \"EPS\": \"2.97\",\n      \"total_assets\": \"338B\",\n      \"total_liabilities\": \"248B\"\n    },\n    {\n      \"year\": 2018,\n      \"revenue\": \"265B\",\n      \"net_income\": \"59.5B\",\n      \"EPS\": \"3.00\",\n      \"total_assets\": \"365B\",\n      \"total_liabilities\": \"258B\"\n    }\n  ]\n}\n```\n\n# Notes\n\n- Ensure the financial data is accurate and credible, ideally sourced from official company reports or reliable financial databases.  \n- Handle edge cases where data might be incomplete, unavailable, or formatted differently. Provide appropriate fallback text (e.g., \"Unavailable\") in such cases.  \n- Do not fabricate data; ensure it reflects real-world accuracy or clearly state if the data cannot be provided.  "
            },
            {
                "role": "user",
                "content": prompt
            }] 
    
        messages = chat_prompt  
    
            # Generate the completion  
        completion = client.chat.completions.create(  
            model=self.deployment,
            messages=messages,
            max_tokens=800,  
            temperature=0.7,  
            top_p=0.95,  
            frequency_penalty=0,  
            presence_penalty=0,
            stop=None,  
            stream=False
        )

        response = completion.choices[0].message.content
        response_dict = json.loads(response)

        print(f"\n\nResponse from Ollama model: {response_dict}")

        return response_dict

        #print(completion.to_json()) 
        #return completion.response.choices[0].message.content