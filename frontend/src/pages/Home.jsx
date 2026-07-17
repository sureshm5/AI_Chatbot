import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import {

    createConversation,

    getConversations,

    getMessages

} from "../services/conversation";

export default function Home() {

    const [messages, setMessages] = useState([]);

    const [conversations, setConversations] = useState([]);

    const [currentConversation, setCurrentConversation] = useState(null);

    useEffect(() => {
        loadConversations();
    }, []);

    async function loadConversations() {

        const data = await getConversations();

        setConversations(data);

        if (data.length > 0) {
            setCurrentConversation(data[0]);

            loadMessages(data[0]);
        }

    }

    async function loadMessages(conversation){

        const data = await getMessages(
            conversation.id
        );

        const formatted = data.map(msg => ({

            role: msg.role,

            content: msg.content

        }));

        setMessages(formatted);

    }

    async function newChat() {

        const convo = await createConversation();

        setCurrentConversation(convo);

        setMessages([]);

        await loadConversations();

    }

    return (

        <div className="flex h-screen bg-[#0f172a] text-white">

            <Sidebar
                conversations={conversations}
                newChat={newChat}
                currentConversation={currentConversation}
                loadConversations={loadConversations}
                setCurrentConversation={(chat)=>{

                    setCurrentConversation(chat);

                    loadMessages(chat);

                }}
            />

            <div className="flex flex-col flex-1">

                <Header/>

                <ChatWindow
                    messages={messages}
                />

                <ChatInput
                    messages={messages}
                    setMessages={setMessages}
                    conversation={currentConversation}
                />

            </div>

        </div>

    );

}   