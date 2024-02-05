export async function load({params}){
    const slug = params.slug;

    const data = async () => {
         try {
             const response = await fetch("https://localhost:442/users/" + slug, {
                 credentials: 'include',
             });
             if (response.ok) {
                 const data = await response.json();
                 return {user: data, status: 'ok'};
             }
             else {
                 return {user: slug, status: response.status};
             }
         }
         catch (e) {
             return {user: slug, status: 'fetch error'};
         }
    }
    return await data()
}