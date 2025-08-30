import { GraphData, ExecutionTrace } from '../types';

const LOCAL_SERVER_URL = 'http://127.0.0.1:5001/api/generate_graph';

export const generateGraphFromCode = async (code: string): Promise<{ graph: GraphData; trace: ExecutionTrace; }> => {
  try {
    const response = await fetch(LOCAL_SERVER_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code }),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ error: 'Server returned an invalid error response.' }));
      throw new Error(errorData.error || `Server error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();

    if (!data.graph || !data.trace) {
      throw new Error('Invalid data structure received from the local server.');
    }

    return {
      graph: data.graph,
      trace: data.trace,
    };

  } catch (error) {
    console.error("Error calling local processing server:", error);
    if (error instanceof Error) {
        // Provide a user-friendly message
        if (error.message.includes('Failed to fetch')) {
            throw new Error('Could not connect to the local Python server. Is it running?');
        }
        throw new Error(error.message);
    }
    throw new Error('An unknown error occurred while communicating with the local server.');
  }
};