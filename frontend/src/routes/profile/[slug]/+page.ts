import type {PageLoad} from './$types';

export async function load({params}){

    const slug = params.slug;
     const data = async () => {
         try {
             const response = await fetch("http://localhost:8000/users/" + slug, {
                 credentials: 'include',
             });

             if (response.ok) {
                 const data = await response.json();
                 console.log(data);
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