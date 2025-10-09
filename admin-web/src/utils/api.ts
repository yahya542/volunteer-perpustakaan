// API client using native fetch
const API_BASE_URL = 'http://localhost:8000/api'; // Adjust to your Django API URL

export const apiRequest = async (endpoint: string, options: RequestInit = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  const config: RequestInit = {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  };

  try {
    const response = await fetch(url, config);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
};

// Example usage:
// apiRequest('/users/').then(data => console.log(data));