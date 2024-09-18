const API_URL = 'http://127.0.0.1:8000';

export const getVisitors = async () => {
    const result = await fetch(`${API_URL}/report/visits`, {
        cache: 'no-store',
    });
    return await result.json();
}
