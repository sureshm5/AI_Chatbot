import { useEffect, useRef } from "react";

import MessageBubble from "./MessageBubble";

export default function ChatWindow({ messages }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({

            behavior: "smooth"

        });

    }, [messages]);

    return (

        <div className="flex-1 overflow-y-auto p-8">

            <div className="max-w-4xl mx-auto">

                {

                    messages.length === 0 ?

                    <div className="text-center mt-40">

                        <h1 className="text-5xl font-bold">

                            Hello 👋

                        </h1>

                        <p className="mt-4 text-gray-400">

                            Ask me anything...

                        </p>

                    </div>

                    :

                    messages.map((msg, index) => (

                        <MessageBubble

                            key={index}

                            message={msg}

                        />

                    ))

                }

                <div ref={bottomRef}></div>

            </div>

        </div>

    );

}