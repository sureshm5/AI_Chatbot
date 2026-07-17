import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

export default function MessageBubble({ message }) {

    const isUser = message.role === "user";

    return (

        <div
            className={`flex mb-6 ${
                isUser ? "justify-end" : "justify-start"
            }`}
        >

            <div
                className={`max-w-3xl rounded-2xl p-4 whitespace-pre-wrap ${
                    isUser
                        ? "bg-blue-600 text-white"
                        : "bg-slate-800 text-gray-100"
                }`}
            >

                <ReactMarkdown

                    remarkPlugins={[remarkGfm]}

                    components={{

                        code({ inline, className, children, ...props }) {

                            const match = /language-(\w+)/.exec(className || "");

                            return !inline && match ? (

                                <SyntaxHighlighter

                                    style={oneDark}

                                    language={match[1]}

                                    PreTag="div"

                                    {...props}

                                >

                                    {String(children).replace(/\n$/, "")}

                                </SyntaxHighlighter>

                            ) : (

                                <code
                                    className="bg-slate-900 px-1 py-0.5 rounded"
                                    {...props}
                                >

                                    {children}

                                </code>

                            );

                        }

                    }}

                >

                    {message.content}

                </ReactMarkdown>

            </div>

        </div>

    );

}