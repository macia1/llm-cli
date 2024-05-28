import sys
import requests
import os

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ${YOUR_API_KEY}"
}

data = {"messages": [],
        "model": "llama3-70b-8192",
        "temperature": 1,
        "max_tokens": 8192,
        "top_p": 1,
        "stream": False,
        "stop": None
        }


def main(arg):
    while True:
        if arg is not None:
            user_input = ' '.join(arg)
            arg = None
            print("You: " + user_input)
        else:
            user_input = input("You: ")
        if user_input.lower() == "q":
            print("exit.")
            sys.exit(0)
        if user_input.lower() == "cls":
            data['messages'] = []
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if user_input.lower() == 'info':
            print(data)
            continue
        u_q = {"role": "user", "content": user_input}
        data['messages'].append(u_q)
        try:
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data,
                                     proxies={"http": "127.0.0.1:17890", "https": "127.0.0.1:17890"})
            if (response.status_code == 200):
                result = response.json()['choices'][0]['message']['content']
                print(f'Groq:{result}')
                a_a = {"role": "assistant", "content": result}
                data['messages'].append(a_a)
            else:
                print("request fail...")
        except Exception as e:
            print("request exception...")
        finally:
            print()


if __name__ == "__main__":
    arg = None
    if len(sys.argv) > 1:
        arg = sys.argv[1:]
    main(arg)
