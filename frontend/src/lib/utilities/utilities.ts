export async function get_user_and_refresh() {

    const user = async () => {
        const response = await fetch("http://localhost:8000/users/me", {
            credentials: 'include',
        });
        const data = await response.json();
        return {user: data, status: response.status};
    }
    try {
        const u = await user()
        if (u.status === 401) {
            await refresh()
            return await user()
        }
        return u;
    } catch (e) {
        return {user: '404', status: 'fetch error'};
    }
}
export async function refresh() {
    try {
        const response = await fetch("http://localhost:8000/auth/token/refresh/", {
            method: 'POST',
            credentials: "include"
        })
        if (response.ok) {
            console.log("Token refreshed succesfully")
        } else {
            console.log("Token refres error")
        }
    }
    catch (e) {
        console.log("Error refreshing token:", e)
    }
}


export async function getFriends(userID: string) {
    const response = async () => {
        const data = await fetch(`http://localhost:8000/friends/${userID}/`, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        return await data.json()
    }
   try {
       const r = await response()
       if (r.status === 401) {
           await refresh()
           return await response()
       }
       return r;
   } catch (e) {

        return e
   }
}

export async function deleteFriends(fromUser: string, toUser: string) {
    const response = async () => {
        const cookiePair = document.cookie.split("=")
        const data = await fetch("http://localhost:8000/friends/", {
            method: 'DELETE',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                "x-csrftoken": cookiePair[1],
            },
            body: JSON.stringify({
                "from_user": fromUser,
                "to_user": toUser
            })
        })
        return await data.json()
    }
   try {
       const r = await response()
       if (r.status === 401) {
           await refresh()
           return await response()
       }
       return r;
   } catch (e) {

        return e
   }
}


export async function addFriends(fromUser: string, toUser: string) {
    const response = async () => {
        const cookiePair = document.cookie.split("=")
        const data = await fetch("http://localhost:8000/friends/", {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                "x-csrftoken": cookiePair[1],
            },
            body: JSON.stringify({
                "from_user": fromUser,
                "to_user": toUser
            })
        })
        return await data.json()
    }
   try {
       const r = await response()
       if (r.status === 401) {
           await refresh()
           return await response()
       }
       return r;
   } catch (e) {

        return e
   }
}

export async function modifyUser(user: string, newValues: any) {

    console.log("Modifiying User -> ", user)
    console.log(newValues)
    const cookiePair = document.cookie.split("=")

    const response = async () => {
        let request_headers: {[k: string]: string} = {};
        request_headers["x-csrftoken"] = cookiePair[1]

        if (typeof newValues === 'string') {
            request_headers['Content-type'] = "application/json"
            
        }

        console.log("Request headers -> ", request_headers);
        

        const data = await fetch("http://localhost:8000/users/" + user + "/" , {
            method: 'PATCH',
            credentials: 'include',
            headers: request_headers,
            body: newValues
        })
        return await data.json()
    }
    try {
        const r = await response()
        if (r.status === 401) {
            await refresh()
            return await response()
        }
        return r;
    } catch (e) {
        return e
    }
}
