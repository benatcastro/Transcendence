
import {get_user_and_refresh} from "$lib/utilities/utilities";
import { getFriends } from "$lib/utilities/utilities";
export async function load(){


    const data = async () => {
        const {user, status}  = await get_user_and_refresh();
        console.log("test", user)
        const friends = await getFriends(user.username)
        return {user, friends}
    }
    return await data()
}
