const API_URL = 'http://swarm.dfcubidesc.com:8000';

export const getVisitors = async () => {
    const result = await fetch(`${API_URL}/report/visits/`, {
        cache: 'no-store',
    });
    return await result.json();
}
