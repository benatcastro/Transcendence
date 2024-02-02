export async function load(){

    const data = async () => {
        try {
            const response = await fetch("http://localhost:8000/users/me", {
                credentials: 'include',
            });
            if (response.ok) {
                const data = await response.json();
                return {user: data, status: 'ok'};
            }
            else {
                return {user: '404', status: response.status};
            }
        }
        catch (e) {
            return {user: '404', status: 'fetch error'};
        }
    }
    return await data()
}
