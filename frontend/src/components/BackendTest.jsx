import { useState } from "react";
import {
  getHealth,
  getConversations,
  sendMessage,
} from "../services/api";

function BackendTest() {
  const [health, setHealth] = useState(null);
  const [conversations, setConversations] = useState([]);
  const [chatResponse, setChatResponse] = useState(null);
  const [error, setError] = useState(null);

  const testHealth = async () => {
    try {
      setError(null);

      const data = await getHealth();

      setHealth(data);
    } catch (err) {
      setError(err.message);
    }
  };

  const testConversations = async () => {
    try {
      setError(null);

      const data = await getConversations();

      setConversations(data);
    } catch (err) {
      setError(err.message);
    }
  };

  const testChat = async () => {
    try {
      setError(null);
      setChatResponse(null);

      const data = await sendMessage(
        "Hello. Introduce yourself as my AI Business Operations Copilot."
      );

      setChatResponse(data);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h2>FastAPI Integration Test</h2>

      {/* Health Test */}
      <button onClick={testHealth}>
        Test Health
      </button>

      {/* Conversations Test */}
      <button onClick={testConversations}>
        Load Conversations
      </button>

      {/* Chat Test */}
      <button onClick={testChat}>
        Test Chat
      </button>

      {/* Health Response */}
      {health && (
        <div>
          <h3>Health Response</h3>

          <pre>
            {JSON.stringify(health, null, 2)}
          </pre>
        </div>
      )}

      {/* Conversations Response */}
      {conversations.length > 0 && (
        <div>
          <h3>Conversations</h3>

          <pre>
            {JSON.stringify(
              conversations,
              null,
              2
            )}
          </pre>
        </div>
      )}

      {/* Chat Response */}
      {chatResponse && (
        <div>
          <h3>Chat Response</h3>

          <pre>
            {JSON.stringify(
              chatResponse,
              null,
              2
            )}
          </pre>
        </div>
      )}

      {/* Error */}
      {error && (
        <div>
          <h3>Error</h3>

          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default BackendTest;