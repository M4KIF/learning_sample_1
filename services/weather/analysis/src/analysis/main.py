#from langchain_community.llms.ollama import Ollama  
from langchain.llms.ollama import Ollama
import httpx 
import asyncio
import trio

def main():
    llm = Ollama(model="deepseek-r1:1.5b")  

    print("Sending a request to the weatherApi")

    town = "Warsaw"

    request = httpx.get("http://api.weatherapi.com/v1/current.json", params={"key": "37e09d488a00412f956180840250305", "q": town})
    if request.status_code > 300:
        print(f"Text: {request.text} and status: {request.status_code}")
        return

    print(f"Received response from the weather api '{request.text}'")

    # internet_connection_proof = llm.invoke("cite me the headline of the newest article from www.purepc.pl")
    # print(internet_connection_proof)

    # Potential weather analysis utilizing the llm

    weather_analysis_template = '{"city":"response_variable_1", "temp_range[C]":"response_variable_2", "text_description":"response_variable_3", "automotive_conditions_description": "response_variable_4", "can_i_put_a_mini_skirt_on?", "response_variable_5", "severe_weather_alerts":"response_variable_6"}'

    weather_analysis = llm.invoke(f"Please analyse the weather for {town} utilizing historical data and provided dataset: '{request.text}' and give response in exact format as follows: '{weather_analysis_template}'")
        
    print(weather_analysis)  

    # Trio

    # Asyncio

if __name__ == "__main__":
    main()