import sys
import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ${YOUR_API_KEY}"
}

data = {"messages": [],
        "model": "llama3-70b-8192"}

def main(arg):
    user_input = arg
    while True:
        if user_input is not None:
            print("You: " + user_input)
        else:
            user_input = input("You: ")
        if user_input.lower() == "q":
            print("exit.")
            sys.exit(0)
        u_q = {"role": "user","content": user_input}
        data['messages'].append(u_q)
        try:
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data,proxies=${YOUR_PROXY})
            if(response.status_code == 200):
                result = response.json()['choices'][0]['message']['content']
                print(f'Groq:{result}')
                a_a = {"role": "assistant","content": result}
                data['messages'].append(a_a)
            else:
                print("request fail...")
        except Exception as e:
            print("request exception...")
        finally:
            user_input = None
        

if __name__ == "__main__":
    arg = None
    if len(sys.argv) > 1:
        arg = sys.argv[1:]
    main(arg)
