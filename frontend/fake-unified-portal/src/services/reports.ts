const API_URL = 'http://swarm.dfcubidesc.com:8000';

export type Visitors = {
    local_visit_count: number;
    visit_count: number;
}

export const getVisitors = async (): Promise<Visitors> => {
    const result = await fetch(`${API_URL}/report/visits`, {
        cache: 'no-store',
    });
    return await result.json();
}
