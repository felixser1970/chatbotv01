import os
from dotenv import load_dotenv

# Add Azure OpenAI package
from openai import AzureOpenAI


def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Initialize the Azure OpenAI client...
        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
                azure_endpoint = azure_oai_endpoint, 
                api_key=azure_oai_key,  
                api_version="2024-02-15-preview"
                )
    
        # Create a system message
        system_message = """Resultados de la euroliga de Baloncesto. Equipos participantes
            """
        


        while True:
            # Get input text
            input_text = input("Introduzca pregunta ( 'quit' para salir): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Introduzca una pregunta.")
                continue

            print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            
            # Add code to send request...
            response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.7,
            max_tokens=400,
            messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": input_text}
                     ]
            )
            generated_text = response.choices[0].message.content

            # Print the response
            print("Response: " + generated_text + "\n")
            
            
            

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()