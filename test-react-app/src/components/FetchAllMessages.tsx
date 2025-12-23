import { useEffect, useState } from "react";

interface MessageData {
    id: number;
    message: string;
}

const FetchAllMessages: React.FC = () => {
    const [messages, setMessages] = useState<MessageData[]>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/getAllMessages')
        .then((res) => {
            if (!res.ok) throw new Error('Failed to fetch the messages');{
                return res.json();
            }
        })
        .then((data: MessageData[]) => setMessages(data))
        .catch((err) => setError(err.message));
    },[]);

    if (error) return <div style={{ color:'red'}}>Error: {error}</div>

    return (
        <div>
            <h2>All Messages</h2>
            <ul>
                {messages.map((m) => (
                    <li key={m.id}>{m.message}</li>
                ))}
            </ul>
        </div>
    )
}

export default FetchAllMessages; 