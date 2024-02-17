import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from nltk.chat.util import Chat, reflections

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.configure(background='#FFC0CB')  # Set background color to pink

        self.chatbot = Chat(self.get_chatbot_responses(), reflections)

        self.chat_label = tk.Label(root, text="Chatbot:", background='#FFC0CB', font=('Arial', 14))
        self.chat_label.pack(pady=10)

        self.chat_history = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
        self.chat_history.pack(padx=10, pady=5)

        self.user_label = tk.Label(root, text="You:", background='#FFC0CB', font=('Arial', 14))
        self.user_label.pack(pady=5)

        self.user_input = tk.Entry(root, width=40)
        self.user_input.pack(padx=10, pady=5)

        self.send_button = tk.Button(root, text="Send", command=self.send_message, background='white')
        self.send_button.pack(padx=10, pady=10)

        # Focus the user input field when the app starts
        self.user_input.focus_set()

    def get_chatbot_responses(self):
        # Define patterns and responses for the chatbot
        patterns = [
            (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
            (r'how are you?', ["I'm doing well, thank you!", "I'm good, thanks for asking!"]),
            (r'what is your name?', ["I'm a chatbot.", "You can call me Chatbot."]),
            (r'quit', ['Bye!', 'Goodbye!', 'Take care!']),
            (r'(.*)', ["Sorry, I didn't understand that.", "Can you please repeat?"])
        ]
        return patterns

    def send_message(self):
        user_input_text = self.user_input.get()
        if user_input_text.strip() == "":
            messagebox.showerror("Error", "Please enter a message.")
            return
        self.user_input.delete(0, tk.END)
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, f"You: {user_input_text}\n")
        self.chat_history.see(tk.END)
        response = self.chatbot.respond(user_input_text)
        self.chat_history.insert(tk.END, f"Chatbot: {response}\n")
        self.chat_history.see(tk.END)
        self.chat_history.configure(state='disabled')

root = tk.Tk()
app = ChatbotApp(root)
root.mainloop()
