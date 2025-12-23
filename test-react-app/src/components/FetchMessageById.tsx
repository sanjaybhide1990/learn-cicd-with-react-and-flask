import { useState } from "react";

interface MessageData {
    id: number;
    message: string;
}

const FetchMessageById: React.FC = () => {
    const [id, setId] = useState<string>('');
    const [result, setResult] = useState<MessageData | null>(null);
    const [error, setError] = useState<string | null>(null);

    const handleFetch = () => {
        setError(null);
        setResult(null);

        fetch(`http://127.0.0.1:5000/getMessage/${id}`)
        .then((res) => {
            if (!res.ok) throw new Error('Message not found');
            return res.json();
        })
        .then((data: MessageData) => setResult(data))
        .catch((err) => setError(err.message));
    }

    return(
        <div style={{marginTop: '20px',padding: '10px', border: '1px solid #ccc'}}>
            <h2>Search Message by ID</h2>
            <input 
                type="number" 
                value={id} 
                onChange={(e) => setId(e.target.value)}
                placeholder="Enter ID"
            />
            <button onClick={handleFetch}>Display Message</button>
            {error && <p style={{ color: 'red'}}>{error}</p>}

            {result && (
                <div style={{ marginTop: '10px', fontWeight: 'bold'}}>
                    ID: {result.id} | Message: {result.message}
                </div>
            )}
        </div>
    );
};

export default FetchMessageById;