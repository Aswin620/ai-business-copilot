const API_BASE_URL = "http://127.0.0.1:8000";

export async function getHealth() {
    const response = await fetch(
        `${API_BASE_URL}/health`
    );

    if (!response.ok) {
        throw new Error("Health check failed");
    }

    return response.json();
}

export async function getConversations() {
    const response = await fetch(
        `${API_BASE_URL}/api/v1/conversations`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch conversations");
    }

    return response.json();
}

export async function sendMessage(message) {
    const response = await fetch(
        `${API_BASE_URL}/api/v1/chat`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: message,
            }),
        }
    );

    if (!response.ok) {
        throw new Error("Failed to send message");
    }

    return response.json();
}