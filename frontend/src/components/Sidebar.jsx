import { Trash2, Pencil } from "lucide-react";

import {
    deleteConversation,
    renameConversation
} from "../services/conversation";

export default function Sidebar({

    conversations,

    newChat,

    currentConversation,

    setCurrentConversation,

    loadConversations

}) {

    async function removeChat(id) {

        if (!window.confirm("Delete this conversation?"))
            return;

        await deleteConversation(id);

        loadConversations();

    }

    async function renameChat(chat) {

        const title = chat.title + " (Edited)";

        await renameConversation(

            chat.id,

            title

        );

        loadConversations();

    }

    return (

        <div className="w-72 bg-[#020617] border-r border-slate-800 p-5">

            <button

                onClick={newChat}

                className="w-full rounded-lg bg-blue-600 py-3 font-semibold hover:bg-blue-700"

            >

                + New Chat

            </button>

            <div className="mt-8">

                <h3 className="text-gray-400 mb-4">

                    Recent Chats

                </h3>

                <div className="space-y-2">

                    {

                        conversations.map((chat) => (

                            <div

                                key={chat.id}

                                className={`

                                flex

                                justify-between

                                items-center

                                rounded

                                p-3

                                cursor-pointer

                                hover:bg-slate-700

                                ${

                                    currentConversation?.id === chat.id

                                        ? "bg-slate-700"

                                        : "bg-slate-800"

                                }

                                `}

                            >

                                <span

                                    className="flex-1"

                                    onClick={() => setCurrentConversation(chat)}

                                >

                                    {chat.title}

                                </span>

                                <div className="flex gap-2">

                                    <Pencil

                                        size={18}

                                        className="text-blue-400 hover:text-blue-600"

                                        onClick={(e) => {

                                            e.stopPropagation();

                                            renameChat(chat);

                                        }}

                                    />

                                    <Trash2

                                        size={18}

                                        className="text-red-400 hover:text-red-600"

                                        onClick={(e) => {

                                            e.stopPropagation();

                                            removeChat(chat.id);

                                        }}

                                    />

                                </div>

                            </div>

                        ))

                    }

                </div>

            </div>

        </div>

    );

}