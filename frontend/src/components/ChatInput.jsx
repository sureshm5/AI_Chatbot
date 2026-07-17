import { useState } from "react";
import { SendHorizontal } from "lucide-react";

import { sendMessage } from "../services/conversation";

export default function ChatInput({

    messages,

    setMessages,

    conversation

}) {

    const [input, setInput] = useState("");

    async function send() {

        if (!input.trim()) return;

        if (!conversation) {

            alert("Create a new chat first.");

            return;

        }

        const userMessage = {

            role: "user",

            content: input

        };

        setMessages(prev => [...prev, userMessage]);

        const question = input;

        setInput("");

        try {

            const response = await sendMessage(

                conversation.id,

                question

            );

            const ai = {

                role: "assistant",

                content: response.response

            };

            setMessages(prev => [...prev, ai]);

        }

        catch (err) {

            console.log(err);

            alert("Backend Error");

        }

    }

    return (

        <div className="border-t border-slate-700 p-5">

            <div className="max-w-4xl mx-auto flex">

                <textarea

                    rows={2}

                    value={input}

                    onChange={(e) => setInput(e.target.value)}

                    className="flex-1 rounded-xl bg-slate-800 p-4 resize-none outline-none"

                    placeholder="Message AI..."

                />

                <button

                    onClick={send}

                    className="ml-3 rounded-xl bg-blue-600 px-5"

                >

                    <SendHorizontal />

                </button>

            </div>

        </div>

    );

}