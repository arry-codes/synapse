import requests
from config import Config

def test_huggingface_api():
    """Test if Hugging Face API is working correctly"""
    
    # Your API details from config
    API_URL = Config.HUGGING_FACE_API_URL
    API_TOKEN = Config.HUGGING_FACE_TOKEN
    
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    # Simple test prompt
    test_prompt = "Hello, how are you?"
    
    try:
        print(f"Testing Hugging Face API connection to: {API_URL}")
        print(f"Using token: {API_TOKEN[:10]}...{API_TOKEN[-10:]}")
        print("-" * 50)
        
        payload = {
            "inputs": test_prompt,
            "parameters": {
                "max_new_tokens": 50,
                "temperature": 0.7
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Connection Successful!")
            print(f"Response: {result}")
            
            if isinstance(result, list) and len(result) > 0:
                if 'generated_text' in result[0]:
                    print(f"Generated Text: {result[0]['generated_text']}")
                else:
                    print(f"Full Response: {result[0]}")
            else:
                print(f"Full Response: {result}")
                
        elif response.status_code == 503:
            print("❌ Model is loading. Please wait and try again in a few minutes.")
            print("This is normal for models that aren't frequently used.")
            
        elif response.status_code == 401:
            print("❌ Authentication failed. Please check your API token.")
            
        elif response.status_code == 404:
            print("❌ Model not found. Please check the model URL.")
            
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The API might be overloaded.")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    test_huggingface_api()